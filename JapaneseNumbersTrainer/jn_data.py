# Imports
import sys
import os

numbers_kanji = ('','一','二','三','四','五','六','七','八','九','十')
numbers_hiragana = ('','いち','に','さん','よん/し','ご','ろく','なな/しち','はち','きゅう/く','じゅう')
place_kanji = ('千','百','十','')
place_hiragana = ('せん','ひゃく','じゅう','')
counters = ('年','月','日')

numbers_dict = {n:[numbers_kanji[n],numbers_hiragana[n]] for n in range(0,11)}
