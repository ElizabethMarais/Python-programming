#Coursera Python Course 4: Using Databases
#NB: test data file: DATA must contain no FLOAT numbers, only INTEGERs, and no special characters.
print "PROGRAM reads a text file line by line, (it uses 'DaleneMatthee_books_db.txt' as default), data was obtained from  "
print "it parses the words, stores info in a list. It prints the table rows in the database. "
print "Please enter 'DaleneMatthee_books_db.txt' as data file."

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS DaleneMattheebooks''')

cur.execute('''
CREATE TABLE DaleneMattheebooks (number INTEGER, year INTEGER, name TEXT, language TEXT) ''')
# year	name	language
import string
books = list()
i = 0
j = 0
print " "
fname = raw_input('Please enter text file name of Dalene Matthee s most favourite book translations of "Kringe in n bos" and "Fiela se kind": ')
if ( len(fname) < 1 ) : fname = 'DaleneMatthee_books_db.txt'
fh = open(fname)
for line in fh:
  if line.find(',') > 0:
            pos_num = line.find(',')
            numb = line[0:pos_num]  #find the number, read from begin of line till comma 
            numb_int = int(numb) 
            pos_year = line.find(',', pos_num+1)
            year = line[pos_num+1:pos_year]  #find the year book was published, read from begin of line till comma 
            year_int = int(year)          #strip all blank spaces before it, make integer
            #find the name in rest of line:
            pos_name  = line.find(',', pos_year+1)
            name = line[pos_year+1:pos_name]
            name = name.lstrip()
            #find the language in rest of line:
            pos_lang = line.find(',', pos_name +1)
            lang = line[pos_name +1:pos_lang]
            lang = lang.lstrip()    #strip all blank spaces before it
            item_list = numb_int, year_int, name, lang
            books.append(item_list)
            cur.execute('SELECT name FROM DaleneMattheebooks WHERE number = ?', (numb_int, ))   
            try:       #try: to test if there are rows
               pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
               cur.execute('UPDATE DaleneMattheebooks SET name = name WHERE number = ?', (numb_int, )) 
            except:
#if no rows, write a row, start with index 1
              cur.execute('''INSERT INTO DaleneMattheebooks (number, year, name, language) VALUES (?,?,?,?)''', (numb_int, year_int, name, lang))
  conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#OUTPUT:
print " "
print "PRINTING rows stored in table, displaying limited to 30 rows. "
print "No.  Year    Name 	                 Language "
space1 = "  "
space2 = " "
sqlstr = 'SELECT * FROM DaleneMattheebooks order by number ASC LIMIT 30'   # if want to limit rows printed: LIMIT 100

for row in cur.execute(sqlstr):
   if row[0] < 10:
       space = space1
   else:
       space = space2
   print row[0], space, row[1], "  ", row[2], "     ", row[3]

print " "
print "PRINT selected rows of 'Year published', year entered by the user, first 15. "
string_build  = None
string_build = ""
x = raw_input("Please enter the year to select books published, 1984: ")
like_str = "'" + x + '%' + "'"
string_build1 = 'like ' + like_str + 'LIMIT 15'
string_build  = "SELECT * FROM DaleneMattheebooks WHERE year " + string_build1
sqlstr = string_build

for row in cur.execute(sqlstr):
   print row[0], space, row[1], "  ", row[2], "     ", row[3]

cur.close()