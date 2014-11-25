"""Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).

The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:

Consider use range(#begin, #end) method"""
# Ex 1 PLP
li = []
for i in range(2000, 3201):
	if i % 7 == 0 and i % 5 != 0:
		li.append(str(i))
print ','.join(li)

li = ','.join([str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0])

# asta e vreo diferenta semnificativa?

numbers_in_range = []
for i in range(2000, 3201):
	if i % 7 == 0 and i % 5 != 0:
		numbers_in_range.append(i)
print numbers_in_range

# Ex 2 PLP
class MyClass:
	def _init_(self):
		self.answer = ''
	def getString(self):
		self.answer = raw_input('Say something: ')
	def printString(self):
		print self.answer.upper()

x = MyClass()
x.getString()
x.printString()

# Ex. 3
a = raw_input("Give me a list of words: ")
b = a.split(',')
b.sort()
print ','.join(b)

# Ex. 4
def return_count(s):
    digits = 0
    letters = 0
    for char in s:
        if char.isdigit() == True:
            digits = digits + 1
        elif char.isalpha() == True:
            letters = letters + 1
    print "DIGITS: ", digits
    print "LETTERS: ", letters
return_count('hello world! 123')

# or

import string
alphabet = string.ascii_lowercase

# use dictionary
def smth(s):
    nlr = 0
    for i in alphabet:
        if s.count(i, 0, len(s)) > 0:
            nlr = nlr + 1
        print "%s appears %i" % (i,s.count(i, 0, len(s)))
    print "distinct letters ", nlr

smth('this is me 234')

# Ex. 5
subject = ["I", "You"]
verb = ["play", "love"]
sent_obj = ['hockey', 'football']

for subj in subject:
    print "Subj ", subj
    for vb in verb:
        print "Verb ", vb
        for obj in sent_obj:
            print "Obj ", obj
            print "------------------"
            print subj + " " + vb + " " +  obj
            print "------------------"
# Ex. 6
textfile = open("my_text.txt", 'r')
my_smth =[]
for line in textfile:
    words = line.split()
    for word in words:
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        digits = "0123456789"
        word = word.lower()
        #if word.isdigit() == True or word.punctuation == True:
        #if word.isdigit() == True or word in punctuation:
        if word in punctuation or word in digits:
            #del word
            str(my_smth).strip(punctuation)
        #else:
            #my_smth.append(word)
textfile.close()
print my_smth

def my_funct(my_smth):
    my_dict = {}
    #count_word = 0
    for word in my_smth:
        my_dict[word] = my_smth.count(word)

    max_value = max(my_dict.values())
    li = [k for k, v in my_dict.items() if v == max_value]
    return li

    #print my_dict
print my_funct(my_smth)


#def most_occurences(my_dict):
#Read: seturi, tuple

