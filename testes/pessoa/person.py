import requests


class Person():
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.obtained_data = False

    def get_all_data(self):
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if response.ok:
            self.obtained_data = True
            return 'OK'

        self.obtained_data = False

        return 'ERRO 404'
