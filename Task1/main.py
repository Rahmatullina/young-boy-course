#read text from file into variable text
with open('train.txt', 'r') as fileRead:
   text = fileRead.readlines()
#change text to lower case and replace 'snake' with 'python'
for line in text:
    line = line.lower()
    line = line.replace('snake', 'python')
#find lines that contain  words 'anaconda' and 'python' and write them to a file
    with open('result.txt', 'a+') as fileWrite:
        if 'anaconda' in line and 'python' in line:
            fileWrite.write(line+'\n')