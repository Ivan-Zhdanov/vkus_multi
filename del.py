from bs4 import BeautifulSoup
import requests

l =[]
with open('./urls/vsepolezno.com', 'r') as f:
    st = f.readlines()
print(st)

for s in st:
    url = s.replace('\n', '')
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    if len(soup.text) >8000:
        print(url)