import requests
import base64
import os
from urllib.parse import urlparse
from PIL import Image
# from Compare_pic import compare_pic

def take_url_img_from_wp(old_url_img) -> str:  # работает / в цикл надо поставить, чтобы перебор был
    a = urlparse(old_url_img)
    name_img = os.path.basename(a.path)  # Output: 571378756077.jpg
    img_data = requests.get(old_url_img).content  # скачиваем миниатюру с сайта и добавляем к себе в медиабиблиотеку WP
    with open(f'pictures/{name_img}', 'wb') as f:  # сохранили у себя на компьютере
        f.write(img_data)

    url = "https://vkusmus.ru/wp-json/wp/v2/"
    user = "vkusmus"
    password = "jQtG 7bQG 3eoR F6bh YrMo Bn27"
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    # date = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())

    # Проверка на высотку картинки и размер в байтах
    pic = Image.open(f'pictures/{name_img}')
    # print('ПРОВЕРКА НА РАЗМЕР КАРТИНКИ __________')
    if pic.height > 50:
        if os.path.getsize(f'pictures/{name_img}') > 1024*5:  # проверка чтобы картинка была большой
            media = {'file': open(f'pictures/{name_img}', 'rb'), 'caption': 'pic'}
            responce_media = requests.post(url + 'media', headers=header, files=media)
            img_url_in_wp = responce_media.json()['guid']['rendered']  # ссылка в ВП на картинку

            idpic = responce_media.json()['id']  # id картинки в ВП, которую сделать как миниатюру
            f = open('idpic.txt', 'w')
            f.write(str(idpic))
            print('id картинки', idpic)
    return img_url_in_wp

