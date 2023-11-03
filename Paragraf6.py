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
        img.find_parent('p').unwrap()
        img.attrs.pop('alt', None)

        # img.replace_with(img.contents)

    # ЗАМЕНА ТЕГОВ DIV SHORTCODE НА BLOCKQUOTE
    div_shorts = content_article.find_all('div', class_='shortcodestyle')
    for div_short in div_shorts:
        div_short.name = 'blockquote'


    # УДАЛЕНИЕ ОДНОГО ТЕГА DIV КЛАССУ
    div_tag = content_article.find("div",class_="tptn_counter")
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

    # print(content_article, end='**************** \n\n')

    # # Посмотреть какие теги находятся в объекте bs4
    # for num, tag in enumerate(content_article):
    #     print(num, '', tag)


    # # Работа с контентом
    # # Пошли по тегам, которые находятся в редактированном объекте bs4
    # doc = ''
    # for tag in content_article:
    #     tags = tag.find_all()
    #     for t in tags:
    #         if t.name == "p" or t.name == "h2" or t.name == "h3" or t.name == "ul" or t.name == "ol" or t.name == "li" or t.name == "img" or t.name =='blockquote':
    #             t.extract()
    #             # print(' --- ', t)
    #             doc = doc + str(t)
    # # Документ с первичными основными тегами
    # # print(doc, sep='\n')


    # Работа с очищенным текстом преобразованным в объект BS4
    # soup = BeautifulSoup(doc, "html.parser")
    # нашли все теги в отфильтрованном html
    tags = content_article.find_all(['h2', 'h3', 'p', 'ul', 'ol', 'table', 'img', 'blockquote'])
    # print(soup)


    h2 = ''
    abzac_str = ''
    img_str = ''
    all_article_list = []

    h2_abzac_tuple = (h2, abzac_str, img_str)
    html = ''
    for num, p in enumerate(tags):
        print(num, ' ======= ', p)
        # Кортеж данных по БЛОКУ Н2 - ТЕКСТ


        # корректировка Н2 или Н3 берется как заголовок
        if p.name == 'h2' or p.name == 'h3':
            h2 = p.text
            print(h2)
            # abzac_str = ''  # обнулили абзац
            # img_str = ''    # обнулили картинку
            # img_url_prev = ''
            html = html + h2

        if p.name == 'p':
            abzac_str = p.text
            response_gpt3 = Chat_converstaion_p(abzac_str)
            print(response_gpt3)
            html = html + '<p>'+ response_gpt3 + '</p>'
            # abzac_str = abzac_str + p.text + ' '
            # abzac_str = ''
            img_str = ''
            h2 = ''
        if p.name == 'ul' or 'ol':
            responce_gpt3 = Chat_converstaion_ul_ol(p)
            print(p, ' ---> ', responce_gpt3)
            html = html + responce_gpt3


        if p.name == 'table':
            responce_gpt3 = Chat_converstaion_table(p)
            print(p, ' ---> ', responce_gpt3)
            html = html + p

        if p.name == 'blockquote':
            responce_gpt3 = Chat_converstaion_quote(p)
            print(p, ' ---> ', responce_gpt3)
            html = html + p


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
                    img_str = take_url_img_from_wp(full_url)
                except:
                    img_str = ""
            html = html + '<<img class="alignnone size-medium wp-image-29881" src="' + img_str +'"/>'


    #             # # добавлено при включении в текст картинки ....
    #             # abzac_str = abzac_str + '<<img class="alignnone size-medium wp-image-29881" src="' + img_str +'"/>'
    #             # # img_url_prev = img_str
    #
    # # можно вообще убать работу по кортежу, сделать все в список и по очереди добавлять элементы потом в нейронку
    # # добавление кортежа данных
    # all_article_list.append(h2_abzac_tuple)
    # # print('Данные которые разложили кортеж до обновление img --> ', all_article_list)
    # cc = 0
    #

    # print(*all_article_list,sep='\n')

    # # Идет замена картинок и их заливка на сервак
    # for h, p, i in all_article_list:
    #     if i != '':
    #         cc = cc + 1
    # print('количество img', cc)
    #
    # # Идет запрос к WP о загрузке картинок
    # all_article_list2 = []
    # cort = ("", "", "")
    # for h, t, im in all_article_list:
    #     try:
    #         cort = (h, t, take_url_img_from_wp(im))
    #     except:
    #         cort = (h, t, '')
    #     finally:
    #         all_article_list2.append(cort)
    #
    # # print(all_article_list2)
    # return all_article_list2
    return html
# get_h2_text_image('https://vkusvill.ru/media/journal/chto-takoe-sparzha-chem-polezna-i-kak-eye-gotovit.html')
s = get_h2_text_image('https://vsepolezno.com/plants/kapusta/pekinskaya-kapusta-polza-i-vred-ovoshha/')
# s = get_h2_text_image('https://semenagavrish.ru/articles/chudesa-botaniki-kvadratnye-arbuzy/')
# # s = get_h2_text_image('https://skin.ru/article/samye-jeffektivnye-procedury-dlja-vosstanovlenija-volos/')
print('__________ИТОГОВЫЙ КОД__________')
print(s)