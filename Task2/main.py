import re
#open and read tetx from file into variable content
with open('train.txt', 'r') as fileRead:
    content = fileRead.read()
#split variable content on words and delete repeatable words
line = re.split(r'[0-9]+-[a-z]+|[^a-zA-Z-0-9]', content)
line = [word for word in line if word != '']
unique_line = []
[unique_line.append(word) for word in line if word not in unique_line]
#write the result to a file
with open('result1.txt', 'a+') as fileWrite1:
    fileWrite1.write('\n'.join(unique_line))
years = []
#find years in unique list
for word in unique_line:
    if re.match(r'([12])(?:[0-9]){3}', word):
        years.append(int(word))
years.sort()
#write years from text to a file
with open('result2.txt', 'a+') as fileWrite2:
    fileWrite2.write(str(years).strip('[]'))

