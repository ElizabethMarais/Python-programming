print "FUNCTION: Dictionaries: South Africa's provinces and their population, stored in a dictionary; print provinces with the largest and smallest populations."

pop_dict = {'North West':3707100, 'KwaZulu-Natal':10919100, 'Gauteng':13200300, 'Northern Cape':1185600, 'Western Cape':6200100, 'Limpopo':5726800,'Eastern Cape':6916200,'Mpumalanga':4283900,'Free State':2817900}

#determine biggest, smallest population in dictionary
bigname = None
bigpop = 0
smallname = None
smallpop = 0

for key, value in pop_dict.iteritems():
     name = key
     pop = value 

     if bigpop == 0 or pop > bigpop:
        bigname = name
        bigpop = pop
     if smallpop == 0 or pop < smallpop:
        smallname = name
        smallpop = pop

print " "

print "The SA province with the largest population is", bigname, "with", bigpop, "people."
print "The SA province with the smallest population is", smallname, "with", smallpop, "people."


for key, value in pop_dict.iteritems():
    print key,":",value

#LISTS
print " "

print "Printing information from a list in sentences, sorted ascending according to provinces: "
pop_list = [['North West',3707100,6.7], ['KwaZulu-Natal',10919100,19.9], ['Gauteng',13200300,24], ['Northern Cape',1185600,2.2], ['Western Cape',6200100,11.3], 
['Limpopo', 5726800,10.4], ['Eastern Cape',6916200,12.6], ['Mpumalanga',4283900,7.8], ['Free State',2817900,5.1]]
pop_list.sort()
for i in range(len(pop_list)):
    print pop_list[i][0],"has",pop_list[i][1],"people with a percentage of the total population of", pop_list[i][2]



#build a list from the dictionary
popu_list = list()

def pop_lf(pop_dict):
    for key, value in pop_dict.iteritems():
        popu_list.append([value,key])
    return popu_list

print " "
popu_list = pop_lf(pop_dict)
popu_list.sort(reverse=True)

print "LIST: Print elements in list with largest to smallest population:"
print "Population : Province"
i = 0
for i in range(len(popu_list)):
    print popu_list[i]
    i += 1

print " "
print "LISTS: Build two new lists, showing provinces with percentages 10% and higher, and percentages lower than 10%:"

popu_lsmall = list()
popu_lbig = list()
for i in range(len(pop_list)):
    if pop_list[i][2] < 10:
         item = pop_list[i][2],pop_list[i][0],pop_list[i][1]
         popu_lsmall.append(item)
    else:
         item = pop_list[i][2],pop_list[i][0],pop_list[i][1]
         popu_lbig.append(item)

print "Provinces with percentages lower than 10%:" 
for i in range(len(popu_lsmall)):
    print popu_lsmall[i][0], "%, province is", popu_lsmall[i][1], "with a population of", popu_lsmall[i][2]

print " "
print "Provinces with percentages 10% and higher:"
for i in range(len(popu_lbig)):
    print popu_lbig[i][0], "%, province is", popu_lbig[i][1], "with a population of", popu_lbig[i][2]


