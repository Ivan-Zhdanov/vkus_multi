# Создание нового текста от вопроса в OPENAI
import openai
import time
from Wrap_text_simple import wrap_tags3
from GPT3_API_cheker import api_cheker, list_api


# предыдущий ключ с аккаунта ivan.zhdanov.moscow4
# openai.api_key = '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'

# 28/09
# openai.api_key = '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'

# ключ от аккаунта helloword (5$)
# openai.api_key = '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'

model_id = 'gtp-3.5-turbo'
num_text = ()

apis = [{'api': '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',
            'org': 'org-P2npiBe9mSXnIbfTd6assEgK'},
        {'api': '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',
           'org': 'org-recbE9TFaxDkDKgSjtzUYKo5'},
        {'api': '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',
            'org': 'org-oPaqKkEuv9yRhCw4ovdHf0N8'}
        ]




def GPT3(query):
    flag = False
    i = 0
    while flag == False:

        # api = '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'
        # org = 'org-PAxr1I9jpenI9tI6mgGAhi7k'
        print(apis[0])
        api = apis[i]['api']
        org = apis[i]['org']
        openai.api_key = api
        openai.organization = org
        print("Текущий АПИ = ", api)
        try:
            print("КАКОЙ ЗАПРОС ________________________ ", query)

            responce = openai.ChatCompletion.create(
                # model="gpt-3.5-turbo-16k-0613",
                model="gpt-3.5-turbo",
                # temperature=0,
                # max_tokens=1024,
                max_tokens=2500,
                messages=[
                    {"role": "system", "content": ""},
                    {"role": "user", "content": f"{query}"},
                ]
            )
            text3 = responce['choices'][0]['message']['content']
            print("************")
            flag = True
            return text3
            break
        except Exception as e:
            print('Название ошибки --', e)
            flag = False
            i = i + 1
            time.sleep(2)
    return text3


def Chat_converstaion_p(text2):
    query2 = f'Перепиши с дополнениями:"""{text2}"""'
    text4 = GPT3(query2)
    return text4

def Chat_converstaion_ul_ol(text2):
    query2 = f'Перепиши с дополнением оставляя теги:"""{text2}"""'
    text4 = GPT3(query2)
    return text4

def Chat_converstaion_table(text2):
    query2 = f'Перепиши таблицу с дополнением оставляя теги:"""{text2}"""'
    text4 = GPT3(query2)
    return text4

def Chat_converstaion_quote(text2):
    query2 = f'Перепиши с дополнением оставляя теги:"""{text2}"""'
    text4 = GPT3(query2)
    return text4




# text2 = 'Шалтай балтай'
# s = Chat_converstaion_p(text2)
# print(s)