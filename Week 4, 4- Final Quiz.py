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

