import os
from Parsing_all_page import call_parsing


def parsing_to_list(domain):
    domain2 = domain.split('://')[1]
    print(domain2)
    if domain2 in os.listdir(path='urls'):
        print('уже спарсили урлы сайта')
    else:
        call_parsing(domain)  # Парсинг всех урлов по названию домена (domain) в папку urls

    # открываем файл со спарсенными урлами
    with open('urls/' + domain2, 'r') as file:
        urls_list = file.read().splitlines()  # список всех урлов по домену

    return urls_list

# domain = 'https://vsepolezno.com'
# parsing_to_list(domain)