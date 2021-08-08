import requests
import responses

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

# creating mocks
@responses.activate
def test_simulate_data_cannot_be_found():
    responses.add(
        responses.GET,
        "http://api.zippopotam.us/us/9999999999",
        json={"error": "No data exists for US zip code 9999999999"},
        status=404
    )
    response = requests.get("http://api.zippopotam.us/us/9999999999")
    assert response.status_code == 404
    response_body = response.json()
    assert response_body["error"] == "No data exists for US zip code 9999999999"

# If, during testing, you accidentally hit an endpoint that 
# does not have an associated mock response, 
# you’ll get a ConnectionError
@responses.activate
def test_unmatched_endpoint_raises_connectionerror():
    with pytest.raises(ConnectionError):
        requests.get('http://api.zippopotam.us/us/12345')
