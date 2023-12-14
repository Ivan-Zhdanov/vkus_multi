urls_list = [1,2,3]
url_1 = 1
def log_write(urls_list, url_1):
    with open('log.txt', "a+") as f:
        f.writelines(str(urls_list.index(url_1))+"\n")
        return 1

c = urls_list.index(url_1)

log_write(urls_list,url_1)