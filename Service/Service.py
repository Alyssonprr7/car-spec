import requests


def get_all_cars(max_rows):
    fetch_data = requests.get('https://5f0785109c5c2500163070bb.mockapi.io/cars')
    return fetch_data.json()


def get_unique_car(id):
    fetch_data = requests.get('https://5f0785109c5c2500163070bb.mockapi.io/cars/{}'.format(id))
    return fetch_data.json()
