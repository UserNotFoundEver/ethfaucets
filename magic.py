#  eligible walletsmagic.py gets wall your wallets to verify if you are eligible, if not eligible then other options are available. this is mostly for testnet eth gas but further confirmation may make you eligible for real gas, manually verified even with our smart algorithm #

import requests
import pandas as pd

# API URL to get 0x wallets
API_URL = 'https://api.example.com/get-wallets'  # Replace with the actual API endpoint

# Function to get wallet data from the API
def get_wallets(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Function to process wallets
def process_wallets(wallets):
    # Create a DataFrame from the API response
    df = pd.DataFrame(wallets)

    # Log all wallets in a .txt file
    with open('wallets.txt', 'w') as f:
        for wallet in wallets:
            f.write(f"{wallet['address']}\n")

    # Save all wallets to a CSV file
    df.to_csv('wallets.csv', index=False)

    # Save all wallets to an Excel spreadsheet
    df.to_excel('wallets.xlsx', index=False)

    # Filter eligible wallets
    eligible_wallets = df[df['status'] == 'ELIGIBLE']

    # Save eligible wallets to a separate CSV file
    eligible_wallets.to_csv('eligible_wallets.csv', index=False)

    # Save eligible wallets to a separate Excel spreadsheet
    eligible_wallets.to_excel('eligible_wallets.xlsx', index=False)

    return eligible_wallets

# Main function
def main():
    # Get wallet data from the API
    wallets = get_wallets(API_URL)

    # Process wallets and get eligible wallets
    eligible_wallets = process_wallets(wallets)

    # Print eligible wallets
    print(eligible_wallets)

if __name__ == '__main__':
    main()
