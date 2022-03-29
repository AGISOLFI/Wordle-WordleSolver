#wordle
#ask user for a 5 letter word
#Randomly generste a 5 letter word( from a file)
#CHeck to see if they are the same, if not, check individual letters for similarity
#stop after 6 guesses

#generate a random word from a file
#start asking our user for words
#check to see if it has 5 letters
#compare to random word
#if they are the same you win
#IF not print out letter comparison then make them guess again
#after 6 guesses they lose

import random

f = open('words.txt','r')
words=f.read()
f.close

word_list=(words.split('\n'))

r = random.randint(0,len(word_list)-1)

random_word = word_list[r]
random_word = random_word.lower()

for guess in range(6):
    player_word=input("Give me a five letter word: ")
    while len(player_word) != 5:
      player_word=input("Give me a five letter word: ")

    if player_word == random_word:
        print("YOU WIN!")
        break
    else:
        for i in range(len(random_word)):
                if player_word[i] == random_word[i]:
                    print('The {} letter is correct'.format(i+1))
                elif player_word[i] in random_word:
                    print("The {} letter is in the wrong spot".format(i+1))
                else:
                    print("The {} letter is incorect".format(i+1))
        if guess == 5:
            print("YOU LOSE")
            print("The correct word was ")
            print(random_word)