# функция добавления для сайта
import requests
import base64
import time


def addWordpress(h1, neurotext):  # подключаемся к WP по REST API
    url = "https://supergardener.ru/wp-json/wp/v2/"
    user = "superg"
    password = "ZkYn CSVh RFku gx1T KOIF Hank"
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    date = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())
    f = open('idpic.txt', 'r')
    idpic = f.read()
    print(idpic)

    post = {
        'title': h1,
        'status': 'publish',
        'content': neurotext,
        'categories': 1,
        'date': date,
        'featured_media': idpic,
    }
    responce = requests.post(url + 'posts', headers=header, json=post)  #  отправляем статью
    print('Добавили статью {}. Результат:'.format(h1), responce.status_code)
    return


# addWordpress('h1', 'text')