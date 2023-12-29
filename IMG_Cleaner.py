from bs4 import BeautifulSoup
from Cort import cort
import requests
from bs4 import BeautifulSoup
import bs4
from PIL import Image
from io import BytesIO


def get_image_height(url):
    try:
        # Получаем содержимое изображения по URL
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок при запросе

        # Читаем изображение с использованием библиотеки Pillow
        image = Image.open(BytesIO(response.content))

        # Получаем высоту изображения
        height = image.height

        return height

    except Exception as e:
        print(f"Error: {e}")
        return None


t = '<img alt="Польза и вред фиников: 8 научных фактов" class="js-rbcslider-image smart-image__img" height="1291" itemprop="url contentUrl" loading="lazy" src="https://s0.rbk.ru/v6_top_pics/media/img/5/04/756178639097045.jpg" width="2000"/>'
t1 = '<img data-wpfc-original-src="https://images.dmca.com/Badges/dmca_protected_sml_120am.png?ID=a6e7d2aa-4c63-434f-9d67-437e28529ebb" height="21" onload="Wpfcll.r(this,true);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" width="123"/>'
t2 = '<img class="alignright wp-image-66292" data-wpfc-original-sizes="(max-width: 300px) 100vw, 300px" data-wpfc-original-src="https://foodandhealth.ru/wp-content/uploads/2023/07/bodrost-300x300.jpeg" data-wpfc-original-srcset="https://foodandhealth.ru/wp-content/uploads/2023/07/bodrost-768x575.jpeg 768w, https://foodandhealth.ru/wp-content/uploads/2023/07/bodrost-140x104.jpeg 140w, https://foodandhealth.ru/wp-content/uploads/2023/07/bodrost-1000x749.jpeg 1000w, https://foodandhealth.ru/wp-content/uploads/2023/07/bodrost.jpeg 1008w" height="225" loading="lazy" onload="Wpfcll.r(this,true);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" title="Бодрость | Food and Health" width="300"/>'
t3 = f'<img alt="1" height="16" id="rating_66285_1" onclick="rate_post();" onkeypress="rate_post();" onmouseout="ratings_off(2.3, 3, 0);" onmouseover="current_rating(66285, 1);" src="https://foodandhealth.ru/wp-content/plugins/wp-postratings/images/stars_crystal_32/rating_on.gif" style="cursor: pointer; border: 0px;" title="1" width="16"/>'
t4 = '<div class="post-ratings" data-nonce="1cf59a2f62" id="post-ratings-66285"><img alt="1" height="16" id="rating_66285_1" onclick="rate_post();" onkeypress="rate_post();" onmouseout="ratings_off(2.3, 3, 0);" onmouseover="current_rating(66285, 1);" src="https://foodandhealth.ru/wp-content/plugins/wp-postratings/images/stars_crystal_32/rating_on.gif" style="cursor: pointer; border: 0px;" title="1" width="16"/><img alt="2" data-wpfc-original-src="https://foodandhealth.ru/wp-content/plugins/wp-postratings/images/stars_crystal_32/rating_on.gif" height="16" id="rating_66285_2" onclick="rate_post();" onkeypress="rate_post();" onload="Wpfcll.r(this,true);" onmouseout="ratings_off(2.3, 3, 0);" onmouseover="current_rating(66285, 2,);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" style="cursor: pointer; border: 0px;" title="2" width="16"/><img alt="3" data-wpfc-original-src="https://foodandhealth.ru/wp-content/plugins/wp-postratings/images/stars_crystal_32/rating_half.gif" height="16" id="rating_66285_3" onclick="rate_post();" onkeypress="rate_post();" onload="Wpfcll.r(this,true);" onmouseout="ratings_off(2.3, 3, 0);" onmouseover="current_rating(66285, 3);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" style="cursor: pointer; border: 0px;" title="3" width="16"/><img alt="4" data-wpfc-original-src="https://foodandhealth.ru/wp-content/plugins/wp-postratings/images/stars_crystal_32/rating_off.gif" height="16" id="rating_66285_4" onclick="rate_post();" onkeypress="rate_post();" onload="Wpfcll.r(this,true);" onmouseout="ratings_off(2.3, 3, 0);" onmouseover="current_rating(66285, 4);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" style="cursor: pointer; border: 0px;" title="4" width="16"/><img alt="5" data-wpfc-original-src="https://foodandhealth.ru/wp-content/plugins/wp-postratings/images/stars_crystal_32/rating_off.gif" height="16" id="rating_66285_5" onclick="rate_post();" onkeypress="rate_post();" onload="Wpfcll.r(this,true);" onmouseout="ratings_off(2.3, 3, 0);" onmouseover="current_rating(66285, 5);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" style="cursor: pointer; border: 0px;" title="5" width="16"/> (<strong>6</strong> оценок, среднее: <strong>2,33</strong> из 5)<br/></div><div class="post-ratings-loading" id="post-ratings-66285-loading"><img alt="blank" class="post-ratings-image" data-wpfc-original-src="https://foodandhealth.ru/wp-content/plugins/wp-postratings/images/loading.gif" height="16" onload="Wpfcll.r(this,true);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" width="16"/> Загрузка...</div></div><div class="clear"></div></div>, <div class="entry-content"><p>Современный темп жизни настолько активный, что иногда жаль тратить время на дневной сон. И зря – говорят ученые, утверждая, что полноценно высыпаясь днем, можно чувствовать себя бодрым до вечера и успевать даже больше в течение суток, чем без сна. А все потому, что отдых столько часов в сутки, сколько требует организм, укрепляет здоровье, продлевает молодость, обеспечивают жизненной энергией и позитивно воздействуют на наш мозг. Как же влияет дневной сон на наш организм, разберемся в этой статье.<a href="https://foodandhealth.ru/wp-content/uploads/2023/07/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga.jpeg"><img alt="Регулярный дневной сон сохраняет молодость мозга" class="aligncenter wp-image-66290" data-wpfc-original-sizes="(max-width: 600px) 100vw, 600px" data-wpfc-original-src="https://foodandhealth.ru/wp-content/uploads/2023/07/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga-300x300.jpeg" data-wpfc-original-srcset="https://foodandhealth.ru/wp-content/uploads/2023/07/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga-768x377.jpeg 768w, https://foodandhealth.ru/wp-content/uploads/2023/07/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga-140x68.jpeg 140w, https://foodandhealth.ru/wp-content/uploads/2023/07/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga-1000x491.jpeg 1000w, https://foodandhealth.ru/wp-content/uploads/2023/07/regulyarniy-dnevnoy-son-sohranyaet-molodost-mozga.jpeg 852w" height="295" loading="lazy" onload="Wpfcll.r(this,true);" src="https://foodandhealth.ru/wp-content/plugins/wp-fastest-cache-premium/pro/images/blank.gif" title="Регулярный дневной сон сохраняет молодость мозга | Food and Health" width="600"/></a></p>'
content_article = BeautifulSoup(t4, "lxml")



# Находим все теги p с вложенными тегами img
p_tags_with_img = content_article.find_all('p', recursive=False)
print(content_article.prettify())
print('----------------------', content_article)
# Создаем новые теги p и img
for p_tag in p_tags_with_img:
    # Создаем новый тег p
    new_p_tag = content_article.new_tag('p')
    new_p_tag.string = p_tag.get_text(strip=True)  # Копируем текст из старого тега p

    # Вставляем новый тег p после старого тега p
    p_tag.insert_after(new_p_tag)

    # Создаем новый тег img и вставляем его в новый тег p
    img_tag = content_article.new_tag('img')
    img_tag['src'] = p_tag.img['src']
    img_tag['alt'] = p_tag.img['alt']
    new_p_tag.append(img_tag)

    # Удаляем тег img из старого тега p
    p_tag.img.unwrap()

print(content_article.prettify())