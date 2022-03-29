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
letter = 0
for letter in range(4):
    for i in range(len(word_list)):
        if word_list[i][letter] == random_word[letter]:
            empty_list.append(word_list[i])
    word_list=empty_list.copy()
    if len(word_list)==1:
        break
    print((empty_list))
    empty_list.clear()



print("The random word is " + str(word_list))




