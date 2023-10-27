import openai
from openpyxl import load_workbook
import time


def list_api():
    list_api = []
    wb = load_workbook('API_KEYS.xlsx')
    ws = wb.active
    for row in range(1, ws.max_row):
        if ws[f'B{row}'].value < 1000:
            print(f'Взятый API {row}', ws[f'A{row}'].value)
            count = ws[f'B{row}'].value
            ws[f'B{row}'] = count + 1
            API_KEY = ws[f'A{row}'].value
            list_api.append(API_KEY)
            wb.save('API_KEYS.xlsx')
    return list_api

def api_cheker():
    # API_KEY = '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'
    print(time.time())
    wb = load_workbook('API_KEYS.xlsx')
    ws = wb.active

    # вызываем запрос

    API_KEY = None
    # while API_KEY == None:
    while True:
        for row in range(1, ws.max_row):
            # print('НОМЕР СТРОКИ', row)
            if ws[f'B{row}'].value < 1000:
                if int(time.time()) - ws[f'C{row}'].value > 25:
                    print(f'Взятый API {row}', ws[f'A{row}'].value)

                    # запись
                    count = ws[f'B{row}'].value
                    ws[f'B{row}'] = count + 1
                    ws[f'C{row}'] = int(time.time())
                    API_KEY =  ws[f'A{row}'].value
                    wb.save('API_KEYS.xlsx')
                    return API_KEY
            # print('следующий API')
        time.sleep(3)

    # time.sleep(3)


    # вызываем запрос

    # API_KEY = None
    # while API_KEY == None:
    #     for row in range(1, ws.max_row):
    #         if ws[f'B{row}'].value < 50:
    #             # if int(time.time()) - ws[f'C{row}'].value > 20:
    #             print('Взятый API ', ws[f'A{row}'].value)
    #
    #             # запись
    #             count = ws[f'B{row}'].value
    #             ws[f'B{row}'] = count + 1
    #             ws[f'C{row}'] = int(time.time())
    #             API_KEY = ws[f'A{row}'].value
    #             wb.save('API_KEYS.xlsx')
    #             return [row, API_KEY]
    #         print('следующий API')
    # time.sleep(3)

# print(api_cheker())


# # аккаунт word
# openai.api_key = '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'
#
# text2 = """
# Активация по СМС — самый простой способ подтверждения номера при регистрации. Код подтверждения приходит на указанный номер в виде СМС, для завершения регистрации вам необходимо ввести его на сайте или в приложении. Если вы не хотите указывать свой личный номер, воспользуйтесь виртуальным — код придет в ваш личный кабинет SMS-Activate.
# Как приобрести услугу активации по СМС?
# В левом меню на главной странице выберите сервис. Если необходимого сервиса нет, выберите опцию «Любой другой»;
# Определите страну и количество номеров;
# Кликните на иконку-«корзину», чтобы купить номер;
# Номер появится на странице «Активации», скопируйте его и укажите в поле регистрации;
# Код подтверждения появится в карточке активации рядом с номером.
# Важно! Если код по каким-то причинам не придет в течение 20 минут, деньги автоматически вернутся на ваш баланс.
# """
# query = f'Выдели 3-4 ключевых идей из текста. Добавь новые уточняющие мысли и факты:"""{text2}"""'
# responce = openai.ChatCompletion.create(
#     # model="gpt-3.5-turbo-16k-0613",
#     model="gpt-3.5-turbo",
#     # temperature=0,
#     # max_tokens=1024,
#     max_tokens=2500,
#     messages=[
#         {"role": "system", "content": ""},
#         {"role": "user", "content": f"{query}"},
#     ]
# )
# text3 = responce['choices'][0]['message']['content']
# print(text3)
#
#
#
#
#
#
#
#
# #






#
# # openai.api_key = os.getenv(API_KEY)
# API_KEY = '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'
# # data = {'login':'wordh866@gmail.com',
# #         'password':'123456qQ'}
#
#
# # url = 'https://api.openai.com/dashboard/billing/credit_grants'
# # url = 'https://api.openai.com/v1/dashboard/billing/subscription'
# url = 'https://api.openai.com/v1/chat/completions'
# # Регистрация
# headers = {
#   "Content-Type": "application/json",
#   "Authorization": f"Bearer {API_KEY}",
#   'Accept': "*/*", 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }
#
#
# responce = requests.post(url, headers=headers)
#
# # responce = requests.get(url, headers=data)
# print(responce)


# s = list_api()
# print(s)
# q = s.pop()
# print(q)