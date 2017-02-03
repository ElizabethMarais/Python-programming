##www.coursera.org: Python Data stuctures, course 2, week 5, chapter 9

print "FUNCTION: Dictionaries: get() method - check which word occurs the most in the sentence entered."
#sentence = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"

print " "

counts = dict()	
name = raw_input('Enter the sentence to check which word occurs the most:')
words = name.split()

for word in words:
    counts[word] = counts.get(word,0) + 1
    bigcount = None
    bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print " "
print "The dictionary: ",(counts)
 
print " "
print "The word that occurs the most in the sentence is '", bigword, "' and it occurs", bigcount, "times."


#characters = {}  #create an empty dict
#for character in sentence:
#    characters[character] = characters.get(character, 0) + 1 

#print(characters)