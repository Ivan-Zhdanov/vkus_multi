# Функция делает обертку найденных цифр или тире
import re

def wrap_tags3(text2):
    html = ''
    ls = text2.splitlines()
    # пошел по списку. Поиск selectiona
    select = 0
    i = 0
    while i < len(ls):
        # если пустая строка то дальше
        nums = re.search(r'\d{1,2}\.|\d{1,2}\)', ls[i][:8])
        marks = re.search(r'\-', ls[i][:8])
        advantages = re.search(r'недостатки', ls[i].lower())

        if ls[i] == "":
            pass

        elif marks != None:
            # удалили маркеры заменили на теги маркеров
            str_li = '<p><li>' + ls[i].replace(marks.group(0), "") + '</li></p>' + '\n'
            html = html + str_li

        elif nums != None:
            # img = f'<img class="alignnone" src="https://supergardener.ru/wp-content/uploads/2023/09/{nums.group(0)[0]}num.jpg" alt="" width="36" height="35" />'
            img = f'<img class="alignnone" src="https://supergardener.ru/wp-content/uploads/2023/09/num{nums.group(0).replace(".","").replace(")","")}.jpg" alt="" width="36" height="35" />'
            str_li = '<p>' + img + ls[i].replace(nums.group(0), "") + '</p>' + '\n'
            html = html + str_li


        else:
            str_p = '<p>' + ls[i] + '</p>' + '\n'
            # str_p = ls[i] + '\n'
            html = html + str_p


        i = i + 1

    return html

# s = wrap_tags3(text)
# print(s)