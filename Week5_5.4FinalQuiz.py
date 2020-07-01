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


