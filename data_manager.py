
import requests


SHEET_END= "https://api.sheety.co/1c5fc36e34c5fd06214a7441304005d2/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destinationdata = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_END)
        self.destinationdata = response.json()['prices']
        return self.destinationdata

    def update_codes (self):
        for city in self.destinationdata:
             params = {
                 "price":{
                     "iataCode": city["iataCode"]
                 }
             }

             response = requests.put(url= f"{SHEET_END}/{city['id']}", json= params)
             print(response.text)

