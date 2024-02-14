#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from datetime import datetime, timedelta
from data_manager_W_D39_v00_r13 import DataManager
from flight_search_W_D39_v00_r13 import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()  # needs () because it is a Class
flight_search = FlightSearch()
sheet_data = data_manager.get_request_for_getting_destination_data()

origin_iata_code = "SAN"  #original city to fly from

# TODO: Authenticate with a Bearer Token
# TODO: Ensure all sensitive data is extracted and created into an Environment Variable, above here.


print("Sheet Data before any Updates: ")
pprint(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
# def iataCode_Checking():
for row in sheet_data:
    # global flight_search
    # check if "iatacode" for the row is empty:
    if row.get("iataCode") == "":
        print(f"iataCode data is empty for {row['city']}, UPDATING ROW...")
        # use the flightsearch class to get the corresponding iata code for the city:
        iata_code = flight_search.get_destination_code(row["city"])
        # update the "iatacode" in the row with the new value:
        row["iataCode"] = iata_code
        # iata_code = iata_code
        # return iata_code

print("\nSheet Data After Updates: ")
pprint(sheet_data)

# update the google sheet via sheety api if any changes were made:
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

now = datetime.now()
tomorrow = now + timedelta(days=1)
six_months_from_today = now + timedelta(days=181)


for destination in sheet_data:
    flight = flight_search.check_flights(origin_iata_code, destination["iataCode"], from_time=tomorrow, to_time=six_months_from_today)
    if flight:
        print(f"Flight found: {flight.destination_city} at {flight.price}")
    else:
        print(f"No flights found for {destination['iataCode']}.")
# elif not sheet_data[0]["iataCode"] == "":
#     print()
#     print("Data was found inside the first row of the IATA Code Column")
# # iataCode_Checking()




