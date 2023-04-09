
#Python's built-in dictionary methods
#.clear() -> clears dictionary
#.get(<key>) -> gets value from key
#.items() -> returns tuples of dictionary
#.keys() -> list of keys
#.values() -> list of values
#.pop(<key>) -> pop / get rid of the value at specified key
#.popitem() -> pop / get rid of last item in dictionary
#.update(<dictionary>) -> will append the dictionary specified to the current dictionary


#list() -> convert to list if you cannot get the value from a dictionary method. Use this to convert to 
#standard Python list

#======================
# #Dictionary initialization

#General form when specifying -> #Key : #Value
# dictionary = {
#     'a' : 'b',
#     'c' : 3,
# }

#When you want to access an element at a key value you would do it as if you were accessing an
#element via an array but with the key value specified

#print(dictionary)

#This should print 'b'. This is because we are getting it from key value 'c' from dictionary
#print(dictionary['c'])

#======================
# #String splitting

# string = "Hello world"

# delimited = string.split(' ') #You can change the delimite within the brackets

# print(delimited[0])


#======================
#Tuples

#tuples = ("hello", (12,), True, 'c')

#print(tuples[1])

#======================
# #Read scores function (parsing arguments)

# def readScores(scores):
#     f = open(scores, 'r')
#     lines = f.readlines() #Returns array of lines
#     print(lines)


# readScores("scores.txt")

#======================
# #Iterating through list value in dictionary

dictionary = {
    'list' : ['a','b','c','d'],
    'list1' : ['e','f','g','h']
}

# #Iterate through all the keys in the dictionary
# for j in dictionary:
#     #Iterate through all the elements in value list
#     for i in dictionary[j]:
#         #Print the element from list
#          print(f'- {i}')

#======================
#List of Dictionaries
                        #0           #1           #2
# list_of_dictionaries = [{'a' : 'b'}, {'c' : 'd'}, {'e' : 'f'}]
#                         #list_of_dictionaries[1] -> {'c' : 'd'}
#                         #list_of_dictionaries[1]['c'] -> d

# print(list_of_dictionaries[0]['a'])

#======================
#Array sort

# arr = [3,8,2,10,55,22]

# #Should sort the array without any return (modifies the actual array we're using)
# arr.sort()

# #Should return the sorted array with 'sorted()' (doesnt modify the array we're using)
# sorted_arr = sorted(arr)

# print(sorted_arr)

#Looping through a dictionary

#'i' represents the key value returned from the dictionary as we iterate through out it
#dictionary[i] represents the value we obtain from the key as we iterate through out it

# for i in dictionary:
#     print(i,dictionary[i][0])

# set1 = {1.2, 2, 3, 4}

# set2 = {1.2, 3, 5, 6}

# #Union of the two sets
# print(set1 | set2, "is the union") #set1.union(set2)

# #Intersection of two sets (what they have in common)
# print(set1 & set2, "is the intersection") #set1.intersection(set2)

# #Difference of two sets (Getting the difference between the two sets)
# print(set1 - set2, "is the difference of set1")
# print(set2 - set1, "is the difference of set2")

# #Symmetric difference of two sets (Getting the difference between the two sets and obtaining all the differences)
# print(set1 ^ set2, "is the symmetric difference") #set1.symmetric_difference(set2)

# class NewClass:
#     #Constructor is usually required for a class definition
#     def __init__(self, name, ageNumber): #self represents the instance of the class
#         self.name = name #Specify the name within the instance of the class
#         self.age = ageNumber #Specify the age within the instance of the class
    
#     #Print the name function (gets the name from instance)
#     def say_hello(self):
#         print("Hello",self.name)
    
#     #Print age function definition (gets the age from instance)
#     def say_age(self):
#         print("You are",self.age,"years old")
    
    

# #When we create the object/class we call the constructor (or the __init__)
# var = NewClass('John',20)

# var.name = 'Smith' #We changed name variable of object to 'Smith'

# var.say_hello() #Call the "say_hello()" function specfied from the class

# var.say_age() #Call the 'say_age()' function specified from the class

def main():
    #Initialize the string as an array (so we can call the .join() method to join with ':' as string)
    string = []
    with open('scores.txt', 'r') as f: #Open the text file ('scores.txt' contains the data, might want to change it)
        for i in f.readlines(): #Read each line
            line = i.strip().split() #Strip any newlines and split by space
            string.append(line[0].upper()+":"+line[1].upper()) #Append the text to string list
        
    #Print in the format we want. The .join method should 'join' the list as a string with the
    #':' symbol that acts as a separator from each element
    #More info here: https://www.w3schools.com/python/ref_string_join.asp
    print("cbrc_CTF{" + ":".join(string) + "}")

main()
