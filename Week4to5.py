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


#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.1 What is a list?
THEORY
-A list uses square brackets, the elements are separated by commas.
    The elements can be strings or numbers or any other data type
- print(list)       displays contents of the list
- type(list)        asks Python what is the data type
- len(list)         find out the length of a list (how many elements it contains)
- element IN list   find out if a certain element exists in the list
- list[0],          access an element with index 0
- list[1:3],        access a range of elements from index 1 to index 2
- list[:2],         access a range of elements from index 0 to index 1 (by default, blank is considered 0)
- list[2:]          access a range of elements from index 2 to last index (by default, blank is considered the last index)
- list[::-1]        reverses the order!
-The JOIN METHOD, "delimiter".join(list), takes 1 argument, the list
    the join method, joins the elements of a list together, and produces a string
COMMON CHARACTERISTICS BETWEEN LISTS AND STRINGS
- FOR LOOPS                 to iterate over characters in strings
                            to iterate over elements in lists
                            
- access a certain element, string[x]
                            list[x]
                            
- len() function            to find out the number of characters in a string
                            to find out the number of elements in a list
                            
- use the + symbol          to concatenate strings together to a bigger string
                            to concatenate lists together to a bigger list
                            
- use the IN keyword        to ask if a character is in the string (True, False)
                            to ask if an element is in the list (True, False)
DIFFERENCE BETWEEN LISTS AND STRINGS
    strings are immutable, lists are mutable
    we cannot change a string, but we can change a list
Lists are mutable so we can:  
    add one list to another list with symbol +
    add an element with APPEND     to the end of the list
    add an element with INSERT     to a certain index position of the list
    remove an element with REMOVE  only first occurence is removed
    remove an element with POP     the removed element is displayed
    replace an element with assign replace an existing element of a certain index                          
   
    list.append(element)        takes 1 argument    adds element to the end of the list
    list.insert(index, element) takes 2 arguments   adds element to the list (beginning, middle, end)
    list.remove(element)        takes 1 argument    removes element from the list (only first occurence is removed)
    list.pop(index)             takes 1 argument    removes element from the list (the removed element is displayed)
    list[2] = new element       not a function      replaces element of index 2, with the element we provide
-   Strings     sequences of characters         immutable
    Lists       sequences of any data type      mutable     []
    Tuples      sequences of any data type      immutable   ()
TUPLES ()
Tuples are useful when we need an element to exist permanently in a certain index position.
 the position of the elements in a tuple, is MEANINGFUL
-Where do we use tuples?
 When a function returns more than one value, then it's actually returning a tuple of values
  
-Advantages of tuples over lists
    Iterating through tuple is faster than with list, since tuples are immutable.
    Tuples that consist of immutable elements can be used as key for dictionary, which is not possible with list
    If you have data that is immutable, implementing it as tuple will guarantee that it remains write-protected
How to unpack a tuple:  assign Variables on the left for the values of the tuple on the right 
                        the number of variables on left hand side should be equal to number of values in given tuple
Why unpack the tuple:   to get each tuple element as a separate Variable
We can also unpack a list, following the same method
(Packing and Unpacking Arguments in Python see http://hangar.runway7.net/python/packing-unpacking-arguments)
ENUMERATE FUNCTION
    enumerates the elements of a sequence and produces a tuple with index number-element. tuple = ('index number', 'element')
    
    the enumerate(), adds the index for each element of the list
    enumerate(list, number) and the result is: ('0', 'element 0'), ('1', 'element 1')
    The argument "number" is optional and tells the function where to start counting the index
    If the argument "number" is left blank, index numbering starts from 0!
    
    The enumerate function returns a tuple for each element in the list. 
        The first value in the tuple is the index of the element in the sequence. 
        The second value in the tuple is the element in the sequence.
    
    The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
    The enumerate() function adds a counter as the key of the enumerate object.
create a list using the APPEND METHOD (first create an empty list to which to will append elements one by one)
create a list using LIST COMPREHENSION
LIST COMPREHENSION
technique to create lists, write one line of code within square brackets!
-it allows us to create new lists, based on sequences or ranges
-we can create a list, with just one line of code
-we can create a list from:     a range
                                a list
                                a tuple
                                any other Python sequence
- it is like using natural language to solve a problem
List Comprehension
1   [expression for variable in sequence] 
    Creates a new list based on the given sequence. Each element is the result of the given expression.
2   [expression for variable in sequence if condition]
    Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.
COMMON CHARACTERISTICS BETWEEN  LISTS AND TUPLES
1   len(sequence)               Returns the length of the sequence
2   for element in sequence     Iterates over each element in the sequence
3   if element in sequence      Checks whether the element is part of the sequence
4   sequence[i]                 Accesses the element at index i of the sequence, starting at zero
5   sequence[i:j]               Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
6   for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time
for more sequence operations see  https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
OPERATIONS SPECIFIC TO LISTS (only for lists, because lists are mutable)
list.append(x)      Inserts x at the end of the list
list.insert(i, x)   Inserts x at index i
list.remove(x)      Removes the first occurrence of x in the list
list.pop(i)         Removes element from position i and also returns it. If i is omitted, the last element is removed and returned
list[i] = x         Replaces the element at index i with x
list.sort()         Sorts the items in the list
list.reverse()      Reverses the order of items of the list
list.clear()        Removes all the items of the list
list.copy()         Creates a copy of the list
list.extend(other_list) Appends all the elements of other_list at the end of list
for list specific documentation visit https://docs.python.org/3/library/stdtypes.html#lists
EXAMPLE 1
A list uses square brackets, the elements are separated by commas.
The elements can be strings or numbers or any othe data type
- print(list)       displays contents of the list
- type(list)        asks Python what is the data type
- len(list)         find out the length of a list (how many elements it contains)
- element IN list   find out if a certain element exists in the list
- list[0],          access an element with index 0
- list[1:3],        access a range of elements from index 1 to index 2
- list[:2],         access a range of elements from index 0 to index 1 (by default, blank is considered 0)
- list[2:]          access a range of elements from index 2 to last index (by default, blank is considered the last index)
"""
list1 = ["now", "we", "are", "cooking!"] 
print(list1) # displays the contents of the list
# output is ['now', 'we', 'are', 'cooking!']
print(type(list1)) # ask Python what is the data type
# output is <class 'list'>
#%%
len(list1)# find out the length of the list, how many elements it contains
# output is 4, so 4 elements in this list of strings
#%%
"are" in list1 # examine if a certain element is in the list with the IN keyword
# output is True, so yes that element is in the list
# the above is a Boolean, which we can use for branching or looping
#%%
print(list1[0])# we want to access one specific element of the list
# output is now
#%%
list1[1:3] # we want to access a range of elements
# output is['we', 'are']
#%%
list1[:2] # we want to access a range of elements
# output is ['now', 'we']
#%%
list1[2:] # we want to access a range of elements
# output is ['are', 'cooking!']

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.1 What is a list?
EXAMPLE 2
The JOIN METHOD, "delimiter".join(list), takes 1 argument, the list
the join method, joins the elements of a list together, and produces a string
here, we will join the elements of a list and produce a string.
"users_new" will be a string of the elements of the list "users"
in the return statement we will concatenate the string "group" with the string "members" using ":"
the return statement provides the argument with which we will call the function
"""
# QUESTION
def group_list(group, users):
  members = ___
  return ___

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
#%%
# ANSWER
def group_list(group, users):
  users_new = ",".join(users)
  return group + ":" + users_new

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.1 What is a list?
EXAMPLE 3
lists and strings are both sequences
so, they have the following common characteristics
- FOR LOOPS                 to iterate over characters in strings
                            to iterate over elements in lists
- access a certain element, string[x]
                            list[x]
- len() function            to find out the number of characters in a string
                            to find out the number of elements in a list
- use the + symbol          to concatenate strings together to a bigger string
                            to concatenate lists together to a bigger list
- use the IN keyword        to ask if a character is in the string (True, False)
                            to ask if an element is in the list (True, False)
"""
string1 = "Coca "
string2 = "Cola"
print(string1 + string2)
# output is Coca Cola
list1 =[1,2,3,4]
list2=[10,8,7,6,]
print(list1 + list2)
# output is [1, 2, 3, 4, 10, 8, 7, 6]

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.2 Modifying the Contents of a List
EXAMPLE 4
lists and strings are both sequences
but, they have the following difference: strings are immutable
                                         lists are mutable
Lists are mutable so we can:    add an element with APPEND,     to the end of the list
                                add an element with INSERT,     to a certain index position of the list
                                remove an element with REMOVE,  only first occurence is removed
                                remove an element with POP,     the removed element is displayed
                                replace an element with assign, replace an existing element of a certain index                          
   
list.append(element)        takes 1 argument    adds element to the end of the list
list.insert(index, element) takes 2 arguments   adds element to the list (beginning, middle, end)
list.remove(element)        takes 1 argument    removes element from the list (only first occurence is removed)
list.pop(index)             takes 1 argument    removes element from the list (the removed element is displayed)
list[2] = new element       not a function      replaces element of index 2, with the element we provide
"""
fruits = ['Pineapple', 'Banana', 'Apple', 'Melon']
fruits.append("Kiwi")
print(fruits)
# output is ['Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']
fruits.insert(0, "Orange")
print(fruits)
# output is ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']
fruits.insert(25, "Peach")
print(fruits)
# output is ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi', 'Peach']
fruits.remove('Melon')
print(fruits)
# output is ['Orange', 'Pineapple', 'Banana', 'Apple', 'Kiwi', 'Peach']
fruits.pop(3)
# output is 'Apple'
print(fruits)
# output is ['Orange', 'Pineapple', 'Banana', 'Kiwi', 'Peach']
fruits[0] = "Tomato"
print(fruits)
# output is ['Tomato', 'Pineapple', 'Banana', 'Kiwi', 'Peach']
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.2 Modifying the Contents of a List
EXAMPLE 5
use the append method, to add to the new list, only the even index elements of the old list
the return statement provides the argument with which we will call the function
"""
# QUESTION
def skip_elements(elements):
	# code goes here

	return ___

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
#%%
#ANSWER, create a new list and append elements with an even index number
def skip_elements(elements): # elements is a list. In fact we have 3 such lists below
    new_list = []           # create a new list into which I will add elements with an even index number
    x = 0                   # INITIALIZE the index number x
    for element in elements:# iterate over the list "elements"
        if x%2==0:          # if x, the index number of the element, is even, then
            new_list.append(element) # append the element with the even index number to the new empty list
        x=x+1               # INCREMENT the  index number x, outside of the IF block to let the for loop continue even when x is odd!!
    return new_list         # return the result of this function as an argument inside the function
	
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.3 Lists and Tuples
EXAMPLE 6
Strings     sequences of characters         immutable
Lists       sequences of any data type      mutable     []
Tuples      sequences of any data type      immutable   ()
-Tuples are useful when we need an element to exist permanently in a certain index position.
 the position of the elements in a tuple, is MEANINGFUL
-Where do we use tuples?
 When a function returns more than one value, then it's actually returning a tuple of values
  
-Advantages of tuples over lists
    Iterating through tuple is faster than with list, since tuples are immutable.
    Tuples that consist of immutable elements can be used as key for dictionary, which is not possible with list
    If you have data that is immutable, implementing it as tuple will guarantee that it remains write-protected
See below that the function results in 3 values which are displayed in a tuple
hours, minutes, seconds (1, 23, 20)
the return statement provides the argument with which we will call the function
"""
fullname = {'Grace', 'M', 'Hopper'} # this is a tuple, and the position of the elements is meaningful
#%%
# convert given seconds, to: hours, minutes and remaining seconds
# 1 hour contains 3.600 seconds
# 1 minute contains 60 seconds
def convert_seconds(seconds):
    hours = seconds // 3600 # Variable hours is defined
    minutes = (seconds - hours * 3600) // 60 # Variable minutes is defined
    remaining_seconds = seconds - hours * 3600 - minutes * 60 # Variable remaining_seconds is defined
    return hours, minutes, remaining_seconds # return 

convert_seconds(5000) # call the function by providing an argument

# Analysis
# hours= 5000:3600=1.388 we keep 1 because of the floor division
# minutes = (5000 - 1x3600) : 60 = 23.333 we keep 23  because of the floor division
# remaining_minutes = 5000 - 1x3600 - 23x60=20 here we calculate the remainders of the above divisions
# output is  the tuple (1, 23, 20)
#%%
type(convert_seconds(5000))
# we ask Python what data type is the result of this function
# output is tuple

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.3 Lists and Tuples
EXAMPLE 7
How to unpack a tuple:  assign Variables on the left for the values of the tuple on the right 
                        the number of variables on left hand side should be equal to number of values in given tuple
Why unpack the tuple:   to get each tuple element as a separate Variable
We can also unpack a list, following this method
(Packing and Unpacking Arguments in Python see http://hangar.runway7.net/python/packing-unpacking-arguments)
the return statement provides the argument with which we will call the function
"""
def convert_seconds(seconds):
    hours = seconds // 3600 # Variable hours is defined
    minutes = (seconds - hours * 3600) // 60 # Variable minutes is defined
    remaining_seconds = seconds - hours * 3600 - minutes * 60 # Variable remaining_seconds is defined
    return hours, minutes, remaining_seconds # here we ask Python to display the calculation result for each Variable. Each result will be the element of a tuple 

hours, minutes, seconds = convert_seconds(5000)
#we unpack the previously produced tuple into 3 separate values
print(hours, minutes, seconds)
# output is 1 23 20, it is no longer a tuple
#%%
t = (0, 1, 2)           # tuple
a, b, c = (0, 1, 2)     # UNPACK THE TUPLE by assigning 3 variables for the 3 values of the tuple
print(a)                # print Variable a
print(b)
print(c)
# 0
# 1
# 2
l = [0, 1, 2]           # list
a, b, c = [0, 1, 2]     # assign 3 variables for the 3 values of the list
print(a)                # print Variable a
print(b)
print(c)
# 0
# 1
# 2
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.3 Lists and Tuples
EXAMPLE 8
We have a list, and its elements are tuples.
So,     we have list elements (which are tuples)
        we have tuple elements (which are strings and integers)
We want to concatenate the tuple elements with text and produce a string.
This will be the argument with which we will call the function (return statement)
So, the function guest_list should give the result:
    guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer"))
        Ken is 30 years old and works as Chef.
        Pat is 35 years old and works as Lawyer.
        Amanda is 25 years old and works as Engineer.
        
format method
    "{} and {} and {}". format(Variable1, Variable2, Variable3)
    placeholders contain value 1, value 2, value 3 which correspond to Variable 1, variable 2, Variable 3
"""
# QUESTION
def guest_list(guests):
	for ___:
		___
		print(__.format(__))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#%%
#ANSWER
def guest_list(guests): 
    	for x in guests: 
            # we ask the function to iterate over the elements of the list "guests" 
            name, age, profession = (x[0], x[1], x[2]) 
            # for each element of the list, we unpack it by assigning a Variable to each value of the tuple
            # tuple element x[0] is assigned to the Variable "name"
            
            print("{} is {} and works as {}.".format(name, age, profession)) 
            # after unpacking the tuple elements, we use the FORMAT METHOD to concatenate the tuple elements with text
            # tuple string + is + tuple integer + works as + tuple string
            # order of placeholders corresponds to the order of the variables
	

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
# output is Ken is 30 and works as Chef.
#           Pat is 35 and works as Lawyer.
#           Amanda is 25 and works as Engineer.

# this is a list, where each element is a tuple
# we have 3 list elements with indexes 0, 1,2
# for each list element after unpacking its  tuple, it contains 3 tuple elements x[0], x[1], x[2]
# we do 3 iterations
# for list element x, we examine its tuple: (x[0], x[1], x[2])
#       1st placeholder corresponds to the tuple element x[0] and the Variable name
#       2nd placeholder corresponds to the tuple element x[1] and the Variable age
#       3rd placeholder corresponds to the tuple element x[2] and the Variable profession

# result of 1st iteration over the list is
# list element is x=0, it is the tuple ('Ken', 30, "Chef"),
# concatenate the unpacked tuple elements with text, Ken is 30 and works as Chef

# result of 2nd iteration over the list is
# x=1, tuple is ("Pat", 35, 'Lawyer'), 
#concatenate the unpacked tuple elements with text,Pat is 35 and works as Lawyer

# result of 3rd iteration over the list is
# x=2, tuple is ('Amanda', 25, "Engineer"), 
#concatenate the unpacked tuple elements with text,Amanda is 25 and works as Engineer

# Iteration stops, we examined all 3 list elements
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.4 Iterating over Lists and Tuples
EXAMPLE 9
In a list whose elements are strings:
    find sum of number of characters    (sum = characters of element0 + characters of element1 + ...)
    find average number of characters   (average = sum/number of elements)
    use the format method to display results
"""
animals = ["Lion", "Zebra", "Dolphin", "Monkey"] 
# list with 4 elements. Elements are strings
chars = 0 
# INITIALIZE.
# Number of characters start at 0
for element in animals: #ITERATE over each element of this list
    chars = chars + len(element) 
    # INCREMENT. 
    # The total number of characters starts from 0 and in each iteration we add the number of characters of 1 element 
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
# the format method concatenates the values with text. We have placed an operation as the 2nd Variable!

#1st iteration
# element 0= Lion, chars = 0+ len("Lion")= 0 + 4=4
#2nd iteration
# element 1=Zebra, chars = 4 + len("Zebra")=4 + 5=9
#3rd iteration
# element 2 = Dolphin, chars = 9 + len("dolphin")= 9 + 7=16
# 4th iteration
# element 3= Monkey, chars = 16 +len(Monkey) = 16 + 6= 22

# iteration stops
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.4 Iterating over Lists and Tuples
EXAMPLE 10
The ENUMERATE function
    enumerates the elements of a sequence and produces a tuple with index number-element
    
    the enumerate(), adds the index for each element of the list
    enumerate(list, number) and the result is: ('0', 'element 0'), ('1', 'element 1')
    The argument "number" is optional and tells the function where to start counting the index
    If the argument "number" is left blank, index numbering starts from 0!
    The enumerate function returns a tuple for each element in the list. 
        The first value in the tuple is the index of the element in the sequence. 
        The second value in the tuple is the element in the sequence.
    
    The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
    The enumerate() function adds a counter as the key of the enumerate object.
here, we have a list of strings and we want to display each string along with the index number
    we will use     the FOR LOOP with the enumerated list not the given list
                    (to iterate over all list elements based on 2 Variables, index and element. Start index at 1)
                    the format method
                    (to display a string concatenated with "-")
"""
winners = ["Ashley", "Dylan", "Reese"]
for index, element in enumerate(winners,1): # we do the loop, by looking at 2 Variables: index and element
    print("{} - {}".format(index, element) )
    
# Output is 3 tuples (from the 3 elements of the list)
#1 - Ashley (it is a tuple. First value is the index of the element, second value is the element)
#2 - Dylan
#3 - Reese
#%%
"""
here we have a list which we want to enumerate
we will use the for loop to iterate over the enumerated list with 2 arguments!
"""
fruits = ['apple', 'banana', 'grapes', 'pear']  
for index, element in enumerate(fruits,1):
    print(index, element)
#Output is
#1 apple
#2 banana
#3 grapes
#4 pear 
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.4 Iterating over Lists and Tuples
EXAMPLE 11
we have a list with even and odd index number elements.
we want to display only the even index number elements.
use the enumerate function to select even index elements,
then append them to a new list
the return statement provides the argument with which we will call the function
"""
# QUESTION
def skip_elements(elements):
	# code goes here
	return ___

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
#%%
# ANSWER
def skip_elements(elements):
    new_list = []
    index = 0
    for index, element in enumerate(elements,0):# 
        if index % 2 == 0:
            new_list.append(element)
        index = index + 1
    return new_list
 
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
# Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
# Should be ['Orange', 'Strawberry', 'Peach']

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.4 Iterating over Lists and Tuples
EXAMPLE 12
we have an old list where each element is a tuple
    each tuple contains 2 elements which are strings (1st string is email address, 2nd string is full name)
we want a new list where each element is a string.
    each string should contain the tuple elements concatenated , "fullname<email address>", using the format method
define the function
create new list
iterate over the old list elements. Use 2 Variables (2 tuple elements) for the iteration
for each iteration append the 2 tuple elements to the new list
return the new list as an argument to call the function
"""
old_list = [('foteinirodis@gmail.com', 'Foteini Rodi'), ('john@gmail.com', 'John Marks')] 
# we want a new list ["Foteini Rodi<foteinirodis@gmail.com>"]
#%%
def full_emails(old_list):
    new_list = []
    for email, name in old_list:
        new_list.append('{}<{}>'.format(name, email))
    return new_list
        
print(full_emails([('foteinirodis@gmail.com', 'Foteini Rodi'), ('john@gmail.com', 'John Marks')] ))
# Output is ['Foteini Rodi<foteinirodis@gmail.com>', 'John Marks<john@gmail.com>']
# Output is a list with 2 elements. The elements are strings
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.5 List Comprehension
EXAMPLE 13
How to create a list using the APPEND METHOD
(We will create a list that contains multiples of 7, from 7 to 70)
"""
multiples = []
#create an empty list
for x in range(1,11): 
# perform iteration from 1 to 10, at a step of 1
    multiples.append(x*7)
    # this belongs to the for loop block.
    # multiply each element x of the range to 7
    
print(multiples)
# output is [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.5 List Comprehension
EXAMPLE 14
LIST COMPREHENSION, technique to create lists, write one line of code within square brackets!
-it allows us to create new lists, based on sequences or ranges
-we can create a list, with just one line of code
-we can create a list from:     a range
                                a list
                                a tuple
                                any other Python sequence
- it is like using natural language to solve a problem
here we will create a list, with multiples of 7, from 7 to 70, with the list comprehension technique
"""
multiples = [x*7 for x in range(1,11)]
print(multiples)
#output is [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# natural language: multiply x to 7, for all the x's in the range of 1 to 10"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.5 List Comprehension
EXAMPLE 15
-here we will create the list "lengths" from the list "languages".
 the new list will display the length of each element. (e.g. 6 is the character length for the element 'Python')
-we can do this by creating a new list, and append the measurements BUT now  we will use the technique LIST COMPREHENSION
"""
languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C']

lengths = [len(element) for element in languages]
print(lengths)

# output is [6, 4, 4, 2, 4, 1]"""
#natural language: display length of element for each element in the list"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.5 List Comprehensions
EXAMPLE 16
here we will create a list, containing all numbers divisible by 3, between 0 to 100.
we add the conditional clause if x is divisible by 3, after the range
we will use the list comprehension technique
"""
z = [x for x in range(0,101) if x%3 == 0]
print(z)


#Output is: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
#-natural language: for all numbers in the range 0 to 100, create a list only if the- numbers are divisible by 3
# mention x before the for loop
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.5 List Comprehensions
EXAMPLE 17
create a new list with only the even index number elements
use the list comprehension to generate the new list 
with the for loop, iterate over the enumerated old list 
"""
#QUESTION
def skip_elements(elements):
	return [___]  

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
#%%
# ANSWER
def skip_elements(elements):
	return [element for index,element in enumerate(elements,0) if index%2 == 0]  

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.6 Reading: Lists and Tuples Operations Cheat Sheet
EXAMPLE 18
Common sequence operations between Lists and Tuples
1   len(sequence)               Returns the length of the sequence
2   for element in sequence     Iterates over each element in the sequence
3   if element in sequence      Checks whether the element is part of the sequence
4   sequence[i]                 Accesses the element at index i of the sequence, starting at zero
5   sequence[i:j]               Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
6   for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time
for more sequence operations see  https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.6 Reading: Lists and Tuples Operations Cheat Sheet
EXAMPLE 19
Operations and methods specific only for Lists (because lists are mutable)
list.append(x)      Inserts x at the end of the list
list.insert(i, x)   Inserts x at index i
list.remove(x)      Removes the first occurrence of x in the list
list.pop(i)         Removes element from position i and also returns it. If i is omitted, the last element is removed and returned
list[i] = x         Replaces the element at index i with x
list.sort()         Sorts the items in the list
list.reverse()      Reverses the order of items of the list
list.clear()        Removes all the items of the list
list.copy()         Creates a copy of the list
list.extend(other_list) Appends all the elements of other_list at the end of list
for list specific documentation visit https://docs.python.org/3/library/stdtypes.html#lists
official documentation for mutable sequences visit https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.6 Reading: Lists and Tuples Operations Cheat Sheet
EXAMPLE 20
List comprehension
1   [expression for variable in sequence] 
    Creates a new list based on the given sequence. Each element is the result of the given expression.
2   [expression for variable in sequence if condition]
    Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.7 Practice Quiz: Lists
EXAMPLE 21
we have a list of elements
we want a list of tuples. Each tuple will contain (element, new element)
    if element does not contain "hpp" then each tuple will be (element, element)
    if element contains "hpp" then then each tuple will be (element, new element). New element contains "h" instead of "hpp"
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
- create a new list
- iterate over the old list
-   create a tuple, tuple( [element 1] + [element 2] ) and append it to the new list
        -if element contains "hpp", then:
            .append(tuple( [element] + [element.replace("hpp", "h")]))
        -if element does not contain "hpp", then:
            .append(tuple( [element] + [element]))
"""
#%%
# QUESTION
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []

print (newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]


#%%
# ANSWER
old_list = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
new_list = []

for element in old_list: 
    if ".hpp" in element:
        new_list.append(tuple([element]+[element.replace('.hpp','.h')]))
    else:
        new_list.append(tuple([element]+[element]))
        
print(new_list) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.7 Practice Quiz: Lists
EXAMPLE 22
The permissions of a file in a Linux system are split into three sets of three permissions:
    read, write, and execute for the owner, group, and others.
#	Permission	               rwx	    Binary
7	read, write and execute	   rwx	    111
6	read and write             rw-	    110
5	read and execute           r-x      101
4	read only                  r--      100
3	write and execute	       -wx      011
2	write only	               -w-      010
1	execute only               --x	    001
0	none	                   ---      000
So, relationship between octal format and string format is
    640, 6 = read and write for the OWNER/ 4 = read only for the GROUP / 0 = none for OTHERS 
        and in string format, rw- / r-- / ---
   
    755, 7 =read, write and execute for the OWNER / 5 = read and execute for the GROUP / 5 read and execute for OTHERS
        and in string format, rwx / r-x / r-x
"""
#%%
# QUESTION
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for n in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if n >= value:
                result += ___
                ___ -= value
            else:
                ___
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

#%%
# ANSWER
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # this is a key with the pairs of value and letters
    for number in [int(n) for n in str(octal)]:
    # checking the individual numbers in octal like (755) and giving them variable as "number"
        for value, letter in value_letters:
          # iterating through values and letters in key 
            if number >= value:
                result += letter
                number -= value
 # if the individual numbers (7,5,5) are larger than values in key (4,2,1) they write out the corresponding letters - ALL of them until nothing is left - similar to % function or floor division you look for remainder! 7 becomes rwx (7-4(r), 3-2(w), 1-1(x), 5 becomes r-x (5-4(r). 1 - 1(x) - no w because the 1 left over from 5-4 is less than 2. Anytime the remainder is less than what the number is you get a "-" mark instead of the letter
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

"""
for the octal list we will perform 3 iterations as it contains 3 elements (3 integers)
for each iteration of the octal list, we will perform 3 iterations over the value_letters list because it contains 3 elements (3 tuples)
1st iteration
number = 7, iterate again over the value_letters list which contains 3 elements (3 tuples)
            1st iteration (value = 4 and letter = r)
            7 >= 4, so activate the IF BLOCK
            result = result + letter = blank + r = r
            number = number - value = 7 - 4 = 3
            2nd iteration (value = 2 and letter = w)
            3 >= 2, so activate the IF BLOCK
            result = result + letter = r + w = rw
            number = 3 -2 = 1
            3rd iteration (value = 1 and letter = x)
            1>=1,so activate the IF BLOCK
            result = result + letter = rw + x = rwx
            number = number - value = 1 - 1 = 0
            Iteration stops over the value_letters list
 
2nd iteration           
number = 5, iterate again over the value_letters list which contains 3 elements (3 tuples)
            1st iteration (value = 4 and letter = r)
            5 >= 4, so activate the IF BLOCK
            result = result + letter = blank + r = r
            number = number - value = 5 - 4 = 1
            2nd iteration (value = 2 and letter = w)
            1 is not >= 2, so activate ELSE
            result = result + - = r + - = r-
            3rd iteration (value = 1 and letter = x)
            1>= 1, so activate the IF BLOCK
            result = result + letter = r- + x = r-x
            number = number - value = 1 - 1 = 0
            Iteration stops over the value_letters list
  
3rd iteration
number = 5, iterate again over the value_letters list which contains 3 elements (3 tuples)
            1st iteration (value = 4 and letter = r)
            5 >= 4, so activate the IF BLOCK
            result = result + letter = blank + r = r
            number = number - value = 5 - 4 = 1
            2nd iteration (value = 2 and letter = w)
            1 is not >= 2, so activate ELSE
            result = result + - = r + - = r-
            3rd iteration (value = 1 and letter = x)
            1>= 1, so activate the IF BLOCK
            result = result + letter = r- + x = r-x
            number = number - value = 1 - 1 = 0
            Iteration stops over the value_letters list
Iteration stops over the octal list
Result is: rwx r-x r-x
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.2 Lists
4.2.7 Practice Quiz: Lists
EXAMPLE 23
Let's create a function that turns text into pig latin:
a simple text transformation that modifies each word moving the first character to the end and
appending "ay" to the end. For example, python ends up as ythonpay.
for each word:
move first character to the end
append ay
"""
# QUESTION
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = ___
  for word in words:
    # Create the pig latin word and add it to the list
    ___
    # Turn the list back into a phrase
  return ___
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

#%%
# ANSWER
def pig_latin(text):
  new_list = []
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    new_list.append(str(word[1:]) + str(word[0])+"ay")
    # Turn the list back into a phrase
  return (" ".join(new_list))
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

"""
create a list (words) of the words in text by splitting (split(" ")).
iterate over word in words and for each word you create the new pig latin word(say) by taking word[1:] and adding word[0] and "ay". Append say to new list (I added a new list out of the loop).
Then join the new words to create the new sentence. (return " ".join(new)), new is my variable name for the new list.
"""


#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.1 What is a dictionary?
Dictionaries {}
        we use curly brackets {}
        dictionaries are mutable (changeable, we can add, remove and replace elements)
        the elements of dictionaries have the form of Key:Value 
        a dictionary can only hold a single value for a given key (so one key, one value)
        ATTENTION:      keys can be present only once in a dictionary
                        that is why, DICTIONARIES ARE A GREAT TOOL FOR COUNTING ELEMENTS AND ANALYZING FREQUENCY
        Key:Value is the quivalent of Word:Definition in a language dictionary
        dictionary = {'key1':'value1', 'key2': 'value2'}
        key is an immutable data type!
        value is a mutable data type
        the value of a key does not need to be a number, it can be: string, integer, float, tuple e.t.c.
        in a dictionary we have a series of keys that point at values
        
        like lists, dictionaries are used to organize elements into collections
        unlike lists, we do not access elements inside dictionaries by using their position index number
        
-How can we create a dictionary from scratch?
    first create empty dictionary
    then, assign values to keys this way: dictionary[key] = value
    
-How can we access a value in the dictionary?
    we will use the corresponding key to access the value
    dictionary[key] and use square brackets !
- How to access the Keys of a dictionary
    just write dictionary.keys()
    
- How to access the Values of a dictionary
    just write dictionary.values() 
   
-How can we examine if a key is in the dictionary?
    use the IN keyword, key IN dictionary then it is true or false    
    
-How to add an element to the end of a dictionary
    dictionary[key] = value. 
    Create the key then assign a new value to it
    
-How to change the value of a key in a dictionary (modify an element)
    dictionary[key] = new value. 
    The old value is over-written
-How to delete an element from a dictionary
    use the DEL keyword
    del dictionary[key]  
    
- We can use FOR LOOPS to iterate over
    strings
    lists
    tuples
    dictionaries
- How to iterate over dictionaries with a FOR LOOP 
    1   iterate over the Keys of the dictionary (2 ways)
        the iteration Variable will be the Key 
        for KEY in dictionary:
        for KEY in dictionary.keys():
        
    2   iterate over the Values of the dictionary
        the iteration Variable will be the Value
        for VALUE in dictionary.values():
            
    3   iterate over the elements (key:value) of the dictionary
        the iteration Variables will be Key and Value
        for KEY,VALUE in dictionary.items():
        the result is a tuple for each pair of key-value, e.g. tuple = ('key1', 'value1')    
    
ATTENTION:      
keys can be present only once in a dictionary
that is why, DICTIONARIES ARE A GREAT TOOL FOR COUNTING ELEMENTS AND ANALYZING FREQUENCY   
    
 - When to choose a List and When to choose a Dictionary
    1 - Lists are slow to search - Dictionaries are fast
        time to access an element in a list depends on the number of elements in the list
        time to access an element in a dictionary is independent from the number of elements in the dictionary!
    e.g.we need the same time to access a given key in a dictionary of 10 elements and in a dictionary of 10.000 elements!
    so, we can search FASTER in a dictionary than in a list
    SO WE SHOULD USE A DICTIONARY WHEN PLANNING TO SEARCH FOR A SPECIFIC ELEMENT 
    2 - Lists can contain any data type
      - Dictionary keys must be immutable data types
      - Dictionary values can be any data type even lists, or dictionaries!
    
    in lists, we can store ANY data type
    in dictionaries, Keys are restricted to specific data types and Values can be ANY data type
    Keys can be only immutable data types (like numbers,booleans,strings,tuples)
    Keys cannot be lists or dictionaries
    Values can be any data type, including lists and other dictionaries.
    We can use Values of more complex data type to represent more complex data, like directory trees in the file system
    
    Dictionaries are especially useful with large data sets   
  
We know that in dictionaries,   dictionary = {key:value}
                                a Key appears only once
                                a Key can be associated to one Value
                                so, how can we associate one Key to more Values?
                                by using a list as a Value!    
    
Another data type is a Set
    - a Set is a combination of a list and a dictionary
    - a Set is used when we want to store elements and be certain that they are only present ONCE
    - the elements of a Set must be immutable
    - we can imagine the Set as a dictionary which contains only Keys and no associated Values
    - we can imagine the Set as a list where we do not care about the order of the elements,
        we only care about whether an element is in the list or not   
    
Dictionary definition: x = {key1:value1, key2:value2}
OPERATIONS we can do on Dictionaries
-len(dictionary) -                      Returns the number of elements in the dictionary
-for key in dictionary -                Iterates over each key in the dictionary
-for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
-if key in dictionary -                 Checks whether the key is in the dictionary
-dictionary[key] -                      Accesses the element with given key of the dictionary
dictionary[key] = value -               Sets the value associated with key
del dictionary[key] -                   Removes the element with given key from the dictionary
METHODS we can apply on dictionaries
-dict.get(key, default) -               Returns the element corresponding to key, or default if it's not present
-dict.keys() -                          Returns a sequence containing the keys in the dictionary
-dict.values() -                        Returns a sequence containing the values in the dictionary
-dict.update(other_dictionary) -        Updates the dictionary with the elements coming from the other dictionary. 
                                        Existing elements will be replaced; new elements will be added.
                                        
-dict.clear() -                         Removes all the items of the dictionary    
    
    
    
    
    
EXAMPLE 1    
    
"""
# create an empty dictionary
x = {}
type(x)
# Output is dict. So Python tells us that it is a dictionary
dictionary = {}
dictionary['one'] = 'un' # assign Value un to Key one
dictionary['two'] = 'deux'
dictionary['three'] = 'trois'
print(dictionary)
# otuput is {'one': 'un', 'two': 'deux', 'three': 'trois'}
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.1 What is a dictionary?
EXAMPLE 2
In this example, we're using a dictionary to store the number of files corresponding to each extension.
We represent: the file extension as a string,
              the count of the file extension as an integer.
-How can we access a value in the dictionary?*
    we will use the corresponding key to access the value
    dictionary[key] and use square brackets !
-How can we examine if a key is in the dictionary?
    use the IN keyword, key IN dictionary then it is true or false
    
* ALSO
- How to access the Keys of a dictionary
    just write dictionary.keys()
    
- How to access the Values of a dictionary
    just write dictionary.values()
"""

file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23 }
print(file_counts)
# outout displays the above dictionary
file_counts['txt']
# outuput is 14
"jpg" in file_counts
# Output is True
#%%
file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23 }
file_counts.keys()
"""the output is dict_keys(['jpg', 'txt', 'csv', 'py'])
"""
file_counts.values()
"""
the output is dict_values([10, 14, 2, 23])
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.1 What is a dictionary?
EXAMPLE 3
How to add an element to the end of a dictionary
    dictionary[key] = value. Create the key then assign a new value to it
    
How to change the value of a key in a dictionary (modify an element)
    dictionary[key] = new value. The old value is over-written
How to delete an element from a dictionary
    use the DEL keyword
    del dictionary[key]
    
"""
file_counts['cfg'] = 8
print(file_counts)
# output is {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
file_counts['csv'] = 17
print(file_counts)
# Output is {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}
del file_counts['cfg']
print(file_counts)
# output is {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23}
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.1 What is a dictionary?
EXAMPLE 4
The "toc" dictionary represents the table of contents for a book.
Fill in the blanks to do the following: 
    1) Add an entry for Epilogue on page 39. 
    2) Change the page number for Chapter 3 to 24. 
    3) Display the new dictionary contents. 
    4) Display True if there is Chapter 5, False if there isn't.
"""
# QUESTION
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
___ # Epilogue starts on page 39
___ # Chapter 3 now starts on page 24
___ # What are the current contents of the dictionary?
___ # Is there a Chapter 5?
#%%
# ANSWER
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc['Epilogue'] = 39 # Epilogue starts on page 39
toc['Chapter 3'] = 24# Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print('Chapter 5' in toc) # Is there a Chapter 5?
#Here is your output:
#{'Introduction': 1, 'Chapter 1': 4, 'Chapter 2': 11, 'Chapter 3': 24, 'Chapter 4': 30, 'Epilogue': 39}
#False
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.2 Iterating over the Contents of a Dictionary
EXAMPLE 5
- We can use FOR LOOPS to iterate over
    strings
    lists
    tuples
    dictionaries
- iteration with a FOR LOOP in dictionaries
    1   iterate over the Keys of the dictionary (2 ways)
        the iteration Variable will be the Key 
        for KEY in dictionary:
        
    2   iterate over the Values of the dictionary
        the iteration Variable will be the Value
        for VALUE in dictionary.values():
            
    3   iterate over the elements (key:value) of the dictionary
        the iteration Variables will be Key and Value
        for KEY,VALUE in dictionary.items():
        the result is a tuple for each pair of key-value, e.g. tuple = ('key1', 'value1')
"""
"""
Iterate over the Keys of the dictionary
1st way
"""
file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23 }
for key in file_counts:
    print(key)
# output is 
#jpg
#txt
#csv
#py
#%%
"""
Iterate over the Keys of the dictionary 
2nd way
"""
file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23 }
for key in file_counts.keys():
    print(key)
#%%
"""
Iterate over the Values of the dictionary.  
"""
file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23 }
for value in file_counts.values():
    print(value)
# dispplays only the values from the key:value elements of the dictionary
#%%
"""
Iterate over the elements(key:value) of the dictionary.  
"""
file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23 }
for key,value in file_counts.items():
    print(key,value)
#output is
#jpg 10
#txt 14
#csv 2
#py 23

"""
or we can use the format method for a nicer output
"""
file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23 }
for key,value in file_counts.items():
    print(" There are {} files with the extension .{}". format(value,key))
# Output is
# There are 10 files with the extension .jpg
# There are 14 files with the extension .txt
# There are 2 files with the extension .csv
# There are 23 files with the extension .py
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.2 Iterating over the Contents of a Dictionary
EXAMPLE 6
Complete the code to iterate through the keys and values of the cool_beasts dictionary.
Remember that the items method returns a tuple of key, value for each element in the dictionary.
"""
# QUESTION
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for ___ in cool_beasts.items():
    print("{} have {}".format(___))
#%%
# ANSWER
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))

# key octopuses, value tentacles
# octopuses have tentacles
#dolphins have fins
#rhinos have horns   
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.2 Iterating over the Contents of a Dictionary
EXAMPLE 7
How to count the number of appearances of a letter in a text
(how many times does a letter appear in a text)
ATTENTION:      
keys can be present only once in a dictionary
that is why, DICTIONARIES ARE A GREAT TOOL FOR COUNTING ELEMENTS AND ANALYZING FREQUENCY
"""

#%%
def count_letters(text):
    dictionary = {} # 
    for letter in text: # ITERATE
        if letter not in dictionary:
            dictionary[letter] = 0 # INITIALIZE THE APPEARANCE NUMBER FOR EACH LETTER
        dictionary[letter] = dictionary[letter] + 1 # INCREMENT THE APPEARANCE NUMBER FOR EACH LETTER
    return dictionary
count_letters(' tenant')
#Output is {'t': 2, 'e': 1, 'n': 2, 'a': 1}

#%%
"""
EXPLANATION
-   construct a function that will tell us, how many times does a letter appear within a text
    e.g. the letter t appears 60 times
    
-   create an empty dictionary where we will place the results of the iteration
    so, Key will be the letter and Value will be the number of appearances of the letter
    so, the iteration looks for the keys and the values will be added later
    
-   iterate over text (string) with Iteration Variable letter (iteration will examine each string character in our string)
-   if condition: if the letter we find in the text is not in the dictionary then add element letter:0 
    (if the iteration finds a letter multiple times, it will not add as a Key multiple times because Keys are unique )
-   ATTENTION: the expression dictionary[key] returns the value of the key !!!
    so dictionary[letter] is essentially the value (number of appearances) associated with the letter
    
-   ELSE condition:  when a letter is in the dictionary then add 1 for each time the iteration finds it
-   The function above also counts the number of spaces too!
    To only count the letters, we'd need to specify which characters we're taking into account
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.3 Dictionaries vs. Lists
EXAMPLE 8
- When to choose a List and When to choose a Dictionary
    1 - Lists are slow to search - Dictionaries are fast
    -for IP adresses, a list is better
    -for host names and their corresponding IP addresses, then a dictionary is better
    pair host names and IP address in a key:value pair
    example: dictionary with keys=usernames and values=groups that the users belong to
    so, username:group
        time to access an element of this dictionary is independent from the number of users!
    we need the same time to access a given user name in a dictionary of 10 users and in a dictionary of 10.000 users!
    so, we can search FASTER in a dictionary than in a list
    SO WE SHOULD USE A DICTIONARY WHEN PLANNING TO SEARCH FOR A SPECIFIC ELEMENT 
    2 - Lists can contain any data type
      - Dictionary keys must be immutable data types
      - Dictionary values can be any data type even lists, or dictionaries!
    
    in lists, we can store ANY data type
    in dictionaries, Keys are restricted to specific data types and Values can be ANY data type
    Keys can be only immutable data types (like numbers,booleans,strings,tuples)
    Keys cannot be lists or dictionaries
    Values can be any data type, including lists and other dictionaries.
    We can use Values of more complex data type to represent more complex data, like directory trees in the file system
    
    Dictionaries are especially useful with large data sets
"""
ip_addresses = ['192.168.1.1', '127.0.0.1', '8.8.8.8', ]

host_addresses = {'router':'192.168.1.1', 'localhost':'127.0.0.1', 'google':'8.8.8.8'}
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.3 Dictionaries vs. Lists
EXAMPLE 9
We know that in dictionaries,   dictionary = {key:value}
                                a Key appears only once
                                a Key can be associated to one Value
                                so, how can we associate one Key to more Values?
                                by using a list as a Value!
exercise
In Python, a dictionary can only hold a single value for a given key.
To workaround this, our single value can be a list containing multiple values.
 Here we have a dictionary called "wardrobe" with items of clothing and their colors.
 Fill in the blanks to print a line for each item of clothing with each color, for example:
     "red shirt", "blue shirt", and so on.
"""
#%%
# QUESTION
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for __:
	for __:
		print("{} {}".format(__))
#%%
# ANSWER     
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key,value in wardrobe.items(): 
	for x in value:
		print("{} {}".format(x, key))
"""
explanation
iterate over the dictionary for both key and value with the items method
then for each iteration, iterate again but now over the list 
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.3 Dictionaries vs. Lists
EXAMPLE 10
Another data type is a Set
    - a Set is a combination of a list and a dictionary
    - a Set is used when we want to store elements and be certain
        that they are only present ONCE
    - the elements of a Set must be immutable
    - we can imagine the Set as a dictionary which contains only Keys and no associated Values
    - we can imagine the Set as a list where we do not care about the order of the elements,
        we only care about whether an element is in the list or not
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.4 Dictionary Methods Cheat Sheet
EXAMPLE 11
Dictionary definition: x = {key1:value1, key2:value2}
OPERATIONS we can do on Dictionaries
-len(dictionary) -                      Returns the number of elements in the dictionary
-for key in dictionary -                Iterates over each key in the dictionary
-for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
-if key in dictionary -                 Checks whether the key is in the dictionary
-dictionary[key] -                      Accesses the element with given key of the dictionary
dictionary[key] = value -               Sets the value associated with key
del dictionary[key] -                   Removes the element with given key from the dictionary
METHODS we can apply on dictionaries
-dict.get(key, default) -               Returns the element corresponding to key, or default if it's not present
-dict.keys() -                          Returns a sequence containing the keys in the dictionary
-dict.values() -                        Returns a sequence containing the values in the dictionary
-dict.update(other_dictionary) -        Updates the dictionary with the elements coming from the other dictionary. 
                                        Existing elements will be replaced; new elements will be added.
-dict.clear() -                         Removes all the items of the dictionary
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.5 Practice Quiz
EXAMPLE 12
The email_list function receives a dictionary, 
which contains domain names as keys, and a list of users as values.
Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
"""
# QUESTION

#%%
# ANSWER
def email_list(domains):
	emails = []
	for key, value in domains.items():
	  for user in value:
	    emails.append("{}@{}".format(user,key))
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
                  "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
"""
explanation
create the list emails
attach the key to each Value contained in the list
iterate over dictionary
iterate over list
append each result of iteration to the new list
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.3 Dictionaries
4.3.5 Practice Quiz
EXAMPLE 13
The groups_per_user function receives a dictionary, 
which contains group names with the list of users. 
Users can belong to multiple groups.
Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
(the reverse of what group_dictionary is)
"""
def groups_per_user(group_dictionary):
	user_groups = {}
	# iterate over group_dictionary with 2 iteration variables (key, value) and apply items() method
	for group, value in group_dictionary.items():
		# sub-iterate over only value of the group_dictionary
		for user in value:
		  if user not in user_groups: 
		    # ofcourse user IS NOT in the empty users_group dictionary. We just do that to find the initial value for the key
		    user_groups[user] = [group]
		  else:
		    user_groups[user].append(group) 
		    # the user_groups[user] is essentially the list [group] that we set before. So, after each iteration, we append values to this list
			
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

"""
explanation
in the group_dictionary dictionary we have 3 elements, so we will do 3 iterations
1st iteration (1st for loop)
key=local
value=[admin, userA]
        now we will do the sub-iteration (of the 2nd for loop) over the value [admin, userA]
        1st sub-iteration
        value = 'admin'
        now, 'admin' is not in the empty dictionary user_groups (as expected!), so IF condition is true and we execute the IF BLOCK
        user_groups[admin] = [local], here we define admin as the key and local as its associated value.
        RESULT user_groups[admin] = [local]
        2nd sub-iteration
        value = 'userA'
        now, 'userA' is not in the dictionary user_groups , so IF condition is true and we execute the IF BLOCK
        user_groups[userA] = [local], here we define userA as the key and local as its associated value.
        sub-iteration stops as we had 2 elements in our list
        
        
        RESULTS
        user_groups[admin] = [local]
        user_groups[userA] = [local]
        OR user_groups{'admin':[local], 'userA':[local]}
        
2nd iteration (2nd for loop)
key = public
value = [admin, userB]
        now we will do the sub-iteration (of the 2nd for loop) over the value [admin, userB]
        1st sub-iteration
        value = 'admin'
        now, 'admin' is in the dictionary user_groups. So IF condition is false and IF BLOCK not executed. We execute ELSE
        user_groups[user].append(group) 
        because user_groups[user] is equal to [group] so it is a list, we can go ahead and add [public] to the existing list [local]
        so user_groups[admin].append(public)= [local].append(public)=[local, public]
        2nd sub-iteration
        value = 'userB'
        
"""

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
THEORY
    "\n" is an escape sequence that can be used within a string to represent a newline
    
    METHOD split
    splits a string into elements of a LIST. The delimiter is space, by default
    The split() method splits a string into a list
    You can specify the separator, default separator is any whitespace
    string.split()
    string.split(separator, maxsplit)
    Separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
    When maxsplit is specified, the list will contain the specified number of elements plus one
    maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
    
    METHOD isnumeric
    syntax: element.isnumeric(), examines if the element consists of only number or not
   
    METHOD isdigit
    isdigit()
    string.isdigit()
    The isdigit() method returns True if all the characters are digits, otherwise False.
    Exponents, like ², are also considered to be a digit.
    
    DIFFERENCE BETWEEN ISNUMERIC AND ISDIGIT
    Char.IsNumber:
        Valid numbers are members of the DecimalDigitNumber, LetterNumber, or OtherNumber category.
        DecimalDigitNumber
        Decimal digit character, that is, a character in the range 0 through 9. 
        Signified by the Unicode designation "Nd" (number, decimal digit). The value is 8.
        LetterNumber
        Number represented by a letter, instead of a decimal digit, for example, the Roman numeral for five, which is "V". The indicator is signified by the Unicode designation "Nl" (number, letter). The value is 9.
        OtherNumber
        Number that is neither a decimal digit nor a letter number, for example, the fraction ½. The indicator is signified by the Unicode designation "No" (number, other). The value is 10.
    Char.IsDigit:
        Valid digits are members of the DecimalDigitNumber category only.
    
    
    
    METHOD isalpha
    syntax: string.isalpha()
    The isalpha() method returns True if all the characters are alphabet letters (a-z).
      
    METHOD append
    syntax: list.append(elmnt), appends an element to the end of a list
    we can append nothing also! list.append("")
    
    METHOD join
    syntax: "delimiter".join(iterable) and "delimiter".join(list)
    "delimiter".join(list), takes 1 argument, the list.
    the join method, joins the elements of a list together, and PRODUCES A STRING
    it can join the Keys of a dictionary too, but not the values
    
    METHOD replace
    replaces a specified value with a new one
    string.replace(oldvalue, newvalue, count)
    oldvalue	Required. The string to search for
    newvalue	Required. The string to replace the old value with
    count       Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
    
    METHOD UPDATE for Dictionaries
    dictionary1.update(dictionary2)
EXERCISE 1
The format_address function separates out parts of the address string into new strings: house_number and street_name, 
and returns: "house number X on street named Y". 
The format of the input string is: 
numeric house number, 
followed by the street name which may contain numbers, but never by themselves, and could be several words long. 
For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 
Fill in the gaps to complete this function.
"""
# QUESTION
def format_address(address_string):
  # Declare variables

  # Separate the address string into parts

  # Traverse through the address parts
  for __:
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(__)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
#%%
# ANSWER
def format_address(address_string):
    
    initial_list = address_string.split() # split the string "address_string" by default at spaces and produce a list with smaller strings
    house_number = [] # create an empty list on which we will append elements of the above list, according to conditions
    street_name = [] # create an empty list on which we will append elements of above list, according to conditions
  
    for element in initial_list: # iterate over the list we just created
        if element.isnumeric(): # if element is numeric, append it
              house_number.append(element)
        else:
            house_number.append("") # if element is not numeric append nothing
            
            if element.isalpha: # if element contains only letters
                  street_name.append(element)
            else:
                street_name.append("") # if element contains also other characters than letters
    house_number1 = "".join(house_number) # create a new list, in that we will join all the appended elements and recreate a string
    street_name1 = " ".join(street_name) # create a new list, in that we will join all the appended elements and recreate a string
       # the join method, joins the elements of a list together, and produces a string

   
  # Return the new strings into the function
    return "house number {} on street named {}".format(house_number1, street_name1)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 2
The highlight_word function changes the given word in a sentence to its upper-case version.
For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
Can you write this function in just one line?
"""
# QUESTION
def highlight_word(sentence, word):
	return(___)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
#%%
# ANSWER
def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))
    # This is LIST COMPREHENSION
    # technique to create lists, write one line of code within square brackets
    # SENTENCE = "Have a nice day"
    # WORD = "nice"
    # USE THE METHOD sequence.replace(old, new), takes 2 arguments replaces old with new

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 3
A professor with two assistants, Jamie and Drew, wants an attendance list of the students,
in the order that they arrived in the classroom.
Drew was the first one to note which students arrived, and then Jamie took over.
After the class, they each entered their lists into the computer and emailed them to the professor, 
who needs to combine them into one, in the order of each student's arrival.
Jamie emailed a follow-up, saying that her list is in reverse order.
Complete the steps to combine them into one list as follows: 
    the contents of Drew's list, followed by Jamie's list in reverse order, 
    to get an accurate list of the students as they arrived.
"""
# QUESTION
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
#%%
# ANSWER
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  # in general, list[::-1] reverses the order for the elements within the list
  list3 = Drews_list + Jamies_list[::-1] # lists can be concatenated with + symbol
  return list3 # return argument and call the function with this argument

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

"""
i will reverse Jamie's list
then concatenate it with Drew's list
1st is Drew's list, then I attach reversed Jamie's list
list 1 is Jamies_list, reverse it!
list 2 is Drews_list
"""
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 4
Use a list comprehension to create a list of squared numbers (n*n).
The function receives the variables start and end, and returns a list of squares of consecutive numbers between
start and end inclusively.
For example, squares(2, 3) should return [4, 9].
"""
# QUESTION

#%%
def squares(start, end):
	return [ ___ ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#%%
# ANSWER
def squares(start, end):
    
    x = start
    y = end
    return [n*n for n in range(x,(y+1),1)]
#raise n to the power of n, for all n's in the range (start, stop, step)
# we add 1 to the stop value, because by default range stops at a number less than 1 of the mentioned
print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 5
Complete the code to 
iterate through the keys and values of the car_prices dictionary, printing out some information about each one.
"""
# QUESTION
def car_listing(car_prices):
  result = ""
  for __:
    result += "{} costs {} dollars".__ + "\n"
    # this string "\n" tells Python to create a new line
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

#%%
# ANSWER
def car_listing(car_prices):
  result = ""
  for key, value in car_prices.items():
    result += "{} costs {} dollars".format(key, value) + "\n"
    # format method to concatenate strings between them and also with our own text
    # "\n" is an escape sequence that can be used within a string to represent a newline
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 6
Taylor and Rory are hosting a party. 
They sent out invitations, and each one collected responses into dictionaries, 
with names of their friends and how many guests each friend is bringing. 
Each dictionary is a partial list, but Rory's list has more current information about the number of guests. 
(so overwrite Taylors guests!)
Fill in the blanks to combine both dictionaries into one, 
with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, 
if a name is included in both dictionaries. 
Then print the resulting dictionary.
dictionary.update(iterable)
d.update(d1)
"""
# QUESTION
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
#%%
# ANSWER
def combine_guests(guests1, guests2):
    Taylors_guests.update(Rorys_guests)
    # dictionary1.update(dictionary2)
    
    return Taylors_guests
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 7
Use a dictionary to count the frequency of letters in the input string. 
Only letters should be counted, not blank spaces, numbers, or punctuation. 
Upper case should be considered the same as lower case. 
For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
"""
#%%

# QUESTION
def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in ___:
    # Check if the letter needs to be counted or not
    ___
    # Add or increment the value in the dictionary
    ___
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
#%%
# ANSWER
def count_letters(text):
  unwantedchars = '''+, =, ., !'''
  dictionary = {} # create an empty dictionary
  text2=text.lower() # convert initial text to lower characters
  text3=text2.split() # split initial text into a list of smaller strings separated by space
  text4="".join(text3) # join elements of above list into a new string, using nothing as a delimiter
  text5=''.join([i for i in text4 if not i.isdigit()]) # iterate over sequence text4 and join elements together (using nothing as a delimiter)
                                                         # iterate over all elements except digits! Here we removed digits
    # Go through each letter in the text
  for letter in text5: # iterate over text 5
    if letter not in unwantedchars: # exclude unwanted characters
      if letter not in dictionary: # initialize the appearance number of the letter . We initialize at 1
        dictionary[letter] = 1
      else:
         dictionary[letter] = dictionary[letter] + 1 # increment the appearance number of the letter
 
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 8
What do the following commands return when animal = "Hippopotamus"?
"""
        
animal = "Hippopotamus" 
 print(animal[3:6])
>>> print(animal[-5])
>>> print(animal[10:])
# SLICING
#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 9
What does the list "colors" contain after these commands are executed?
"""

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
# WE INSERT ELEMENT YELLOW AT INDEX POSITION 2

#%%
"""
Google's Crash course on Python, Week 4: Strings, Lists, Dictionaries
4.4 FINAL QUIZ
EXERCISE 10
What do the following commands return?
"""
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()

# RESULT IS dict_keys(['router', 'localhost', 'google'])

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.1 Object-oriented Programming
Theory from Google
What is Object-oriented Programming
    Python uses a programming pattern, called object-oriented programming, to explain concepts to a computer.
    Python OOP models these concepts by using classes and objects. 
    The point of object oriented programming is:
        to help define a real-world concept in a way that the computer understands    
    CLASS: represents and defines concepts
    OBJECT: it is an instance of a class (e.g. class is Fruits and instance is Apple)
     
    Everything in Python is an object!
        numbers, strings, lists, dictionaries are objects
        each object is, an instance of a class representing a concept
    
    The essence of OOP, is the ATTRIBUTES and METHODS associated with a type
        ATTRIBUTES: they are the characteristics associated to a type
        METHODS: they are the functions associated to a type
                a method defines what you do with an object.
    example 
    class = Apple
    objects = instances of the apple class (jonagold, granny_smith)
    attributes = color, flavor
    methods = cut method (cuts into pieces), eat method(reduces apple size)
    example File
    class = 
    objects = the typical file object, focuses on the file's contents
    attributes = name, size, date created, permissions to access it
    There are actually so many different file attributes, that Python has multiple classes to deal with files
    methods = there are many methods to read and modify what is inside the file
    
    A CLASS has attributes and methods
        about the  CLASS string
        attributes = content of the string
        methods = .upper(), .isnumeric() 
        each string we have used until now, is a DIFFERENT INSTANCE of the CLASS string
        all of these instances had different attributes BUT the same methods
        so, when we applied the methods the result was different since the attributes (content) were different
    
    attribute = "", we expect attribute to be text
    attribute = 0, we expect attribute to be  a number?
   
What is the type() used for?
    with the type (), Python tells us the CLASS of the value (or the Variable) 
    e.g. 1 belongs to the class Integer,  "" belongs to the class String
How to see all atributes and all methods for a Class 
    use the dir() function
    e.g. with dir(""), we see all atributes and methods for the string CLASS
        1)we see the special methods, that begin and end with double underscores
        these methods are not applied by using these names
        e.g. the __len__ method is called by the len function, len()
        e.g. the __ge__ method is called by the operator >=
        2)we see other methods
            we just see the names of the methods, not how to use them
How to see ALL DOCUMENTATION for a CLASS
    use the help() function
    we can use help(), on any Variable or value to show all documentation for the corresponding class
    e.g. help(""), full documentation for the class String (the class where the strings objects/instances belong to)
        1) special methods
        2) methods
            now we see name of method, 
            how the method works
            the parameters/arguments it receives (optional arguments are within []) 
            the return value
SO, help() function is better than type() and dir(), because it gives us more information
Python contains a lot of pre-defined classes BUT the power of OOP is that WE CAN ALSO DEFINE OUR OWN CLASSES!
   
 
    
HOW TO CREATE A CLASS
    -class Name:
        class keyword then name of the class and colon 
        keyword tells the computer we are defining a new class
        class name should start with a capital letter
    - pass
        pass keyword
        it shows that the class is empty
        the pass keyword can be used aa placeholder in any empty Python block
    -define 2 attributes of the class
        attribute 1 = ....
        attribute 2 = ...
        at the moment attributes are empty
            e.g.color = ""
            e.g.flavor = ""
            (we define them as strings because that is expected)
            
    -instance = class()
        create one instance of the class
        we assign a name to the instance 
            e.g.jonagold = Apple()  
            jonagold is the instance and Apple is the class where it belongs
        now we have a new object for our class
        To create an object, you have to instantiate it. 
        An instantiated object is called an instance of a class
        
    -provide values for the attributes
        instance.attribute1 = ...
        instance.attribite2 = ...
            e.g. jonagold.color = "red"
            e.g. jonagold.flavor = "sweet"
            
    -The syntax used to access the attributes is DOT NOTATION
        retrieve the values of the attributes and display them
        print(instance.attribute1)
            e.g. print(jonagold.color) we retrieve the attribute "color" of the instance "jonagold" and print it
        print(instance.attribute2)
             e.g. print(jonagold.flavor)
        DOT NOTATION Lets us access 
            the information the object may store (also called attributes)
            the abilities the object might have (also called methods)
Attention
    the attributes and methods of an object can be ANOTHER OBJECT (with its own attributes and methods)
    print(jonagold.color.upper())
    print(object.attribute1.attribute2)
    we have the attribute1 color
    we have the attribute2 .upper(). This attribute is a string method
jonagold and golden are INSTANCES of the same CLASS
    they have same attributes, color and flavor
    the attributes have different values
    
 ----------------------------------------------------------------------------   
    Theory from Openclasses
    Objects can be designed to model real-world things in software.
    Objects group together details.
    Abstraction means showing only what’s relevant and useful for the person using it.
    By hiding all the inner workings of a given object with abstraction, 
        we are able to reduce their apparent complexity.
    A plan or blueprint for an object is called a class.
    A class defines the attributes (a description), 
        the methods (what it does), and 
        the access level (who can use it) for an object.
    To create an object, you have to instantiate it. An instantiated object is called an instance of a class.
    Objects from the same class can differ in the details if they have different values for their attributes. 
        They still have to follow the class plan, though! 
    Encapsulation is the bundling together of attributes, methods, and access control in order to protect an object. 
    Objects can have attributes that are objects. 
        These objects also have their own independent blueprint (class), attributes, behaviors, and access.
    Objects communicate with one another by sending messages.
    Associating objects with other objects allows you to more easily adapt and make changes to your system.  
"""
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.1 Object-oriented Programming
    5.1.1 OOP Introduction
    5.2.2 What is Object-oriented programming?
    5.2.3 Classes and Objects in Python
EXAMPLE 1
type() function     see the CLASS of the value (or of the Variable)
dir() function      see all attributes and all methods (just names of methods)
help() function     see all attributes and all methods (methods are explained in depth)
"""
type(0) # ask Python what type is 0
# output is int

type("")
# ask Python what type is ""
# output is str

dir("")

help("")


#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.1 Object-oriented Programming
    5.1.4 Defining New Classes
the point of object oriented programming is to help define a real-world concept in a way that the computer understands
let's look at how we can represent a concept in Python code
EXAMPLE 2
How to create a class
    -class keyword then name of the class and colon 
        keyword tell the computer we are defining a new class
        class name should start with a capital letter
    -pass keyword 
        it shows that the class is empty
        the pass keyword can be used aa placeholder in any empty Python block
    -define 2 attributes of the class
        color = ""
        flavor = ""
        (we define them as strings because that is expected)
        at the moment attributes are empty
    -create one instance of the class
        instance = class()
        we assign a name to the instance 
        e.g.jonagold = Apple()
        now we have a new object for our class
        -To create an object, you have to instantiate it. 
        An instantiated object is called an instance of a class
    -provide values for the attributes
        instance.attribute1 = 
        instance.attribute2 = 
        e.g. jonagold.color = "red"
        e.g. jonagold.flavor = "sweet"
    -syntax used to access the attributes, DOT NOTATION
        retrieve the values of the attributes and display them
        print(instance.attribute1)
        e.g. print(jonagold.color)
        print(instance.attribute2)
         e.g. print(jonagold.flavor)
        DOT NOTATION Lets us access 
            the information the object may store (also called attributes)
            the abilities the object might have (also called methods)
Attention
    the attributes and methods of an object can be AN OBJECT too (with its own attributes and methods)
    print(jonagold.color.upper())
    print(object.attribute1.attribute2)
    we have the attribute1 color
    we have the attribute2 .upper(). This attribute is a string method
jonagold and golden are INSTANCES of the same CLASS
    they have same attributes, color and flavor
    the attributes have different values
"""
 
class Apple:    # CREATE CLASS NAMED APPLE
    color = ""  # PROVIDE ATTRIBUTE FOR THE CLASS
    flavor = "" # PROVIDE ATTRIBUTE FOR THE CLASS
    
jonagold = Apple()          # CREATE 1ST INSTANCE OF THE APPLE CLASS
jonagold.color = "red"      # PROVIDE VALUE FOR THE ATTRIBUTE
jonagold.flavor = "sweet"   # PROVIDE VALUE FOR THE ATTRIBUTE

print(jonagold.color)       # ACCESS ATTRIBUTE WITH DOT NOTATION
print(jonagold.flavor)      # ACCESS ATTRIBUTE WITH DOT NOTATION

print(jonagold.color.upper()) # SECOND ATTRIBUTE IS A STRING METHOD!
# USE UPPER METHOD TO TRANSFORM COLOR ATTRIBUTE VALUE INTO CAPITAL LETTERS

golden = Apple()            # CREATE 2ND INSTANCE OF THE APPLE CLASS
golden.color = "yellow"     # PROVIDE NEW VALUE FOR THE ATTRIBUTE
golden.flavor = "soft"      # PROVIDE NEW VALUE FOR THE ATTRIBUTE

print(golden.color)       # ACCESS ATTRIBUTE WITH DOT NOTATION
print(golden.flavor)

print(golden.color.upper())
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.1 Object-oriented Programming
    5.1.4 Defining New Classes
    
EXAMPLE 3
Fill in the blanks to display the poem
    Roses are red,
    violets are blue,
    honey's sweet, and so are you
"""
#%%
#   question
class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = "honey's sweet, and so are you"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

#%%
# answer
class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = "honey's sweet, and so are you"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

"""
explanation
create the  class Flower
define an attribute of the class
instantiate the object rose (rose is an instance of the class Flower, so is violet)
retrieve the values of the attributes using DOT Notation (rose.color and  violet.color)
   
we also use the format method that concatenates strings
"roses are{}". format(instance.attribute)
the placeholder {} contains the result of the DOT NOTATION
"""
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.1.5 QUIZ
EXAMPLE 4
Let’s say we have a class called Birds. 
Birds has two attributes: color and number. 
Birds also has a method called count() that counts the number of birds (adds a value to number). 
Which of the following lines of code will correctly print the number of birds?
Keep in mind, the number of birds is 0 until they are counted!
"""


"""
class is Birds
attributes of class are color and number
class Birds also has the method count(), that counts the number of birds (adds a value to the attribute "number")
instance is bluejay
1 WRONG
bluejay.number = 0
print(bluejay.number)
This will print 0, because you assigned it as 0 first.
2 WRONG
print(bluejay.number.count())
This will fail because the method count() is being called from another attribute number.
foteini: we not not apply the count method on the attribute number. 
3 CORRECT
bluejay.count()
print(bluejay.number)
We must first call the count() method, 
which will populate the number attribute, allowing us to print number and receive a correct response.
4 WRONG
print(bluejay.number)
Without calling the count() method first, the number attribute will be 0.
"""
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.1.5 QUIZ
attribute = "", we expect attribute to be text
attribute = 0, we expect attribute to be  a number?
EXAMPLE 5
Creating new instances of class objects can be a great way to keep track of values 
(called attributes, remember? Though attributes do not have to be a value, they can be strings or anything else) 
associated with the object. 
This makes it easier to add and subtract from values associated with the objects in a class.
 The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people.
 Fill in the blanks to make the code fulfill the behavior described in the quote.
"""
# “If you have an apple and I have an apple and we exchange these apples, then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person: # define new class with the name Person
    apples = 0 # provide an attribute to the class. We expect an integer as value for this attribute
    ideas = 0  # provide an attribute to the class. We expect an integer as value for this attribute

johanna = Person() # instantiate a new object OR creat an instance for the class
johanna.apples = 1 # provide a value for the attribute. (this is an instance attribute)
johanna.apples2 = 0 # provide a value for the attribute. (this is an instance attribute). THE VALUE WILL BE PRODUCED BY THE FUNCTION EXCHANGE APPLES

johanna.ideas = 1 # provide a value for the attribute. (this is an instance attribute)
johanna.ideas2 = 0 # provide a value for the attribute. (this is an instance attribute). THE VALUE WILL BE PRODUCED BY THE FUNCTION EXCHANGE IDEAS

martin = Person() # instantiate a new object OR creat an instance for the class
martin.apples = 2  # provide a value for the attribute. (this is an instance attribute)
martin.apples2 = 0  # provide a value for the attribute. (this is an instance attribute). THE VALUE WILL BE PRODUCED BY THE FUNCTION EXCHANGE APPLES

martin.ideas = 1  # provide a value for the attribute. (this is an instance attribute)
martin.ideas2 = 0  # provide a value for the attribute. (this is an instance attribute)THE VALUE WILL BE PRODUCED BY THE FUNCTION EXCHANGE IDEAS

def exchange_apples(johanna, martin):
  #exchange the apples
  johanna.apples2 = martin.apples
  martin.apples2 = johanna.apples
  
  return johanna.apples2, martin.apples2
    
def exchange_ideas(johanna, martin):
  # share the ideas
  johanna.ideas2 = johanna.ideas + martin.ideas
  martin.ideas2 = martin.ideas + johanna.ideas
  
  return johanna.ideas2, martin.ideas2

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples2, martin.apples2))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas2, martin.ideas2))


"""
Did you properly add or equivalate the attributes
of both instances of the Person() class?
"""
#%%
# question
class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
  #"you" and "me" will exchange ALL our apples with one another
  __
  return you.apples, me.apples
    
def exchange_ideas(you, me):
  #"you" and "me" will share our ideas with one another
  you.ideas __
  me.ideas __
  return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.1 Instance Methods
THEORY
we use methods to get the objects to do something
for objects to perform actions they need methods
a method is a function that performs on a single instance of an object
methods are just functions that belong to a specific class
           
METHODS
    they are functions that operate on the Attributes of a specific instance (object) of a class
    
the 'self' parameter REPRESENTS the instance that the method is executed on
the method is applied to all instances of the class
the method uses the attribute value of the INSTANCE, not of the CLASS
The method takes into account the value of the instance attribute, not the class attribute
INSTANCE VARIABLES
they are variables that have different values for different instances of the same class
CONSTRUCTOR METHOD
    def __init__(self, + attributes):
    we define attributes with their values the moment we create the instance with the constructor method.
    The CONSTRUCTOR METHOD is always called __init__
    it is a special method
    (methods that start and end with two underscores, are special methods)
Other special methods
        str(), string method to convert an object to a string
        try to print the instance jonagold:
        when we try to print(jonagold) we get the message <__main__.Apple object at 0x0000014F85433D48>
        Python uses the default method that prints the position where the object is stored in the computer's memory. 
        prints position of the object in the computers memory
        -again, try to print the instance jonagold
        now, we have used an additional special method:
            __str__
        then we created the instance of the class
        we provided values for the attributes of the instance within the parenthesis of the class
        the result is a friendly message without numbers/characters
The function help()
    to find information on built-in classes and methods
    to find information for our OWN classes and methods!
    
    The help () function tells us about
    the attributes of the class 
    the methods of the class
    !
    we can add docstrings in order to receive MORE information when using the help()
This information is too little, so we will use DOCSTRINGS
How to use DOCSTRINGS
    a brief text that explains what something does
    we can incorporate a docstring to the function
    be careful to indent the docstring under the function/method/class
    when we use help(), we can see this docstring!
    when writing your code, add docstrings to explain your functions, classes, and methods to help yourself and others
Classes and Instances
    Classes define the behavior of all instances of a specific class.
    Each variable of a specific class is an instance or object.
    Objects can have attributes, which store information about the object.
    You can make objects do work by calling their methods.
    The first parameter of the methods (self) represents the current instance.
    Methods are just like functions, but they can only be used through a class.
JUPYTER NOTEBOOKS
    A Jupyter Notebook is a special kind of document that can contain pieces of programming code.
    We can execute these pieces of code inside the notebooks one piece at a time, 
    and the notebooks can also contain other things like text, images, interactive widgets, and a whole lot more.
    
    Jupyter Notebooks let us edit and run our code in the web browser.
    The difference is that we can add explanations and between the code, and also 
    the pieces of code are related to each other. 
Jupyter Notebooks are an open-source technology and you could even run it locally on your computer.
EXAMPLE 1
"""
class Piglet: # create the class
    pass        # pass keyword, it shows that the class is empty
        
hamlet = Piglet() #create an instance of the class / instantiate an object

#%%
"""
Let's add a method to our class
"""
class Piglet: # create a class
    def speak(self): # create a method inside the class
        print("oink oink") #display this when the above method is applied to all instances of the class

hamlet = Piglet() # create the instance hamlet of the class piglet
hamlet.speak()      # instance.method. We call the method to operate for this instance

# output is oink oink    
#%%        
"""
we define a method with the def keyword (just like we do for a function)
the line is indented to the right, INSIDE the class
that's how we define a function as a method of the class
this function receives a parameter called 'self'
the 'self' parameter REPRESENTS the instance that the method is executed on
the method is applied to all instances of the class and produces same result
"""
#%%
class Piglet: #create a class
    name = "piglet" # define an attribute of the class
                    # this attribute is the name and we have given it the value "piglet"
                    # name is the Variable and piglet is the value
                    # we can change this value later, we just initialized it now
    def speak(self): #create a method for all instances of the class
                        # the parameter self, actually represents the instamce on which the method will be applied
        print("Oink! I'm {}! Oink!".format(self.name))
        
hamlet = Piglet() # create an instance of the class
hamlet.name = "Hamlet" # provide value for the attribute (instance attribute)
hamlet.speak() # we call the method speak, fot his instance

# output is Oink! I'm Hamlet! Oink!
#%%
"""
format method allows us to concatenate string with the output
of a function which is in {}. 
the format method accesses the name from the attribute of the class
See that the method used the name that we provided for the INSTANCE
"""
#%%
class Piglet: #create a class
    name = "piglet" # define an attribute of the class
                    # this attribute is the name and we have given it the value "piglet"
                    # name is the Variable and piglet is the value
                    # we can change this value later, we just initialized it now
    def speak(self): #create a method for all instances of the class
                        # the parameter self, acrually represents the instamce on which the method will be applied
        print("Oink! I'm {}! Oink!".format(self.name)) # dot notation for the attribute 'name' of the instance
        
hamlet = Piglet() # create an instance of the class
hamlet.name = "Hamlet" # provide value for the attribute (instance attribute)
hamlet.speak() # we call the method speak, for this instance

petunia = Piglet() # create another instance of the class
petunia.name = "Petunia"
petunia.speak()

# Output is 
#Oink! I'm Hamlet! Oink!
#Oink! I'm Petunia! Oink!
#%%
"""
INSTANCE VARIABLES
they are variables that have different values for different instances of the same class
e.g the Variable "name" in this example
"""
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.1 Instance Methods
EXAMPLE 2
methods are just functions that belong to a specific class, so they can work as any other function.
 So they can receive more parameters and return values if needed. 
 Let's check out what a method returning a value looks like.
convert pig years to human years
piggy is 2 years old in human years
how old is she in pig years?
See that, when the attribute value changes for the instance,
then the return value of the method changes too.
The method takes into account the value of the instance attribute, not the class attribute
"""

class Piglet: # create the class
    years = 0 # define an attribute of the class (with or eithout value)
    def pig_years(self): # create a method that will be applied to every instance of the class
        return self.years*18 # dot notation to retrieve the value of the attribute YEARS from the instance
                                # we get the value and then multiply it to 18, to convert human years into pig years

piggy = Piglet() # create an instance of the class
print(piggy.pig_years()) # display the application of the method on the instance
# output is 0, because we have given a value for the Variable years in the body of the class

piggy.years = 2 # we define the value of the attribute of the instance
print(piggy.pig_years()) # again, display the application of the method on the instance
# output is 2x18=36

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.1 Instance Methods
EXAMPLE 3
Create a Dog class with dog_years based on the Piglet class shown before
(one human year is about 7 dog years).
"""
# question
class Dog:
  years = 0
  __
    
fido=Dog()
fido.years=3
print(fido.dog_years())

#%%
# answer
class Dog:
  years = 0
  def dog_years(self):
      return self.years*7
    
fido=Dog()
fido.years=3
print(fido.dog_years())

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.2 Constructors and Other Special Methods
EXAMPLE 4
Use the CONSTRUCTOR METHOD
we can create classes and then define attributes with empty or default values.
this works but it is not ideal
when creating an instance, we have to define its attribute with a value and we might forget!
so, we will define attributes with values the moment we create the instance with 
the constructor method.
The CONSTRUCTOR METHOD is always called __init__
methods that start and end with two underscores, are special methods
"""
class Apple:
    def __init__(self, color, flavor): # we define the CONSTRUCTOR METHOD
        self.color = color # dot notation. retrieves value of the instance attribute
        self.flavor = flavor
        
jonagold = Apple("red", "sweet") # create the instance jonagold of the class Apple
                                # the class has 2 parameters!
print(jonagold.color) # display dot notation, retrieve value of the attribute color for the instance jonagold

#%%
"""
The constructor method __init__,
receives 3 parameters: the instance, color and flavor
"""

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.2 Constructors and Other Special Methods
EXAMPLE 5
In this code, there's a Person class that has an attribute name, which gets set when constructing the object.
Fill in the blanks so that 
1) when an instance of the class is created, the attribute gets set correctly, and
2) when the greeting() method is called, the greeting states the assigned name.
"""
# question
class Person:
    def __init__(self, name):
        self.name = ___
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ___ 

# Create a new instance with a name of your choice
some_person = ___  
# Call the greeting method
print(some_person.___)
#%%
# answer
class Person: # create the class
    def __init__(self, name): # use the constructor method. 2 parameters: self = instance and name a class attribute
                                # the constructor method 
        self.name = name # dot notation, accesses the value of the instance attribute.
                            # we set the value of the instance attribute to be "name"
    def greeting(self): # we create the function 'greeting' which has one parameter, the instance
        # Should return "hi, my name is " followed by the name of the Person.
        return ("hi, my name is {}".format(self.name)) # the function 'greeting' returns a message with the help of the format method
                                                        # the format method has 2 parameters, the instance and the attribute 'name'

# Create a new instance with a name of your choice
some_person = Person("Foteini") # here we create the instance 'some_person' AND give a parameter to the class
                                # the parameter is a value for the attribute 'name'
# Call the greeting method
print(some_person.greeting()) # here we call the 'greeting' method for the instance 'some_person'

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.2 Constructors and Other Special Methods
EXAMPLE 6
Other special methods
    - str(), string method to convert an object to a string
"""
class Apple:
    def __init__(self, color, flavor): # we define the CONSTRUCTOR METHOD
        self.color = color # dot notation. retrieves value of the instance attribute
        self.flavor = flavor
        
jonagold = Apple("red", "sweet") # create the instance jonagold of the class Apple
                                # the class has 2 parameters!
print(jonagold)

#%%
"""
try to print the instance jonagold
when we try to print(jonagold) we get the message
<__main__.Apple object at 0x0000014F85433D48>
this means:
Python uses the default method that prints 
the position where the object is stored in the computer's memory. 
prints position of the object in the computers memory
"""
#%%
class Apple:
    def __init__(self, color, flavor): # we define the CONSTRUCTOR METHOD
        self.color = color # dot notation. retrieves value of the instance attribute
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)

# output is This apple is red and its flavor is sweet
"""
again, try to print the instance jonagold
now, we have used an additional special method:
    __str__
then we created the instance of the class
we provided values for the attributes of the instance within the parenthesis of the class
the result is a friendly message without numbers/characters
"""

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.3 Documenting Functions, Classes, and Methods
EXAMPLE 7
help(), 
to find information on built-in classes and methods
to find information for our OWN classes and methods!
docstring
a brief text that explains what something does
"""
class Apple:
    def __init__(self, color, flavor): # we define the CONSTRUCTOR METHOD
        self.color = color # dot notation. retrieves value of the instance attribute
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

help(Apple)

#%%
"""
we ask Python information about the class Apple that we constructed
it tells us 
the attributes of the class (color, flavor)
the methods of the class
    __init__ (constructor method)
    Initializes self (self parameter represents the instance)
    __str__ (conversion to string method)
    Returns the string of self (self parameter represents the instance)
This information is too little, so we will use DOCSTRINGS
"""
#%%
def to_seconds(hours, minutes, seconds):   
    """Returns the amount of seconds in the given hours,minutes,seconds"""
    return hours*3600+minutes*60+seconds

help(to_seconds)

"""
we have incorporated a docstring to the function
be careful to indent the docstring under the method it is documenting
when we use help(to_seconds), we can see this docstring!
we can add docstrings to classes and methods too
when writing your code, add docstrings to explain your functions, classes, and methods
"""
#%%
class Piglet: 
    years = 0 
    name = ""
    def speak(self): 
        """Outputs a message including the name of the piglet """
        print("Oink! I'm {}! Oink!".format(self.name))
    def pig_years(self):
        """Converts the current age to equivalent pig years"""
        return self.years*18

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.3 Documenting Functions, Classes, and Methods
EXAMPLE 8
add a docstring to the greeting method. 
 “Outputs a message with the name of the person”.
Then use the help function to see that docstring
"""
# question
class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    ___
    print("Hello! My name is {name}.".format(name=self.name)) 

help(___)
#%%
# answer
class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person) # use help() for the whole CLASS

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.4 Classes and Methods Cheat Sheet
EXAMPLE 8
Defining classes and methods
    class ClassName:
    def method_name(self, other_parameters):
        body_of_method
Classes and Instances
    Classes define the behavior of all instances of a specific class.
    Each variable of a specific class is an instance or object.
    Objects can have attributes, which store information about the object.
    You can make objects do work by calling their methods.
    The first parameter of the methods (self) represents the current instance.
    Methods are just like functions, but they can only be used through a class.
Special methods
    Special methods start and end with __.
    Special methods have specific names, like
    __init__ for the constructor or
    __str__ for the conversion to string.
Documenting classes, methods and functions
    You can add documentation to classes, methods, and functions 
    by using docstrings right after the definition. 
    Like this:
        
    class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
    def function_name(parameters):
    """Documentation for the function."""
    body_of_function


"""
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.5 About Jupyter Notebooks

EXAMPLE 9

JUPYTER NOTEBOOKS
A Jupyter Notebook is a special kind of document that can contain pieces of programming code.
We can execute these pieces of code inside the notebooks one piece at a time, 
and the notebooks can also contain other things like text, images, interactive widgets, and a whole lot more.

Jupyter Notebooks let us edit and run our code in the web browser.
The difference is that we can add explanations and between the code, and also 
the pieces of code are related to each other. 

Jupyter Notebooks are an open-source technology and you could even run it locally on your computer. 
"""
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.6 Help with Jupyter Notebooks
EXAMPLE 10
Help with Jupyter Notebooks
We've aimed to make our Jupyter notebooks easy to use. But, if you get stuck, you can find more information here.
https://learner.coursera.help/hc/en-us/articles/360004995312-Solve-problems-with-Jupyter-Notebooks
If you still need help, the discussion forums are a great place to find it! Use the forums to ask questions and source answers from your fellow learners.
If you want to learn more about Jupyter Notebooks as a technology, check out these resources:
Jupyter Notebook Tutorial, by datacamp.com
How to use Jupyter Notebooks, by codeacademy.com
Teaching and Learning with Jupyter, by university professors using Jupyter
"""

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.2 Classes and Methods
5.2.7 QUIZ on Jupyter Notebooks
EXAMPLE 11
"""

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current = self.current + 1
               
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > -1:
            self.current = self.current - 1
                    
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        
    def __str__(self):
        return "Current floor: {}".format(self.current)
        
    

elevator = Elevator(-1, 10, 0)

elevator.up() 
elevator.current #should output 1

#%%
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current = self.current + 1
               
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > -1:
            self.current = self.current - 1
                    
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        
    def __str__(self):
        return "Current floor: {}".format(self.current)
        
elevator.down() 
elevator.current #should output 0

#%%
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current = self.current + 1
               
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > -1:
            self.current = self.current - 1
                    
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        
    def __str__(self):
        return "Current floor: {}".format(self.current)

elevator.go_to(10) 
elevator.current #should output 10

#%%
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current = self.current + 1
               
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > -1:
            self.current = self.current - 1
                    
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        
    def __str__(self):
        return "Current floor: {}".format(self.current)

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

#%%
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current = self.current + 1
               
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > -1:
            self.current = self.current - 1
                    
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        
    def __str__(self):
        return "Current floor: {}".format(self.current)

elevator.go_to(5)
print(elevator) #For example, in the 5th floor it should say "Current floor: 5"

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.3 Code re-Use
5.3.1 Inheritance
THEORY
-inheritance in OOP = objects have an ancestry
-The principle of inheritance let's a programmer build relationships between concepts and group them together. 
 In particular, this allows us to reduce code duplication by generalizing our code
 
-With the inheritance technique, we can use the parent class to store information that applies 
    to all instances of the child classes and keep specific attributes stored in the child classes
- with the inheritance technique:
        in the parent class:we provide attributes/methods applicable to all instances of the child classes
        in the child classes: we provide attributes/methods that are specific to the child class
we can create a child class Cat within a parent class Feline
    class cat is the child of class feline
    class Feline:
        class Cat(Feline):
    In Python, we use parentheses in the class declaration to show an inheritance relationship.
        
child classes inherit attributes and methods from the parent class
INHERITANCE LETS YOU REUSE CODE WRITTEN FOR ONE CLASS IN OTHER CLASSES.
EXAMPLE 1
Inheritance Technique
create a parent class Fruit which contains other classes, like Apple and Grape
class Apple and class Grape, have the same constructor method, of their parent class Fruits
With the inheritance technique, we can use the fruit class to store information that applies to all kinds of fruit, 
and keep apple or grape specific attributes in their own classes. 
-create the class "Fruit"
-use the constructor method to define attributes with their values at the time the instance is created
    we define the attributes and their values of the instances
    we initialize the values of the attributes of the instances?
- we create the class "Apple" which is the child of the class "Fruits"
    the class "Apple" is empty, as we useed the "pass" keyword
- we create the class "Grape" which is the child of the class "Fruits"
    the class "Grape" is empty, as we useed the "pass" keyword
- the classes Apple and Grape are siblings, and children of the class Fruits
- we create the instance "granny_smith" under the class Apple
    we provide 2 parameters for the class Apple, color=green and flavor=tart
- we create the instance "carnelian" under the class Apple
    we provide 2 parameters for the class Apple, color=purple and flavor = sweet
- we display the attribute flavor for the instance granny_smith, with dot notation
-we display the attribute color for the instance carnelian, with dot notation
"""

class Fruit:
    def __init__(self, color, flavor):
        
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)    
print(carnelian.color)

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.3 Code re-Use
5.3.1 Inheritance
EXAMPLE 2
How does inheritance work
parent class Animal
we provide sound as an attribute
with the constructor method, we define the attribute name and its value 
    that will be given to the instance once it is created
child classes inherit attributes and methods from the parent class
child class Piglet
we provide the value for the attribute sound
everything else( attribute :name") is inherited from parent class!
-we create the class "Animal"
-we provide an attribute to this class, sound = "", this attribute is a string
-we use the constructor method to assign values to attributes of instances
    we have one attribute called name
-we create the method "speak" to print a message with the help of the format method
    the format method takes 2 parameters, name = self.name and sound = self.sound
    instance.name, dot notation, retrieves the value of attribute "name" of the instance 
    instance.sound, dot notation, retrieves the value of attribute "sound" of the instance
    
-we create the class "Piglet", which is the child of the class "Animal"
-we provide an attribute with its value to this class (Piglet)
    sound = "Oink!"
-we create the instance "hamlet" under the class "Piglet" and provide the parameter of name = "Hamlet" for the class
-we call the method speak for this instance
-we create the class "Cow", child of the class "Animal"
-we provide an attribute with its value to this class (Cow)
    sound = "Mooo
-we create the instance "milky" under the class "Cow" and provide the parameter of name = "Milky White"
-we call the method speak for this instance 
"""

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        """the method speak, prints the following message"""
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak() # here we call the method speak, for the instance hamlet
# output is Oink! I'm Hamlet! Oink!

class Cow(Animal):
    sound = "Moooo"

milky = Cow("Milky White")
milky.speak()
# output is Moooo I'm Milky White! Moooo

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.3 Code re-Use
5.3.1 Inheritance
EXAMPLE 3
Let’s create a new class together and inherit from it. 
Below we have a base class called Clothing. 
Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. 
Fill in the blanks to make it work properly.
"""
#%%
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.___,self.___))
			
class Shirt(___):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

#%%
# ANSWER
class Clothing: # create parent class
  material = "" # provide attribute to parent class
  def __init__(self,name): #use constructor method to give attribute and value to instances when created
    self.name = name
  def checkmaterial(self):# use method "checkmaterial" to print a message with format method
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):# create child class
  material="Cotton" # provide value for the attribute outside the constructor method attributes

polo = Shirt("Polo") #create instance and provide attribute "name" for the class
polo.checkmaterial()

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.3 Code re-Use
5.3.2 Composition
EXAMPLE 4
Inheritance creates an ancestry for our objects
How to examine the ancestry of an object
    -with the IS A rule, we can find who is the parent class
        e.g. class Apple and class Fruits, jonagold belongs to Fruits
        e.g. class Piglet and class Animals, hamlet belongs to Animal
    -for classes that do not have a parent -child relationship.....++++++
class Package
    -represents a software package which can be installed on every machine
    in our network
    -this class has a lot of information on the software (name, version,size).We are interested in name and size
class Repository
    -represents all the packages that we have available for installation internally
    -in this class we want to know how many packages there are
    and what is the total size of all the packages
    -the class Repository contains packages
    -to model this with code, the class Repository will have an attribute 
        (list or dictionary containing instances of the class Package )
So for this scenario, we'll make use of the code in the other classes by calling their methods. 
This is what's called composition. 
SO
we will create the class "Repository"
with constructor method, we will assign values to attributes of instances
    in reality, we will provide the attribute "packages" define it as a dictionary and the value is empty for now
    Key: name of package instance
    and Value: size of package instance, in bytes
    instance of class Package is called package
    dictionary is named packages, each element of the dictionary is a package (instance of class Package)
    Key = name
    Value = size
Why provide this attribute with the constructor method instead of providing it directly under the class?
-when providing the attribute under the class, the attribute gets assigned to ALL instances
    1st way to provide attributes to instances
    create attribute at a class level
    provide attribute when class is created
    attributes are assigned to all instances
-when providing the attribute with the constructor method, we assign the attribute to the instance at the time the instance is created
    2nd way to provide attributes to instances
    create attribute at an instance level
    provide attribute when instance is created
    attributes are assigned to certain instances
    
    PLEASE PROVIDE ATTRIBUTE USING THE CONSTRUCTOR <WHEN> THE ATTRIBUTE IS MUTABLE ?
    (This happens with all attributes that are mutable, 
    because when we modify immutable attribute, we're not replacing a value with another, we're changing the contents of the original attribute.)
In this example, the attribute "packages" is a dictionary which is mutable(changeable)
    we will be modifying the dictionary's contents by adding and removing elements from it
    if we created it at the class level then all instances of the class Repository would use the SAME dictionary
    and elements added or removed would affect all instances at the same time
SO, we use the constructor to provide the attribute to the instances of the class Repository, 
        because we want to provide this attribute at Repository instance level
        because this attribute is a dictionary of instances of the class Package
        the dictionary is mutable (instances of the class Package may change and so the contents of the dictionary)
        and we want each instance of the class Repository to have as an attribute its own personalized dictionary
        instances of the class Repository depend on the instances of the class Package
        
        how do instances of the class Repository can be different from one another????
        
ALWAYS INITIALIZE MUTABLE ATTRIBUTES IN THE CONSTRUCTOR
packages have a size attribute that holds the size in bytes that the software package requires
    so how can we calculate the size of the whole repository?
    we will iterate over all packages and add their sizes
"""
class Repository:
    def __init__(self): # self represents an instance of the class Repository
                        # with constructor, we provide the instances with the attribute packages when they are created
        """initializes the value for the mutable attribute 'packages' """
        self.packages = {} # initialize the value of the attribute 'packages'
                            # the attribute 'packages' is an empty dictionary
                            # 'packages' = dictionary = {'package1': '100', 'package2': '200', etc}
                            # this dictionary will contain instances of the class 'Package', 
                            # Key  = name of package and Value = size of package
                            # create attribute at an instance level
    def add_package(self, package): # package is the instance of the class Package
        self.packages[package.name] = package # dictionary[key]=value. Here we create elements to add to the empty dictionary
                                                # each element of the dictionary is a package (Key=name and Value=size)
# write a similar method that removes packages 
    def total_size(self):
        result_sum = 0 # result sums up the sizes, we INITIALIZE the value here
        for package in self.packages.values(): # we care only for the values not the keys of the dictionary
            result_sum = result_sum + package.size # dot notation, we get the value that is the size of the package
        return result_sum
        
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.3 Code re-Use
5.3.2 Composition
EXAMPLE 5   
Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock.
When you’re finished, the script should add up to 10 cotton Polo shirts.
 
"""
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]} #dictionary, key is a string, value is a list
                                                  # this is an attribute on class level, applies to ALL instances of the parent class
                                                  # all Value in this dictionary are empty lists which will be filled later!
  def __init__(self,name):
    material = "" # here we provide an attribute at instance level, so it will be applied on certain instances not all
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name) # we append to a list. Which is the list? it is the list next to name. dictionary[key]=value, so dictionary[name]= []
    Clothing.stock['material'].append(self.material)# Clothing.stock['material'] is the empty list []
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0 # 
    n=0
    for item in Clothing.stock['material']: #iterate over the list next to material! dictionary[key]=value
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing): # we create the child class 'shirt', under the parent class 'Clothing'
  material="Cotton"     # we provide the attribute and its value for the instances of the class 'shirt'
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo") # we create the instance of the class 'shirt'. we provide the attribute name via constructor
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4) # we call the method 'add_item' for the instance 'polo'. The method has 3 parameters
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton") # we call the method'Stock_by_Material for the instance 'polo'
print(current_stock)

"""
You successfully used composition to reuse the
Clothing.stock attribute and stock_by_material() function of
the Clothing class to take stock of the Cotton shirts!
"""


#%%
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['___']:
      if item == material:
        count += Clothing.___['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.3 Code re-Use
5.3.3 Python Modules
EXAMPLE 5 
 Python provides an abstraction called a module.
 Modules can be used to organize functions, classes, and other data together in a structured way. 
Python already comes with a bunch of ready-to-use modules. 
All these modules are contained in a group called the Python standard library.
IMPORT keyword to import the RANDOM module
This module is useful for generating random numbers or making random choices.
We must use the import keyword to import the module before it can be used.
How to call a function provided by a module?
    module.function()
    random.randint(1,10)
"""

import random # import the module random

random.randint(1, 10) # use the function randint that is provided by the module random
                        # this function takes 2 parameters and generates a random number which lies between these 2 parameters
# 7
random.randint(1, 10)
# 2
random.randint(1, 10)
# 8
#%%
import datetime
now = datetime.datetime.now()
print(type(now))
# <class 'datetime.datetime'>

"""
--module is datetime
--function is now()
--why do we have datetime twice?
    -the module datetime, provides a class datetime
    -then, the now () method (not function as it is a function of a class),
    generates an instance of the class datetime for the current time
"""
#%%
import datetime
now = datetime.datetime.now()
# module.class.method
print(now)
# 2020-02-22 03:32:58.029594
now.year # access the instance through its attributes and methods
            # here we access the 
# 2020

"""
The datetime module provides more classes than the datetime class
For example the class timedelta to calculate a date in the future or past
"""
#%%%
import datetime
now = datetime.datetime.now()

print(now + datetime.timedelta(days = 28))
# 2020-03-21 03:40:46.041619

"""
we are adding two instances
datetime.datetime.now(), module.class.method, calculates today's date
datetime.timedelta(days = 28), module.class.method, adding 28 days to today's date
"""

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.3 Code re-Use
5.3.4 Supplemental Reading for Code Reuse
EXAMPLE 6
Supplemental Reading for Code Reuse
The official Python documentation lists all the modules included in the standard library. 
It even has a turtle in it...
Pypi is the Python repository and index of an impressive number of modules developed by 
Python programmers around the world.
https://pypi.org
""" 
#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.3 Code re-Use
5.3.5 QUIZ
EXAMPLE 7
"""
class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

class Snake(Animal):
    category = "reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category  should be 2

#%%
class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

class Snake(Animal):
    category = "reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.______.values():
            if ______ == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category

#%%
"""
Google's Crash course on Python, Week 5: Object-oriented Programming (OOP)
5.4 FINAL QUIZ
In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then
a load balancer that ensures that there are enough servers to serve those connections.
To represent the servers that are taking care of the connections, we'll use a Server class. 
Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the 
server. 
For our simulation, each connection creates a random amount of load in the server, between 1 and 10.
fill in the missing parts for the add_connection and load methods to print a number different than zero.
As the load is calculated randomly, this number should be different each time the code is executed.
Hint: Recall that you can iterate through the values of your connections dictionary just as you would any sequence.
"""
#Begin Portion 1#
import random # we import the module 'random'

class Server: # we create the class 'Server'
    def __init__(self): # the constructor creates attribute assigned to the instance when the instance is created
        """Creates a new server instance, with no active connections."""
        self.connections = {} # attribute 'connections' is an empty dictionary . This is a mutable attribute and we initialize it here
# dictionary:  Key = connection_id and Value = connection_load?
        
    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1 # each connection creates a random amount of load in the server, between 1 and 10
        self.connections[connection_id] = connection_load # dictionary method! Creates a dictionary
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        del self.connections[connection_id]
        """Closes a connection on this server."""
        # Remove the connection from the dictionary

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for connection_load in self.connections.values():
            total = total + connection_load
        # Add up the load for each of the connections
        # add up the value of the dictionary for all elements of the dictionary
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#
# Now run the following cell to create a Server instance and add a connection to it, then check the load:
server = Server() #create the instance 'server' under the class "Server"
server.add_connection("192.168.1.1") # execute the method "add connection" for the instance "server"

print(server.load()) # execute the method "load" for the instance "server"
# the add_connection method prints a random number between 1 and 10 e.g 5.884808002135085
#each connection creates a random amount of load in the server, between 1 and 10.
server.close_connection("192.168.1.1") # execute the method "close connection" for the instance "server"
print(server.load())


# the close_connection method  prints 0



"""
Alright, we now have a basic implementation of the server class. 
Let's look at the basic LoadBalancing class. 
the class LoadBalancing ensures that there are enough servers to serve the connections 
This class will start with only one server available. 
When a connection gets added, it will randomly select a server to serve that connection,
and then pass on the connection to the server. 
The LoadBalancing class also needs to keep track of the ongoing connections to be able to close them. 
This is the basic structure:
"""

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {} # empty dictionary, contains Key = connection_id and Value = connection_load  as before?
        self.servers = [Server()] # list 
                                    # the elements of this list are instances of the class Server. Instance is 'server'

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers) # with random.choice(), we select an element of the list self.servers 
                                                # the element we selected is a server, instance of the class Server
         
        self.connections[connection_id] = server # Key = connection_id and Value = server
        # Add the connection with the selected server, to the dictionary
        
        server.add_connection(connection_id)
        # Add the connection to the server (add to a list with append)
        
        print(self.connections)


    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        result = 0
        for server in self.connections.values():
            result = result + server.load()
        return (result / len(self.servers))

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        pass

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#
l = LoadBalancing() #create instance 1 under the class LoadBalancing
l.add_connection("fdca:83d2::f20d") # execute the method add_connection with the parameter fdca:83d2::f20d for this instance with 
print(l.avg_load())
