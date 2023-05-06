# References in Python

#Pass by value if its immutable
#Pass by reference if its mutable
# def func(i):
#     #i is a 'copy' so when we pass in 'val', it will not get the 'reference' of val
#     i = 200

# my_list = [1, 2, 3] #In python this is mutable (lists, dictionaries, sets, classes)

# val = 3 #This is immutable (ints, characters, True/Flase)

# #We call 'func' and pass in 'val' (immutable) but because it's immutable it will pass in the value and copy it
# #to the function which means we are not modifying anything in 'val' variable
# func(val)

# #Value 'val' will not be modified if its an immutable value because its passed as 'value'
# #But when we changed val to a list it was able to change the value because we passed by 'reference'
# print(val)

# # =================

# #Now we are making another variable equal to another list
# #But we are actually making 'my_list_2' point to the same reference/memory to 'my_list'
# my_list_2 = my_list

# #Appending my_list_2 would affect my_list_2 and my_list because they are pointing to the same memory
# my_list_2.append(7)

# #Print the values (they are the same)
# print(my_list_2)
# print(my_list)

#They share the same memory address
#print(id(my_list), id(my_list_2))

# # =======

# #Classes are also mutable which means we pass by reference
# class MyClass:
#     #Constructor of class
#     def __init__(self, x):
#         self.x = x

# #Create a function that takes in an object (our class), and modifies the 'x' value
# def func2(obj):
#     obj.x = 42

# my_obj = MyClass(10) #Initialize the class
# func2(my_obj) #Pass in the object/class 'my_obj' to 'func2()'
# print(my_obj.x) #Because classes pass by reference the 'x' value is changed via the reference to the object

#=== Try/Except/Finally ===

#When we want to an error with 'try/except' you pass in the code within the 'try' block.
#If there are any errors raised within the try block then the 'except' will be raised
#'finally' is just to be called no matter we have an error or no error
try:
    val = 3 / 0
    print(val)
except ZeroDivisionError: #Handle 'ZeroDivisionError'
    print('Cannot divide by zero')
except TypeError: #Handle 'TypeError' 
    print('Raised a type error')
except: #This is for all the exceptions to handle
    print('Error')
finally:
    print('Finally')


# Try/Except question
# Write a small program where it takes a user input and the user input is then used as a divisor to
# the number '100' as the dividend (100 / <user-input>)
# Handle the exceptions raised by the error (so if the user inputs/divides by 0 it shold print:
#'Cannot divide by zero'. 
# If the user inputs a non-integer value it should print 
# 'Value is not a number!'
