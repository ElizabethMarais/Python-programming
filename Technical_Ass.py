print "Touchsides Technical Assignment 1 part A: the frequency of each word that appears in a text data file, fomoe-full.txt'"

# Output:  
# Most frequent word: {word} occurred {x} times
# Most frequent 7-character word: {word} occurred {x} times
# Highest scoring word(s) (according to Scrabble): {word} with a score of {x}

# -*- coding: utf-8 -*-
#The reason why it works differently in console and in the IDE is, likely, because of different default encodings set. You can check it by running:

words_list = list()
name = raw_input('Please enter the file name of the text file: ')

handle = open(name, 'r')
#handle = codecs.open(name, 'r', encoding='utf-8')   #.readlines()
text = handle.read()
#text.encode('utf-8')
words = text.split()

print " " 
#============== # Most frequent word: {word} occurred {x} times ===================

counts = dict()	
 
for word in words:
    word = word.lower()
    counts[word] = counts.get(word,0) + 1
    
bigcount = 0
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print "Most frequent word: '", bigword, "' occurred", bigcount, "times."

#============== # Most frequent 7-character word: {word} occurred {x} times ===================

counts7 = dict()	
for word in words:
  if len(word) == 7:
    word = word.lower()
    counts7[word] = counts7.get(word,0) + 1

bigcount7 = 0
bigword7 = None

for word,count in counts7.items():
    if bigcount7 is None or count > bigcount7:
        bigword7 = word
        bigcount7 = count

print "Most frequent 7-character word: '", bigword7, "' occurred", bigcount7, "times."

# ================== # Highest scoring word(s) (according to Scrabble): {word} with a score of {x}  ===============

import string
import re

Scrab_scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}

def scrabble_score(word):
  total = 0
  for letter in word:
       total += Scrab_scores[letter]
  return total

high_scrab = dict()

bigscore = 0
bigwordS = None

#struggle when data file has a curly double quotation mark, gives error    \x93

for word in words:
 word = word.lower()
 pos_split_www = word.find('//')
 if pos_split_www > 0:  continue
 pos_split = word.find('/')
 while pos_split > 0:
     word_start = word[0:pos_split]
     word_rest = word[pos_split+1:]
     word = word_rest
     score = scrabble_score(word_start)
     high_scrab[word_start] = score                 #create a dict, each item is the word, and the value is the scrabble score
     pos_split = word_rest.find('/')

 word = word.translate(string.maketrans("",""), string.punctuation)   # to strip words of punctuation
 test =  re.findall('[0-9]',word)
 if test == []:
    test_word = word.isdigit()
    if test_word == False:  #to make sure it is a word consisting of letters, no digits
        score = scrabble_score(word)
        high_scrab[word] = score   #create a dict, each item is the word, and the value is the scrabble score

#print high_scrab	

for word,score in high_scrab.items():
    if bigscore is None or score > bigscore:
        bigwordS = word
        bigscore = score

print "Highest scoring word(s) (according to Scrabble): '", bigwordS, "' with a score of", bigscore


handle.close()