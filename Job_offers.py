import requests
from bs4 import BeautifulSoup

# File to store previously seen offers
seen_offers_file = "seen_offers.txt"

def load_seen_offers():
    """Load previously seen offers from a file."""
    try:
        with open(seen_offers_file, "r", encoding="utf-8") as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

def save_seen_offers(offers):
    """Save the current set of offers to a file."""
    with open(seen_offers_file, "w", encoding="utf-8") as file:
        file.write("\n".join(offers))

# URL of the job offers page
url = "https://students.pl/oferty/staz"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all job offers
    products = soup.find_all('div', class_='c-ListingCard_headerHeadline')
    print("Job offers:")
    
    # Load previously seen offers
    seen_offers = load_seen_offers()
    current_offers = set()
    
    for product in products:
        name = product.find('h2').text.strip()
        current_offers.add(name)
        
        # Mark as **new** if not seen before
        if name not in seen_offers:
            print(f"**NEW** {name}")
        else:
            print(name)
    
    # Save the current offers for the next comparison
    save_seen_offers(current_offers)
