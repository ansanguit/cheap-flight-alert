#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data = DataManager()
info = data.get_destination_data()
flight_search= FlightSearch()
pprint(info)

ORIGIN_CITY_IATA = "LON"

if info[0]['iataCode'] == "":
    from flight_search import FlightSearch
    flight= FlightSearch()
    for city in info:
        city["iataCode"] = flight.get_destination_code(city["city"])
    print(info)
    data.destination_data = info
    data.update_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(12 * 30))

for destination in info:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
        if flight.price < info[0]['lowestPrice']:
            print("bargain")
            message = NotificationManager(price=flight.price, origin_city=flight.origin_city,
                                          origin_airport=flight.origin_airport,
                                          destination_city=flight.destination_city,
                                          destination_airport=flight.destination_airport, out_date=flight.out_date,
                                          return_date=flight.return_date)

            message.send_notification()
        else:
            print("not great deal")
    except AttributeError:
        print(f"No flights found for {destination['city']}.")




