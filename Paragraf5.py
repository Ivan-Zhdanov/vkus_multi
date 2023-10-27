# ГИПОТЕЗА СОЕДИНИТЬ ТЕКСТ И КАРТИНКИ В КОРТЕЖЕ
# Сейчас работает устойчиво, картинка получается только одна
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from Get_url_Img_from_WP import take_url_img_from_wp


def check_img_url(url):
    return urlparse(url).netloc



def merge_4_links(urls: list) -> list:
    big_article_list = []
    for url in urls:
        big_article_list = big_article_list + get_h2_text_image(url)
    return big_article_list



def get_h2_text_image(url: str):    # return clear text of article

    # Исправленный текст для очистки от лишних тегов   **************************************************************
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=headers).text
    soup0 = BeautifulSoup(r, 'html.parser')
    h1_tag = soup0.h1
    content = soup0.find_all()

    if h1_tag:
        tags_under_h1 = h1_tag.find_next_siblings()
    else:
        tags_under_h1 = content

    doc = ''
    # Пошли по тегам, которые ниже чем Н1
    for tag in tags_under_h1:
        tags = tag.find_all_next()
        for t in tags:
            if t.name == "p" or t.name == "h2" or t.name == "h3" or t.name == "img" or t.name == "ul" or t.name == "ol" or t.name == "li":
                t.extract()
                # print(' --- ', t)
                doc = doc + str(t)
    # print(doc)


    # Работа с очищенным текстом преобразованным в объект BS4
    soup = BeautifulSoup(doc, "html.parser")
    tags = soup.find_all()

    h2 = ''
    abzac_str = ''
    img_str = ''
    all_article_list = []


    for p in tags:
        # Кортеж данных по БЛОКУ Н2 - ТЕКСТ
        h2_abzac_tuple = (h2, abzac_str, img_str)
        # корректировка Н2 или Н3 берется как заголовок
        if p.name == 'h2' or p.name == 'h3':
            all_article_list.append(h2_abzac_tuple)
            h2 = p.text
            abzac_str = ''  # обнулили абзац
            img_str = ''    # обнулили картинку
            img_url_prev = ''

        if p.name == 'p':
            abzac_str = abzac_str + p.text + ' '

        if p.name == 'img':
            src_value = None
            src_list = ['src', 'data-src', 'src-lazy']
            for s in src_list:
                src_value = p.get(s)

                # нашли первый src
                if src_value:
                    break

            if src_value:
                # print(src_value)
                full_url = requests.compat.urljoin(url, src_value)
                # print(full_url)
                img_str = full_url
                # Добавление тега с картиной со урлом
                try:
                    # img_str = take_url_img_from_wp(full_url)
                    pass

                except:
                    img_str = ""

                # # добавлено при включении в текст картинки ....
                # abzac_str = abzac_str + '<<img class="alignnone size-medium wp-image-29881" src="' + img_str +'"/>'
                # # img_url_prev = img_str

    print('Данные которые разложили кортеж до обновление img --> ', all_article_list)
    cc = 0


    for h, p, i in all_article_list:
        if i != '':
            cc = cc + 1
    print('количество img', cc)

    # Идет запрос к WP о загрузке картинок
    all_article_list2 = []
    cort = ("", "", "")
    for h, t, im in all_article_list:
        try:
            cort = (h, t, take_url_img_from_wp(im))
        except:
            cort = (h, t, '')
        finally:
            all_article_list2.append(cort)

    # print(all_article_list2)
    return all_article_list2

# get_h2_text_image('https://vkusvill.ru/media/journal/chto-takoe-sparzha-chem-polezna-i-kak-eye-gotovit.html')
# s = get_h2_text_image('https://semenagavrish.ru/articles/chudesa-botaniki-kvadratnye-arbuzy/')
# s = get_h2_text_image('https://skin.ru/article/samye-jeffektivnye-procedury-dlja-vosstanovlenija-volos/')
# print(s)