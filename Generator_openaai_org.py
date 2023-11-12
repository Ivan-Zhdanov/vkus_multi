# Проверка баланса
# пока не понятно нужна ли она т.к. и так может быть подключены api
import openai
from openai import organization
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
    print(r.json())
    return r.json()['data'][0]['organization_id']

def open_file(file_name):
    api_org = []
    with open(file_name) as f:
        s = f.readlines()

    for el in s:
        api = el.split(':')[1].replace('\n','')
        try:
            org = get_organization(api)
        except:
            api_org =""
            continue
        dict = {'api': f'{api}',
                'org': f'{org}'}
        api_org.append(dict)
    return api_org




def get_organization2(api_key):
    openai.api_key = api_key
    # response = openai.Organization.retrieve
    response = openai.organization
    return response

#
# # API_KEY = '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'
# API_KEY = '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'
# s = get_organization(API_KEY)
# print(s)

# f = '05a50e.txt'
# s = open_file(f)
# print(s)
api_key = "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"
# s = get_organization2(api_key)
# print(s)



