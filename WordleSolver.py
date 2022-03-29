#Wordle Solver
import random

f = open('words.txt','r')
words=f.read()
f.close

word_list=(words.split('\n'))

r = random.randint(0,len(word_list)-1)

random_word = word_list[r]
random_word=random_word.lower()

alphabet=["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
computer_guess=""

for i in alphabet:
    if i == random_word[0]:
        computer_guess= computer_guess + i
for i in alphabet:
    if i == random_word[1]:
        computer_guess= computer_guess + i
for i in alphabet:
    if i == random_word[2]:
        computer_guess= computer_guess + i
for i in alphabet:
    if i == random_word[3]:
        computer_guess= computer_guess + i
for i in alphabet:
    if i == random_word[4]:
        computer_guess= computer_guess + i

print(computer_guess)
print(random_word)






