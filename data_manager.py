import os
from dotenv import load_dotenv
from pprint import pprint
import requests

# load_dotenv(r"G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")
load_dotenv(r"C:\Users\watsorob\Google Drive\Programming\Python\EnvironmentVariables\.env.txt")
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_KEY")

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self, call_sheety: bool = False) -> list:
        if call_sheety:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT)
            data = response.json()
            self.destination_data = data["prices"]
        else:
            data = [{"city": "Paris", "iataCode": "PAR", "lowestPrice": 954, "id": 2},
                    {"city": "Berlin", "iataCode": "BER", "lowestPrice": 942, "id": 3},
                    {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 1485, "id": 4},
                    {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 1551, "id": 5},
                    {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 995, "id": 6},
                    {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 9414, "id": 7},
                    {"city": "New York", "iataCode": "NYC", "lowestPrice": 9240, "id": 8},
                    {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 9260, "id": 9},
                    {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 9378, "id": 10},
                    {"city": "Bali", "iataCode": "DPS", "lowestPrice": 1500, "id": 11}, # price was 501
                    {"city": "Nagoya", "iataCode": "NGO", "lowestPrice": 1500, "id": 12},
            ]
            self.destination_data = data
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
