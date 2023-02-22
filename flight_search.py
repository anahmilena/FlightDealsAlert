import requests
import json
from datetime import datetime, timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.API_KEY = "G3aUyg8QecRs8jKjbYllfDpzcS0ZgoTj"
        self.API_EP = "https://api.tequila.kiwi.com/"
        self.header = {"apikey": self.API_KEY}
        self.DAYS = 90
        self.CITY_FROM = "LIM"
        self.MAX_STO = 0
        self.flag = 0

    def get_iata(self, city):
        ep = f"{self.API_EP}locations/query"
        query = {"location_types": "city", "term": city}
        kiwi_response = requests.get(url=ep, params=query, headers=self.header)
        return json.loads(kiwi_response.text)["locations"][0]["code"]

    def search_price(self, iata_code, price):
        date_from = datetime.now().strftime("%d/%m/%Y")
        date_to = (datetime.now() + timedelta(days=self.DAYS)).strftime("%d/%m/%Y")
        ep = f"{self.API_EP}v2/search"
        query = {
            "fly_from": self.CITY_FROM,
            "fly_to": iata_code,
            "date_from": date_from,
            "date_to": date_to,
            "curr": "USD",
            "price_to": price,
            "max_stopovers": self.MAX_STO,
            "flight_type": "round",
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
        }
        kiwi_response = requests.get(url=ep, params=query, headers=self.header)
        kiwi_data = json.loads(kiwi_response.text)['data']
        if len(kiwi_data) == 0 and self.flag == 0:
            self.MAX_STO = 2
            self.flag = 1
            return self.search_price(iata_code, price)
        elif len(kiwi_data) == 0 and self.flag == 1:
            self.reset_parameter()
            return None
        else:
            self.reset_parameter()
            flights = len(kiwi_data[0]["route"])
            data = {
                "price": kiwi_data[0]["price"],
                "city_to": kiwi_data[0]["cityTo"],
                "fly_to": kiwi_data[0]["flyTo"],
                "date_from": kiwi_data[0]["route"][0]["local_departure"].split("T")[0],
                "date_to": kiwi_data[0]["route"][flights - 1]["local_arrival"].split("T")[0],
                "stop_over": f"{(flights-2)} - {kiwi_data[0]['route'][1]['cityFrom']}",
                "link": kiwi_data[0]["deep_link"],
            }
            return data

    def reset_parameter(self):
        self.MAX_STO = 0
        self.flag = 0
