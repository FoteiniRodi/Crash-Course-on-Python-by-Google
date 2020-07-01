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
