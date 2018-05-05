import os

import requests

API_KEY = os.environ.get('WEATHER_API_KEY')


def main():

    celsius_symbol = u"\u00b0"
    country = input("Name of the country: ").replace(' ', '_')
    state = input("If it is located in US, name of the state: ").replace(' ', '_')
    city = input("Name of the city: ").replace(' ', '_')
    if state:
        url = f'http://api.wunderground.com/api/{API_KEY}/geolookup/conditions/q/{country}/{state}/{city}.json'
    else:
        url = f'http://api.wunderground.com/api/{API_KEY}/geolookup/conditions/q/{country}/{city}.json'
    response = requests.get(url)
    json_string = response.json()
    location = json_string['location']['city']
    location_state = json_string['location']['state']
    location_country = json_string['location']['country_name']
    temp_c = json_string['current_observation']['temp_c']
    temp_condition = json_string['current_observation']['weather']
    try:
        location_state = int(location_state)
        print(f"Current weather conditions in {location},{location_country}:\n{temp_condition} with current temperature"
              f" of: {temp_c} C{celsius_symbol}")
    except ValueError:
        print(f"Current weather conditions in {location},{location_state}:\n{temp_condition} with current temperature"
              f" of: {temp_c} C{celsius_symbol}")
    response.close()


if __name__ == '__main__':
    main()



