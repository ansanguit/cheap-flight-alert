#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData


data = DataManager()
info = data.get_destination_data()
pprint(info)


if info[0]['iataCode'] == "":
    from flight_search import FlightSearch
    flight= FlightSearch()
    for city in info:
        city["iataCode"] = flight.get_destination_code(city["city"])
    print(info)

    data.destination_data = info
    data.update_codes()
