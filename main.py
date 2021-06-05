import random
import requests
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return 'Salemberdik'


@app.get('/bloopers')
def bloopers():
    bloopers = [
        'Bir bala jaqsy, al basqa bala okinishke orai',
        'Bala jasaganda bizden ryqsat syragan joqsyndar goi',
        'Eki siyr bagyp oz ozindi asyra',
        'Nakonecto u nas koronovirus',
        'Potomu shto potomu shto',
        'Salut dlya podderjki vrachei',
    ]
    result = random.choice(bloopers)
    return result


# colleagues

colleagues = ['mariam', 'ali']

colleagues_db = {
    'mariam': {
        'department': 'managment',
        'age': 21
    },
    'ali': {
        'department': 'IT',
        'age': 25
    },
    'sergey': {
        'department': 'IT',
        'age': 26
    }
}


# OOP route

class RequestAPI:
    url = 'https://api.quotable.io/random'

    def get_quote(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            quote = response.json()
            return quote

    def get_content(self):
        quote = self.get_quote()

        return quote['content']

    def get_text_with_quote_for_name(self, name):

        result = 'Досым %s. Мынау менің саған кеңесім: %s' % (name.capitalize(), self.get_content())
        return result


# colleagues route

@app.get('/colleagues')
def colleagues():
    return colleagues_db


# personel colleagues route

@app.get('/colleagues/{name}')
def colleagues(name):
    if name in colleagues_db:
        return colleagues_db[name]
    else:
        return 'Qate'


@app.get('/quotes/{name}')
def colleagues(name):
    my_request = RequestAPI()

    return my_request.get_text_with_quote_for_name(name)

