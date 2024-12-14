import argparse
import csv
import os
from datetime import datetime
from Bio import Entrez

# Configure Entrez email
Entrez.email = "aishwaryasng246@gmail.com"

# Search and download data from NCBI
def search_download(database, term, number):
    print(f"Searching database '{database}' for term '{term}'...")

    # Perform the search
    search_handle = Entrez.esearch(db=database, term=term, retmax=number)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    ids = search_results["IdList"]
    tot_found = search_results["Count"]

    print(f"Found {tot_found} result. Downloading {number} items...")

    # directory 
    output_dir = term.replace(" ", "_")
    os.makedirs(output_dir, exist_ok=True)

    file_name = []

    # Download by ID
    for record_id in ids:
        fetch_handle = Entrez.efetch(db=database, id=record_id, rettype="gb", retmode="text")
        record_data = fetch_handle.read()
        fetch_handle.close()

        filename = os.path.join(output_dir, f"{record_id}.txt")
        with open(filename, "w") as file:
            file.write(record_data)
        file_name.append(filename)

    print("Downloaded files:")
    for fname in file_name:
        print(fname)

    return file_name, tot_found

# Function to log metadata to a CSV file
def log_metadata(date, database, term, number, total):
    log_file = "search_log.csv"
    log_exists = os.path.exists(log_file)

    with open(log_file, "a", newline="") as csvfile:
        fieldnames = ["date", "database", "term", "max", "total"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not log_exists:
            writer.writeheader()

        writer.writerow({
            "date": date,
            "database": database,
            "term": term,
            "max": number,
            "total": total
        })

    print(f"Metadata logged in {log_file}.")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Download data from NCBI databases.")
    parser.add_argument("--database", default="nucleotide", help="NCBI database to search (default: nucleotide)")
    parser.add_argument("--term", required=True, help="Search term")
    parser.add_argument("--number", type=int, default=10, help="Number of items to download (default: 10)")

    args = parser.parse_args()

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    database = args.database
    term = args.term
    number = args.number

    file_name, tot_found = search_download(database, term, number)
    log_metadata(date, database, term, number, tot_found)

if __name__ == "__main__":
    main()