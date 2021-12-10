from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint


data_manager = DataManager()
sheet_data = data_manager.get_destination_data(call_sheety=False)
flight_search = FlightSearch()
notification_manager = NotificationManager()

print(sheet_data)

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"


for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    url = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
          f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
    if flight is None:
        continue

    print(flight.stop_overs)
    if flight.price < destination["lowestPrice"]:
        if flight.stop_overs > 0:
            print("layover")
            # notification_manager.send_sms(
            #     message=f"Low price alert! Only £{flight.price} to fly from"
            #             f" {flight.origin_city}-{flight.origin_airport} to "
            #             f"{flight.destination_city}-{flight.destination_airport}, from "
            #             f"{flight.out_date} to {flight.return_date}."
            # )
            message = f"""\ Subject: New Low Price Flight!
To: {receiver}
From: {sender}

Low price alert! Only £{flight.price} to fly from"
f" {flight.origin_city}-{flight.origin_airport} to "
f"{flight.destination_city}-{flight.destination_airport}, from "
f"{flight.out_date} to {flight.return_date}.\n
f"{url}"""
            notification_manager.send_email(message=message, sender=sender, receiver=receiver)
        else:
            print("no layover")
            # notification_manager.send_sms(
            #     message=f"Low price alert! Only £{flight.price} to fly from"
            #             f" {flight.origin_city}-{flight.origin_airport} to "
            #             f"{flight.destination_city}-{flight.destination_airport}, from "
            #             f"{flight.out_date} to {flight.return_date}."
            # )
