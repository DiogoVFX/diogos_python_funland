import random
import jn_data
from jn_utils import generate_numbers

close = False

reading_writing = input('Do you want to train your reading or writing? (r/w): ')
while reading_writing not in ('r','w'):
    reading_writing = input('Do you want to train your reading or writing? (r/w): ')

hiragana_kanji = input('Do you want to train hiragana or kanji? (h/k) :')
while  hiragana_kanji not in ('h','k'):
    hiragana_kanji = input('Do you want to train hiragana or kanji? (h/k) :')
if hiragana_kanji == 'h':
    hiragana_kanji = 0
else:
    hiragana_kanji = 1

while not close:
    number, hiragana, kanji = generate_numbers()
    if reading_writing == 'r':
        answer = input(f'What is {number}:')
        if hiragana_kanji == 0:
            if answer == hiragana:
                print('You got that right! Welldone!')
            else:
                print(f'oof, you got that wrong. It is actually {hiragana}.')
        else:
            if answer == kanji:
                print('You got that right! Welldone!')
            else:
                print(f'oof, you got that wrong. It is actually {kanji}.')
    elif reading_writing == 'w':
        if hiragana_kanji == 0:
            answer = input(f'What is {hiragana}: ')
        else:
            answer = input(f'What is {kanji}: ')
        if number == answer:
            print('You got that right! Welldone!')
        else:
            print(f'oof, you got that wrong. It is actually {number}.')
            
    if input('Would you like to go again? (y/n)') != 'y':
        close = True