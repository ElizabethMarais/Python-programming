#Coursera Python Course 4: Using Databases
print "PROGRAM reads text files of projects and client details (it uses 'Eng_ProjectsR.txt', 'Eng_ClientsCI.txt', 'EngProj_Projinfo.txt' as default), it parses the words, stores info in a list. It prints the table rows in the database."
print "Please enter the 'Eng_ProjectsR.txt' when prompted as data file (this text file has FLOAT/REAL values for Invoice Amounts."

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS EngProjects ''')

cur.execute('''
DROP TABLE IF EXISTS EngClients ''')

cur.execute('''
DROP TABLE IF EXISTS EngProjInfo ''')

cur.execute('''
CREATE TABLE EngProjects (Acc_no TEXT, Invoice_no TEXT, Proj_no TEXT, Proj_name TEXT, Client TEXT, Client_Id INTEGER, Date_Inv TEXT, Amount REAL)''')

cur.execute('''
CREATE TABLE EngClients (Client_Id INTEGER, name TEXT, address TEXT, VAT_No INTEGER, Contact_person TEXT, Email_address TEXT)''')

cur.execute('''
CREATE TABLE EngProjInfo (ProjNo TEXT, ProjectName TEXT, Contract_Amount INTEGER, ProfFee INTEGER)''')

# EngClients
#read project clients details from text file, 'Eng_ClientsCI.txt'
import string
client_list = list()
i = 0
j = 0
fname = 'Eng_ClientsCI.txt'
fh = open(fname)
for line in fh:
   if line > "/n":   #if it is not a blank line

#find the Client_Id
      pos_Client_Id = line.find(';')
      Client_Id = line[0:pos_Client_Id]
      Client_IdI = Client_Id.lstrip() #strip all blank spaces before it, change to type integer
      Client_IdI = int(Client_IdI)

# find client name
      pos_name = line.find(';', pos_Client_Id+1)
      nameI = line[pos_Client_Id+1:pos_name] 
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
      
      list_item = Client_Id, nameI, addressI, VAT_NoI, contact_personI, EmailI
      client_list.append(list_item)
#      position = j
      cur.execute('SELECT address FROM EngClients WHERE Client_Id = ?', (Client_IdI, ))   
#1. ? place holder   2.(  , ) is a tuple (need comma, space), instead of WHERE...
      try:       #try: to test if there are rows
        pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
        cur.execute('UPDATE EngClients SET name = nameI WHERE Client_Id = ?', (Client_IdI, ))   
      except:
#if no rows, write a row, start with index 1
        cur.execute('''INSERT INTO EngClients (Client_Id, name, address, VAT_No, Contact_person, Email_address) VALUES (?,?,?,?,?,?)''', (Client_IdI, nameI, addressI, VAT_NoI, contact_personI, EmailI))
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#print client_list

# Eng_ProjectsR
import string
projects = list()
i = 0
j = 0
print " "
fname = raw_input('Please enter text file name of engineering projects: ')
if ( len(fname) < 1 ) or fname <> 'Eng_ProjectsR.txt' : fname = 'Eng_ProjectsR.txt'
fh = open(fname)
for line in fh:
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

#find the Client_Id in rest of line
         pos_Client_Id = line.find(';', pos_Client+1)
         Client_Id = line[pos_Client+1:pos_Client_Id]
         Client_IdI = int(Client_Id.lstrip()) #strip all blank spaces before it, change to type integer
#         print Client_IdI
 
#find the Date Invoice in rest of line
         pos_Date_Inv = line.find(';', pos_Client_Id+1)
         Date_Inv = line[pos_Client_Id+1:pos_Date_Inv]
         Date_InvI = Date_Inv.lstrip() #strip all blank spaces before it
#         print Date_InvI

#find the Amount in rest of line
         pos_Amount = line.find(';', pos_Date_Inv+1)
         Amount = line[pos_Date_Inv+1:pos_Amount]   #read till end of line
         AmountI = float(Amount.lstrip()) #strip all blank spaces before it
 #        print AmountI

         item_list = accnoI, Invoice_noI, Proj_noI, Proj_nameI, ClientI, Client_IdI, Date_InvI, AmountI
         projects.append(item_list)      
#         position = j
         cur.execute('SELECT Date_Inv FROM EngProjects WHERE Invoice_no = ?', (Invoice_noI, ))   
	#1. ? place holder   2.(  , ) is a tuple (need comma, space), instead of WHERE...
         try:       #try: to test if there are rows
            pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
            cur.execute('UPDATE EngProjects SET Date_Inv = Date_InvI EngProjects WHERE Invoice_no = ?', (Invoice_noI, ))   
         except:
#if no rows, write a row, start with index 1
             cur.execute('''INSERT INTO EngProjects (Acc_no, Invoice_no, Proj_no, Proj_name, Client, Client_Id, Date_Inv, Amount) VALUES (?,?,?,?,?,?,?,?)''', (accnoI, Invoice_noI, Proj_noI, Proj_nameI, ClientI, Client_IdI, Date_InvI, AmountI))
#         j += 1   #increment word count, position
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#print projects

# EngProjInfo
#read projects info details from text file, 'EngProj_Projinfo.txt'
#ProjNo.	  Project Name	Contract_Amount	  ProfFee
import string
ProjInfo_list = list()
i = 0
j = 0
fname = 'EngProj_Projinfo.txt'
fh = open(fname)
for line in fh:
   if line > "/n":   #if it is not a blank line
#find the Client_Id
      pos_ProjNo = line.find(';')
      ProjNo = line[0:pos_ProjNo]
      ProjNoI = ProjNo.lstrip()  #strip all blank spaces before it
#      print ProjNoI

# find client name
      pos_ProjectName = line.find(';', pos_ProjNo+1)
      ProjectName= line[pos_ProjNo+1:pos_ProjectName] 
      ProjectNameI = ProjectName.lstrip()  #strip all blank spaces before it
#      print ProjectNameI
           
#find the Contract_Amount
      pos_Contract_Amount = line.find(';', pos_ProjectName +1)
      Contract_Amount = line[pos_ProjectName+1:pos_Contract_Amount]  
      Contract_AmountI = int(Contract_Amount.lstrip())      #strip all blank spaces before it, to int.
#      print Contract_AmountI

#find the ProfFee
      pos_ProfFee  = line.find(';', pos_Contract_Amount +1)
      ProfFee  = line[pos_Contract_Amount+1:pos_ProfFee]  
      ProfFeeI  = int(ProfFee.lstrip())      #strip all blank spaces before it, to int.
  
      list_item = ProjNoI, ProjectNameI, Contract_AmountI, ProfFeeI
      ProjInfo_list.append(list_item)
      position = j
      cur.execute('SELECT * FROM EngProjInfo WHERE ProjNo = ?', (ProjNoI, )) 
      try:       #try: to test if there are rows
        pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
        cur.execute('UPDATE EngProjInfo SET ProjectName = ProjectNameI WHERE ProjNo = ?', (ProjNoI, ))   
      except:
#if no rows, write a row, start with index 1
        cur.execute('''INSERT INTO EngProjInfo (ProjNo, ProjectName, Contract_Amount, ProfFee) VALUES (?,?,?,?)''', (ProjNoI, ProjectNameI, Contract_AmountI, ProfFeeI))
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#print ProjInfo_list

print " "
print "OUTPUT 1: PRINT rows in Projects info table."
print "Proj.No ProjectName          Contract_Amount  Prof.Fee"
sqlstr = 'SELECT * FROM EngProjInfo'   # order by year ASC'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", "R", row[2], "  ",  "R", row[3]

print " "
print "OUTPUT 2: PRINT rows in Invoices table , amounts decimal (real/float))(first 6)."
print "Acc no Invoice no   Project No.   Project Name       Client                    Date Inv.    Amount"
sqlstr = 'SELECT Acc_no, Invoice_no, Proj_no, Proj_name, Client, Date_Inv, Amount FROM EngProjects LIMIT 6'   # order by year ASC'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4], "  ", row[5], "  ", "R", row[6]

print " "
print "OUTPUT 3: PRINT rows in Clients table (first 6)."
print "Client Name   Address                       VAT_No    Contact person    Email address" 
sqlstr = 'SELECT name, address, VAT_No, Contact_person, Email_address FROM EngClients order by Client_Id LIMIT 6'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4]

print " "
#COMBINED SQL STATEMENTS
print "OUTPUT 4: Print some information from Invoice table; add Client VAT no. & email address extracted from Clients table using COMBINED SQL STATEMENTS (first 6). "
print "Invoice no.  Amount  ProjNo. Client                 VAT no.   EmailAddress"
sqlstr = "SELECT EngProjects.Invoice_no, EngProjects.Amount,  EngProjects.Proj_no, EngProjects.Client, EngClients.VAT_no,  EngClients.Email_address FROM EngProjects JOIN EngClients ON EngProjects.Client_Id = EngClients.Client_Id LIMIT 6"
for row in cur.execute(sqlstr):
    amount = "R" + str(row[1])
    print row[0], " ", amount, "", row[2], " ",  row[3], " ", row[4]," ", row[5]

print " "
print "OUTPUT 5: Print some from Invoice table, add Client VAT no. & email address extracted from Clients table, and Project's Prof. Fee amount from ProjInfo table using COMBINED SQL STATEMENTS. "
print "Invoice no.  Amount  ProjNo. Client                 VAT no.   EmailAddress    Prof.Fee"
sqlstr = "SELECT EngProjects.Invoice_no, EngProjects.Amount,  EngProjects.Proj_no, EngProjects.Client, EngClients.VAT_no,  EngClients.Email_address, EngProjInfo.ProfFee FROM EngProjects JOIN EngClients JOIN EngProjInfo ON EngProjects.Client_Id = EngClients.Client_Id AND EngProjects.Proj_no = EngProjInfo.ProjNo "
for row in cur.execute(sqlstr):
    amount = "R" + str(row[1])
    print row[0], " ", amount, "", row[2], " ",  row[3], " ", row[4]," ", row[5], " ", "R", row[6]

cur.close()
