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
