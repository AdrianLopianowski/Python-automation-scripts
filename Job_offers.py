import requests
from bs4 import BeautifulSoup
import json
import os 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# File to store all offers in JSON format
offers_file = "offers.json"
load_dotenv()
sender_email = os.getenv("EMAIL_ADDRESS")
recipient_email = os.getenv("RECIPIENT_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")
port = int(os.getenv("SMTP_PORT"))
print("Loaded configuration:")
print(f"SMTP Server: {smtp_server}")
print(f"Port: {port}")
print(f"Sender Email: {sender_email}")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Testowe dane
subject = "Testowy e-mail"
body = "Cześć! To jest testowy e-mail wysłany z Pythona."




def send_email(recipient_email, subject, body):
    try:
        # Stwórz wiadomość e-mail
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Dodaj treść wiadomości
        msg.attach(MIMEText(body, 'plain'))

        # Połącz się z serwerem SMTP
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Szyfruj połączenie
            server.login(sender_email, password)
            server.send_message(msg)

        print("Email wysłany pomyślnie!")
    except Exception as e:
        print(f"Wystąpił błąd podczas wysyłania e-maila: {e}")

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
    # Wywołaj funkcję
send_email(recipient_email, subject, body)
