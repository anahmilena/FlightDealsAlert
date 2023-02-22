# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

shetty_data_places = data_manager.get_data_places()
shetty_data_users = data_manager.get_data_users()

# Check if IATA code is fulfilled, if not, code fulfills the IATA code.
iata_code_data = [1 for item in shetty_data_places if len(item["iataCode"]) == 0]
if len(iata_code_data) != 0:
    city_list = [item["city"] for item in shetty_data_places]
    row_id = 2
    for item in city_list:
        iata_code = flight_search.get_iata(item)
        data_manager.update_row(iata_code, row_id)
        row_id += 1

# Search flights and send alert message
for user in shetty_data_users:
    for item in shetty_data_places:
        data = flight_search.search_price(item["iataCode"], item["lowestPrice"])
        if data is not None:
            notification_manager.send_email(data, user["email"])
