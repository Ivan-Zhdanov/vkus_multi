# Создание нового текста от вопроса в OPENAI
import openai
import time
import re
import requests
from GPT3_API_cheker import api_cheker, list_api
from Get_url_Img_from_WP import take_url_img_from_wp
from Api_List import api_list
import threading
# предыдущий ключ с аккаунта ivan.zhdanov.moscow4
# openai.api_key = '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'

# 28/09
# openai.api_key = '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'

# ключ от аккаунта helloword (5$)
# openai.api_key = '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'

model_id = 'gtp-3.5-turbo'
num_text = ()

apis = api_list
th_list = []

def response_gpt():
    return 0


def GPT3(query):
    org =''
    api = ''
    # Создали список из потоков которые обрабатывают
    thread_id = threading.current_thread().ident
    print(f"Текущий номер потока: {thread_id}")
    if thread_id in th_list:
        pass
    else:
        try:
            th_list.append(thread_id)
        except:
            pass

    # time.sleep(21)

    # print('71')
    if th_list.index(thread_id) == 0:

        i = 0
        print('Первый поток 1111111')
        # api = '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'
        # org = 'org-ti0AtndnoVICaKoNOBVE76ng'
    elif th_list.index(thread_id) == 1:
        # time.sleep(20)
        i = 1
        print('Второй поток 2222222')
        # api = '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'
        # org = 'org-recbE9TFaxDkDKgSjtzUYKo5'
    elif th_list.index(thread_id) == 2:
        # time.sleep(20)
        i = 2
        print('Третий поток 333333333')
        # api = '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'
        # org = 'org-nzFZKQwB7qGCNPltIjDj5Hcf'
    elif th_list.index(thread_id) == 3:
        # time.sleep(20)
        i = 3
        print('Четвертый поток')
        # api = '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'
        # org = 'org-7Z0mU40Nc9WQRjyFj6L0joal'
    elif th_list.index(thread_id) == 4:
        # time.sleep(20)
        i = 4
        print('Пятый поток')
        # api = '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'
        # org = 'org-Swm9BgI7MBkBXyWbLx8q7twG'
    flag = False
    # i = 0
    while flag == False:
        print('Номер цикла: ', i)
        # сбросить счетчик после 32 api
        if i >= 1:
            time.sleep(21)
            i = 0

        # api = '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'
        # org = 'org-psxfn6TGWHbSD653IoAC1wlz'
        # print(apis[0])
        org = apis[i]['org']
        api = apis[i]['api']

        time_now = time.time()
        # print('72')
        openai.api_key = api
        openai.organization = org
        print("Текущий АПИ = ", api)
        if int(time_now) - int(apis[i]['time']) > 21:
        # if int(time_now) - int(apis[i]['time']) > 21 and int(apis[i]['err'] != 1):
            apis[i]['time'] = time.time()
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                # openai.api_key = apis[i]['api']
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
                apis[i]['err'] = 1

                print('Название ошибки --', e)
                # Если ошибка лимиты в день
                if 'RPD' in e:
                    apis[i]['time'] = time.time() + 24*60
                flag = False
                i = i + 1
                # time.sleep(2)
                # Не корректный API - убрать
                # if 'Incorrect' in e:
                #     apis[i]['err'] = 1
        else:
            print('времени меньше 20 с')
            i = i + 1
            # time.sleep(2)

    time.sleep(21)






    #  отключил
    # return text3


def Chat_converstaion_ppp(tag):
    html = ''
    print('ТЕКУЩИЙ ТЕГ:', tag)
    try:
        if tag.name == 'h2' or tag.name == 'h3':
            h2 = tag.text
            print(h2)
            html = '<h2>' + h2 + '</h2>'


        elif tag.name == 'p':
            abzac_str = tag.text
            flag = False
            if len(abzac_str) < 40:
                html = abzac_str
                flag = True

            while flag == False:
                try:
                    print('строка ', abzac_str)
                    r1 = Chat_converstaion_p(abzac_str)
                    print('вызвали обработку р нейронкой')
                    r1_clean = re.sub(r'^([«»]+)|([«»]+)$', '', r1)
                    html = '<p>' + r1_clean + '</p>'
                    flag = True
                except Exception as e:
                    print('ошибка в теге Р ', e)
                    html = ''
                    print('ожидание 10c ...')
                    time.sleep(2)



        elif tag.name == 'ul' or tag.name == 'ol':
            r2 = Chat_converstaion_ul_ol(tag)
            print(tag, ' ---> ', r2)
            r21 = r2.replace("<li><li>","<li>").replace("</li></li>","</li>")
            html = r21

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
                if r'https://polzaivrededy.ru' in src_value:
                    full_url = src_value
                else:
                    full_url = 'https://polzaivrededy.ru' + src_value
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
    # text44 = re.sub(r'^([«»]+)|([«»]+)$', '', text4)
    print('____ЗАПРОС ОБРАБОТАЛСЯ ____')

    return text4

def Chat_converstaion_ul_ol(text2):
    query2 = f'Перепиши с дополнением оставляя html теги:"""{text2}"""'
    text4 = GPT3(query2)
    # text44 = text4.replace("<li><li>", "<li>").replace("</li></li>", "</li>")

    return text4

def Chat_converstaion_table(text2):
    query2 = f'Перепиши таблицу с дополнением оставляя html теги:"""{text2}"""'
    text4 = GPT3(query2)

    return text4

def Chat_converstaion_quote(text2):
    query2 = f'Перепиши с дополнением оставляя html  теги:"""{text2}"""'
    text4 = GPT3(query2)

    return text4

