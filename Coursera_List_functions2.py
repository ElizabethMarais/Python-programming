##www.coursera.org: Python Data stuctures, course 2
#list operations

print "FUNCTION: User enter a name, and each index and the letter is displayed."
def veg_parse():
    vegetable = raw_input("Enter a vegetable of which the letters must be displayed: ")
    try:
        inp_int = float(vegetable)
        if inp_int >= 0:
            print "Wrong input, please enter a vegetable name of letters to be displayed."
            veg_parse()
    except:
        index = 0
        while index<len(vegetable):
            letter = vegetable[index]
            print index, letter
            index = index + 1

veg_parse()

print " "  #print open line

def veg_parse_1():
    vegetable = raw_input("Enter a fruit of which the letters must be displayed: ")
    try:
        inp_int = float(vegetable)
        if inp_int >= 0:
            print "Wrong input, please enter a fruit name."
            veg_parse_1()
    except:
        index = 0
        for letter in vegetable:
            print index, letter
            index = index + 1

veg_parse_1()
print " "  #print open line
print "END"

