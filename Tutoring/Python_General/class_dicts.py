#Question 1
# Create a class named Person that takes in a dictionary in the constructor 
# for the same of this a dictionary has already been provided to you named 'people'

# In this Person class, I want you to define a method called 'personInfo()' which reads the
# values in the people dictionary and print their information

#Define class here

#Create another class called Employee, which inherits from the Person class. The Employee's constructor should
#inherit from the Person's constructor as well as have its own variable known as 'company' passed.
#Define employeeInfo() which should print the names, age and city as well as the company they work in.

class Person:
    def __init__(self, people):
        self.people = people

    def personInfo(self):
        for person in self.people.values():
            print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
        
        #  for person in self.people:
        #     print(f"Name: {self.people[person]['name']}, Age: {self.people[person]['age']}, City: {self.people[person]['city']}")

people = {
    "Alice": {"name": "Alice", "age": 30, "city": "New York"},
    "Bob": {"name": "Bob", "age": 25, "city": "San Francisco"},
    "Charlie": {"name": "Charlie", "age": 35, "city": "Chicago"}
}

# Use this for printing/calling the class method
persons = Person(people)
persons.personInfo()

#Question 2

#import math
#Use this import for math (math.pi will give you PI value)
#Create a parent class called 'Shape' which takes in the following attributes/variables: color, get_color()
#Create Rectangle child class (from Shape) which should have: color, width, height and get_area()
#Create a Circle child class (from Shape) which should have: color, radius, get_area()

#In case you forgotten area of circle: math.pi * radius ** 2

#Here is a set of defined shapes stored in a list.
# shapes = [
#     Rectangle("red", 5, 10),
#     Circle("blue", 3),
#     Rectangle("green", 7, 4),
#     Circle("yellow", 2.5)
# ]

#Use this list and calculate the area for all the shapes with their get_area() method
