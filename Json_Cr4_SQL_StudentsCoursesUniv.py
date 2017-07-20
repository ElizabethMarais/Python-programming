#Coursera Python course 4: SQL extra
print "PROGRAM reads a data file: Universities listed, with details: also 11 official languages of South-Africa, spoken by number of people, and percentage of total languages."
print "UNIVERSITIES "

import sqlite3
import json
conn = sqlite3.connect('univ_studentsdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Universities ''')

cur.execute('''
DROP TABLE IF EXISTS Languages ''')

cur.execute('''
DROP TABLE IF EXISTS Students ''')

cur.execute('''
DROP TABLE IF EXISTS Stud_Courses ''')

cur.execute('''
CREATE TABLE Universities (Institution TEXT, Nickname TEXT, Founded TEXT,   University_status TEXT, Total_students INTEGER, Location TEXT, Medium TEXT)''')   
 
cur.execute('''
CREATE TABLE Languages (Language TEXT, Number_spoken INTEGER, Percent REAL)''')    

cur.execute('''
CREATE TABLE Students (Student_no TEXT, Name TEXT, ID_no TEXT, Birth_date TEXT, Address TEXT,   Cell_no TEXT)''') 
   
cur.execute('''
CREATE TABLE Stud_Courses (Student_no TEXT, Institution TEXT, Course TEXT)''')    


#Universities
file1 = 'Json_Cr4_SQL_Students_Universities.json'
connection = open(file1)
data = connection.read()
info1_data = json.loads(data)
info1 = info1_data["data"]
print 'Retrieved', len(info1),'items in list'
print " "

for i in range(0, len(info1)):
    print 'Institution:', info1[i]["Institution"]
    print 'Nickname:', info1[i]["Nickname"]
    print 'Founded:', info1[i]["Founded"]
    print 'University_status_date:', info1[i]["University_status"]
    print 'Total students:', info1[i]["Total_students"]
    print 'Location:', info1[i]["Location"]
    print 'Medium:', info1[i]["Medium"]
    print " "

    Institution = info1[i]["Institution"]
    Nickname = info1[i]["Nickname"]
    Founded = info1[i]["Founded"]
    University_status = info1[i]["University_status"]
    Total_students = info1[i]["Total_students"]
    Location = info1[i]["Location"]
    Medium = info1[i]["Medium"]
    cur.execute('''INSERT INTO Universities (Institution, Nickname, Founded, University_status,Total_students,Location, Medium) VALUES (?,?,?,?,?,?,?)''', (Institution,Nickname, Founded, University_status,Total_students,Location, Medium))
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#Languages
j = 0
file2 = 'Json_Cr4_SQL_Students_Languages.json'
connection = open(file2)
data = connection.read()
info2_data = json.loads(data)
info2 = info2_data["data"]
print 'Retrieved', len(info2),'items in list'
print " "

for i in range(0, len(info2)):
    print 'Language:', info2[i]["Language"]
    print 'Number spoken:', info2[i]["Number_spoken"]
    print 'Percent:', info2[i]["Percent"], "%"
    print " "
    Language = info2[i]["Language"]
    Number_spoken = info2[i]["Number_spoken"]
    Percent = info2[i]["Percent"]
    cur.execute('''INSERT INTO Languages (Language, Number_spoken, Percent) VALUES (?,?,?)''', (Language, Number_spoken, Percent))
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#Students 
#(Student_no TEXT, Name TEXT, ID_no TEXT, Birth_date TEXT, Address TEXT,  Cell_no TEXT)''') 
j = 0
file3 = 'Json_Cr4_SQL_Students_info.json'
connection = open(file3)
data = connection.read()
info3_data = json.loads(data)
info3 = info3_data["data"]

print 'Retrieved', len(info3),'items in list'
print " "
for i in range(0, len(info3)):
    print 'Student_no:', str(info3[i]["Student_no"])
    print 'Name:', str(info3[i]["Name"])
    print 'ID no:', str(info3[i]["ID_no"])
    print 'Birth date:', str(info3[i]["Birth_date"])
    print 'Address:', str(info3[i]["Address"])
    print 'Cell no:', str(info3[i]["Cell_no"])
    print " "

    Student_no =  info3[i]["Student_no"]
    Name =  info3[i]["Name"]
    ID_no= info3[i]["ID_no"]
    Birth_date= info3[i]["Birth_date"]
    Address= info3[i]["Address"]
    Cell_no= info3[i]["Cell_no"]
            
    cur.execute('''INSERT INTO Students (Student_no, Name, ID_no, Birth_date, Address,  Cell_no) VALUES (?,?,?,?,?,?)''', (Student_no, Name, ID_no, Birth_date, Address,  Cell_no))
conn.commit()

# Read from Stud_Courses data file, build into a list, write into SQL table
file4= 'Json_Cr4_SQL_Students_courses.json'
connection = open(file4)
data = connection.read()
info4_data = json.loads(data)
info4 = info4_data["data"]
print 'Retrieved', len(info4),'items in list'
print " "

for i in range(0, len(info4)):
    print 'Student_no:', info4[i]["Student_no"]
    print 'Institution:', info4[i]["Institution"]
    print 'Course:', info4[i]["Course"]
    print " "
    Student_no =  info4[i]["Student_no"]
    Institution= info4[i]["Institution"]
    Course= info4[i]["Course"]

    cur.execute('''INSERT INTO Stud_courses VALUES (?,?,?)''', (Student_no, Institution, Course))
conn.commit()

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
print "OUTPUT 3: PRINT rows in Students info table."
print "Student_no Name  ID_no  Birth_date Address  Cell_no "
sqlstr = 'SELECT Student_no, Name, ID_no, Birth_date, Address FROM Students'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "  ",  row[4]

print " "
print "OUTPUT 3b: PRINT rows in Students course table."
print "Student_no Institution Course  "
sqlstr = 'SELECT * FROM Stud_Courses'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2]

print " "
#COMBINED SQL STATEMENTS
print "OUTPUT 4: User enters a student no, print Student and their courses subscribed, and its student detail, the language of that University, using Combined SQL."
print "Student_no  StudentName   Stud_Address    Course  Institution    Univ_language"
Stud_noI = raw_input("Please enter a student number: ")
sqlstr = 'SELECT Stud_courses.Student_no, Students.Name, Students.Address,  Stud_Courses.Institution, Stud_Courses.Course FROM Students, Stud_Courses WHERE Students.Student_no ="' + Stud_noI + '" AND Stud_courses.Student_no ="' + Stud_noI + '" '
#sqlstr = 'SELECT Stud_courses.Student_no,  Students.Name, Students.Address, Stud_Courses.Course, Stud_Courses.Institution, Universities.Medium FROM Students JOIN Stud_Courses JOIN Universities JOIN Languages WHERE Students.Student_no ="' + Stud_noI + '" AND Students.Student_no =  Stud_Courses.Student_no AND Universities.Medium = Languages.Language'
#sqlstr = 'SELECT Students.Student_no,  Students.Name, Students.Address FROM Students WHERE Students.Student_no =' + Stud_noI
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], " ", row[2] ," ", row[3], " ",  row[4]#,  "  ",  row[5]

cur.close()