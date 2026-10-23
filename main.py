import json
from pathlib import Path
from datetime import datetime
import hashlib

DATA_FILE = Path(__file__).with_name("evidence.json")


def load_evidence():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print("Error reading evidence.json.")
            return []
    return []


def save_evidence(records):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def add_evidence(records):
    print("\n--- Add New Evidence ---")

    evidence_id = input("Enter Evidence ID: ").strip()

    if not evidence_id:
        print("Evidence ID cannot be empty.")
        return

    if any(item["evidence_id"].casefold() == evidence_id.casefold()
           for item in records):
        print("This Evidence ID already exists.")
        return

    case_number = input("Enter Case Number: ").strip()
    item_name = input("Enter Evidence Name: ").strip()
    description = input("Enter Description: ").strip()
    collected_by = input("Collected By: ").strip()

    record = {
        "evidence_id": evidence_id,
        "case_number": case_number,
        "item_name": item_name,
        "description": description,
        "collected_by": collected_by,
        "collection_date": datetime.now().isoformat(timespec="seconds"),
        "status": "Collected"
    }

    records.append(record)
    save_evidence(records)
    print("Evidence added and saved successfully!")


def view_evidence(records):
    print("\n--- All Evidence Records ---")

    if not records:
        print("No evidence records found.")
        return

    for item in records:
        print("-" * 35)
        for key, value in item.items():
            print(f"{key.replace('_', ' ').title()}: {value}")


def search_evidence(records):
    print("\n--- Search Evidence ---")
    evidence_id = input("Enter Evidence ID to search: ").strip()

    for item in records:
        if item["evidence_id"].casefold() == evidence_id.casefold():
            print("\nEvidence Found:")
            for key, value in item.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            return

    print("No matching evidence found.")


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()

def hash_evidence_file():
    file_path = input("Enter the path of the evidence file: ").strip()
    file_path = file_path.strip('"')

    try:
        file_hash = calculate_sha256(file_path)
        print("\nSHA-256 Hash:", file_hash)
    except FileNotFoundError:
        print("Error: File not found.")
    except OSError as error:
        print(f"Error reading file: {error}")

def main():
    records = load_evidence()

    while True:
        print("\nDIGITAL FORENSICS EVIDENCE TRACKER")
        print("----------------------------------")
        print("1. Add New Evidence")
        print("2. View All Evidence")
        print("3. Search Evidence")
        print("4. Exit")
        print("5. Calculate SHA-256 Hash")

        choice = input("Enter your choice (1-5): ").strip()

         
        try:
            if choice == "1":
                add_evidence(records)
            elif choice == "2":
                view_evidence(records)
            elif choice == "3":
                search_evidence(records)
            elif choice == "4":
                print("Exiting Evidence Tracker.")
                break
            elif choice == "5":
                hash_evidence_file()
            else:
                print("Invalid choice. Enter 1, 2, 3, 4, or 5.")
        except OSError as error:
            print(f"File error: {error}")



if __name__ == "__main__":
    main()

def view_evidence(records):
    print("\n--- All Evidence Records ---")
 
