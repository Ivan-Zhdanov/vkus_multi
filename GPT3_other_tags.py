# Создание нового текста от вопроса в OPENAI
import openai
import time
import re
import requests
from GPT3_API_cheker import api_cheker, list_api
from Get_url_Img_from_WP import take_url_img_from_wp
from Api_List import api_list
import threading
from log_write import log_api
# предыдущий ключ с аккаунта ivan.zhdanov.moscow4
# openai.api_key = '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'

# 28/09
# openai.api_key = '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'

# ключ от аккаунта helloword (5$)
# openai.api_key = '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'

model_id = 'gtp-3.5-turbo'
num_text = ()

apis = api_list
# def th_lsit():
th_list = []
step = 6
#     return th_list

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
        time.sleep(22)
        i = 0
        print('Первый поток 1111111')
        flag = False
        while flag == False:
            print('в потоке 1 api под номером - ', i)
            api1 = apis[i]['api']
            openai.api_key = api1
            openai.organization = apis[i]['org']
            print("Текущий АПИ = ", api1)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    # model="gpt-3.5-turbo",
                    model="gpt-3.5-turbo-16k-0613",
                    max_tokens=2500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text3 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(22)
                apis[i]['err'] = 1

                # запись в лог файл об ошибках по api
                log_api(i, e, api1)

                # берем следующий api
                i = i + 1
                if i > step: i = 0
        return text3


    elif th_list.index(thread_id) == 1:
        time.sleep(22)
        j = step
        print('Второй поток 2222222')

        flag = False
        while flag == False:
            print('в потоке 2 api под номером - ', j)
            api2 = apis[j]['api']
            openai.api_key = api2
            openai.organization = apis[j]['org']
            print("Текущий АПИ = ", api2)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    # model="gpt-3.5-turbo",
                    model="gpt-3.5-turbo-16k-0613",
                    max_tokens=2500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text32 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(22)
                apis[j]['err'] = 1

                # запись в лог файл об ошибках по api
                log_api(j, e, api2)

                # берем следующий api
                j = j + 1
                if j > step*2: j = step

        return text32

    elif th_list.index(thread_id) == 2:
        time.sleep(22)
        k = step*2
        print('Третий поток 333333333')
        flag = False
        while flag == False:
            print('в потоке 3 api под номером - ', k)
            api3 = apis[k]['api']
            openai.api_key = api3
            openai.organization = apis[k]['org']
            print("Текущий АПИ = ", api3)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    # model="gpt-3.5-turbo",
                    model="gpt-3.5-turbo-16k-0613",
                    max_tokens=2500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text33 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(22)
                apis[k]['err'] = 1

                # запись в лог файл об ошибках по api
                log_api(k, e, api3)

                # берем следующий api
                k = k + 1
                if k > step*3: k = step*2
        return text33


    elif th_list.index(thread_id) == 3:
        time.sleep(22)
        h = step*3
        print('Четвертый поток')
        flag = False
        while flag == False:
            print('в потоке 4 api под номером - ', h)
            api4 = apis[h]['api']
            openai.api_key = api4
            openai.organization = apis[h]['org']
            print("Текущий АПИ = ", api4)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    # model="gpt-3.5-turbo",
                    model="gpt-3.5-turbo-16k-0613",
                    max_tokens=2500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text34 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(22)
                apis[h]['err'] = 1
                # запись в лог файл об ошибках по api
                log_api(h, e, api4)

                # берем следующий api
                h = h + 1
                if h > step*4: h = step*3
        return text34




    elif th_list.index(thread_id) == 4:
        time.sleep(22)
        g = step*4
        print('Пятый поток')
    flag = False
    while flag == False:
        print('в потоке 4 api под номером - ', g)
        api5 = apis[g]['api']
        openai.api_key = api5
        openai.organization = apis[g]['org']
        print("Текущий АПИ = ", api5)
        try:
            print("КАКОЙ ЗАПРОС ________________________ ", query)
            responce = openai.ChatCompletion.create(
                # model="gpt-3.5-turbo",
                model="gpt-3.5-turbo-16k-0613",
                max_tokens=2500,
                messages=[
                    {"role": "system", "content": ""},
                    {"role": "user", "content": f"{query}"},
                ]
            )
            text35 = responce['choices'][0]['message']['content']
            print("************")
            flag = True
            break
        except Exception as e:
            print('Название ошибки --', e)
            # if 'RPM' in e:
            time.sleep(22)
            apis[g]['err'] = 1
            # запись в лог файл об ошибках по api
            log_api(g, e, api5)

            # берем следующий api
            g = g + 1
            if g > step*5: g = step*4
    return text35
    # -----------------------------------------------------------------------------------------

    # flag = False
    # i = 0
    # while flag == False:
    #     # print('Номер цикла: ', i)
    #     # # сбросить счетчик после 32 api
    #     # if i >= 1:
    #     #     time.sleep(21)
    #     #     i = 0
    #
    #     # api = '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'
    #     # org = 'org-psxfn6TGWHbSD653IoAC1wlz'
    #     # print(apis[0])
    #     # org = apis[i]['org']
    #     # api = apis[i]['api']
    #
    #     time_now = time.time()
    #     # print('72')
    #     openai.api_key = api
    #     openai.organization = org
    #     print("Текущий АПИ = ", api)
    #     # if int(time_now) - int(apis[i]['time']) > 21:
    #     # убрал чтобы не выходила проверка времени
    #     # if int(time_now) - int(apis[i]['time']) > 21 and int(apis[i]['err'] != 1):
    #     # apis[i]['time'] = time.time()
    #     try:
    #         print("КАКОЙ ЗАПРОС ________________________ ", query)
    #         # openai.api_key = apis[i]['api']
    #         responce = openai.ChatCompletion.create(
    #             # model="gpt-3.5-turbo-16k-0613",
    #             model="gpt-3.5-turbo",
    #             # temperature=0,
    #             # max_tokens=1024,
    #             max_tokens=2500,
    #             messages=[
    #                 {"role": "system", "content": ""},
    #                 {"role": "user", "content": f"{query}"},
    #             ]
    #         )
    #         text3 = responce['choices'][0]['message']['content']
    #         print("************")
    #         flag = True
    #         return text3
    #         # break
    #     except Exception as e:
    #         apis[i]['err'] = 1
    #
    #         print('Название ошибки --', e)
    #         # Если ошибка лимиты в день
    #         if 'RPD' in e:
    #             apis[i]['time'] = time.time() + 24*60
    #         flag = False
    #         i = i + 1
    #         # time.sleep(2)
    #         # Не корректный API - убрать
    #         # if 'Incorrect' in e:
    #         #     apis[i]['err'] = 1
    # else:
    #     print('времени меньше 20 с')
    #     i = i + 1
    #     # time.sleep(2)
    # ---------------------------------
    # time.sleep(21)



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


def Chat_converstaion_p(text21):
    # print('66')
    query21 = f'Перепиши с дополнениями:"""{text21}"""'
    # print('67')
    text41 = GPT3(query21)
    # text44 = re.sub(r'^([«»]+)|([«»]+)$', '', text4)
    print('____ЗАПРОС ОБРАБОТАЛСЯ ____')

    return text41

def Chat_converstaion_ul_ol(text22):
    query22 = f'Перепиши с дополнением оставляя html теги:"""{text22}"""'
    text42 = GPT3(query22)
    # text44 = text4.replace("<li><li>", "<li>").replace("</li></li>", "</li>")

    return text42

def Chat_converstaion_table(text23):
    query23 = f'Перепиши таблицу с дополнением оставляя html теги:"""{text23}"""'
    text43 = GPT3(query23)

    return text43

def Chat_converstaion_quote(text24):
    query24 = f'Перепиши с дополнением оставляя html  теги:"""{text24}"""'
    text44 = GPT3(query24)

    return text44

