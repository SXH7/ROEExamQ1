file = open('Week 4/text.txt', 'r')
words = file.read()
answer = open('Week 4/answer.txt', 'w')
words = words.split('\n')

for word in words:
    if word == '':
        words.remove('')

counter = 0

while counter < len(words):
    
    x = '|'
    counter2=0
    while counter2<10:
        counter2+=1
        x+=words[counter]+'|'
        counter+=1
    answer.write(x+'\n')

