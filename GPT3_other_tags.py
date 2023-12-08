# Создание нового текста от вопроса в OPENAI
import openai
import time
import re
import requests
from GPT3_API_cheker import api_cheker, list_api
from Get_url_Img_from_WP import take_url_img_from_wp
from Api_List import api_list
# предыдущий ключ с аккаунта ivan.zhdanov.moscow4
# openai.api_key = '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'

# 28/09
# openai.api_key = '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'

# ключ от аккаунта helloword (5$)
# openai.api_key = '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'

model_id = 'gtp-3.5-turbo'
num_text = ()

apis = api_list


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
        if tag.name == 'h2' or tag.name == 'h3':
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
                    print('ожидание 0c ...')
                    time.sleep(5)



        elif tag.name == 'ul' or tag.name == 'ol':
            r2 = Chat_converstaion_ul_ol(tag)
            # print(tag, ' ---> ', r2)
            r22 = r2.replace("<li><li>", "<li>").replace("</li></li>", "</li>")
            html = r22

        elif tag.name == 'table':
            r3 = Chat_converstaion_table(tag)
            # print(tag, ' ---> ', r3)
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