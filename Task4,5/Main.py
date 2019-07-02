import re
import pymorphy2
import collections
from yargy import (
    Parser,
    rule, not_,and_
)
from yargy.predicates import (
    eq, normalized,gte,lte
)


def findall(gr, text):
    array = []
    for match in Parser(gr).findall(text):
        array.append([_.value for _ in match.tokens])
    return array

morph = pymorphy2.MorphAnalyzer()
#разделяем текст на слова исключая знаки пунктуции ,цифры и другие символы ,а также убираем пустыем строки
text1 = open('News.txt', 'r', encoding='utf-8').read()
text = re.split(r'[^A-Za-zа-яА-ЯёЁ-]|[-]{2,}', text1)
text = ' '.join(text)
text = re.split(r'\s+-[а-яА-ЯёЁ]*\s|[\s]+', text)
text = [word for word in text if word != '']
text = [(morph.parse(word)[0]).normal_form for word in text]

#загружаем стоп-слова в список
stopWords = open('StopWords', 'r', encoding='utf-8').read()
stopWords = stopWords.split()
stopWords.extend(['автор','дата'])
#вычленяем слоп-слова из text
text = [word for word in text if word not in stopWords]
#подсчитываем частоту слов в тексте
words_TF = collections.Counter(text)
#записываем рультат в файл 'task4'
for (key, value) in words_TF.most_common():
    open('task4.txt', 'a+', encoding='windows-1251').write(str(key) + ' : ' + str(value) + '\n')
#----------задание 5----------
#берем первые 5 попярных слов
five_common = words_TF.most_common(5)
res = []
#ищем с ними словосочестания и записываем в массив res
for (key, value) in five_common:
    GR = rule(normalized(key), and_(not_(eq(',')), not_(eq('.')), not_(eq('?')), not_(eq('!')), not_(eq('-')),
                                          not_(eq('—')), not_(eq('(')), not_(eq(')')), not_(eq(':')), not_(eq('...')),
                                          not_(eq('»')), not_(eq('«')), not_(and_(gte(0), lte(1000))),
                                          not_(eq('\n')), not_(eq('\n\n\n'))))
    res.append(findall(GR, text1))
#подсчитываем количество словосочетаний и записываем в result2
res2 = []
for element in res:
    res2.append(collections.Counter([(morph.parse(word1)[0]).normal_form + ' ' + (morph.parse(word2)[0]).normal_form for [word1, word2] in element]))
#записываем реезультат в файл 'task5.txt'
for counter in res2:
    for (key, value) in counter.most_common():
        open('task5.txt', 'a+',encoding='windows-1251').write(str(key) + ' : ' + str(value) + '   ')
    open('task5.txt', 'a+').write('\n')