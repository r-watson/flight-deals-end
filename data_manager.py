import os
from dotenv import load_dotenv
from pprint import pprint
import requests

load_dotenv(r"G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")
# load_dotenv(r"C:\Users\watsorob\Google Drive\Programming\Python\EnvironmentVariables\.env.txt")
SHEETY_FLIGHT = os.getenv("SHEETY_FLIGHT")
SHEETY_AUTH = os.getenv("SHEETY_KEY")

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}
        self.headers = {
            "Authorization": SHEETY_AUTH,
        }

    def get_destination_data(self, call_sheety: bool = False) -> list:
        if call_sheety:
            response = requests.get(url=f"{SHEETY_FLIGHT}/prices", headers=self.headers)
            data = response.json()
            self.destination_data = data["prices"]
        else:
            data = [{"city": "Chicago", "iataCode": "ORD", "lowestPrice": 954, "id": 2},
                    {"city": "Atlanta", "iataCode": "ATL", "lowestPrice": 942, "id": 3},
                    {"city": "Denver", "iataCode": "DEN", "lowestPrice": 1485, "id": 4},
                    {"city": "Dallas", "iataCode": "DAL", "lowestPrice": 1551, "id": 5},
                    {"city": "Los Angeles", "iataCode": "LAX", "lowestPrice": 995, "id": 6},
                    {"city": "Charlotte", "iataCode": "CLT", "lowestPrice": 9414, "id": 7},
                    {"city": "New York", "iataCode": "NYC", "lowestPrice": 9240, "id": 8},
                    {"city": "Las Vega", "iataCode": "LAS", "lowestPrice": 9260, "id": 9},
                    {"city": "Phoenix", "iataCode": "PHX", "lowestPrice": 9378, "id": 10},
                    {"city": "Orlando", "iataCode": "MCO", "lowestPrice": 1500, "id": 11},  # price was 501
                    {"city": "Miami", "iataCode": "MIA", "lowestPrice": 1500, "id": 12},
                    ]
            # data = [{"city": "Paris", "iataCode": "PAR", "lowestPrice": 954, "id": 2},
            #         {"city": "Berlin", "iataCode": "BER", "lowestPrice": 942, "id": 3},
            #         {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 1485, "id": 4},
            #         {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 1551, "id": 5},
            #         {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 995, "id": 6},
            #         {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 9414, "id": 7},
            #         {"city": "New York", "iataCode": "NYC", "lowestPrice": 9240, "id": 8},
            #         {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 9260, "id": 9},
            #         {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 9378, "id": 10},
            #         {"city": "Bali", "iataCode": "DPS", "lowestPrice": 1500, "id": 11}, # price was 501
            #         {"city": "Nagoya", "iataCode": "NGO", "lowestPrice": 1500, "id": 12},
            # ]
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
                url=f"{SHEETY_FLIGHT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_user_data(self, call_sheety: bool = False) -> list:
        if call_sheety:
            response = requests.get(url=f"{SHEETY_FLIGHT}/users", headers=self.headers)
            data = response.json()
            self.user_data = data
        else:
            self.user_data = {'users': [{'firstName': 'Robert', 'lastName': 'Watson', 'email': 'rtw@rtw.com', 'id': 2},
                                        {'firstName': 'Magic ', 'lastName': 'Johnson', 'email': 'mj@mj.com', 'id': 3},
                                        {'firstName': 'Giggly', 'lastName': 'Wiggles', 'email': 'gw@gw.com', 'id': 4}]}
            return self.user_data["users"]
