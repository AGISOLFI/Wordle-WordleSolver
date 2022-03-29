import random

f = open('words.txt','r')
words=f.read()
f.close

word_list=(words.split('\n'))

r = random.randint(0,len(word_list)-1)

random_word = word_list[r]
random_word = random_word.lower()

for i in range(len(word_list)):
    word_list[i]=word_list[i].lower()

print(random_word)
print(len(word_list))

empty_list=[]
for i in range(len(word_list)):
    if word_list[i][0] == random_word[0]:
       empty_list.append(word_list[i])
word_list=empty_list.copy()
print((empty_list))
empty_list.clear()
for i in range(len(word_list)):
    if word_list[i][1] == random_word[1]:
       empty_list.append(word_list[i])
word_list=empty_list.copy()
empty_list.clear()

for i in range(len(word_list)):
    if word_list[i][2] == random_word[2]:
       empty_list.append(word_list[i])
word_list=empty_list.copy()
empty_list.clear()

for i in range(len(word_list)):
    if word_list[i][3] == random_word[3]:
       empty_list.append(word_list[i])
word_list=empty_list.copy()
empty_list.clear()


for i in range(len(word_list)):
    if word_list[i][4] == random_word[4]:
       empty_list.append(word_list[i])
word_list=empty_list.copy()
empty_list.clear()

## use nested for loops to increase efficency
print(len(word_list))
print(word_list)

