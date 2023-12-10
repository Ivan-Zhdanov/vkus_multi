
def html_cleaner(html):
    t1 = html.replace("«»»", "").replace('"""',"").replace("»»»", "")
    t2 = t1.replace("<li>&lt;li&gt;", "<li>")
    t3 = t2.replace("&lt;/li&gt;</li>", "</li>")
    cl_html = t3.strip('"')
    return cl_html