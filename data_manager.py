import requests
import json


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.SH_EP = "https://api.sheety.co/e214a91fe7d251bcca71a9c9bd6d0f94/flightDeals"
        self.AUTH = "Basic YW5haG1pbGVuYTpBbmRvUnJhIzM4"
        self.header = {"Authorization": self.AUTH}

    def get_data_places(self):
        shetty_response = requests.get(url=f"{self.SH_EP}/prices", headers=self.header)
        return json.loads(shetty_response.text)["prices"]

    def get_data_users(self):
        shetty_response = requests.get(url=f"{self.SH_EP}/users", headers=self.header)
        return json.loads(shetty_response.text)["users"]

    def update_row(self, iata_code, row_id):
        ep = f"{self.SH_EP}/{row_id}"
        data = {"price": {"iataCode": iata_code}}
        requests.put(url=ep, json=data, headers=self.header)
