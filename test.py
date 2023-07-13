"""This app is for the test of entrance for MOZIO Group"""
import os
import pprint
import requests
from dotenv import load_dotenv

# this method is called for the usage of env files in the program.
load_dotenv()

# we gonna use pprint method for a better and more legible format in the results.


# This function will make the POST method of creating the search
def create_search():
    """function in charge of create search"""

    # using url from the documentation
    api_endpoint = 'https://api-testing.mozio.com/v2/search/'

    # giving the parameters of the create search
    parameters = {
        "start_address": "44 Tehama Street, San Francisco, CA, USA",
        "end_address": "SFO",
        "mode": "one_way",
        "pickup_datetime": "2023-12-01 15:30",
        "num_passengers": 2,
        "currency": "USD",
        "campaign": "Edward Marzal"
    }

    # headers containing API_KEY on an env file
    headers = {
        'Content-type': 'application/json',
        'Accepts': 'application/json',
        'API-KEY': os.getenv('API_KEY_ENV'),
    }

    response = requests.post(url=api_endpoint, json=parameters,
                             headers=headers, timeout=10)

    print(response)
    pprint.pprint(response.json())


# This function will make the GET method of making a poll search
# the id we got was  'search_id': '36f1cff2f1274025b6b92348e2e6f0a1'
def get_search():
    """function in charge of search using the parameters"""

    # using url from the documentation
    url = 'https://api-testing.mozio.com/v2/search/36f1cff2f1274025b6b92348e2e6f0a1/poll/'

    # giving the parameters of the search
    parameters = {
        'search_id': '36f1cff2f1274025b6b92348e2e6f0a1'
    }

    # headers containing API_KEY on an env file
    headers = {
        'Content-type': 'application/json',
        'Accepts': 'application/json',
        'API_KEY': os.getenv('API_KEY_ENV'),
    }

    response = requests.get(url=url, params=parameters,
                            headers=headers, timeout=30)

    print(response)
    pprint.pprint(response.json())


# This function will make the POST method of creating a reservation
def create_reservation():
    """function in charge of create search"""

    # using url from the documentation
    url = 'https://api-testing.mozio.com/v2/reservations/'

    # giving the parameters of the create reservation using provider
    # and the cheapest vehicle found was a bus for 60$
    # 'vehicle_id': '467e2e37800cc144cef852d6118e0f52'
    parameters = {
        'search_id': '36f1cff2f1274025b6b92348e2e6f0a1',
        'result_id': '966c4ee7ec631fb4c6416b28609edae8',
        "email": "happytravel@mozio.com",
        "country_code_name": "US",
        "phone_number": "8776775544",
        "first_name": "Happy",
        "last_name": "Travel",
        "airline": "AA",
        "flight_number": "133",
        "customer_special_instructions": "My doorbell is broken, please yell"
    }

    # headers containing API_KEY on an env file
    headers = {
        'Accepts': 'application/json',
        'API_KEY': os.getenv('API_KEY_ENV'),
    }

    response = requests.post(url=url, json=parameters,
                             headers=headers, timeout=10)

    print(response)
    pprint.pprint(response.json())


# This function will make the GET method of searching for the reservation poll
def get_reservation():
    """function in charge of search using the parameters"""

    # using url from the documentation
    url = 'https://api-testing.mozio.com/v2/reservations/36f1cff2f1274025b6b92348e2e6f0a1/poll/'

    # giving the parameters of the search reservation
    parameters = {
        'search_id': '36f1cff2f1274025b6b92348e2e6f0a1'
    }

    # headers containing API_KEY on an env file
    headers = {
        'Accepts': 'application/json',
        'API_KEY': os.getenv('API_KEY_ENV'),
    }

    response = requests.get(url, params=parameters,
                            headers=headers, timeout=30)

    print(response)
    pprint.pprint(response.json())


# his function will make the DELETE method of deleting the reservation
# the reservation ID we got from the get fucntion was 'id': '28d9802247df4f9bbf6072d4b16e583c'
def delete_reservation():
    """function in charge of search using the parameters"""

    # using url from the documentation
    url = 'https://api-testing.mozio.com/v2/reservations/28d9802247df4f9bbf6072d4b16e583c'

    # giving the parameters of the delete
    parameters = {
        'hashed_id': '28d9802247df4f9bbf6072d4b16e583c',
    }

    # headers containing API_KEY on an env file
    headers = {
        'Accepts': 'application/json',
        'API_KEY': os.getenv('API_KEY_ENV'),
    }

    response = requests.delete(url, json=parameters,
                               headers=headers, timeout=10)

    print(response)
    pprint.pprint(response.json())


create_search()
get_search()
create_reservation()
get_reservation()
delete_reservation()
