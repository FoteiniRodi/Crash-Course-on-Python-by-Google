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
