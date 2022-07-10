# A script that plays the game hangman

# Import Modules
import os
from random import randint

# Functions
def is_user_correct(guess_word, chosen_word, guess_number, guesses, input):
      if input in chosen_word:
            letter_loc = [pos for pos, char in enumerate(chosen_word) if char == input]
            print(letter_loc)
            for i in letter_loc:
                  guess_word.replace(guess_word[i*2],input)
                  
      else:
            guess_number += 1
      guesses.append(input)
      return guess_word, guess_number, guesses
            

# Ascii output
hang_ascii = open(os.path.join(os.getcwd(),"hg_ascii.txt"), "r")
ascii_art = hang_ascii.read().split(',')

# Word to guess
word_list = '''hateful rambunctious pretend hand 
tank wide-eyed like salt crash hill
lying moor mountainous jittery fanatical
holistic friction brave rot haircut count
funny crate month zinc unknown ambiguous
frighten prickly gamy melodic clam oil
callous wire wacky remind bath cure bump
haunt vivacious slim party incompetent
plausible sail arrogant strap scribble'''.split(' ')

chosen_word = word_list[randint(0,len(word_list)-1)]


guess_number = 0
guess_word = ''
for i in chosen_word:
      guess_word += '_ '

print(f'You have a {len(chosen_word)} letter word.')

while guess_number <= 5:
      print(f'\n {guess_word}')
      guesses = []
      print(f'Guessed letters:{guesses}')
      user_answer = input('Guess a letter:').lower()
      guess_word, guess_number, guesses = is_user_correct(guess_word, chosen_word, guess_number, guesses, user_answer)

print(guess_word)