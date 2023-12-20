# import time
# from GPT3_other_tags import Chat_converstaion_ppp
# import threading
# import concurrent.futures
# # ЕСЛИ МЫ ОТПРАВЛЯЕТ ОБЪЕКТ ТЭГ, А ТАМ УЖЕ ЕГО ПРОВЕРЯЕМ НА ТО ИЛИ ИНОЕ
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     # Запуск функции process_data в пуле потоков и передача данных из списка
#     results = list(executor.map(Chat_converstaion_ppp, tags))
#     print('пауза на основном потоке 5с')
#     time.sleep(5)
# print(results)
# # Распаковка созданного списка
# for res in results:
#     string = string + res
# # закрыть все потоки которые есть
# executor.shutdown(wait=True)
#
# # очистка списка
# th_list.clear()
#
# return string