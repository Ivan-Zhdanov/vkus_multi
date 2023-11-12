# -*- mode: python ; coding: utf-8 -*-
# скорость низкая (-)
# Заменил на Parsing_All_Page


import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from multiprocessing import Pool
import time

# url = 'https://finzz.ru'
links = []
links_page = []
links_clear = []
# URL = 'https://mvagro.ru/'
URL = 'https://kladovaia-krasoti.ru'
# URL = 'https://cabinet-bank.ru/'
# URL = 'https://migrantplanet.com/'
clean_el = ['.doc', '/tag',  'wp-content', '/uploads', '/sitemap', '#', 'privacy-policy']
clean_el_2 = ['/page', '/category', '/sitemap', '/page', ]


# создается список с первой страницы со всеми urls
def take_url(i):
    # print("444r", links[i])
    return links[i]


# def parse(url):
def parse(url, i):


    if url == None:
        print("Парсинг завершен")
        return print('Завершение')
    try:
        website = requests.get(url)
        soup = BeautifulSoup(website.text, "lxml")
        for link in soup.find_all('a'):
            link_page = link.get('href')
            # print(888, link_page)
            if URL in link_page:
                check = 0
                for el in clean_el:
                    if el in link_page:
                        check = 0
                        break
                    else:
                        check = 1

                if link_page in links or check == 0:
                    pass
                    # print('ссылка уже есть или она не сайта')
                else:
                    links.append(link_page)
                    # with open("1.txt", "a") as file:
                    #     file.writelines(link_page + '\n')
        print("СПИСОК- ", links)
    except:
        pass
    finally:
        # print(links)
        i = i + 1
        try:
            # take_url(i)

            links_srez = links[i:i+5]
            links_srez = links[0:5]
            print(links_srez)
            # with Pool(5) as p:
            #     p.map(parse(), links_srez)

            parse(links[i], i)
        except:
            print(7777, links)
            return


if __name__ == "__main__":
    start_time = time.time()
    # отправляем УРЛ
    parse(URL, 0)
    print(999, links)


    # чистка списка
    for elem in clean_el_2:
        for link in links:
            if elem in link:
                links.remove(link)

    print('ITOG ',links)
    with open('../pars.txt', "w+") as file:
        for url in links:
            file.writelines(url)
    # for _ in map(print, links_clear):
    #     pass
    end_time = time.time()
    print(f"ВРЕМЯ ____ ", {end_time - start_time})