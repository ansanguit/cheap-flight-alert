import requests
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = "1WqPjetiGmEqjmVd7MznWCkZpTEDRLHV"


class FlightSearch:
    def __init__(self):
        self.code = "Test"
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        header ={
            "apikey": TEQUILA_API_KEY
        }
        parameters= {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=TEQUILA_ENDPOINT, headers=header, params=parameters)
        code = response.json()["locations"][0]["code"]
        return code
