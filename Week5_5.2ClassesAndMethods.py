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
