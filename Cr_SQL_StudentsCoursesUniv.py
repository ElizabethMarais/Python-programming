#Coursera Python course 4: SQL extra
print "PROGRAM reads a data file: Universities listed, with details: also 11 official languages of South-Africa, spoken by number of people, and percentage of total languages."
print "UNIVERSITIES "

import sqlite3
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



print "When prompted, please enter 'Universities.txt' as data file."
name = raw_input("Enter file of the Universities information: ")
if len(name) < 1 or name <> "Cr4_SQL_Students_Universities.txt" : name = "Cr4_SQL_Students_Universities.txt"
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
fname = 'Cr4_SQL_Students_Languages.txt'
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

#Students (Student_no TEXT, Name TEXT, ID_no TEXT, Birth_date TEXT, Address TEXT,  Cell_no TEXT)''') 
#Students 
students_list = list()
j = 0
fname = 'Cr4_SQL_Students_info.txt'
fh = open(fname)
for line in fh:
   if line > "/n":   #if it is not a blank line
#example:  1971031702666590;	JEH Marais;	197103170200085;	17/03/1971;	5 Hillcrest road, Hatfield, Pretoria;	0828029237;
#find the Student_no 
      pos_Student_no = line.find(';')
      Student_no = line[0:pos_Student_no]
      Student_no = Student_no.lstrip()   #strip all blank spaces before it
#      print Student_no

#find the student Name
      pos_Name = line.find(';', pos_Student_no+1)
      Name = line[pos_Student_no+1:pos_Name]
      Name = Name.lstrip()   #strip all blank spaces before it
#      print Name

# find ID_no 
      pos_ID_no = line.find(';', pos_Name +1)
      ID_no = line[pos_Name+1:pos_ID_no] 
#      print ID_no

#find the student Birth_date 
      pos_Birth_date = line.find(';', pos_ID_no+1)
      Birth_date = line[pos_ID_no+1:pos_Birth_date]
      Birth_date = Birth_date.lstrip()   #strip all blank spaces before it
#      print Birth_date 
# find Address 
      pos_Address = line.find(';', pos_Birth_date+1)	
      Address = line[pos_Birth_date+1:pos_Address] 
#      print Address
 # find Cell_no 
      pos_Cell_no = line.find(';', pos_Address+1)
      Cell_no = line[pos_Address+1:pos_Cell_no] 
#      print Cell_no
            
      list_item = Student_no, Name, ID_no, Birth_date, Address, Cell_no
      students_list.append(list_item)
      cur.execute('''INSERT INTO Students (Student_no, Name, ID_no, Birth_date, Address,  Cell_no) VALUES (?,?,?,?,?,?)''', (Student_no, Name, ID_no, Birth_date, Address,  Cell_no))
conn.commit()

# Read from Stud_Courses data file, build into a list, write into SQL table
stud_course_list = list()
j = 0
fname = 'Cr4_SQL_Students_courses.txt'
fh = open(fname)
for line in fh:
   if line > "/n":                                         #if it is not a blank line

#find the Student_no 
      pos_Student_no = line.find(';')
      Student_no = line[0:pos_Student_no]
      Student_no = Student_no.lstrip()   #strip all blank spaces before it

#find the Institution / University Name
      pos_Institution = line.find(';', pos_Student_no +1)
      Institution = line[pos_Student_no+1:pos_Institution]
      Institution = Institution.lstrip()   #strip all blank spaces before it 

# find Course 
      pos_Course = line.find(';', pos_Institution +1)
      Course = line[pos_Institution +1:pos_Course] 
      Course = Course.lstrip()   #strip all blank spaces before it 

      list_item = Student_no, Institution, Course
      stud_course_list.append(list_item)
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

#1972050902663420

#Students (Student_no TEXT, Name TEXT, ID_no TEXT, Birth_date TEXT, Address TEXT,   Cell_no TEXT)''') 
   
# Stud_Courses (Student_no TEXT, Institution TEXT, Course TEXT)''')    



cur.close()
