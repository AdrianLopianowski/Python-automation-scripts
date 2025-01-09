import requests
from bs4 import BeautifulSoup

url = "https://students.pl/oferty/staz"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = soup.find_all('div', class_='c-ListingCard_headerHeadline')
    print("Job offers:")
    for product in products:
        name = product.find('h2').text.strip()
        print(f"{name}")
   