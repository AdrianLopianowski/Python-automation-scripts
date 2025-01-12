import requests
from bs4 import BeautifulSoup
import json

# File to store all offers in JSON format
offers_file = "offers.json"

def load_offers():
    """Load all previously stored offers from a JSON file."""
    try:
        with open(offers_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_offers(offers):
    """Save all offers to a JSON file."""
    with open(offers_file, "w", encoding="utf-8") as file:
        json.dump(offers, file, ensure_ascii=False, indent=4)

# URL of the job offers page
url = "https://students.pl/oferty/staz"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all job offers
    products = soup.find_all('div', class_='c-ListingCard_headerHeadline')
    print("Job offers:")
    
    # Load previously stored offers
    stored_offers = load_offers()
    stored_offer_names = {offer["name"] for offer in stored_offers}
    current_offers = []

    for product in products:
        name = product.find('h2').text.strip()
        is_new = name not in stored_offer_names
        
        offer_data = {
            "name": name,
            "is_new": is_new
        }
        
        current_offers.append(offer_data)
        
        # Print the offer
        if is_new:
            print(f"**NEW** {name}")
        else:
            print(name)
    
    # Save current offers to the same file
    save_offers(current_offers)
    print(f"All offers saved to {offers_file}.")
