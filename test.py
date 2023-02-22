from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
notification_manager = NotificationManager()

search = flight_search.search_price("BUE", 400)
print(search)
# notification_manager.send_email(search)
