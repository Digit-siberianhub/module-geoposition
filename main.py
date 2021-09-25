from flask import Flask, request
import requests 


app = Flask(__name__)

LAN, LON = (56.048822, 92.919185)

def auth():
    request.post(
        'https://api-digit.siberian-hub.ru/v1/module/',
        data={
            'type': 'Дисциплинированность',
            'name': 'Геопозиция',
            'description': 'Получение геопозиции пользователя'
        }
    )


@app.route('/', methods=['post'])
def hello_world():
    data = request.json
    lan, lon = data.get('lan', 0), data.get('lon', 0)
    if abs(lan-LAN) > 0.0002 or abs(LON-lon) > 0.0002:
        requests.post(
            f'https://api-digit.siberian-hub.ru/v1/module/Геопозиция/send/',
            data={
                'username': data['username'],
                'value': -2, 
            }
        )


if __name__ == 'main':
    auth()
    app.run(host='0.0.0.0')
