#Coursera Python course 4: SQL extra
print "PROGRAM reads a data file: Universities listed, with details: also 11 official languages of South-Africa, spoken by number of people, and percentage of total languages."
print "UNIVERSITIES "

import sqlite3
conn = sqlite3.connect('universitydb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Universities ''')

cur.execute('''
DROP TABLE IF EXISTS Languages ''')

cur.execute('''
CREATE TABLE Universities (Institution TEXT, Nickname TEXT, Founded TEXT,   University_status TEXT,  Total_students INTEGER, Location TEXT, Medium TEXT)''')   
 
cur.execute('''
CREATE TABLE Languages (Language TEXT, Number_spoken INTEGER, Percent REAL)''')    


# University of Cape Town;	Ikeys / UCT;	01/10/1829;	02/04/1918;	33000;	Cape Town;	Eng;
#Institution	Nickname	Founded	University status	Total	Location	Medium

print "When prompted, please enter 'Universities.txt' as data file."
name = raw_input("Enter file of the Universities information: ")
if len(name) < 1 or name <> "Universities.txt" : name = "Universities.txt"
univ_list = list()
j = 0
fh = open(name)
for line in fh:
   if line > "/n":   #if it is not a blank line

#find the name
      pos_Instname = line.find(';')
      Institution = line[0:pos_Instname]
      Institution = Institution.lstrip()   #strip all blank spaces before it1
#      print Institution 

#find the nickname
      pos_nickname = line.find(';', pos_Instname+1)
      Nickname = line[pos_Instname+1:pos_nickname]
      Nickname = Nickname.lstrip()   #strip all blank spaces before it
#      print Nickname 
      
# find year founded
      pos_founded = line.find(';', pos_nickname+1)
      Founded = line[pos_nickname+1:pos_founded] 
#      print Founded 

#find the University_status
      pos_University_status = line.find(';', pos_founded+1) 
      University_status = line[pos_founded+1:pos_University_status]  
      University_status = University_status.lstrip()    #strip all blank spaces before it
#      print University_status 

#find the Total_students in rest of line:
      pos_Total_students = line.find(';', pos_University_status+1)
      Total_students = line[pos_University_status+1:pos_Total_students]
      Total_students = int(Total_students.lstrip())    #strip all blank spaces before it
#      print Total_students
  
#find the Location in rest of line:
      pos_Location = line.find(';', pos_Total_students+1)
      Location = line[pos_Total_students +1:pos_Location]
      Location = Location.lstrip()    #strip all blank spaces before it
#     print Location 

#find the Medium in rest of line:
      pos_Medium = line.find(';', pos_Location +1)
      Medium = line[pos_Location+1:pos_Medium]
      Medium = Medium.lstrip()    #strip all blank spaces before it
#      print Medium 
      
      list_item = Institution, Nickname, Founded, University_status,Total_students,Location, Medium
      univ_list.append(list_item)
      position = j
      cur.execute('''INSERT INTO Universities (Institution, Nickname, Founded, University_status,Total_students,Location, Medium) VALUES (?,?,?,?,?,?,?)''', (Institution,Nickname, Founded, University_status,Total_students,Location, Medium))
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#Languages
lang_list = list()
j = 0
fname = 'languages.txt'
fh = open(fname)
for line in fh:
   if line > "/n":   #if it is not a blank line

#find the Language
      pos_language = line.find(';')
      Language = line[0:pos_language]
      Language = Language.lstrip()   #strip all blank spaces before it

#find the Number_spoken
      pos_Number_spoken = line.find(';', pos_language+1)
      Number_spoken = line[pos_language+1:pos_Number_spoken]
      Number_spoken = int(Number_spoken.lstrip())   #strip all blank spaces before it

# find Percent
      pos_Percent = line.find(';', pos_Number_spoken+1)
      Percent = line[pos_Number_spoken+1:pos_Percent] 
      Percent = float(Percent)
            
      list_item = Language,	Number_spoken,	Percent
      lang_list.append(list_item)
      position = j
      cur.execute('''INSERT INTO Languages (Language, Number_spoken, Percent) VALUES (?,?,?)''', (Language, Number_spoken, Percent))
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

print " "
print "OUTPUT 1: PRINT rows in Universities info table."
print "Institution	Nickname Founded  University_status   Total_students  Location	  Medium/Language"
sqlstr = 'SELECT * FROM Universities order by Total_students DESC'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "  ",  row[4], "  ", row[5], "  ", row[6]

print " "
print "OUTPUT 2: PRINT rows in Languages info table: 11 official languages of South-Africa, spoken by number of people."
print "Language  Number_spoken  Percent_of_total_languages "
sqlstr = 'SELECT * FROM Languages order by Percent DESC'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2]

print " "
#COMBINED SQL STATEMENTS
print "OUTPUT 3: Print some information using COMBINED SQL STATEMENTS. "
print "Institution	Founded  Total_students  Location  Univ_Medium/Language     Language_Spoken_by_SA_people"
sqlstr = "SELECT Universities.Institution, Universities.Founded, Universities.Total_students,  Universities.Location, Universities.Medium, Languages.Number_spoken FROM Universities JOIN Languages ON Universities.Medium = Languages.Language"
for row in cur.execute(sqlstr):
    print row[0], " ", row[1], "", row[2], " ",  row[3], " ", row[4]," ", row[5]

cur.close()