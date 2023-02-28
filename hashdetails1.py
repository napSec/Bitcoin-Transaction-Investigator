import csv
import requests

# Prompt user for input method
input_method = input("Enter 1 to input transaction hash(es) manually, or 2 to read from file: ")

# Read transaction hashes based on input method
if input_method == "1":
    transaction_hashes = input("Enter transaction hash(es), separated by comma: ").split(",")
elif input_method == "2":
    input_file_path = input("Enter the path to the input file: ")

    # Determine file type and read transaction hashes accordingly
    if input_file_path.endswith('.csv'):
        with open(input_file_path, newline='') as f:
            reader = csv.reader(f)
            transaction_hashes = [row[0] for row in reader]
    elif input_file_path.endswith('.txt'):
        with open(input_file_path) as f:
            transaction_hashes = [line.strip() for line in f]
    else:
        print("Invalid file type. Please input a CSV or TXT file.")
        exit()
else:
    print("Invalid input method. Please enter 1 or 2.")
    exit()

results = []

# Query the Blockchain.com Explorer API for each transaction hash
for transaction_hash in transaction_hashes:
    response = requests.get(f"https://blockchain.info/rawtx/{transaction_hash}")

    if response.status_code == 200:
        data = response.json()
        input_addresses = [input_data["prev_out"]["addr"] for input_data in data["inputs"]]
        output_addresses = [output_data["addr"] for output_data in data["out"]]
        results.append({"Transaction hash": transaction_hash, "Input addresses": ", ".join(input_addresses), "Output addresses": ", ".join(output_addresses)})
    else:
        results.append({"Transaction hash": transaction_hash, "Input addresses": "Error", "Output addresses": "Error"})

# Print results to console
for result in results:
    print(f'Transaction hash: {result["Transaction hash"]}, Input addresses: {result["Input addresses"]}, Output addresses: {result["Output addresses"]}')

# Save results to CSV file
with open("results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Transaction hash", "Input addresses", "Output addresses"])
    writer.writeheader()
    writer.writerows(results)
