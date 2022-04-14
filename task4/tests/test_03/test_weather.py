import pytest
import requests_mock
from src.weather_03.weather_wrapper import *

api_key = 'af5e73ed09ab0d1e58288601abc94381'

def test_get_response_city_error():
    wrapper = WeatherWrapper('')
    with pytest.raises(AttributeError):
        wrapper.get_response_city('London', BASE_URL)

def test_get():
    with requests_mock.Mocker() as m:
        m.get(BASE_URL, text='data')
        wrapper = WeatherWrapper(api_key)
        assert 'data' == wrapper.get('London', BASE_URL).text

def test_get_response_city_London():
    with requests_mock.Mocker() as m:
        m.get(BASE_URL, json={'a': 'b'})
        wrapper = WeatherWrapper(api_key)
        assert {'a': 'b'} == wrapper.get_response_city('London', BASE_URL)
def test_get_temperature_tomorrow_city_London():
    with requests_mock.Mocker() as m:
        m.get(FORECAST_URL, json={'list': [0, 0, 0, 0, 0, 0, 0, {'main': {'temp': 7}}]})
        wrapper = WeatherWrapper(api_key)
        assert 7 == wrapper.get_tomorrow_temperature('London')

def test_get_temperature_city_London():
    with requests_mock.Mocker() as m:
        m.get(BASE_URL, json={'main': {'temp': 4}})
        wrapper = WeatherWrapper(api_key)
        assert 4 == wrapper.get_temperature('London')

def test_get_tomorrow_diff_temp_London_str_same():
    wrapper = WeatherWrapper(api_key)
    url1 = BASE_URL + '?q=London&appid=' + api_key + '&units=metric'
    url2 = FORECAST_URL + '?q=London&appid=' + api_key + '&units=metric'
    with requests_mock.Mocker() as m:
        m.register_uri("GET", url1, json={'main': {'temp': 4}})
        m.register_uri("GET", url2, json={'list': [0, 0, 0, 0, 0, 0, 0, {'main': {'temp': 4}}]})
        assert 'The weather in London tomorrow will be the same than today' == wrapper.get_tomorrow_diff('London')

def test_get_diff_temp_London_Moscow():
    wrapper = WeatherWrapper(api_key)
    url1 = BASE_URL + '?q=London&appid=' + api_key + '&units=metric'
    url2 = BASE_URL + '?q=Moscow&appid=' + api_key + '&units=metric'
    with requests_mock.Mocker() as m:
        m.register_uri("GET", url1, json={'main': {'temp': 4}})
        m.register_uri("GET", url2, json={'main': {'temp': -7}})
        assert 11 == wrapper.find_diff_two_cities('London', 'Moscow')

def test_get_diff_temp_London_Moscow_str_warmer():
    wrapper = WeatherWrapper(api_key)
    url1 = BASE_URL + '?q=London&appid=' + api_key + '&units=metric'
    url2 = BASE_URL + '?q=Moscow&appid=' + api_key + '&units=metric'
    with requests_mock.Mocker() as m:
        m.register_uri("GET", url1, json={'main': {'temp': 4}})
        m.register_uri("GET", url2, json={'main': {'temp': -7}})
        assert 'Weather in London is warmer than in Moscow by 11 degrees' == wrapper.get_diff_string('London', 'Moscow')
def test_get_diff_temp_London_Moscow_str_colder():
    wrapper = WeatherWrapper(api_key)
    url1 = BASE_URL + '?q=London&appid=' + api_key + '&units=metric'
    url2 = BASE_URL + '?q=Moscow&appid=' + api_key + '&units=metric'
    with requests_mock.Mocker() as m:
        m.register_uri("GET", url1, json={'main': {'temp': -7}})
        m.register_uri("GET", url2, json={'main': {'temp': 4}})
        assert 'Weather in London is colder than in Moscow by 11 degrees' == wrapper.get_diff_string('London', 'Moscow')
