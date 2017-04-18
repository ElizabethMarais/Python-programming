#www.coursera.org: Python Data structures, course 2 
print "FUNCTION: Reading a data file, build lists, different ways of displaying data."

print "When prompted, please enter 'tennis data.txt' as data file."

name_file = raw_input("Enter the file name with the tennis tournaments information: ")
if len(name_file) < 1: name_file = "tennis data.txt"
name_file = 'tennis data.txt'

print " "
tennis_list = list()
tennis_dict = {}
name_dict = {}
most_tourn = {}
fh = open(name_file)
# Name	                 Year	grass	clay	hard	else
# Andre Agassi ,   1999,	   1,	 1,	 1,          0
for line in fh:
        if line.find(',') > 0:
            pos_name = line.find(',')
            name = line[0:pos_name]    #find the tennis star name, read from begin of line till comma 
            name = name.strip()

                #find the year in rest of line:
            pos_year = line.find(',', pos_name+1)
            year = line[pos_name+1:pos_year]
            yearN = year.strip()    #strip all blank spaces before it

                #find if player won grass tournament in rest of line:
            pos_grass = line.find(',', pos_year+1)
            grass = line[pos_year+1:pos_grass]
            grassN = grass.strip()     #strip all blank spaces before it

              #find if player won clay tournament in rest of line:
            pos_clay = line.find(',', pos_grass+1)
            clay = line[pos_grass+1:pos_clay]
            clayN = clay.strip()     #strip all blank spaces before it

              #find if player won hard tournament in rest of line:
            pos_hard = line.find(',', pos_clay+1)
            hard = line[pos_clay+1:pos_hard]
            hardN = hard.strip()     #strip all blank spaces before it


             #find if player won else tournament in rest of line till end of line:
            elseT = line[pos_hard+1:]
            elseN = elseT.strip()     #strip all blank spaces before it


            #compile the individual items to build a nested list
            item = name, yearN, grassN, clayN, hardN, elseN
            tennis_list.append(item)

print " "
print "LIST:"
print tennis_list

print " "
print "Print data in complete sentences testing which values of tournaments played: "
strT = "" 
for i in range(len(tennis_list)):
  #determine each tennis player list of things won
  if tennis_list[i][2] == "1":
     strT = "grass,"
  if tennis_list[i][3] == "1":
     strT = strT + " " +  "clay,"
  if tennis_list[i][4] =="1":
     strT = strT + " " + "hard,"
  if tennis_list[i][5] == "1":
     strT = strT  + " " + "else,"
  print tennis_list[i][0], "has won in the year", tennis_list[i][1], "the tournaments of", strT, "."
