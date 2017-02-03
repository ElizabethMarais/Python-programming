#www.coursera.org: Python Data stuctures, course 2
#Exercise on video on range, lists, Chapter 8
#Practice list functions 

friends = ['Joshua','Erich','Adriaan', 'Ettienne','Stephen','Kgomotso']
friends.sort()   
print range(len(friends))  #gives output:['Adriaan','Erich','Ettienne','Joshua','Kgomotso','Stephen']

for friend in friends:
    print 'Happy new year,',friend

print " "

#similar output, use IF want to change an item, e.g.  change Joshua to "Joshua Yes"
print "FUNCTION: Joshua's name changed:"
for i in range(len(friends)):
    friend = friends[i]
    if friend == "Joshua":
        friends[i] = "Joshua Yes"
        friend = friends[i]
        print 'Happy new year,',friend

print " "

print "FUNCTION: The user reads in a list of numbers and the average is calculated and printed."  
print "Please enter a series of numbers, enter 'done' when finished."
numlist = list()
while True:
    inp = raw_input("Enter a number for the list: ")
    if inp == 'done': break
    try:
        value = float(inp)
        numlist.append(value)
    except:
        print "Wrong input."
average = sum(numlist)/len(numlist)
print "The Average of the list is", average

print " "

print "FUNCTION: Split parts of the string, '2017 is going to be a good year' and print length of list."
stringA = "2017 is going to be a good year"
parts = stringA.split()
print "The parts of the string is: ", parts
print "There are", len(parts), "parts in the string."

print " "

print "FUNCTION: Split string, 'The birds are chirping     beaufitul in the morning.'; multiple spaces are treated as one delimiter."
stringB = 'The birds are chirping     beaufitul.'
partB = stringB.split()
print partB

print " "

print "FUNCTION: Split string, '2016;2017;2018', using a specific delimeter, ';' ."
listA = '2016;2017;2018'
partA = listA.split(';')
print partA

print "THE END."
