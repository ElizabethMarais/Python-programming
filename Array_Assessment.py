#Optim Python Assessment - Elizabeth (JEH) Marais

#Assignment:
#Use the supplied CSV-files to build an array that will resemble the structure of supplied file called 'Sample Data Capture'. 
#You may use a database or array to create a SQL 'Select' statement that will show one total of all the employees
#working in the 'Sales' and 'Research' departments where the employees of both departments earn an 'Hourly Rate' of between 10 and 20. 
#Also display the total calculated. Create a text file called 'CSV-Result.csv' and insert the resultset into that file. 
#Create a second text file called 'SQL_Syntax.txt' and insert the SQL-syntax you used to obtain the resultset. 
#Create a third file called 'Resultset-Total.txt' and insert the Total of the above mentioned task into that. 

print " "
print "PROGRAM READS DATA FILES, COMPILES IT INTO ONE FILE, CALCULATES THE EARNED AMOUNT, DISPLAYS RESULTS, ALSO WRITES TO A CSV FILE"

import csv
import urllib2
import sqlite3
conn = sqlite3.connect('Assessm_db.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Employees ''')

cur.execute('''
CREATE TABLE Employees (Number INTEGER, First TEXT, Last TEXT, Dept TEXT, Benefit TEXT, Hours REAL, HourlyRate REAL, GrossPay REAL)''')    

print " "
EmpList = list()
fileEmp = 'Employee data.csv'
fh = open(fileEmp)
connection = open(fileEmp)
data = connection.read()

with open('Employee data.csv') as csvfile:
    employees = list(csv.DictReader(csvfile))

print " "

print "Employee data list:"
for i in range(0, len(employees)):
    num = int(employees[i]["NUM"])
    first = employees[i]["FIRST"]
    last = employees[i]["LAST"]

    itemEmp = num, first, last
    EmpList.append(itemEmp)

EmpList.sort()
print EmpList
print " "


print " ~~~~~~~~~~~~~~~~~~~~~~ Department data  ~~~~~~~~~~~~~~~~~~~~~"
DepList = list()
fileDep = 'Department_data.csv'
fh = open(fileDep)
connection = open(fileDep)
data = connection.read()

with open('Department_data.csv') as csvfile:
    department = list(csv.DictReader(csvfile))

print "Department data list:"
for i in range(0, len(department)):
    num = int(department[i]["NUM"])
    dep = department[i]["DEPT"]
	
    itemDep = num, dep
    DepList.append(itemDep)

DepList.sort()
print DepList 

print " "

print " ~~~~~~~~~~~~~~~~~~~~~~ Health Benefits Data ~~~~~~~~~~~~~~~~~~~~~~"
HBList = list()
fileHB = 'Health Benefits Data2.csv'
fh = open(fileHB)
connection = open(fileHB)
data = connection.read()

with open('Health Benefits Data2.csv') as csvfile:
    HB= list(csv.DictReader(csvfile))

print "Health Benefits Data list:"
for i in range(0, len(HB)):
  try:
    num = int(HB[i]["NUM"])
    benefit = HB[i]["BEN"]
    itemHB = num, benefit
    HBList.append(itemHB)
  except:   pass   #Data_error	:
       
HBList.sort()
print HBList 

print " "

print " ~~~~~~~~~~~~~~~~~~~~ Salary Data ~~~~~~~~~~~~~~~~~~~~~~~~~~ "

SalList = list()
fileSal = 'Salary Data .csv'
fh = open(fileSal)
connection = open(fileSal)
data = connection.read()

with open('Salary data .csv') as csvfile:
   Sal = list(csv.DictReader(csvfile))

print "Salary Data list:"
for i in range(0, len(Sal)):
  try:
    num = int(Sal[i]["NUM"])
    hours = float(Sal[i]["HRS"])
    Hrlyrate = float(Sal[i]["HOURLYRATE"])
    itemSal = num, hours, Hrlyrate
    SalList.append(itemSal)
  except:   pass   #Data_error	:
       
SalList.sort()
print SalList 

print " "

# ~~~~~~~~~~~~~~~~~~~~~~ Append the other data to the EmpList and write the rows into the sqlite file  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TempList = list()
EmpDepList = list()
for j in range(0, len(EmpList)):   
         for i in range(0,3) :                    
                TempList.append(EmpList[j][i])    #append each of 3 items of original EmpList into a new Templist
                i = i +1		
         TempList.append(DepList[j][1])           #append Department code
         TempList.append(HBList[j][1])            #append Health benefit
         TempList.append(SalList[j][1])            #append Salary hours
         TempList.append(SalList[j][2])            #append Salary hourlyrate   
         Gross_salary = round(SalList[j][1] * SalList[j][2],2)    #compile the gross salary
         TempList.append(Gross_salary)
         EmpDepList.append(TempList)
         # write a line into the sqlite db
         cur.execute('''INSERT INTO Employees(Number, First, Last, Dept, Benefit, Hours, HourlyRate, GrossPay) VALUES (?,?,?,?,?,?,?,?)''', (TempList[0], TempList[1], TempList[2], TempList[3], TempList[4], TempList[5], TempList[6], TempList[7]))
         TempList = list()                          #redefine list to clear it
         j = j + 1
conn.commit()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ SQL STATEMENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print " "
print "RESULT: Select the employees working in the 'Sales' and 'Research' departments where the employees of both departments earn an 'Hourly Rate' of between 10 and 20 sorted alphabetically. The total earned is displayed at the end."
print " "
print "First  Last   Department   Benefit   Hours   HourlyRate    GrossPay"
sqlstr = "SELECT First, Last, Dept, Benefit, Hours, HourlyRate, GrossPay FROM Employees WHERE (Dept = 'Sales' OR Dept = 'Research') AND (HourlyRate >= 10 AND HourlyRate <= 20) ORDER BY Last, First"
i = 1
total = 0
datalist = list()
for row in cur.execute(sqlstr):
     print i, row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4], "  ", "$", row[5], "   $", row[6]
     row_csv = i, row[0], row[1], row[2], row[3], row[4], "$"+str(row[5]), "$"+str(row[6])
     datalist.append(row_csv)
     total = total + row[6]
     i = i + 1
cur.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ WRITE RESULTS INTO CSV ILE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write the results into a csv file
with open('CSV-Result.csv', 'wb') as csvfile:
       spamwriter = csv.writer(csvfile, delimiter=',') 
       spamwriter.writerows(datalist)
csvfile.close()

print " "
print "Total earned is: $", total

   

