# Создание нового текста от вопроса в OPENAI
import openai
import time
import re
import requests
from GPT3_API_cheker import api_cheker, list_api
from Get_url_Img_from_WP import take_url_img_from_wp

# предыдущий ключ с аккаунта ivan.zhdanov.moscow4
# openai.api_key = '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'

# 28/09
# openai.api_key = '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'

# ключ от аккаунта helloword (5$)
# openai.api_key = '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'

model_id = 'gtp-3.5-turbo'
num_text = ()

apis = apis = [
{"api":"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","org":"org-JLUvQEIqiOCXct56FSEgQ2ny",'time':0},
{"api":"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","org":"org-v4655xc6zdsugyi4qZLubxNj",'time':0},
{"api":"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","org":"org-tIqGtFWaNq246JFE3uQhs13g",'time':0},
{"api":"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","org":"org-H8FgKHlFLBzhreRuSJcm7dSW",'time':0},
{"api":"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","org":"org-Qoel3tcWLrElQaZJvp257eql",'time':0},
{"api":"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","org":"org-teYqXAPDwzUfcjlBZqQFS939",'time':0},
{"api":"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","org":"org-2TxLYxmO6V1KvlUGxKdeDNLn",'time':0},
{"api":"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","org":"org-L7aRk6OXDZSxB05Ci7schipb",'time':0},
{"api":"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","org":"org-hUJCQdx1gA6IEmpT3fZA2Od4",'time':0},
{"api":"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","org":"org-yOKVcXZqDliuzXVtVNdp7naq",'time':0},
{"api":"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","org":"org-8UaJ9vME2KKTSH3KUqjzHx7J",'time':0},
{"api":"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","org":"org-UKq05wPJNRrfyMwTFhG6Fjpy",'time':0},
{"api":"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","org":"org-4oWbNfwpXtuM5MXxyTDsx3EN",'time':0},
{"api":"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","org":"org-xaXeTK1WOTH3cPMnYE20kteD",'time':0},
{"api":"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","org":"org-cDAupWgrctJ6aULyMUl1W8lq",'time':0},
{"api":"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","org":"org-TthaGmWd4t9D51bY1QN62nmp",'time':0},
{"api":"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","org":"org-WgUUFsfak8nmp0kvacHC0R24",'time':0},
{"api":"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","org":"org-7eQQXBHvZAmigmcEDpylE2SE",'time':0},
{"api":"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","org":"org-RQrpTXBqlxfnty1yqvwfUxHD",'time':0},
{"api":"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","org":"org-OH7hWo7NbfRtFxyCxXVF1qjD",'time':0},
{"api":"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","org":"org-UB9QlJyWvfvDjnwo2ZwdkRKd",'time':0},
{"api":"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","org":"org-e5v2hyRBKHq2dDxxcIEQoZuc",'time':0},
{"api":"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","org":"org-jL2NdpiyJIWKR9fjBzARiNXT",'time':0},
{"api":"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","org":"org-IPEp5TRcE0iy7IbkYinFKDkp",'time':0},
{"api":"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","org":"org-GYlx3dgPkUB1IlKZLNxqA1Zr",'time':0},
{"api":"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","org":"org-JqdqBFA3N47rk2fbp34Iac8H",'time':0},
{"api":"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","org":"org-DMe1ZSbbN7qyRqpFlegB6y1t",'time':0},
{"api":"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","org":"org-v6PaHgWiW0NdX43CNWHhvqWu",'time':0},
{"api":"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","org":"org-r9MHVUjmzkHsEbPR7x3t8hQ7",'time':0},
{"api":"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","org":"org-LSzWw9UPaozY6VAnZ80TgBJB",'time':0},
{"api":"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","org":"org-1Iai7L73YfpHLt46Yis6cIbS",'time':0},
{"api":"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","org":"org-30q24QznMAJj8LkXInNd8hhK",'time':0},
{"api":"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","org":"org-kLcqB2590NveBJM2pYesZ5rd",'time':0},
{"api":"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","org":"org-QTSYQEOWV8v1HrmdzFSJ7ZZu",'time':0},
{"api":"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","org":"org-oniELXuK8SArDuRiABtk8fLF",'time':0},
{"api":"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","org":"org-KfYvOStbFMISX9l7CC3AJfZS",'time':0},
{"api":"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","org":"org-Gq6XfSTlY6nyPEdJ7HZHD7gF",'time':0},
{"api":"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","org":"org-LEKLpI6xGd4NlXpVbuJewzie",'time':0},
{"api":"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","org":"org-qlV6HfJ9ilJRJKoQ6rKzCRjl",'time':0},
{"api":"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","org":"org-FSJp3nxZPmRPgWJJdBFyHVsg",'time':0},
{"api":"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","org":"org-Yc3P7LRGBDfb9TOVxgWXhwx6",'time':0},
{"api":"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","org":"org-pK1bnM7Ob1nATteKSVNNRCRW",'time':0},
{"api":"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","org":"org-D5Y0CsLaevIdVhU4veVcV4RP",'time':0},
{"api":"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","org":"org-uAP369CvssPfen5rnuH6nJx2",'time':0},
{"api":"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","org":"org-Y6rsjj7YkRKQvFXSVYdyPahL",'time':0},
{"api":"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","org":"org-5QUKhf0sFvS04vtmD8zqoDf9",'time':0},
{"api":"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","org":"org-lYpY2s4RS8wqRfVYixK8kwCh",'time':0},
{"api":"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","org":"org-CI0JKrd4U9msZg0ldPGOUU7z",'time':0},
{"api":"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","org":"org-NWCnCStmvIrXlnLIcEhOEJH5",'time':0},
{"api":"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","org":"org-N4pHOn7vfSpvCSDj3dqwduO7",'time':0},
{"api":"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","org":"org-xEK74UDN9OvP264nItYF05Co",'time':0},
{"api":"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","org":"org-zV8RRoABA2NGid7FY8wzRNQF",'time':0},
{"api":"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","org":"org-tWEg4F657oL2bUPIeYReZrDy",'time':0},
{"api":"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","org":"org-7fqSQzpCFISNsHujeBwe7WUn",'time':0},
{"api":"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","org":"org-UVl6Px5a4fFxF6lY37MpTahW",'time':0},
{"api":"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","org":"org-L8x6HQQsxm3prUFWJB50BxN2",'time':0},
{"api":"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","org":"org-P2npiBe9mSXnIbfTd6assEgK",'time':0},
{"api":"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","org":"org-w1IbKIhSiEEzyF3oapj5o7Yc",'time':0},
{"api":"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","org":"org-PAxr1I9jpenI9tI6mgGAhi7k",'time':0},
{"api":"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","org":"org-TeyJLBTK3orrtWGqja0EGebV",'time':0},
{"api":"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","org":"org-omtc2VQu5SWFH0shqy3aWYIO",'time':0},
{"api":"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","org":"org-zeiAQQTGnBvgSoiM5Dc9Mj2w",'time':0},
{"api":"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","org":"org-hmlx91olt9LSwMWdj4W0rI15",'time':0},
{"api":"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","org":"org-WVtH82a66P6BIY05O5e5jXf8",'time':0},
{"api":"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","org":"org-ti0AtndnoVICaKoNOBVE76ng",'time':0},
{"api":"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","org":"org-Swm9BgI7MBkBXyWbLx8q7twG",'time':0},
{"api":"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","org":"org-Qo3H5RrYAieEwjBkVvbO8TwX",'time':0},
{"api":"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","org":"org-y1xDniHOSiJ07g1GyMOcE4I1",'time':0},
{"api":"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","org":"org-ts8o7uVqM55klUd6uqT8FL9r",'time':0},
{"api":"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","org":"org-AdqVFzOGdTHzhvOcQL2YwL4D",'time':0},
{"api":"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","org":"org-9g0P7fUJe98v4y65iW9SUVrZ",'time':0},
{"api":"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","org":"org-R5zHu3iL6v4q2nreUjYoh78g",'time':0},
#  сверху новые аккаунты

{"api":"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","org":"org-c2F6gAhcvLKr8iUhTPM83m95",'time':0},
{"api":"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","org":"org-F138ahY8KG6sHQI1mNWEHKuX",'time':0},
{"api":"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","org":"org-eGZHzlIxP14xiqOF5jxyNVjf",'time':0},
{"api":"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","org":"org-vOrp1v9biSSLV9BTakunbt9b",'time':0},
{"api":"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","org":"org-VwaoA7vwUdmmjaeVLjUwP3UB",'time':0},
{"api":"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","org":"org-7Z0mU40Nc9WQRjyFj6L0joal",'time':0},
{"api":"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","org":"org-nzFZKQwB7qGCNPltIjDj5Hcf",'time':0},
{"api":"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","org":"org-recbE9TFaxDkDKgSjtzUYKo5",'time':0},
{"api":"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","org":"org-KSmOQXKrDl71ssG1z2xxjLay",'time':0},
{"api":"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","org":"org-tFuXexbQVxNvaF49BaeAceOD",'time':0},
{"api":"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","org":"org-5cWrj5HWangHuW3VAfGchtdj",'time':0},
{"api":"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","org":"org-MYYYbpxKDGiaFEDlto8d8s8a",'time':0},
{"api":"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","org":"org-mlTPHgEOzZ0M3OPueJ5mQMrA",'time':0},
{"api":"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","org":"org-AYXJnA18jT1gZDJY7mxqOOhM",'time':0},
{"api":"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","org":"org-W6xjkRqTsVj2LyRYbS3qmJUL",'time':0},
{"api":"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","org":"org-GZo84AD5JpnPdj4XHSj8hC2o",'time':0},
{"api":"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","org":"org-e88ctB70bh4gPZahH67cBE6A",'time':0},
{"api":"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","org":"org-cpPheZJ6Yz2OgbeOHEK0ygtb",'time':0},
{"api":"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","org":"org-u3g6OKfclmfK4ze9u9uvchWU",'time':0},
{"api":"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","org":"org-zbVZjFF1eUsk8COBdXVrgWk5",'time':0},
{"api":"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","org":"org-2HkDOd9MnDUufPoZtwqt7xug",'time':0},
{"api":"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","org":"org-IGRrq8WxwWdlYa8raGepPmO7",'time':0},
{"api":"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","org":"org-VBVoFLaY5fhnapJwKaBRqhSe",'time':0},
{"api":"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","org":"org-MrySNb9On13HJRM6yA2zPWaS",'time':0},
{"api":"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","org":"org-dVw6Gge1g9Q0CRBakcztQ6CT",'time':0},
{"api":"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","org":"org-OJAszY9isIM0DvgcOUMq9vCe",'time':0},
{"api":"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","org":"org-5u380WNU2tt6fRWWoWHKO4vj",'time':0},
{"api":"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","org":"org-w3gt0jbTahOusj5JX5RsxhcS",'time':0},
{"api":"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","org":"org-Q8PguFoj46xKQCLbPWQrWlwy",'time':0},

{'api': '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', 'org': 'org-F138ahY8KG6sHQI1mNWEHKuX','time':0},
{'api': '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', 'org': 'org-7Z0mU40Nc9WQRjyFj6L0joal','time':0},
{'api': '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', 'org': 'org-RWwKRxAkZfRzT2jZXgKGZ2A5','time':0},
{'api': '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', 'org': 'org-TeyJLBTK3orrtWGqja0EGebV','time':0},
{'api': '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', 'org': 'org-5cWrj5HWangHuW3VAfGchtdj','time':0},
{'api': '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', 'org': 'org-WVtH82a66P6BIY05O5e5jXf8','time':0},
{'api': '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', 'org': 'org-PAxr1I9jpenI9tI6mgGAhi7k','time':0},
{'api': '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', 'org': 'org-c2F6gAhcvLKr8iUhTPM83m95','time':0},
{'api': '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', 'org': 'org-F138ahY8KG6sHQI1mNWEHKuX','time':0},
{'api': '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', 'org': 'org-eGZHzlIxP14xiqOF5jxyNVjf','time':0},
{'api': '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', 'org': 'org-vOrp1v9biSSLV9BTakunbt9b','time':0},
{'api': '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', 'org': 'org-VwaoA7vwUdmmjaeVLjUwP3UB','time':0}]




def GPT3(query):
    flag = False
    i = 0
    while flag == False:
        # print('71')
        # api = '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'
        # org = 'org-PAxr1I9jpenI9tI6mgGAhi7k'
        # print(apis[0])
        api = apis[i]['api']
        # org = apis[i]['org']
        time_now = time.time()
        # print('72')
        openai.api_key = api
        # openai.organization = org
        print("Текущий АПИ = ", api)
        if int(time_now) - int(apis[i]['time']) > 21:
            apis[i]['time'] = time.time()
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

                # Если ошибка лимиты в день
                if 'RPD' in e:
                    apis[i]['time'] = time.time() + 24*60
                flag = False
                i = i + 1
                time.sleep(2)
        else:
            print('времени меньше 20 с')
            i = i + 1
    return text3


def Chat_converstaion_ppp(tag):
    html = ''
    print('ТЕКУЩИЙ ТЕГ:', tag)
    try:
        if  tag.name == 'h2' or tag.name == 'h3':
            h2 = tag.text
            print(h2)
            html = '<h2>' + h2 + '</h2>'


        elif tag.name == 'p':
            abzac_str = tag.text
            flag = False
            while flag == False:
                try:
                    print('строка ', abzac_str)
                    r1 = Chat_converstaion_p(abzac_str)
                    r1_clean = re.sub(r'^([«»]+)|([«»]+)$', '', r1)
                    html = '<p>' + r1_clean + '</p>'
                    flag = True
                except:
                    print('ошибка в теге Р')
                    html = ''
                    print('ожидание 20c ...')
                    time.sleep(20)



        elif tag.name == 'ul' or tag.name == 'ol':
            r2 = Chat_converstaion_ul_ol(tag)
            print(tag, ' ---> ', r2)
            html = r2

        elif tag.name == 'table':
            r3 = Chat_converstaion_table(tag)
            print(tag, ' ---> ', r3)
            html = r3

        elif tag.name == 'blockquote':
            r4 = Chat_converstaion_quote(tag)
            print(tag, ' ---> ', r4)
            html = r4

        elif tag.name == 'img':
            print('------_', tag)
            src_value = None
            src_list = ['src', 'data-src', 'src-lazy']
            print('________', src_value)
            for s in src_list:
                print('ssssssss', s)
                src_value = tag.get(s)
                print('valueeeeeeeee', src_value)
                # нашли первый src
                if src_value:
                    break
            if src_value:
                print('valuee intooooo', src_value)
                # закрыл обработку если урл не полный и его соединение с базовым урлом
                # full_url = requests.compat.urljoin(url_1, src_value)
                full_url = src_value
                print(full_url)
                img_str = full_url
                # Добавление тега с картиной с урлом
                try:
                    img_str = take_url_img_from_wp(full_url)
                except:
                    img_str = ""
                print('полученный адрес картинки', img_str)
            html = '<img class="alignnone size-medium wp-image-29881" src="' + img_str + '"/>'

        elif tag.name == 'iframe':
            print(tag, ' ---> ')
            html = str(tag)

        else:
            print('тег не найден')
    except:
        print('какая то ошибка с тегами')
    return html


def Chat_converstaion_p(text2):
    # print('66')
    query2 = f'Перепиши с дополнениями:"""{text2}"""'
    # print('67')
    text4 = GPT3(query2)
    return text4

def Chat_converstaion_ul_ol(text2):
    query2 = f'Перепиши с дополнением оставляя html теги:"""{text2}"""'
    text4 = GPT3(query2)
    return text4

def Chat_converstaion_table(text2):
    query2 = f'Перепиши таблицу с дополнением оставляя html теги:"""{text2}"""'
    text4 = GPT3(query2)
    return text4

def Chat_converstaion_quote(text2):
    query2 = f'Перепиши с дополнением оставляя html  теги:"""{text2}"""'
    text4 = GPT3(query2)
    return text4



#
# ls = [<p>У вас на кухне находится много продуктов, полезные свойства которых мы просто не представляем. Обескураженные популярными мифами, мы отказываемся от употребления в пищу здоровой еды, что является ошибкой. Вряд ли кто-то понимает, что среди этих, казалось бы, средних продуктов есть настоящие герои. Их вклад в здоровье трудно переоценить.</p>, <p>Диетологи много лет пытались определить, что служит причиной болезней, с которыми сталкиваются люди. Как и судьи, иногда они делают ошибки, обвиняя невинную еду в ужасных преступлениях против тела.<br/>
# Обыватели изучают сотни сообщений о предполагаемой вредности продуктов о которых пойдёт речь ниже и, действуя в ущерб себе, удаляют их из рациона.<br/>
# Следует выступить адвокатом любимых продуктов и опровергнуть мифы о некоторых из них, представив их преимущества, чтобы вы могли поедать их без угрызений совести.</p>, <h2>Тунец – вреден или полезен?</h2>, <p>Многих, сидящих на диете, предостерегают от употребления в пищу этой рыбы из-за того, что она якобы может содержать тяжелые металлы и токсины.</p>, <iframe allowfullscreen="allowfullscreen" height="314" src="//www.youtube.com/embed/yjckrFACdaA" width="560"></iframe>, <img class="aligncenter wp-image-7417" decoding="async" height="413" loading="lazy" sizes="(max-width: 734px) 100vw, 734px" src="https://vsepolezno.com/wp-content/uploads/2021/01/18-1.jpg" srcset="https://vsepolezno.com/wp-content/uploads/2021/01/18-1.jpg 800w, https://vsepolezno.com/wp-content/uploads/2021/01/18-1-768x432.jpg 768w" width="734"><br/>
# Однако никто не советует вам покупать рыбу вьетнамского происхождения.<br/>
# Вы можете купить ее из надежного источника. Просто посмотрите на упаковку. Производитель указывает страну отлова.</img>, <blockquote class="shortcodestyle info">Все тунцы из высокоразвитых стран можно считать более безопасными.</blockquote>, <p>Хотя они дороже, иногда даже в два раза, лучше быть уверенным, что вы ничего плохого не едите. А как насчет тяжелых металлов?<br/>
# Тунец является крупным хищником и находится в конце пищевой цепи, и, таким образом, он особенно подвержен накоплению ртути или свинца в организме.<br/>
# Однако вам не нужно бояться вредных последствий употребления этих металлов, если вы едите тунца в умеренных количествах.<br/>
# Дважды в неделю он еще никому не причинял вреда.<br/>
# Существуют общие нормы и правила, не позволяющие распространять мясо с тяжелыми металлами выше безопасного предела.</p>, <h3>Плюсы применения тунца в пищу, витаминный состав</h3>, <p>Преимущество тунца, несомненно, заключается в высоком содержании омега-3 жирных кислот, а они хорошо влияют на систему кровообращения и помогают в борьбе с вредом от холестерина. Помимо снижения уровня холестерина, они также оказывают положительное влияние на мозг.<br/>
# Еще одним преимуществом тунца считается высокое содержание витамина А, положительно влияющий на зрение, и витамина D, влияющего на здоровье костей.<br/>
# Кроме того, мясо этой рыбы содержит значительное количество витаминов группы В и, как и любая морская рыба, йод, отвечающий за регуляцию щитовидной железы.<br/>
# Преимуществом тунца можно назвать обогащение диеты селеном, это редкий элемент, необходимый для функционирования ферментных систем, укрепления иммунитета и замедления старения.<br/>
# Если вы не беременная женщина, вы можете есть тунца до 140 г в неделю, не беспокоясь о своем здоровье.</p>, <h2>Яйца</h2>, <p>Распространенный миф — высокий уровень холестерина в яйцах, что отвращает многих от частого употребления их в пищу и налагает ограничения в размере шести яиц в неделю.</p>, <p>Все люди действительно разные, поэтому кто-то с небольшим телосложением может сделать 3 приема пищи из 6 яиц, в то время как кто-то крупнее и тяжелее лучше съест их сразу. Глупо устанавливать универсальное максимальное потребление яиц в неделю.<br/>
# Ученые провели ряд исследований и по результатам они не наблюдали повышения уровня холестерина после яичной диеты, и все же многие все еще убеждены в их вредности.<br/>
# Зато в желтке много лецитина.  Это антиоксидант с широким спектром активности в организме. Прежде всего, он снижает уровень холестерина, которого мы так боимся в яйцах. Во-вторых, лецитин участвует в обмене веществ, является компонентом нейронов в мозге и защитным барьером для желудка.</p>, <blockquote class="shortcodestyle info">Достаточно известный фитнес блогер и бодибилдер Миша Прыгунов заявляет, что ежедневно по утрам поедает яичницу из шести яиц, удаляя только два желтка</blockquote>, <p>Яйца также служат источником витаминов A, E, D и K, а также B2 и B12. Кроме того, в них можно найти калий, серу, фосфор, железо, цинк.<br/>
# Другим «волшебным» соединением в желтке является лютеин — соединение, защищающее глаза от радиации и улучшает зрение.<br/>
# Яйца любят есть также девушки, соблюдающие диету, потому что они легко усваиваются и содержат мало калорий. Одно среднее яйцо — всего 75 ккал.</p>, <h2>Молоко</h2>, <p>Лактоза, содержащаяся в молоке, не переносится 25% взрослых людей. Если вы принадлежите к их количеству, откажитесь от молока.Однако, если вы переносите лактозу, непонятно, почему вы должны отказаться от молока.<br/>
# Возможно, вы слышали, что молочный белок казеин не нужен людям, потому что он используется для создания рогов и копыт у телят. Это забавный слух, распространенный давным-давно одним некомпетентным ученым.</p>, <p>Человеческое молоко имеет состав, аналогичный коровьему, и тоже содержит казеиновый белок, хотя и в меньших количествах.</p>, <h3>Про аминокислоты</h3>, <p>Белки распадаются на аминокислоты во время пищеварения. Есть 20 основных аминокислот, необходимых для регенерации и роста человека. Казеин — это животный белок, содержащий их набор, поэтому во время пищеварения организм приобретает необходимые «строительные блоки», из которых он может построить любые человеческие клетки.<br/>
# Молочный белок имеет разное время переваривания, что позволяет вам постоянно снабжать ваш организм питательными веществами.</p>, <p>Еще одним слабым аргументом, побуждающим отказаться от молока, является тот факт, что только люди пьют молоко после окончания младенческого возраста.<br/>
# И всё же, мнение о вредности молока неестественно, ведь мы единственные животные, не отказывающиеся от молока после окончания периода младенчества. Однако стоит понимать, что люди, в отличие от животных, используют мыло, салфетки или зубные щетки, которые никто не считает неестественными и вредными для здоровья. Мы — высший вид, и поэтому ведем себя иначе, чем животные.<br/>
# Последняя неправильная причина, почему молоко должно быть плохим, — это мнение, что оно вызывает вздутие живота и запоры. Но это подмена понятий, ведь только те, кому поставлен диагноз непереносимости лактозы, плохо реагируют на потребление молока. Желудок большинства из нас приспособлен к перевариванию молока и не чувствует дискомфорта после его употребления.<br/>
# Болеющие язвой желудка основывают свой рацион на молочных продуктах, потому что они облегчают боль. Разве это не говорит о пользе молока?<br/>
# Лучше всего пить двухпроцентное по жирности молоко, потому что он содержит растворенные витамины A, D, E и K. Кроме того, молочные продукты служат одним из лучших источников кальция, предотвращая остеопороз и гарантируя рост костей у детей.</p>, <h2>Красное мясо</h2>, <p>Сотни, если не тысячи одептов подсели на вегетарианскую диету, прочитав о недостатках красного мяса.<br/>
# Прежде всего, считается, что оно вызывает повышение уровня холестерина. Это правда, хотя следует отметить, что не само мясо несет ответственность за наиболее быстрое поступление этого вредного соединения, а транс-жиры, содержащиеся также в готовых продуктах, маргарине или сладостях.</p>, <blockquote class="shortcodestyle warning"> Вы можете предотвратить избыток холестерина, употребляя ненасыщенные жирные кислоты, которыми, среди прочего, богаты морская рыба или оливковое масло. </blockquote>, <p>Мясо также не несет вины за лишний вес, потому что, как и три продукта, упомянутых выше, оно — отличный источник белка.</p>, <img class="aligncenter size-full wp-image-7416" decoding="async" height="533" loading="lazy" sizes="(max-width: 800px) 100vw, 800px" src="https://vsepolezno.com/wp-content/uploads/2021/01/25-1.jpg" srcset="https://vsepolezno.com/wp-content/uploads/2021/01/25-1.jpg 800w, https://vsepolezno.com/wp-content/uploads/2021/01/25-1-768x512.jpg 768w" width="800"><br/>
# Это строительный материал мышц и органов, необходимый для регенерации. Для переваривания белка необходима дополнительная энергия. Кроме того, белок долго усваивается, предотвращая перекусы.<br/>
# Поэтому глупо обвинять продукт, содержащий большое количество белка, в проблемах с контролем веса, тем более, что если кому-то не нравится жир, он может убрать его перед приготовлением.</img>, <h3>Химический состав мяса</h3>, <p>Красное мясо также содержит ценные микро- и макроэлементы.<br/>
# Например, цинк, отвечающий за здоровье кожи и волос. Мясо также богато железом, без которого не было бы энергии и витаминов группы В.<br/>
# Но красное мясо в избыточном количестве, и особенно содержащийся в нем L-карнитин, может привести к гибели кишечных бактерий, поэтому, если вы любите стейки, ешьте много йогурта и других кисломолочных продуктов, чтобы восполнить микрофлору кишечника.<br/>
# Ученые доказали, что более высокое потребление мяса связано с повышенным риском развития рака. И здесь было установлено безопасное количество потребления в течение недели — 400 грамм.<br/>
# Средний россиянин ест 1500 грамм в неделю, поэтому не будем удивляться тому, что мы нация с большим процентом людей онкологией и с избыточным весом.<br/>
# В потреблении красного мяса, как и везде, важна умеренность. Полное его игнорирование и мясная одержимость одинаково вредны.</p>, <h2>Фрукты</h2>, <p>Возможно, вы были удивлены, обнаружив такую респектабельную и невинную группу продуктов в этом списке. Кто в здравом уме не рекомендовал бы есть фрукты?<br/>
# Ну, такие голоса раздаются все чаще и чаще. И обычно они обращены к людям, желающим похудеть.</p>, <p>Фрукты содержат много сахара и из-за этого многие утверждают, что их надо исключить из рациона. Насмотревшись зарубежных фильмов, где домохозяйка по утрам кидает пару апельсинов в блэндер и потом залпом выпивает такой коктейль, мы делаем также, однако, быстро понимаем, что это очень агрессивный для желудка субстракт, а всего то надо не забывать добавить много воды в такой коктейль. И по этой причине некоторые врачи советуют переключаться на овощи. Но разве диетологи, советующие есть только овощи, не знают, что фрукты содержат ряд других соединений, которые не найти ни в одном овоще? Знают ли они, что у большинства фруктов гликемический индекс ниже, чем у хлеба, пива или макарон?</p>, <blockquote><p>Гликемический индекс является показателем скорости поглощения энергии из пищи. Чем ниже значение IG, тем лучше, потому что это означает высвобождение глюкозы.<br/>
# Лишь немногие фрукты имеют высокий ГИ и, следовательно, могут способствовать ожирению из-за быстрых всплесков инсулина.</p></blockquote>, <p>Гликемический индекс является показателем скорости поглощения энергии из пищи. Чем ниже значение IG, тем лучше, потому что это означает высвобождение глюкозы.<br/>
# Лишь немногие фрукты имеют высокий ГИ и, следовательно, могут способствовать ожирению из-за быстрых всплесков инсулина.</p>, <p>К тому же, каждый фрукт содержит ряд специализированных антиоксидантов, которые предотвращают рак, омолаживают и восстанавливают организм.</p>, <h2>Каков же итог нашего адвокатства?</h2>, <p>Не имеется причины, по которой вы должны бросать какие либо продукты питания в одну сумку с надписью: «Не рекомендуется». Любой из них своеобразен, поэтому важно кушать разные блюда, чтобы получать из них все ценные вещества для организма. Разнообразная диета — залог здоровья. Только благодаря этому вы обеспечите себя необходимыми витаминами и микроэлементами на всю жизнь.</p>
#

# text2 = 'Шалтай балтай'
# s = Chat_converstaion_p(text2)
# print(s)