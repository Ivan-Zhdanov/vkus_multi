s= """https://foodandhealth.ru/wp-content/uploads/2023/07/vse-o-zachatii-i-beremennosti-768x408.jpeg 300w, https://foodandhealth.ru/wp-content/uploads/2023/07/vse-o-zachatii-i-beremennosti-140x74.jpeg 140w, https://foodandhealth.ru/wp-content/uploads/2023/07/vse-o-zachatii-i-beremennosti-1000x532.jpeg 1000w, https://foodandhealth.ru/wp-content/uploads/2023/07/vse-o-zachatii-i-beremennosti.jpeg 770w"""
s1 = """<li>&lt;li&gt;УЗИ органов малого таза, позволяющих определить, нет ли воспалительных заболеваний или других патологий, негативно влияющих на зачатие, вынашивание и рождение ребенка.&lt;/li&gt;</li>
<li>&lt;li&gt;Анализ на TORCH-инфекции, к которым относится краснуха, токсоплазмоз, цитомегаловирус, герпес, ведь некоторые из них имеют серьезное влияние на плод.&lt;/li&gt;</li>
<li>&lt;li&gt;Анализ на ВИЧ, гепатит B, сифилис, которые также опасны для будущего ребенка.&lt;/li&gt;</li>"""


src_value = s.split(',')[0].replace("768w", "").strip()


s3 = s1.replace("&lt;li&gt;","")
# print(src_value)
ls = list(s.split(','))
for l in ls:
    img_src =l.strip().split(' ')[0]
    img_size = int(l.strip().split(' ')[1].rstrip('w'))
    print(img_size)
    print(img_src)
    if img_size > 700:
        src_value = img_src
        break



    # print(l)
# print(ls)