import random
import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request,
        'name': 'Оқырман'
    })


@app.get('/advice')
def advice(request: Request):
    advice = [
        'Өмір бақи джун бол',
        'Тек пайда әкелуге тырыс',
        'Күнделікті жұмысыңды саналы тәжірибеге айналдыр',
        'Басшыңмен байланыста бол',
        'Таза код кітабын оқы',
        'Спандж мультфилмі презентацияға жақсы',
    ]
    advice = random.choice(advice)
    return templates.TemplateResponse('advice.html', {
        'request': request,
        'advice': advice
    })


# colleagues

colleagues = ['нұржан', 'ұлжан', 'анар', 'айбану']

colleagues_db = {
    'нұржан': {
        'қаласы': 'көкшетау',
        'жасы': 28,
        'жұмысы': 'астрофизика(жұлдыздар емес)'
    },
    'ұлжан': {
        'қаласы': 'тараз',
        'жасы': 28,
        'жұмысы': 'project manager'
    },
    'анар': {
        'қаласы': 'семей',
        'жасы': 35,
        'жұмысы': 'стартап'
    },
    'айбану': {
        'қаласы': 'шымкент',
        'жасы': 23,
        'жұмысы': 'PHP & Python Developer'
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
def colleagues(request: Request):
    return templates.TemplateResponse('colleagues.html', {
        'request': request,
        'colleagues': colleagues_db
    })


# personel colleagues route

@app.get('/colleagues/{name}')
def colleagues(request: Request, name):
    if name in colleagues_db:
        return templates.TemplateResponse('colleagues.html', {
            'request': request,
            'name': name,
            'info': colleagues_db[name]
        })
    else:
        return 'Qate'


@app.get('/quotes/{name}')
def colleagues(name):
    my_request = RequestAPI()

    return my_request.get_text_with_quote_for_name(name)

@app.get('/weather')
def weather(request: Request):
    return templates.TemplateResponse('weathermain.html', {
        'request': request,
    })

@app.get('/weather/{city}')
def wea(request: Request, city):
    response = requests.get('https://goweather.herokuapp.com/weather/' + city)

    if response.status_code == 200:
        city = response.json()
        return templates.TemplateResponse('weather.html', {
            'request': request,
            'city': city,
        })
    else:
        return 'Wrong'
