import requests


def get_all_cars(max_rows):
    fetch_data = requests.get('http://localhost:5000/cars', verify=False)
    return fetch_data.json()


def get_unique_car(id):
    fetch_data = requests.get('http://localhost:5000/cars/{}'.format(id), verify=False)
    return fetch_data.json()
