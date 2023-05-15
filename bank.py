import requests
import csv
from bs4 import BeautifulSoup

def scrape_credit_cards():
    url = "https://www.hdfcbank.com/personal/pay/cards/credit-cards"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    cards = soup.select(".cardlist-wrapper .card-tile")

    card_details = []
    for card in cards:
        card_name = card.select_one(".card-title").text.strip()
        card_fee = card.select_one(".card-joining-fee").text.strip()
        reward_points = card.select_one(".reward-points").text.strip()
        lounge_access = card.select_one(".lounge-access").text.strip()
        milestone_benefit = card.select_one(".milestone-benefits").text.strip()
        card_fee_reversal = card.select_one(".fee-reversal-condition").text.strip()

        card_data = {
            "Card Name": card_name,
            "Card Fee": card_fee,
            "Reward Points/Percentage per 100 Spent": reward_points,
            "Lounge Access": lounge_access,
            "Milestone Benefit": milestone_benefit,
            "Card Fee Reversal Condition": card_fee_reversal
        }

        card_details.append(card_data)

    if card_details:
        filename = "credit_card_details.csv"
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = card_details[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(card_details)
        print("Scraping complete. Data saved to", filename)
    else:
        print("No card details found.")

scrape_credit_cards()
