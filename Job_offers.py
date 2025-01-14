import requests
from bs4 import BeautifulSoup
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from datetime import date

# File to store all offers in JSON format
offers_file = "offers.json"
load_dotenv()
sender_email = os.getenv("EMAIL_ADDRESS")
recipient_email = os.getenv("RECIPIENT_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")
port = int(os.getenv("SMTP_PORT"))

def send_email(recipient_email, subject, body):
    """Send an email with the given subject and body."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add message body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error while sending email: {e}")

def load_offers():
    """Load previously stored offers from a JSON file."""
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
    interns = soup.find_all('div', class_='c-ListingCard_headerHeadline')
    
    # Load previously stored offers
    stored_offers = load_offers()
    stored_offer_names = {offer["name"] for offer in stored_offers}
    current_offers = []
    new_offers = []
    today = date.today()


    for intern in interns:
        name = intern.find('h2').text.strip()
        is_new = name not in stored_offer_names
        
        offer_data = {"name": name}
        current_offers.append(offer_data)

        # If the offer is new, add it to the list of new offers
        if is_new:
            new_offers.append(name)
    
    # Save the current offers to the file
    save_offers(current_offers)

    # If there are new offers, send an email
    if new_offers:
        subject = f"New job offers available, {today}"
        body = "The following new job offers have been found:\n\n" + "\n".join(new_offers)
        send_email(recipient_email, subject, body)
    else:
        print("No new job offers found.")
