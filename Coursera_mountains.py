#www.coursera.org: Python Data stuctures, dictionaries exercise

print "File entered with sentences about mountains and their heights, printing each sentence. "
print "If a name of a mountain is found, program prints the name and height."
print "Program determines the lowest mountain, it prints its name and height."
print "Program prints the DICTIONARY formed. Program prints the LIST built up, printing the height first."

print " "
counts = dict()	
name = raw_input("Enter file to find the mountains and their heights: ")
if len(name) < 1: name = "mountains.txt"
name = "mountains.txt"
fh = open(name)

print " "
mountains = {}

for line in fh:
        line = line.rstrip()
        print line
        if line.find('mountain ') > 0:
            pos_mount = line.find('mountain ')
            pos_space = line.find(' ',pos_mount+9)
            mount = line[pos_mount+9:pos_space]  #choose next word, the mountain name
  	    print mount 

            pos_height = line.find('height ')
            pos_spaceh = line.find(' ',pos_height+7)
            height = line[pos_height+7:pos_spaceh]  #choose next word thus the height
  	    print height
            mountains[mount] = height

print " "
print "DICTIONARY: ",mountains

print " "
#Find the lowest mountain, print its name and height
smallmount = None
smallheight = None
for mount,height in mountains.items():
    if smallheight == None or height < smallheight:
        smallmount = mount
        smallheight = height
print "The lowest mountain is", smallmount, "with height", smallheight, "m."

print " "
#Build a List
mount_list = list()
for key, value in mountains.iteritems():
    mount_list.append([int(value),key])  #build list,  first height, then mountain

print "LIST: Height first listed: ", mount_list
print " "

mount_list.sort(reverse=True)     #sort from big to small in height
print "LIST: Height first listed, descending order: ", mount_list

