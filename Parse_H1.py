from bs4 import BeautifulSoup
import requests
import time

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'Accept': '*/*'}

def parse_h1(URL):
    max_retries = 3
    for _ in range(max_retries):
        r = requests.get(url=URL, headers=HEADERS)
        print('1')
        html = r.text
        print('2')
        if r.status_code == 200:
            print(r.status_code)
            soup = BeautifulSoup(html, "lxml")
            h1 = soup.h1.get_text()
            break
        else:
            print("Попытка открытия сайта №:", _)
            time.sleep(5)
    return h1
# parse_h1('https://migrantplanet.com/v-kakie-strany-mozhno-vyezzhat-sotrudnikam-fsb-spisok/')
