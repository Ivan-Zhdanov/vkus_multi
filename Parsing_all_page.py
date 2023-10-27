import threading, os
from usp.tree import sitemap_tree_for_homepage
import time


# в файле domains.txt находится список доменов которых сделать карту
# сделанные карты записываются в папку urls в документ с названием домена
# Парсер УНИВЕРСАЛЬНЫЙ


bad_domains = []
# В базовом варианте
# blocks = ['/page', '/tag']
# чтение файла с плохими частями которые находятся в Url файла
with open('Bad_Pages_Blocked.txt', 'r+') as file:
    blockz = file.readlines()
    blocks = [(lambda i: i.replace('\n',''))(i) for i in blockz]
# print(blocks)


def parse_sitemap(domain):
  domain = domain.strip()
  url = f'http://{domain}/'

  # url = 'https://goodcreditonline.com/'
  # url = 'https://migrantplanet.com/'

  sitemap = sitemap_tree_for_homepage(url)
  urls = {page.url for page in sitemap.all_pages()}
  urls = list(urls)

  # чистка списка
  for url in urls:
    try:
      if blocks in url:
        urls.remove(url)
    except:
      pass

  print('**** ', len(urls))
  print(0000, urls)
  # for url in urls:
  # with open(f'site_map.txt', "w+", encoding="utf-8") as file:
  with open(f'urls/'+domain, "w+", encoding="utf-8") as file:
    file.write('\n'.join(urls))
    end_time = time.time()
    print(f"ВРЕМЯ ____ ", {end_time - start_time})

start_time = time.time()

def call_parsing(domain):
    th = []
    # with open("domains.txt") as domains:
    #     for domain in domains:
    thread = threading.Thread(target=parse_sitemap, args=(domain,))
    th.append(thread)
    thread.start()

    for t in th:
        t.join()

# domain = 'ferma.expert'
# call_parsing(domain)