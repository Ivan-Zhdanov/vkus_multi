import requests
from PIL import ImageFile
from bs4 import BeautifulSoup

tag = fr"""<img alt="Шишелова Ярина Владимировна" class="avatar pp-user-avatar avatar-100 photo" data-del="avatar" data-wpfc-original-src="https://foodandhealth.ru/wp-content/uploads/2021/11/avatar-shishelova-140x140.jpeg" height="100" onload="Wpfcll.r(this,true);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" width="100"/>"""


def endimg_detect(url):
    s = url.endswith(('.gif'))
    # print(s)
    return s

def get_image_size(url):
    response = requests.head(url)
    content_length = response.headers.get('content-length')
    if content_length:
        return int(content_length)
    chunk_size = 128
    image_data = requests.get(url, stream=True).iter_content(chunk_size=chunk_size)
    parser = ImageFile.Parser()
    for chunk in image_data:
        parser.feed(chunk)
        if parser.image:
            return len(chunk)
    return None

url = 'https://foodandhealth.ru/info/primenenie-aloe-v-sovremennoy-farmacevtike/'
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
imgs = soup.find_all('img')
# print(imgs)
for img in imgs:
    # формирование словаря по картинке всех атрибутов
    # print(img.attrs)
    dict_attrs = img.attrs
    for k, v in dict_attrs.items():
        if 'src' in k:
            list_attr_in_src = v.split(' ')
            # print('ключ и значения', k, list_attr_in_src)
            # это строка или список
            for attr_img in list_attr_in_src:
                # смотрим на размер по ссылке
                try:
                    if get_image_size(attr_img) < 15000:
                        continue
                except:
                    continue
                if endimg_detect(attr_img) is True:
                    continue
                else:
                    # мы нашли подходящую url картинки выходим из цикла прохода по атрибутам img
                    print('2', attr_img)
                    continue
                    # break




# смотрим чтобы картинка не оканчивалась на gif
# смотрим чтобы размер было больше 50 кб




