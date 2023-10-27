from Parsing_all_page import call_parsing
# from parsing.take_url import take_url
from Parse_H1 import parse_h1
# from Parsing_Google import search_results
import os

# from Paragraf4 import merge_4_links
from Paragraf5 import merge_4_links

from Different_Paragraf import agenta
from Parsing_Google2 import parsing_google, parsing_yandex
from GPT3_openai_4 import Chat_converstaion, results
import time
import threading
from threading import Thread
from operator import itemgetter
import random
import pandas as pd
# from Random_Promts import random_promts
from Article_add import addWordpress
# from Add_tags import add_tag
domain = 'https://ferma.expert'  # название сайта на основе которого мы хотим сделать ai-сайт
# domain = 'https://kladovaia-krasoti.ru'  # название сайта на основе которого мы хотим сделать ai-сайт
domain2 = domain.split('://')[1]
print(domain2)
if domain2 in os.listdir(path='urls'):
    print('уже спарсили урлы сайта')
else:
    call_parsing(domain)  # Парсинг всех урлов по названию домена (domain) в папку urls

with open('urls/'+domain2, 'r') as file:
    urls_list = file.read().splitlines()  # список всех урлов по домену

print(' метка А')
# Замеряем время работы
start_all_time = time.time()

count = 0
for url_1 in urls_list[98:150]:  # Иду по urls сайта беру первый урл в списке всех урлов сайта
    print('Номер добавленной статьи ----->', count)
    count = count + 1
    # обнуление буфера для статьи
    html = ''
    h1 = ''
    results.clear()
    try:
        h1 = parse_h1(url_1)  # Парсинг H1 текущего урла, если ошибка то следующий url
        if not h1: continue
        print('Заголовок Н1 базовой статьи', h1)
        links_4_g = parsing_yandex(h1)
        print('*** УРЛЫ С КОТОРЫМИ БУДЕМ РАБОТАТЬ ***', links_4_g)

        # Формирование большого кортежа
        ls = merge_4_links(links_4_g)
        print('//// ', ls)

        #  Получили список кортежей -> Необходимо взять и сделать список Н2  -> Отправить в Дифферентатор и Кластеризатор- >
        list_h2 = [i for i, *j in ls]
        print('*** ', list_h2)
        h2_new = agenta(list_h2)     # -> получили список  очищенныый и кластеризованный
        h2_text_img_new = [(h, t, p) for h, t, p in ls if h in h2_new]
        # print('Итоговый кортеж -->', h2_text_img_new)
        print('ДЛИНА -->', len(h2_text_img_new))
        i = 0
        for hti in h2_text_img_new:
            i = i + 1
            print(i, '----------', hti)

        # Удаление кортежей с пустыми элементами в тексте, наличии кодировок, мусорных слов, текста меньше 60 символов
        ls2 = list(filter(lambda x: x[1] != '', h2_text_img_new))
        ls3 = list(filter(lambda x: 'Ð' not in x[1], ls2))
        ls4 = list(filter(lambda x: len(x[1]) > 60, ls3))
        ls41 = list(filter(lambda x: 'регистрац' or 'скидк' or 'социальные сети' or 'Профи ' not in x[1], ls4))
        ls42 = list(filter(lambda x: 'телефон' not in x[1], ls41))
        ls5 = list(filter(lambda x: 'mail' not in x[1], ls42))
        ls6 = []
        for i in ls5:
            # print(i)
            if i[0] != '' or ls5.index(i) != 0:
                ls6.append(i)
        h2_text_img_new_clear = ls6
        
        # закрыл добавил ls6 и строчку 5
        # h2_text_img_new_clear = list(filter(lambda x: 'регистрац' not in x[1], ls4))


        # ---------------
        # Запись в Пандасе простого спарсенного текста в 1.xlsx
        print('Массив который записывается в Эксель: ', h2_text_img_new_clear)
        s = pd.DataFrame(h2_text_img_new_clear, columns=['h2', 'text', ' image'])
        # s = pd.DataFrame([count,end_time-start_time], columns=['count', 'time'])
        print('-----------------------')
        s.to_excel('1.xlsx')
        # ---------------

        # h2_text_img_after_gpt3 = [lambda t: Chat_converstaion(t,'text_2_pr') for t in h2_text_img_new]
        h2_t_img_new_after_gpt3 = []
        tuple = ()
        all_text = ''


        # Замеряем время работы
        start_time = time.time()

        # Делаем список из подзаголовков
        tt = [tt for h, tt, img in h2_text_img_new_clear]
        print("ТТ = ", tt)
        # Создаем и запускаем потоки
        threads = []
        stop_threads = False
        for i in range(0, len(tt)):
            print('номер потока: ', i)
            h2 = h2_text_img_new_clear[i][0]
            img = h2_text_img_new_clear[i][2]
            # ----------
            tex = h2_text_img_new_clear[i][1]

            # Отправка в Нейронку промтов
            trr = Thread(target=Chat_converstaion, args=(tex, 'text_1_pr', i, h2, img), daemon=False)
            print('Потоки ******** ', trr)
            trr.start()
            time.sleep(2)
            threads.append(trr)
            tt.append(trr)

            # Пауза если потоков больше 7
            active_thread_count = threading.active_count()
            print(f"Всего активных потоков: {active_thread_count}")
            if active_thread_count > 7:
                print("Взяли паузу 10 с.")
                time.sleep(10)

            middle_time = time.time()
            if middle_time - start_time > 300:
                for thread in threads:
                    print("уничтожение процесса -------")
                    thread.terminate()
            # ---------------------------
            # for x in threads:
            #     # time.sleep(3)
            #     print('ЖДЕМС')
            #     x.start()
            # -------------------

        #     # Однопотоковость работает / Если будет менять API это будет уже многопотоковость Работает очень долго
        #     Chat_converstaion(tex, 'text_1_pr', i, h2, img)
        #     # задержка если работаю в один поток и на одном API
        #     time.sleep(24)
        # # Проверить существует ли поток

        # Блокировка потоков из списка потоков
        for thread in threads:
            print('Блокировка потока', thread.name)
            thread.join()

        # Сортировка списка кортежей текстов после GPT-3 но до HTML. RESULTS - это список кортежей
        results.sort(key=lambda x: x[0])

        # # Удаление блоков если в h нет назвния, кроме первого
        # results = [(id, h, t, i) for id, h, t, i in results if h !='Нет заголовка' and id !=0]



        # Принт в Терминал итоговую статью:
        for r in results:
            print('ПОШАГОВЫЙ ИТОГ           :', r)
        # Запись в Пандасе в 1.xlsx
        s = pd.DataFrame(results, columns=['num', 'h2', 'text', ' image'])
        # s = pd.DataFrame([count,end_time-start_time], columns=['count', 'time'])
        s.to_excel('2.xlsx')
        # # df = pd.loc[pd['h2'] != 'Нет заголовка']
        # print(s)

        # # Показать Пандас таблицу
        # s['text'][1]

        html_all = ''
        # Соединение всей статьи
        for id, h, t, p in results:
            if h == '<h2>Нет заголовка</h2>' and id != 0:
                continue
            elif id == 0:
                h = ''
            html_all = html_all + h + t + p
        print(html_all)
        # # вставить теги жирности около слов
        # html_all = add_tag('b', 'недостатки', html_all)

        # Добавление статьи на сайт
        addWordpress(h1, html_all)

        end_time = time.time()
        print('Время на создание сатьи', end_time - start_time)

        # Запись в Пандасе в 1.xlsx то что записалось в WordPress
        # s = pd.DataFrame(results, columns=['num', 'h2', 'text', ' image'])
        s = pd.DataFrame([count, end_time - start_time], columns=['count', 'time'])
        s.to_excel('1.xlsx')
        # df = pd.loc[pd['h2'] != 'Нет заголовка']
        print(s)

        # Показать Пандас таблицу
        s['text'][1]




    except:
        continue


end_all_time = time.time()
print('Общее время работы программы: ', end_all_time - start_all_time)
