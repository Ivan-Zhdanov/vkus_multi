# urls_list = [1,2,3]
# url_1 = 1
def log_write(urls_list, url_1):
    with open('log.txt', "a+") as f:
        f.writelines(str(urls_list.index(url_1))+"\n")
        return 1


def log_api(num_threading, api,e):
    line = str(num_threading)+"; "+str(api)+"; "+str(e)+"\n"

    with open('api_detect.txt', 'r') as file:
        for l in file:
            if line in l:
                return print('есть уже ошибка вф файле')

    # with open('api_detect.txt', 'w') as f:
    #     for line in unique_lines:
    #         f.write(line)

    with open('api_detect.txt', "a+") as f:
        f.writelines(line)


