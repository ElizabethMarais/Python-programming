#Coursera Python Course 4: Using a csv data file
print "PROGRAM reads a couple of csv data files, store the data in tables, and does a few queries on it."

import csv
import urllib2
import sqlite3
conn = sqlite3.connect('EngProj_csvdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS BInvoices ''')

cur.execute('''
DROP TABLE IF EXISTS BClients ''')

cur.execute('''
DROP TABLE IF EXISTS BProjInfo ''')

cur.execute('''
CREATE TABLE BInvoices (Acc_no INTEGER, Invoice_no TEXT, Proj_no TEXT, Proj_name TEXT, Client TEXT, Client_Id INTEGER, Date_Inv TEXT, Amount REAL)''')    

cur.execute('''
CREATE TABLE BClients (Client_Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, address TEXT, VAT_no INTEGER, Contact_person TEXT, Email_address TEXT)''')

cur.execute('''
CREATE TABLE BProjInfo (ProjNo TEXT, ProjectName TEXT, Client_Id INTEGER, Contract_Amount INTEGER, ProfFee INTEGER, PRIMARY KEY (ProjNo, ProjectName))''')

print " "

#========= INVOICES TABLE ================

print " "
file = 'EngProjInvoices_info.csv'
print "Retrieving data from a csv data file: ", file
connection = open(file)
data = connection.read()
with open('EngProjInvoices_info.csv') as csvfile:
    invoices = list(csv.DictReader(csvfile))

print " "
print 'Retrieved', len(invoices),'invoices in list'

print "Invoices listed:"
print "Account_no  Inv_No	ProjNo	Project_Name	Client	Client_Id	Date_sent  Amount"
for i in range(0, len(invoices)):
    Account_no = int(invoices[i]["Account_no"])
    Inv_No = invoices[i]["Inv_No"]
    ProjNo = invoices[i]["ProjNo"]
    Project_Name = invoices[i]["Project_Name"]
    Client = invoices[i]["Client"]
    Client_Id = int(invoices[i]["Client_Id"])
    Date_sent = invoices[i]["Date_sent"]
    Amount = float(invoices[i]["Amount"])

    print Account_no,  Inv_No,	ProjNo,	Project_Name,	Client,	Client_Id,	Date_sent,  Amount

    cur.execute('''INSERT INTO BInvoices (Acc_no, Invoice_no, Proj_no, Proj_name, Client, Client_Id, Date_Inv, Amount) VALUES (?,?,?,?,?,?,?,?)''', (Account_no,Inv_No, ProjNo, Project_Name, Client, Client_Id, Date_sent, Amount))
conn.commit()


#========= CLIENTS TABLE ================

print " "
file = 'EngProjClients_info.csv'
print "Retrieving data from a csv data file: ", file
connection = open(file)
data = connection.read()
with open('EngProjClients_info.csv') as csvfile:
    clients = list(csv.DictReader(csvfile))

print " "
print 'Retrieved', len(clients),'clients in list'

print "Clients listed:"
print "Client_Id	Name	Address	VAT_no	Contact_person	Email_address"
for i in range(0, len(clients)):
    Client_Id = int(clients[i]["Client_Id"])
    Name = clients[i]["Name"]
    Address = clients[i]["Address"]
    VAT_no = clients[i]["VAT_no"]
    Contact_person = clients[i]["Contact_person"]
    Email_address = clients[i]["Email_address"]

    print Client_Id, Name, Address, VAT_no, Contact_person,Email_address
    cur.execute('''INSERT INTO BClients (Client_Id, name, address, VAT_no, Contact_person, Email_address) VALUES (?,?,?,?,?,?)''', (Client_Id, Name, Address, VAT_no, Contact_person, Email_address))
conn.commit()
    

# ================ PROJECTS TABLE =======================
file = 'EngProj_info.csv'
print "Retrieving data from a csv data file: ", file
connection = open(file)
data = connection.read()

with open('EngProj_info.csv') as csvfile:
    rec = list(csv.DictReader(csvfile))

print 'Retrieved', len(rec),'projects in list'

print " "

print "Projects listed:"
print "ProjNo,  Project_Name,  Client_Id,  Contract_Amount, ProfFee"
for i in range(0, len(rec)):
    ProjNo = str(rec[i]["ProjNo"])
    Project_Name = rec[i]["Project_Name"]
    Client_Id = rec[i]["Client_Id"]
    Contract_Amount = rec[i]["Contract_Amount"]
    ProfFee = rec[i]["ProfFee"]
    print ProjNo,Project_Name,Client_Id,Contract_Amount,ProfFee

    cur.execute('''INSERT INTO BProjInfo (ProjNo, ProjectName, Client_Id, Contract_Amount, ProfFee) VALUES (?,?,?,?,?)''', (ProjNo, Project_Name, Client_Id, Contract_Amount, ProfFee))
conn.commit()

#========================== SQL queries =======================

print " "
print "OUTPUT 1: PRINT rows in Invoices table , amounts decimal (real/float))(first 6)."
print "Acc no Invoice no   Project No.   Project Name   Client  Date Invoice    Amount"       #Client_Id not shown
sqlstr = 'SELECT Acc_no, Invoice_no, Proj_no, Proj_name, Client, Date_Inv, Amount FROM BInvoices LIMIT 6' 
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4], "  ", row[5], "  ", "R", row[6]

print " "
print "OUTPUT 2: PRINT rows in Clients table (first 6)."
print "Client Name   Address                       VAT_No    Contact person    Email address" 
sqlstr = 'SELECT name, address, VAT_No, Contact_person, Email_address FROM BClients order by Client_Id LIMIT 6'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4]

print " "
print "OUTPUT 3: PRINT rows in Projects info table."
print "Proj.No ProjectName  Contract_Amount  Prof.Fee"
sqlstr = 'SELECT * FROM BProjInfo'  
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", "R",row[3], "  ", "R",row[4]

print " "
#===============COMBINED SQL STATEMENTS================
print "OUTPUT 4: Print all projects associated with a certain client."
client_input = raw_input("Please enter the client you wish to see the projects from: ")
sqlstr = "SELECT BClients.Name, BProjInfo.ProjNo, BProjInfo.ProjectName FROM BClients, BProjInfo WHERE  BClients.Client_Id = BProjInfo.Client_Id AND BClients.Name like " + "'" + client_input + "%'"
for row in cur.execute(sqlstr):
    print row[0], " ", row[1], " ", row[2] 

#Choose all projects where Prof Fee > R50 000.
print " "
print "OUTPUT 5: Print some information from Invoice table, add Client VAT no. extracted from Clients table, and Project's Contract, Prof. Fee amount from ProjInfo table where Prof Fee > R50 000, using COMBINED SQL STATEMENTS. "
print "Invoice no.  Amount  ProjNo. Client  VAT no. ContractAmount  Prof.Fee"
sqlstr = "SELECT BInvoices.Invoice_no, BInvoices.Amount,  BInvoices.Proj_no, BClients.name, BClients.VAT_no,  BProjInfo.Contract_Amount, BProjInfo.ProfFee FROM BInvoices JOIN BClients JOIN BProjInfo ON BInvoices.Client_Id = BClients.Client_Id AND BInvoices.Proj_no = BProjInfo.ProjNo AND  BProjInfo.ProfFee > 50000"
for row in cur.execute(sqlstr):
    amount = "R" + str(row[1])
    print row[0], " ", amount, "", row[2], " ",  row[3], " ", row[4]," ", "R",  row[5], " ", "R", row[6]

print " "
# User chooses Client, it shows info of it, and associated Invoices
print "OUTPUT 6: Print rows showing the Client, its address, its projects and the associated Invoices. "
client_in = raw_input("Please enter the client you wish to see the invoices of: ")
print "Client  Address  ProjNo.  Project  Invoice no.  Amount"     #line 280
client_str = "'" + client_in + '%' + "'"
sqlstr = "SELECT BClients.name, BInvoices.Proj_no, BInvoices.Invoice_no, BInvoices.Amount FROM BInvoices JOIN BClients JOIN BProjInfo ON BClients.Client_Id  = BInvoices.Client_Id AND BInvoices.Proj_no = BProjInfo.ProjNo  WHERE BInvoices.Client like " + client_str
for row in cur.execute(sqlstr):
    print row[0], " ", row[1], "", row[2], " ",  "R", row[3]

print " "
# User chooses a project number, it shows its associated Invoices
print "OUTPUT 7: Print rows project and its associated Invoices. "
projno_in = raw_input("Please enter the project number you wish to see the invoices of: ")
print "ProjNo.  Project  Invoice no.  Amount"     #line 280
projno_str = "'" + projno_in + '%' + "'"
sqlstr = "SELECT BInvoices.Proj_no, BInvoices.Proj_name, BInvoices.Invoice_no, BInvoices.Amount FROM BInvoices WHERE BInvoices.Proj_no like " + projno_str
for row in cur.execute(sqlstr):
    print row[0], " ", row[1], " ", row[2], " ", "R", row[3]


cur.close()