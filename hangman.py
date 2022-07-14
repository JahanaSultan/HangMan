import random
from Hangman_ASCII import *
from Hangman_words import *
print(logo)
chosen_word=random.choice(words)
lives=6
display=[]

for i in range (len(chosen_word)):
    display+='_'
end_of_game=False

while not end_of_game:
    guess=input('Guess a letter: ')
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word.")
        if lives==0:
            end_of_game=True
            print('You Lose')
    print(f'{" ".join(display)}')
    if '_' not in display:
        end_of_game=True
        print('You Win')
    print(stages[lives])

