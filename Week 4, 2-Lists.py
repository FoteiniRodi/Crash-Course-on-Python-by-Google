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
