import re,datetime
from yargy import rule,and_,Parser
from yargy.predicates import (
    eq, gte, lte
)
DAY = and_(gte(1), lte(31))
MONTH = and_(gte(1),lte(12))
YEAR = and_(gte(1),lte(2018))
DATE = rule(DAY, eq('.'), MONTH, eq('.'), YEAR, eq(','), and_(gte(0), lte(24)), eq(':'), and_(gte(0), lte(59)))
NEWSDATE = rule('Дата', eq(':'), DATE)


def findall(gr,Text):
    array = []
    for match in Parser(gr).findall(Text):
        array.append([_.value for _ in match.tokens])
    return array


text = open('News.txt', 'r', encoding='utf-8').readlines()
text = '\n'.join(text)
split = re.split(r'-----------|________________', text)
#убираем лишние пустые строки
splittedText = split[0:len(split):2]
#находит даты в новостях
res = findall(NEWSDATE, ' '.join(splittedText))
dictionary = {}
i = 0
#заполняем словарь элементами (номер новости,дата новости)
for element in res:
    dictionary.update({i: '/'.join(element[2:11:2])})
    i = i+1
#преобразуем строковую дату в формат дата
for (key, value) in dictionary.items():
    if(re.fullmatch(r'([0-9]){2}/([0-9]){2}/([0-9]){4}/([0-9]){1,2}/([0-9]){2}', value)):
        dictionary.update({key: datetime.datetime.strptime(value, '%d/%m/%Y/%H/%M')})
    elif (re.fullmatch(r'([0-9]){2}/([0-9]){2}/([0-9]){2}/([0-9]){1,2}/([0-9]){2}', value)):
        dictionary.update({key: datetime.datetime.strptime(value, '%d/%m/%y/%H/%M')})
#сортируем наш словарь
sorted_dict = sorted((value, key) for (key, value) in dictionary.items())
#записываем в файл новости по порядку даты
for element in sorted_dict:
    open('result.txt', 'a+', encoding='utf-8').write(splittedText[element[1]] + "\n")
