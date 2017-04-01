print "FUNCTION: Dictionaries: South Africa's provinces and their population, stored in a dictionary; print provinces with the largest and smallest populations."

pop_dict = {'North West':3707100, 'KwaZulu-Natal':10919100, 'Gauteng':13200300, 'Northern Cape':1185600, 'Western Cape':6200100, 'Limpopo':5726800,'Eastern Cape':6916200,'Mpumalanga':4283900,'Free State':2817900}

print " "

print "Province : Population"
for key, value in pop_dict.iteritems():
    print key,":",value

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

#build a list from the dictionary
pop_list = list()

def pop_lf(pop_dict):
    for key, value in pop_dict.iteritems():
        pop_list.append([value,key])
    return pop_list

print " "
pop_list = pop_lf(pop_dict)
pop_list.sort(reverse=True)

print "LIST: Print elements in list with largest to smallest population:"
print "Population : Province"
i = 0
for i in range(len(pop_list)):
    print pop_list[i]
    i += 1