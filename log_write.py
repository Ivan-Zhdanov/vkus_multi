
def log_write(urls_list, url_1):
    with open('log.txt', "w") as f:
        f.writelines('#', urls_list.index(url_1))
        return