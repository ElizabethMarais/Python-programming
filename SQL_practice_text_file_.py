#Coursera Python Course 4: Using Databases
print "PROGRAM reads a text file line by line, (it uses intro-short.txt as default);  it parses the words, changes them to lower case, removes all punctuation marks, and stores the word and its position in a table, 'Word-Position'. "
print "It prints the list of individual words formed (first 100); the table rows; all rows with words containing 'you'; and all rows of words starting with a letter the user enters." 
print "Please be patient to parse the file if it is long."	

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS WordPosition''')

cur.execute('''
CREATE TABLE WordPosition (position INTEGER, word TEXT)''')

import string
words = list()
i = 0
j = 0
print " "
fname = raw_input('Please enter text file name: ')
if ( len(fname) < 1 ) : fname = 'intro-short.txt'
fh = open(fname)
for line in fh:
  if line > "/n":   #if it is not a blank line
    pieces = line.split()
    for i in range(len(pieces)):
      word = pieces[i].translate(string.maketrans("",""), string.punctuation)   #remove all punctuation marks e.g. '.'
      word = word.lower()
      list_item = j, word
      words.append(list_item)
      position = j
      j += 1   #increment word count, position
      cur.execute('SELECT word FROM WordPosition WHERE position = ?', (j, ))   
#1. ? place holder   2.(word, ) is a tuple (need comma, space), instead of WHERE...
      try:       #try: to test if there are rows
        position = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
#        cur.execute('UPDATE WordPosition SET position = j+1 WHERE word = ?', (word, ))
        cur.execute('UPDATE WordPosition SET word = word WHERE position = ?', (j, )) 
      except:
#if no rows, write a row, start with index 1
        cur.execute('''INSERT INTO WordPosition VALUES (?,?)''', (position, word))

  conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#OUTPUT:
print " "
print "PRINT Words in list formed from individual words in text (first 10):"
print words[0:10]

print " "
print "PRINTING rows stored in table: print 'Position' and 'Word', the first 15. "
sqlstr = 'SELECT position, word FROM WordPosition order by position ASC LIMIT 15'   # if want to limit rows printed: LIMIT 100

for row in cur.execute(sqlstr):
     print str(row[0]), row[1]
     if row == 20: break

print " "
print "PRINT all words and their positions starting with 'you' or 'your', the first 15."
print "Position Word"
sqlstr_y = 'SELECT position, word FROM WordPosition WHERE word="you" OR word="your" LIMIT 15 '

for row in cur.execute(sqlstr_y):
     print str(row[0]), row[1]
     if row == 30: break

print " "
print "PRINT all words and their positions starting with letter supplied by user, first 15. "
string_build  = None
string_build = ""
x = raw_input("Please enter a letter to select and print all rows of words starting with it: ")
like_str = "'" + x + '%' + "'"
string_build1 = 'like ' + like_str + 'LIMIT 15'
string_build  = "SELECT position, word FROM WordPosition WHERE word " + string_build1
sqlstr = string_build

print "Position Word"
for row in cur.execute(sqlstr):
     print str(row[0]), row[1]
     if row == 30: break

cur.close()