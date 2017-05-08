#Coursera Python Course 4: Using Databases
print "PROGRAM reads text files of projects and client details (it uses 'Eng_Projects.txt' and 'Eng_Clients.txt' as default), it parses the words, stores info in a list. It prints the table rows in the database."
print "Please enter the 'Eng_Projects.txt' when prompted as data file."

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS EngProjects ''')

cur.execute('''
DROP TABLE IF EXISTS EngClients ''')


cur.execute('''
CREATE TABLE EngProjects (Acc_no TEXT, Invoice_no TEXT, Proj_no TEXT, Proj_name TEXT, Client TEXT, Date_Inv TEXT, Amount INTEGER)''')

cur.execute('''
CREATE TABLE EngClients (name TEXT, address TEXT, VAT_No INTEGER, Contact_person TEXT, Email_address TEXT)''')

# EngClients
#read project clients details from text file, 'Eng_Clients.txt'
import string
client_list = list()
i = 0
j = 0
print " "
fname = 'Eng_Clients.txt'
fh = open(fname)
for line in fh:
   if line > "/n":   #if it is not a blank line
# find client name
      pos_name = line.find(';')
      nameI = line[0:pos_name] 
#      print nameI
           
#find the Invoice_no
      pos_address = line.find(';', pos_name +1)
      address = line[pos_name+1:pos_address]  
      address = address.lstrip()    #strip all blank spaces before it
      addressI = address
#      print addressI        

  #find the VAT no. in rest of line:
      pos_VAT_No  = line.find(';', pos_address+1)
      VAT_No = line[pos_address+1:pos_VAT_No  ]
      VAT_No = VAT_No.lstrip()    #strip all blank spaces before it
      VAT_NoI = int(VAT_No)
#      print VAT_NoI
  
  #find the Contact_person in rest of line:
      pos_contact_person = line.find(';', pos_VAT_No +1)
      contact_person = line[pos_VAT_No +1:pos_contact_person]
      contact_personI = contact_person.lstrip()    #strip all blank spaces before it
#      print contact_personI

     #find the Email_address in rest of line:
      pos_Email = line.find(';', pos_contact_person+1)
      Email = line[pos_contact_person+1:pos_Email]
      EmailI = Email.lstrip()    #strip all blank spaces before it
#      print EmailI
      
      list_item = nameI, addressI, VAT_NoI, contact_personI, EmailI
      client_list.append(list_item)
      position = j
      cur.execute('SELECT address FROM EngClients WHERE name = ?', (nameI, ))   
#1. ? place holder   2.(  , ) is a tuple (need comma, space), instead of WHERE...
      try:       #try: to test if there are rows
        pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
        cur.execute('UPDATE EngClients SET address = address WHERE name = ?', (nameI, ))   
      except:
#if no rows, write a row, start with index 1
        cur.execute('''INSERT INTO EngClients (name, address, VAT_No, Contact_person, Email_address) VALUES (?,?,?,?,?)''', (nameI, addressI, VAT_NoI, contact_personI, EmailI))
#     j += 1   #increment count, position
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#print client_list

# Eng_Projects
import string
projects = list()
i = 0
j = 0
print " "
fname = raw_input('Please enter text file name of engineering projects: ')
if ( len(fname) < 1 ) : fname = 'Eng_Projects.txt'
fh = open(fname)
for line in fh:
# EngProjects (Acc_no INTEGER, Invoice_no TEXT, Proj_no TEXT, Proj_name TEXT, Client TEXT, Date_Inv TEXT, Amount INTEGER
   if line > "/n":   #if it is not a blank line
#find the Account no, read from begin of line till comma 
         pos_accno = line.find(';')
         accno = line[0:pos_accno]              
         accnoI = int(accno.lstrip())
#         print accnoI
  
#find the Invoice_no, read after name till comma 
         pos_Invoice_no = line.find(';', pos_accno+1)
         Invoice_no = line[pos_accno+1:pos_Invoice_no] 
         Invoice_no = Invoice_no.lstrip()
         Invoice_noI = 'PEE ' + Invoice_no
#         print Invoice_noI

 #find the Project number in rest of line:
         pos_Proj_no = line.find(';', pos_Invoice_no+1)
         Proj_no = line[pos_Invoice_no+1:pos_Proj_no]
         Proj_noI = Proj_no.lstrip()    
#         print Proj_noI

 #find the Project name in rest of line
         pos_Proj_name = line.find(';', pos_Proj_no+1)
         Proj_name = line[pos_Proj_no+1:pos_Proj_name]
         Proj_nameI = Proj_name.lstrip() #strip all blank spaces before it
#         print Proj_nameI

#find the Client in rest of line
         pos_Client = line.find(';', pos_Proj_name+1)
         Client = line[pos_Proj_name+1:pos_Client]
         ClientI = Client.lstrip() #strip all blank spaces before it
#         print ClientI
 
#find the Date Invoice in rest of line
         pos_Date_Inv = line.find(';', pos_Client+1)
         Date_Inv = line[pos_Client+1:pos_Date_Inv]
         Date_InvI = Date_Inv.lstrip() #strip all blank spaces before it
#         print Date_InvI

#08;	17/026;	    P1170;   Wingtip;	Pretoria;	WINGTIP CROSSING SHOPPING CENTRE (PTY) LTD;	19-04-2017;	44922;
#Acc_no  Invoice_no  Proj_no  Proj_name                  Client TEXT,                                   Date_Inv TEXT,    Amount INTEGER)''')

#find the Amount in rest of line
         pos_Amount = line.find(';', pos_Date_Inv+1)
         Amount = line[pos_Date_Inv+1:pos_Amount]   #read till end of line
         AmountI = int(Amount.lstrip()) #strip all blank spaces before it
#         print AmountI

         item_list = accnoI, Invoice_noI, Proj_noI, Proj_nameI, ClientI, Date_InvI, AmountI
         projects.append(item_list)      
         position = j
         cur.execute('SELECT Date_Inv FROM EngProjects WHERE Invoice_no = ?', (Invoice_noI, ))   
	#1. ? place holder   2.(  , ) is a tuple (need comma, space), instead of WHERE...
         try:       #try: to test if there are rows
            pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
            cur.execute('UPDATE EngProjects SET Date_Inv = Date_InvI EngProjects WHERE Invoice_no = ?', (Invoice_noI, ))   
         except:
#if no rows, write a row, start with index 1
             cur.execute('''INSERT INTO EngProjects (Acc_no, Invoice_no, Proj_no, Proj_name, Client, Date_Inv, Amount) VALUES (?,?,?,?,?,?,?)''', (accnoI, Invoice_noI, Proj_noI, Proj_nameI, ClientI, Date_InvI, AmountI))
         j += 1   #increment word count, position
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#print projects

print " "
print "PRINT rows in Invoices table."
print "Acc no Invoice no   Project No.   Project Name       Client                    Date Inv.    Amount"
sqlstr = 'SELECT * FROM EngProjects'   # order by year ASC'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4], "  ", row[5], "  ",  row[6]

print " "
print "PRINT rows in Clients table."
print "Client Name   Address                       VAT_No    Contact person    Email address" 
sqlstr = 'SELECT * FROM EngClients order by name'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4]

print " "
print "PRINT information from Invoice table, added the Client VAT no. & email address, looked up from Clients table. "
print "Invoice no   Project No.  Project Name       Client                    Date Inv.    Amount    VAT no.   Email"
sqlstr = 'SELECT * FROM EngProjects'
for i in range(len(projects)):
    item1 = projects[i][1]    #Inv no
    item2 = projects[i][2]    # Proj no
    item3 = projects[i][3]    #proj name
    item4 = projects[i][4]    #client
    item5 = projects[i][5]    #date inv
    item6 = "R" + str(projects[i][6])     #amount
    sqlstr = "SELECT VAT_no, Email_address FROM EngClients WHERE name like '" + item4 + "%'"
    for row in cur.execute(sqlstr):
        print item1, "  ",item2, "  ", item3,  "  ", item4,  "  ", item5,  "  ", item6,  "  ", row[0], "  ", row[1]

cur.close()
