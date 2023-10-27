import difflib
import spacy
from spacy.lang.ru import Russian
# Для установки
# python -m spacy download ru_core_news_lg
nlp = spacy.load("ru_core_news_lg")


def similarity_dif(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

def agenta (all_headers):
    # НАКИДАЛИ ВСЕ В ОДНО И ПОТОМ ОЧИСТИЛИ
    # all_headers = list(chain(headers, s22, s11))
    # print(all_headers)
    for h2 in all_headers:
        noh2 = [x for x in all_headers if x != h2]
        q1 = nlp(h2)
        for el in noh2:
            q2 = nlp(el)
            if q1.similarity(q2) > 0.7 or similarity_dif(h2, el) > 0.5:
                try:
                    all_headers.remove(h2)
                except:
                    pass
    # for el in all_headers:
        # print('***', el)

    # МИКСОВАНИЕ СОЗДАННОГО СОДЕРЖАНИЯ (1)
    # Идем постепенно по общему содержанию, если видим что, что-то имеет близкую связь то ставим после
    index = 0
    new_all__headers = []
    end = len(all_headers)
    while index < end:
        elem = all_headers[index]
        if elem not in new_all__headers:
            new_all__headers.append(elem)
        # print('****************** ', elem)
        noh2 = all_headers.copy()
        del noh2[index]
        # print('noh2 --->', noh2)
        q1 = nlp(elem)
        for ee in noh2:
            q2 = nlp(ee)
            if q1.similarity(q2) > 0.3:
                # print(elem, '-----', ee, '---- ', q1.similarity(q2))
                # print('2222', new_all__headers)
                if ee not in new_all__headers:
                    new_all__headers.append(ee)
                break


        index = index + 1
    # print(new_all__headers)
    # print(len(new_all__headers))
    return new_all__headers

