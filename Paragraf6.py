# Задача сделать так, чтобы кортеж был на основе деления по абзацам
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from Get_url_Img_from_WP import take_url_img_from_wp
from GPT3_other_tags import Chat_converstaion_p, Chat_converstaion_ul_ol, Chat_converstaion_table, Chat_converstaion_quote

def check_img_url(url):
    return urlparse(url).netloc



def merge_4_links(urls: list) -> list:
    big_article_list = []
    for url in urls:
        big_article_list = big_article_list + get_h2_text_image(url)
    return big_article_list



def get_h2_text_image(url: str):    # return clear text of article
    print('работаем с урлом - ', url)
    # Исправленный текст для очистки от лишних тегов   **************************************************************
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
               'Accept': '*/*'}
    r = requests.get(url, headers=headers).text

    soup0 = BeautifulSoup(r, 'html.parser')

    # поиск тега h1
    h1_tag = soup0.h1
    # поиск всех тегов
    content = soup0.find_all()

    # объект Beautiful Soup
    content_article = soup0.find("div", class_='singl_post_content')


    # УДАЛЕНИЕ ТЕГОВ SPAN В H2
    h2_all = content_article.find_all('h2')
    for h2 in h2_all:
        span_tags = h2.find_all('span')
        for span_tag in span_tags:
            span_tag.decompose()


    # УДАЛЕНИЕ ПУСТЫХ P
    p_all = content_article.find_all('p')
    for p in p_all:
        if len(p.get_text(strip=True)) == 0:
            p.extract()


    # # УДАЛЕНИЕ ТЕГОВ STRONG В P (СОДЕРЖИМОЕ ОСТАЕТСЯ)
    p_all = content_article.find_all('p')
    for p in p_all:
        strongs_tags = p.find_all('strong')
        for strong_tag in strongs_tags:
            strong_tag.replaceWithChildren()


    # УДАЛЕНИЕ ТЕГОВ SPAN В H3
    h3_all = content_article.find_all('h3')
    for h3 in h3_all:
        span_tags = h3.find_all('span')
        for span_tag in span_tags:
            span_tag.decompose()


    # # УДАЛИТЬ ОКРУЖАЮЩИЙ ТЕГ P У IMG
    img_all = content_article.find_all('img')
    for img in img_all:
        try:
            img.find_parent('p').unwrap()
            img.attrs.pop('alt', None)
        except:
            pass


    # # УДАЛИТЬ ОКРУЖАЮЩИЙ ТЕГ P У IFRAME
    img_all = content_article.find_all('iframe')
    for img in img_all:
        img.find_parent('p').unwrap()


    # ЗАМЕНА ТЕГОВ DIV SHORTCODE НА BLOCKQUOTE
    div_shorts = content_article.find_all('div', class_='shortcodestyle')
    for div_short in div_shorts:
        div_short.name = 'blockquote'


    # УДАЛЕНИЕ ОДНОГО ТЕГА DIV КЛАССУ
    div_tag = content_article.find("div", class_="tptn_counter")
    div_tag.decompose()

    # УДАЛЕНИЕ МНОЖЕСТВА ТЕГОВ DIV
    div_tags = content_article.find_all("div")
    for div_tag in div_tags:
        div_tag.decompose()

    # УДАЛЕНИЕ ТЕГОВ A В P
    p_all = content_article.find_all('p')
    for p in p_all:
        aa = p.find_all('a')
        for a in aa:
            a.replace_with(a.contents)

    tags = content_article.find_all(['h2', 'h3', 'p', 'ul', 'ol', 'table', 'img', 'blockquote', 'iframe'])
    # print(soup)

    # Посмотреть какие находит теги после чистки
    for tag in tags:
        print(tag)


    h2 = ''
    abzac_str = ''
    img_str = ''
    html = ''
    for num, tag in enumerate(tags):
        print(num, ' ======= ', tag)

        # корректировка Н2 или Н3 берется как заголовок
        if tag.name == 'h2' or tag.name == 'h3':
            h2 = tag.text
            print(h2)
            html = html + '<h2>' + h2 + '</h2>'

        elif tag.name == 'p':
            abzac_str = tag.text
            r1 = Chat_converstaion_p(abzac_str)
            print(r1)
            html = html + '<p>' + r1 + '</p>'

        elif tag.name == 'ul' or tag.name == 'ol':
            r2 = Chat_converstaion_ul_ol(tag)
            print(tag, ' ---> ', r2)
            html = html + r2

        elif tag.name == 'table':
            r3 = Chat_converstaion_table(tag)
            print(tag, ' ---> ', r3)
            html = html + r3

        elif tag.name == 'blockquote':
            r4 = Chat_converstaion_quote(tag)
            print(tag, ' ---> ', r4)
            html = html + r4

        elif tag.name == 'img':
            src_value = None
            src_list = ['src', 'data-src', 'src-lazy']
            for s in src_list:
                src_value = tag.get(s)
                # нашли первый src
                if src_value:
                    break
            if src_value:
                # print(src_value)
                full_url = requests.compat.urljoin(url, src_value)
                # print(full_url)
                img_str = full_url
                # Добавление тега с картиной с урлом
                try:
                    img_str = take_url_img_from_wp(full_url)
                except:
                    img_str = ""
            html = html + '<img class="alignnone size-medium wp-image-29881" src="' + img_str + '"/>'

        elif tag.name == 'iframe':
            print(tag, ' ---> ')
            html = html + str(tag)

        else:
            print('тег не найден')

    return html
s = get_h2_text_image('https://vsepolezno.com/drugoe/rejtingi/5-jakoby-vrednyh-produktov-pitanija-i-ih-realnaja-polza/')
# s = get_h2_text_image('https://vsepolezno.com/drugoe/rejtingi/5-jakoby-vrednyh-produktov-pitanija-i-ih-realnaja-polza/')
# # # # # s = get_h2_text_image('https://semenagavrish.ru/articles/chudesa-botaniki-kvadratnye-arbuzy/')
# # # # # # s = get_h2_text_image('https://skin.ru/article/samye-jeffektivnye-procedury-dlja-vosstanovlenija-volos/')
print('__________ИТОГОВЫЙ КОД__________')
print(s)