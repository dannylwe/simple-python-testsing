import requests

# I’ll be using the Zippopotam.us REST API. 
# This API takes a country code and a zip code and 
# returns location data associated with that country and zip code.

def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200

def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers["Content-Type"] == "application/json"

def test_get_locations_for_us_90210_check_country_equals_united_states():
     response = requests.get("http://api.zippopotam.us/us/90210")
     response_body = response.json()
     assert response_body["country"] == "United States"

def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
     response = requests.get("http://api.zippopotam.us/us/90210")
     response_body = response.json()
     assert response_body["places"][0]["place name"] == "Beverly Hills"

def test_get_locations_for_us_90210_check_one_place_is_returned():
     response = requests.get("http://api.zippopotam.us/us/90210")
     response_body = response.json()
     assert len(response_body["places"]) == 1

