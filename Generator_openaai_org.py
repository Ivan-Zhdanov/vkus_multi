# Проверка баланса
# пока не понятно нужна ли она т.к. и так может быть подключены api
import openai
import requests
import datetime
from datetime import datetime


def get_organization(api):
    url = "https://api.openai.com/v1/usage"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api}"}
    date_now = datetime.now().strftime("%Y-%m-%d")
    params = {"date": f"{date_now}"}
    r = requests.get(url, headers=headers, params=params)
    # print(r.raise_for_status())
    return r.json()

#
# API_KEY = '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'
API_KEY = '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'
s = get_organization(API_KEY)
print(s)
