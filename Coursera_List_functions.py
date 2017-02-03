##www.coursera.org: Python Data stuctures, course 2.
#List operations

#user enters any word, and a letter to check how many time(s) the letter appear(s) in the word
def word_check():
    inpstr = raw_input("Enter a word to examine: ")
    try:
        inp_int = float(inpstr)
        print inp_int
        if inp_int >= 0:
            print "Wrong input, please enter a word only, no digits."
            word_check()
    except:
        inputlet = raw_input("Enter a letter to check for in above word: ") 
        count = 0
        for letter in inpstr:
            if letter == inputlet:
                count = count + 1
        print "The letter", inputlet, "appear(s)", count, "time(s) in the word",inpstr

word_check()

inpstr1 = raw_input("Enter a word: ")
inputlet_1 = raw_input("Enter a letter: ")
if inputlet_1 in inpstr1:
    print "Yes, the letter", inputlet_1, "is in", inpstr1
else: 
     print "No, the letter", inputlet_1, "is in not in the word", inpstr1

word = "ccc"
if word == "babana":
   print 'the word', word, 'is same as banana.'
elif word < "babana":
    print 'the word', word, 'is before banana.'
elif word > "babana":
    print 'the word', word, 'is after banana.'
print " "  #print open line
print "THE END"