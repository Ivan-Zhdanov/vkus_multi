from bs4 import BeautifulSoup
import requests

# url = 'https://pandaforecast.com/stock_forecasts/'
# url = 'https://pandaforecast.com/forex/'
# url = 'https://pandaforecast.com/crypto/'
url = 'https://polzavred-edi.ru/category/bobovye/'

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print(soup)

# tickers = soup.find_all('div', class_='stock_box_home_page_1')
# for ticker in tickers:
#     tr = ticker.find('div', class_='stock_box_home_page_ticker')
#     print(tr)