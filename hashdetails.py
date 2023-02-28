import csv
import requests
import os

# Prompt user to select transaction hash input method
input_method = input("Please select transaction hash input method (file or manual): ")

# If user selects file input method, prompt user for the path to the transaction hash file
if input_method.lower() == "file":
    transaction_hash_file = input("Please enter the path to the transaction hash file: ")
    # Read transaction hashes from file
    with open(transaction_hash_file, "r") as f:
        transaction_hashes = f.readlines()
    # Remove newline characters from each transaction hash
    transaction_hashes = [h.strip() for h in transaction_hashes]
# If user selects manual input method, prompt user to enter transaction hashes separated by commas
elif input_method.lower() == "manual":
    transaction_hashes = input("Please enter the transaction hashes separated by commas: ")
    # Split transaction hashes into a list
    transaction_hashes = transaction_hashes.split(",")
    # Remove any leading or trailing white space characters from each transaction hash
    transaction_hashes = [h.strip() for h in transaction_hashes]
else:
    print("Invalid input method selected. Please try again.")
    exit()

# Initialize list to store input and output addresses
results = []

# Loop over each transaction hash
for tx_hash in transaction_hashes:
    # Make API request to get transaction details
    api_url = "https://blockchain.info/rawtx/{}".format(tx_hash)
    response = requests.get(api_url)
    data = response.json()

    # Extract the input and output addresses from the transaction details
    inputs = []
    for input_data in data["inputs"]:
        if "prev_out" in input_data and "addr" in input_data["prev_out"]:
            inputs.append(input_data["prev_out"]["addr"])

    outputs = []
    for output_data in data["out"]:
        if "addr" in output_data:
            outputs.append(output_data["addr"])

    # Append the input and output addresses to the results list
    results.append([tx_hash, ", ".join(inputs), ", ".join(outputs)])

# Save results to CSV file in the same directory as the script
csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)

# Display the results
print("\nResults:")
for r in results:
    print("Transaction hash: {}, Input addresses: {}, Output addresses: {}".format(r[0], r[1], r[2]))

print("\nCSV file saved to {}".format(csv_file))
