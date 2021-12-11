from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint


data_manager = DataManager()
sheet_data = data_manager.get_destination_data(call_sheety=False)
flight_search = FlightSearch()
notification_manager = NotificationManager()
user_data = data_manager.get_user_data(call_sheety=False)

ORIGIN_CITY_IATA = "BWI"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))



for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )

    if flight is None:
        continue

    url = f"https://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
          f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

    if flight.price < destination["lowestPrice"]:
        print("no layover")
        for receiver_email in user_data:
            print(receiver_email["email"])
            sender = "Cheap Flights <cheapflights@example.com>"
            receiver = receiver_email["email"]
            message = f"""Subject: New Low Price Flight!\nTo: {receiver}\nFrom: {sender}\n
            
            Low price alert! Only ${flight.price} to fly from
            {flight.origin_city}-{flight.origin_airport} to
            {flight.destination_city}-{flight.destination_airport}, from
            {flight.out_date} to {flight.return_date}.
            {url}"""
            if flight.stop_overs > 0:
                print("layover")
                message += f"""\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."""
            # notification_manager.send_sms(message)
            notification_manager.send_email(message=message, sender=sender, receiver=receiver)
