##www.coursera.org: Python Data stuctures, course 2 
print "FUNCTION: Reading a data file, processing of data; user enter area; or user enter key word in project names."
print "When prompted, please enter 'projects.txt' as data file."

name_file = raw_input("Enter the file name with the projects information: ")
if len(name_file) < 1: name_file = "projects.txt"
name_file = "projects.txt"

print " "
project_list = list()
city_dict = {}
name_dict = {}
most_city = {}
fh = open(name_file)
for line in fh:
        if line.find(',') > 0:
            pos_num = line.find(',')
            num = line[0:pos_num]  #find the project number, read from begin of line till comma 
            num = num.strip()
                #find the city in rest of line:
            pos_city = line.find(',', pos_num+1)
            city = line[pos_num+1:pos_city]
            cityN = city.strip()    #strip all blank spaces before it
                #find the project name in rest of line:
            pos_name = line.find(',', pos_city+1)
            name = line[pos_city+1:pos_name]
            nameN = name.strip()    #strip all blank spaces before it

            #build a dictionary of project name and country:
            name_dict[nameN] = cityN   

            #compile the individual items to build a nested list
            item = num, cityN, nameN
            project_list.append(item)

print "LIST: Print Projects names information extracted from the file in list form (first 20): "
print project_list [0:20]     #e.g. [Proj num, city, project name]


print " "
print "Print data in complete sentences (first 10): "
for i in range(len(project_list)):
      if i < 10:       
          print project_list[i][0], "is the project", project_list[i][2], "in the city or area", project_list[i][1]
      else:
         break   

#determine which city of area most projects in
print " "
for name, city in name_dict.items():
    most_city[city] = most_city.get(city,0) + 1   #determine how many times a city appear in the dictionary

bigcity = None
bigcount = 0
for city, count in most_city.items():
       if bigcount is None or count > bigcount:
          bigcity = city
          bigcount = count
print "COUNTING: The city in which the most project in this list area, is", bigcity, "and it is", bigcount, "times."

print " "
print "WORD SEARCH: Suggestion of project names containing words: Annlin, Boardwalk, Die Hoewes, Chamberlain, Equestria."
word_dict = {}
while True:

  checkword = raw_input("Please enter word to display projects names containing: ('done' to break): ")
  if checkword == "done" : break
  for i in range(len(project_list)):
    if checkword in project_list[i][2]:
        print project_list[i][0], project_list[i][2]
    i = i + 1
  print " "

print " "
print "AREA SEARCH: Project areas may include Akasia, Pretoria, Johannesburg."
wordarea_dict = {}
while True:
  checkarea = raw_input("Please enter the area to which you want to find projects for: ('done' to break): ")
  if checkarea == "done" : break
  for i in range(len(project_list)):
    if checkarea in project_list[i][1]:
        print project_list[i][1], project_list[i][0], project_list[i][2]
    i = i + 1
  print " "


print " "
print "SORTING: According to project numbers, ascending (first 30)."
	#sort to project numbers
projnew_list = list()
for i in range(len(project_list)):  #remove 'N' to sort
    proj_num_str = project_list[i][0]
    proj_num = proj_num_str[1:]
    proj_num_int = int(proj_num)
    new_item = proj_num_int , project_list[i][1], project_list[i][2]
    projnew_list.append(new_item)
projnew_list.sort()

projP_list = list()
for i in range(len(projnew_list)):   #put back the 'N' at project numbers
    projP = 'P' + str(projnew_list[i][0])
    item_P = projP, projnew_list[i][1], projnew_list[i][2]
    projP_list.append(item_P) 

for i in range(0,30):   #print first 30 projects
    print projP_list[i][0], " ", projP_list[i][1], " ", projP_list[i][2]
