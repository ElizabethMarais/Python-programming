##www.coursera.org: Python Data stuctures, course 2
#string functions

print " "  #print open line

inp_str = raw_input("Type word to count specific letter in: ")
inp_l = raw_input("Type letter to count in the word entered: ")
#slice = int(raw_input("Type number from where to start search from: "))

def test_int():
    slice = raw_input("Type number from where to start search from: ")
    try:
        sli_int = int(slice)
#if int(sli_int) >= 0:
#does not test yet for only digit input
        cnt = inp_str.count(inp_l,sli_int-1)
        print "there is/are", cnt, "appearance(s) of",inp_l,"in", inp_str, "starting from the position", sli_int 
    except:
        print "Please enter a integer number: "
        test_int()

test_int()

print " "  #print open line


#isalnum()   # test if all char in string is alphanumeric  -letters and digits
#isdigit()  # test if all char in string is digits
def test_int():
    text = raw_input("Type in a number, containing only digits: ")
#print text ,"is", type(text)
    if text.isdigit(): 
       print "Yes, they are all numbers."
    else:
        print "Wrong input."
#        text = raw_input("Type in a number, containing only digits: ")
        test_int()

test_int()
print " "  #print open line

#test string starts with - NB case is important
print "The line to check if starts with 'I' is: Ich liebe dich, Adriaan."
line = "Ich liebe dich, Adriaan."
if line.startswith("I"): #answer is true, then execute next line
    print "Yes, the line starts with 'I'."
if line.startswith("i"): #answer is false, then DO NOT execute next line
    print "Yes, the line starts with 'i'."


print " "  #print open line
print "THE END"