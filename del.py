from bs4 import BeautifulSoup
import requests

# s = 'https://fructberry.com/yagody/chernika/mesta-proizrastaniya'
# s = 'https://fructberry.com/frukty/finiki'
# s = 'https://style.rbc.ru/health/606e97389a7947f4ef64a9e8'
s = 'https://rskrf.ru/tips/eksperty-obyasnyayut/polza-i-vred-finikov-dlya-organizma/'
r = requests.get(s)


html = """
<h2>
<p>
	 Питательная ценность и состав фиников
</p>
</h2>"""




soup = BeautifulSoup(html, "html.parser")
# print(soup)

h2s = soup.find_all('h2')
for h2 in h2s:
    tags = h2.find_all('p')
    for tag in tags:
        print(' ddd',tag)
        tag.unwrap()

print(soup)


