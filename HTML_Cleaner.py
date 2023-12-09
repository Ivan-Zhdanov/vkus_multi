
def html_cleaner(html):
    t1 = html.replace("«»»", "")
    t2 = t1.replace("<li><li>", "<li>")
    t3 = t2.replace("</li></li>", "</li>")
    cl_html = t3.replace("»»»", "")
    return cl_html