#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.1 Basic Structures, introduction

THEORY
-A string is a data type in Python that's used to represent a piece of text.

-It's written between quotes

-A string can be as short as zero characters e.g.str="", usually called an empty string or really long. 

-We can concatenate strings with + to create longer strings
        ALSO
        Concatenation can happen 
            -with + between strings
            - with the JOIN METHOD, string.join([here we provide the strings to be joined])
            the join method uses parentheses and square brackets
            the join method concatenates the elements of a LIST!
            -with the FORMAT METHOD

-We can multiply a string by a number, “hello”*3 results in 'hellohellohello'

-We can find out how long a string is with the len() function
        len('string') or 
        len(variable) when the Variable has a string as its value
        
- Contents of a text file (.txt) are strings

- Strings are sequences, like lists, tuples and dictionaries
        strings are sequences, so they have elements.
        the element of a string sequence can be string, integer, float etc. (and space too!)

- How to access a specific element in a string(specific element)
        with indexing
        e.g. string[0], this will give us the character at index position 0
        
- How to access the last element of a string
        with negative indexing
        e.g. string[-1], gives us the last element
        also string[-2], gives us the 2nd element starting from the end
        
- How to access a slice of a string
        with range of indexes
        e.g. color = 'Orange'
        color[1:4]= 'ra'        1 to 3,last index never included
        color[:4] = 'Oran'      0 to 3, blank is by default 0,
        color[4:] = 'ge'        4 until the end, blank is by defalut last element

        color = 'Orange'
        color[::-1]             REVERSES the order, 'egnarO'      


- Strings are immutable (we cannot change them)

- How can we correct a wrong string since it is immutable?
        we can create a new string by using a new name for the Variable, and the value is the corrected string
        
 - ATTENTION
         Python takes into account the LAST value we assigned to a variable.

- How can we find out if an element exists in a string sequence?
        1)with the IN keyword
        e.g. pets = 'cats and dogs'
        'x' in pets
        False
        2)with IF and IN keyword
        e.g. pets = 'cats and dogs'
        if 'at' in pets
        True

 - String Methods
 
         INDEX METHOD
         e.g. pets = 'cats and dogs'
         pets.index('c') = 1
         string.index(element)
                               
         string.lower()     converts all characters into lower case
         string.upper()     converts all letters of the variable into uppercase
         string.strip()     removes spaces from left and right 
         string.lstrip()    removes spaces only from the left
         string.rstrip()    removes spaces only from the right
         
         'The number of times'.count('e')  counts the occurences of the element 
         'forest'.endswith('rest')   examines if the string ends with a certain part, here this is True
         'forest'.isnumeric()       examines if our string is composed only of numbers
         
         JOIN method
         The JOIN METHOD, "delimiter".join(list), takes 1 argument, the list
         the join method, joins the elements of a list together, and produces a string
         Returns a new string with all the strings joined by the delimiter
         
         SPLIT METHOD
         string.split()
         the split method, splits a string into substrings and finally produces a list with the substrings
         the delimiter is the space
         each element of the list is a string
         ATTENTION if argument of split function is left blank, by default splitting happens at white spaces
         we can provide the delimiter we want as an argument 
         so, string.split(delimiter)
         
         FORMAT METHOD
         with the format method we can CONCATENATE strings together
         so, it is like an alternative to concatenating with +
         
         "{} {}".format(Variable1, Variable2)
         
         The format method returns a copy of the string where the {} placeholders 
         have been replaced with the values of the variables. 
         These variables are converted to strings if they weren't strings already. 
         Empty placeholders are replaced by the variables passed to format in the same order.
         
         "{:exp1} {:exp2}".format(value1, value2)
         If the placeholders include a colon, what comes after the colon is a formatting expression. 
        
        FORMATING EXPRESSIONS
        '{:.0f}'.format(10.5)       # formats the float to an integer. Output is 10
        '{:.2f}'.format(0.5)        # formats the float of 1 decimal to a float with 2 decimal places. Output is 0.50
        '{:.2s}'.format('Python')   # formats the string length to 2 characters. Output is 'Py'
        '{:<6s}'.format('Py')       # formats the string length to 6 characters. Output is 'Py    '
                                    # symbol < aligns the string to the left
        '{:>6s}'.format('Py')       # formats the string length to 6 characters. Output is '    Py'
                                    # symbol > aligns the string to the right
        '{:^6s}'.format('Py')       # formats the string length to 6 characters. Output is '  Py  '
                                    # symbol ^ aligns the string to the center

         
         
         FOR LOOP
         we can iterate over the elements of a string
         
         ISALPHA METHOD
         string.isalpha() 
         examines if all characters of the string are alphabetic
         if all aplhabetic, True
         if not all alphabetic, False
         
         REPLACE METHOD
         replaces a string with a new one
         x = "Cat"
         x.replace("Cat", "Dog")
         now x = "Dog"
         so
         string.replace(old,new)
              
- ATTENTION
        when adding '12345' + '54321' the result is '1234554321', so two strings concatenated by +
        if we want the mathematical operation
        int('12345') + int('54321') = 12345+54321 = 66666
        
- function
        The point of functions in general is to take in inputs and return something. 
- print() function
        it displays results on the console
- return statement (return)
        The return statement causes your function to exit and hand back a value to its caller
        The return statement is used when a function is ready to return a value to its caller.
        the return statement provides the argument with which we will call the function)
"""      
"""
EXAMPLE 1

Concatenate strings with +
"""
def greeting(name):             #create a function.HEADER
    print("Welcome, "+ name)    # BODY of the function. It prints a greeting

greeting("Kay")                 #call the function by providing an argument

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.1 Basic Structures, introduction

EXAMPLE 2

Find out if a number is even or odd
"""

def is_even(number): #create a function. HEADER
    if number % 2 == 0: 
        return True # when the if condition is met, display True
    return False # when the if condition is not met, number is odd, return False

is_even(3) # call the function by providing an argument

# if (number/2) is integer, then it is an even number.
# Modulo % returns the remainder of the division
# when there is no remainder, then the dividend is even, then product of number%2 is 0
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.1 Basic Structures, introduction

EXAMPLE 3
loop inside a loop
"""
for left in range(7):
    for right in range (left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

#end=" ", displays vertically
    
# RANGE (START, STOP, STEP). 
#BY DEFAULT START IS 0, STEP IS 1
#BY DEFAULT WE STOP AT 6, for both loops


#%%
"""
EXAMPLE 3 repeated
loop inside a loop
"""

for x in range(7): #Variable is x, the for loop will examine every x from 0 to 6
    for y in range (x,7):# for each x, another for loop will examine every y from x to 6
        print(str(x) + "|" + str(y)) #display x and y for every iteration of the 1st for loop
    print() # this is outside the 2nd for loop. It creates a space when the iteration of the 2nd loop is done for each y.
    # the print() belongs to the 1st for loop. For each x, a space is displayed?

# we do 7 iterations according to the 1st for loop, from 0 to 6
# 1st iteration, x=0 then we do iterations with y for the range(0,7). 1) x=0, y=0 2) x=0, y=1 3) x=0, y=2 4)x=0, y=3 ...
# 2nd iteration, x=1 then we do iterations with y for the range(1,7). 1) x=1, y=1 2) x=1, y=2 3) x=1, y=3 ....
    
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.2 What is a string?

EXAMPLE 4
Modify the double_word function so that it returns the same word repeated twice, 
followed by the length of the new doubled word. 
For example, double_word("hello") should return hellohello10.
"""
#QUESTION
def double_word(word):
    return

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
#%%
#SOLUTION
def double_word(word):
    return (word*2 + str(len(word*2)))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.3 The parts of a string

EXAMPLE 5
how to access a character of a string at a precise position 
type the variable, square brackets and the index number
indexing starts at 0
"""
name = "Jaylen"
print(name[1])

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.3 The parts of a string

EXAMPLE 6
how to access  the last character of a string but you don't know how long it is
with negative indexing
Using negative indexes lets us access the positions in the string starting from the last
"""
text = "Random string with a lot of characters"
print(text[-1]) #display last character
print(text[-2]) #display character previous to last

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.3 The parts of a string

EXAMPLE 7
Modify the first_and_last function so that
it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. 
Remember that you can access characters using message[0] or message[-1]. 
Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
"""
#QUESTION
def first_and_last(message):
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#%%
#SOLUTION
def first_and_last(message):
    if message == "":
        return True
    if message[0] == message[-1]:
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.3 The parts of a string

EXAMPLE 8
slice or substring = portion of a string

we access a slice of a string with 2 index numbers.
type the variable, square brackets and 2 numbers with a colon
"""

color = "Orange"
color[1:4] # from 1 to 3

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.3 The parts of a string

EXAMPLE 9
access a slice of a string with only 1 index
when omitting 1st index, by default it is 0
when omitting last index, by default is is the last character
"""
fruit = "Pineapple"

print(fruit[:4]) # from 0 to 3

print(fruit[4:]) # from 4 to the end

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.4 Creating New Strings

EXAMPLE 10
Strings are immutable
How can we correct a wrong character within a string?
"""
# FIRST ATTEMPT
message = "A kong string with a silly typo"

message[2] = "l"

# IF WE TRY TO CORRECT THE ABOVE STRING, WE GET AN ERROR MESSAGE
#TypeError: 'str' object does not support item assignment
# THAT HAPPENS BECAUSE STRINGS ARE IMMUTABLE AND WE CANNOT CHANGE THEM BY ASSIGNING A NEW CHARACTER USING =

#%%
"""
EXAMPLE 10 continued
we cannot correct a string, 
but we can create a new string that is correct
"""
# SECOND ATTEMPT

new_message = message[0:2] + "l" + message[3:]
print(new_message)

#we use slicing to choose the correct parts of the previous string

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.4 Creating New Strings

EXAMPLE 11
we can keep the same Variable, but change its value
Python recognizes the last assigned value as the value of the Variable, not the previous values we may have used

"""
message = "This is a new message" # 1st assignment

message = "And a new one" # 2nd assignment

print(message) # the print function will display the last value assigned to our Variable

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.4 Creating New Strings

EXAMPLE 12
How to find the index number of a certain character within a string
use the INDEX METHOD
syntax is: variable.index( and in our case string.index("character or substring")
the index method returns the index of the given substring within the given string
"""

pets = "Cats & Dogs"

pets.index("&") # we use the index method to find the index number of the substring & within the above string

# output is 5. So the character & is in the 5th index position of our string

#%%
pets = "Cats & Dogs"

pets.index("C")
#Output is 0. So, C is in index position 0

#%%
pets = "Cats & Dogs"

pets.index("Dogs")

#Output is 7. The Dogs substring starts at index position 7

#%%
pets = "Cats & Dogs"

pets.index("s")

#Output is 3. The index method recognizes the index position of the FIRST s

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.4 Creating New Strings

EXAMPLE 13
Using the index method, find out the position of "x" in
"supercalifragilisticexpialidocious".
"""
#QUESTION
word = "supercalifragilisticexpialidocious"

print()
#%%%
#SOLUTION
word = "supercalifragilisticexpialidocious"

print(word.index("x")) # we ask what is the index position of xand also display the result

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.4 Creating New Strings

EXAMPLE 14
-how to examine if a substring exists within a string
-use the IN keyword (results in True or False)
-the IN keyword is used : 1) in the FOR LOOP for iteration and 2) as a conditional
"""
pets = "Cats & Dogs"

"Dragons" in pets

#output is False since Dragons is not within the string

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.4 Creating New Strings

EXAMPLE 15
in a list of email addresses, replace the old domain with the new domain
"""
def replace_domain(email, old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@" +old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

# first we define the function which has 3 arguments
# 1st argument is the email to be examined
# 2nd argument is the old domain
# 3rd argument is the new domain   

# then we construct the IF block
# if after the @ there is the old domain then we execute the IF BLOCK
# if after the @ there is the new domain then we do not execute the IF BLOCK, we just display the email as it is

# if after the @ there is the old domain (if condition is True) we execute the IF BLOCK
# IF BLOCK execution: 
# find the index position where the old domain starts by using the index method:
# string.index("substring")
# then, define the new Variable of the new email:
# portion of the old email until the index position plus @ and the new domain name

#%%
"""
EXAMPLE 15 continued
we have email addresses with an old domain,
which we want to update and provide them a new domain.
we will write a function that
-examines the email address
-finds if the email address has an old domain or not
-changes the old domain into the new domain
"""

def replace_domain(email, old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@" +old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

replace_domain("foteinirodis@gmail.com", "gmail.com", "dhl.com")

#output is foteinirodis@dhl.com !!

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.5 More string Methods

EXAMPLE 16

string.upper(), this method transforms all characters into uppercase
string.lower(), this method transforms all characters into lowercase
"""
text = "Mountains"

text.upper()

# Output is MOUNTAINS

text.lower()

# Output is mountains

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.5 More string Methods

EXAMPLE 17
users can type in Yes, YES or yeS
we will convert all characters into lowercase and then examine if the user typed in yes or no
"""
answer = "YES"
if answer.lower() =="yes":
    print("User said yes")

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.5 More string Methods

EXAMPLE 18
string.strip(), this method removes spaces from both sides of a string
string.lstrip(), this method removes spaces from the left side of a string
string.rstrip(), this method removes spaces from the right side of a string
"""
text = " yes " # string has one space to its left and one space to its right

text.strip() # output is 'yes'
text.lstrip() # output is'yes '
text.rstrip() # output is ' yes'

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.5 More string Methods

EXAMPLE 19

string.count(), this method counts how many times a substring appears within a string
string.endswith(), this method examines whether a string ends with a specific substring, replies with True or False
string.isnumeric(), this method examines whether a string contains only numbers or not
"""
text = "More String Methods"
text.count("e") # output is 2

text1 = "Forest"
text1.endswith("rest") # output is True

text2 = "1978"
text2.isnumeric() # Output is True

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.5 More string Methods

EXAMPLE 20

the function int(), converts contents to an integer
the function str(), converts contents to a string
the function float(), converts contents to a float
"""
stringA = "12345"
stringB = "11111"

int(stringA) + int(stringB)

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.5 More string Methods

EXAMPLE 21

Concatenation can happen 
-with + between strings

- with the JOIN METHOD, string.join([here we provide the strings to be joined])
the join method uses parentheses and square brackets
the join method concatenates the elements of a LIST!

-with the FORMAT METHOD
"""
# JOIN WITH SPACES
" ".join(["join", "with", "spaces"])
# output is: 'join with spaces'

# JOIN WITH TRIPLE DOTS
"...".join(["join", "with", "triple", "dots"])
# 'join...with...triple...dots'

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.5 More string Methods

EXAMPLE 22

the SLPIT METHOD
splits a string into a LIST of smaller strings
splitting happens automatically at every space
but we can provide a parameter and split at a dot for example
"""
text = "My cat is very fat"

text.split()
#output is a LIST, ['My', 'cat', 'is', 'very', 'fat']

text = "My cat is fat. My dog is slim"
text.split(".")
# output is a LIST with 2 elements, ['My cat is fat', ' My dog is slim']

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.5 More string Methods

EXAMPLE 23

Fill in the gaps in the initials function so that it returns the initials of the words 
contained in the phrase received, in upper case. 
For example: 
"Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
"""
#QUESTION
def initials(phrase):
    words = phrase._____
    result = ""
    for word in words: 
        result += ___
    return ___

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
#%%
# SOLUTION
def initials(phrase):
    words = phrase.split() # HERE WE WILL CONVERT THE PHRASE INTO A LIST OF WORDS WITH THE SPLIT METHOD. In this list each element is a word
    result = "" # INITIALIZE.here we define the intial value, it is a string without any contents
    for x in words: # apply FOR LOOP.We will examine each element of the list. Element is a word
         result = result +x[0] # INCREMENTATION, we define how the value is changing. In each iteration we add the first letter of the iterated word
    return result.upper() # here we convert our final result into uppercase

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

# for the second phrase we have 3 elements, so 3 iterations
# 1st iteration, x="local", result=result+x[0], so result="" + "local"[0] = "l"
# 2nd iteration, x = "area", result=result+x[0], so result = "l" + "area"[0] = "l" + "a" = "la"
# 3rd iteration, x = "network", result=result+x[0],so result = "la" + "network"[0] = "la" + "n" = "lan"
# end of iteration
# then we convert the result into uppercase and that's it

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.6 Formatting strings

EXAMPLE 24

The FORMAT METHOD
use the format method to concatenate strings,
instead of concatenating them with +

"{} {}".method(variable1,variable2)
-curly brackets are empty
-the order of the variables inside the format function is significant
"""

name = "Manny"
number = len(name) * 3

print("Hello {}, your lucky number is {}".format(name, number))

# the {} curly brackets indicate where the value of the Variable should be
# first {} is the place to put the variable of name
# second {} is the place to put the variable of number

# the format method does not care if name is a string and number is an integer
# here the order of variables inside the format method MATTERS

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.6 Formatting strings

EXAMPLE 25

another way to use the format method

-curly brackets contain variables
-the order of the variables inside the format function is NOT significant
- we assign values to the Variable inside the format function
"""
name = "Foteini"
number = len(name) * 3

print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

# the {} contain variables
# the order of the variables in the {}, is different than their order inside the format function, BUT IT DOES NOT MATTER

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.6 Formatting strings

EXAMPLE 26

Modify the student_grade function using the format method, 
so that it returns the phrase "X received Y% on the exam". 
For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
"""
# QUESTION
def student_grade(name, grade):
	return ""

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
#%%
# ANSWER
def student_grade(name, grade):
	return ("{} received {} % on the exam".format(name, grade))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.6 Formatting strings

EXAMPLE 27

calculate the price of an item, with and without tax
select 2 decimals with the FORMAT METHOD
we will use expressions inside the curly brackets {}
"""
price_without_tax = 7.5
price_with_tax = price_without_tax * 1.09 # tax is 9%
print(price_without_tax, price_with_tax)

#output is 7.5 8.175
# the output contains a number with 3 digits after decimal point
# we will correct this in order to have only 2 decimals
#we will do the correction with the FORMAT METHOD

#%%

price_without_tax = 7.5
price_with_tax = price_without_tax * 1.09 # tax is 9%

print("Price before tax:${:.2f}. Price after tax:${:.2f}".format(price_without_tax,price_with_tax))

# :.2f is a FORMATTING EXPRESSION
# The colon : separates the expression from the preceding name?
# .2f, means we format a float number and after its decimal point it is allowed to have 2 decimal digits

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.6 Formatting strings

EXAMPLE 28

convert fahrenheit to celcius 
use the FORMAT METHOD
allow 2 digits after decimal dot
"""

def convertF_toC(x): #we create a new function, Variable x refers to Farenheit values
    return (x-32)*5/9 # this return statement returns the outcome of this 

for x in range(0,101,10): 
    print("{:>3} F | {:>6.2f} C".format(x, convertF_toC(x)))


# arguments of the format method
# x, the variable for values of F degrees
#convertF_toC(x), the function which converts F to C

# the for loop will apply the function to each x (F degree), from 0 to 100 at an increment of 10
# 0 F degrees, 10 F degrees and so on

# the first {:>3}, contains the colon :, 
# the symbol > which aligns the F degrees to the right e.g. 100 
# and alignment to the right will happen for 3 spaces

# the second {:>6.2f}, contains the colon :
# the symbol > which aligns the C degrees to the right
# and alignement to the right will happen for 6 spaces, e.g. -17.78
# the formatting expression .2f which allows 2 decimal places for the C degrees

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.7 String reference cheat sheet

EXAMPLE 29

# NOTE 1 len(string)                # Returns the length of the string

# NOTE 2 for character in string    # Iterates over each character in the string

# NOTE 3 if substring in string     # Checks whether the substring is part of the string. Returns True or False
"""
#%%
def findstring(name):
    if "Py" in name:
        return True
    else:
        return False

findstring("Python")

#%%
"""
# NOTE 4 string[i] 
    # Accesses the character at index i of the string, starting at zero

# NOTE 5 string[i:j] 
    # Accesses the substring starting at index i, ending at index j-1. 
    # If i is omitted, it's 0 by default. 
    # If j is omitted, it's len(string) by default.

# NOTE 6 string.lower() 
    # Returns a copy of the string with all characters converted to lowercase
    
# NOTE 7 string.upper()
    #Returns a copy of the string with all characters converted to uppercase
    
# NOTE 8 string.strip()
    # removes spaces from left and right of the string
    
# NOTE 9 string.lstrip() 
    # removes spaces from the left side of the string

# NOTE 10 string.rstrip()
    # removes spaces from the right side  of the string

# NOTE 11 string.count(substring)
    # Returns the number of times substring is present in the string

# NOTE 12 string.isnumeric()
    # Returns True if there are only numeric characters in the string. If not, returns False.

# NOTE 13 string.isalpha()
    # Returns True if there are only alphabetic characters in the string. If not, returns False.

# NOTE 14 string.split() 
    # Returns a LIST of substrings that were separated by whitespace
    # THE SPLIT METHOD, TAKES A STRING AND CONVERTS IT TO A LIST WHERE EVERY ELEMENT WAS A SUBSTRING

# NOTE 15 string.split(delimiter)
    # Returns a LIST of substrings that were separated by e.g. a dot ., we place the dot in the split method parenthesis

# NOTE 16 string.replace(old, new) 
    # Returns a new string where all occurrences of old have been replaced by new
    # REPLACE METHOD for strings. Remember Strings are immutable
"""
#%%
text = "Kitten"
text.replace("Kitten", "Puppy")     # up to here, output is Puppy
print(text)                         # here , output is Kitten
#%%
"""
# NOTE 17 delimiter.join(list of strings)
    # the JOIN METHOD Returns a new string with all the strings joined by the delimiter
    #the join method uses parentheses and square brackets
    #the join method concatenates the elements of a LIST!

    # JOIN WITH SPACES
    #" ".join(["join", "with", "spaces"])
    # output is: 'join with spaces'

    # JOIN WITH TRIPLE DOTS
    #"...".join(["join", "with", "triple", "dots"])
    # 'join...with...triple...dots'

# NOTE 18 official documentation for all available String methods, https://docs.python.org/3/library/stdtypes.html#string-methods
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.8 Formating Strings cheat sheet

EXAMPLE 30

(see also examples 24 and 25)

The format() method  
a
syntax: "string containing empty placeholders {}".format(variables)
when placeholders are empty, they are replaced by the variables in the parenthesis of the format method
the variables are automatically converted to strings
b
syntax:"{0} {1}".format(first, second)
when placeholders contain a number, they are replaced by the variable corresponding to that order
c
syntax:"{var1} {var2}".format(var1=value1, var2=value2)
when placeholders contain a field name they’re replaced by the variable corresponding to that field name
d
syntax:"{:exp1} {:exp2}".format(value1, value2)
when placeholders include a colon, what comes after the colon is a formatting expression

Official documentation for the format string syntax, https://docs.python.org/3/library/string.html#formatstrings
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.8 Formating Strings cheat sheet

EXAMPLE 31

(see also examples 24 and 25)

Formatting expressions
-they are used inside the placeholders {} of the FORMAT METHOD to 
define how individual values are presented.
"""


'{:.0f}'.format(10.5)       # formats the float to an integer. Output is 10

'{:.2f}'.format(0.5)        # formats the float of 1 decimal to a float with 2 decimal places. Output is 0.50

'{:.2s}'.format('Python')   # formats the string length to 2 characters. Output is 'Py'

'{:<6s}'.format('Py')       # formats the string length to 6 characters. Output is 'Py    '
                            # symbol < aligns the string to the left

'{:>6s}'.format('Py')       # formats the string length to 6 characters. Output is '    Py'
                            # symbol > aligns the string to the right

'{:^6s}'.format('Py')       # formats the string length to 6 characters. Output is '  Py  '
                            # symbol ^ aligns the string to the center

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.9 Practice Quiz: Strings

EXAMPLE 32

The is_palindrome function checks if a string is a palindrome. 
A palindrome is a string that can be equally read from left to right or right to left,
omitting blank spaces, and ignoring capitalization.
Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". 
Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
"""
# QUESTION
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for ___:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if ___:
			new_string = ___
			reverse_string = ___
	# Compare the strings
	if ___:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
#%%
# ANSWER
def is_palindrome(input_string):
    string1= input_string.replace(" ", "")  # remove all spaces
    string2 = string1.lower()               # convert to lowercase
    reverse_string = string2[::-1]          # reverse 
	    
    if string2 == reverse_string:           # examine equality
		    return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.1 Strings
4.1.9 Practice Quiz: Strings

EXAMPLE 33

Using the format method, fill in the gaps in the convert_distance function so that it 
returns the phrase "X miles equals Y km", with Y having only 1 decimal place. 
For example, convert_distance(12) should return "12 miles equals 19.2 km".
"""
#QUESTION
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {___} km".___
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

#%%
#ANSWER
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
