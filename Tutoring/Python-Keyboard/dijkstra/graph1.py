#https://python-course.eu/applications-python/graphs-python.php
import linkedlist as ll

import random
# g = { "a" : {"d"},
#       "b" : {"c"},
#       "c" : {"b", "c", "d", "e"},
#       "d" : {"a", "c"},
#       "e" : {"c"},
#       "f" : {}
#     }

#Make the file to read as a user input/sys.argv
fileRead = open('kb.keyboard','r').read()

#Seperate function here to build the graph
#Randomly generate a graph

#Declare the dictionary 
dictionary = ll.LinkedList()
#Read the keyboard
for i in fileRead:
    #Create the temporary linked list to store our randomized egdes
    tmp = ll.LinkedList()
    for j in fileRead:
        r = random.randint(0,1)
        #Remove the j != i if wanted to have duplicate nodes within the edges
        if j != i and r:
            tmp.add(j)
    #Store the vertex and edges as a tuple (vertex is of type char and edges is our linked list class)
    dictionary.add((i,tmp))
            

print("Linked List with Graph test")

#Print each of the edges with their vertex counterpart
for i in range(dictionary.size):
    #Get the current index through our dictionary
    t = dictionary.IndexOf(i)
    #Get the edges from out current index
    lyst = t[1]
    #Print the edges that are connected to our current node
    for j in range(lyst.size):
        print(t[0],"-->",lyst.IndexOf(j),end='   ')
    print("")


print('='*20)

"""
The goal should be to traverse through the graph and obtain the correct word as we
traverse. So initialize at a starting node then check if the current node is corresponding
to the character we are reading. If not then read each of the edges and if it is contained
within the edges then set the new index to be at that node. If it cannot be found within
the root node or the edges then it is not possible

WORD = ADC
WE START AT NODE 'A'
{ ... } -- are the edges

> A  {B,C,D,E,F}
A is found as the root node increment that path

now look for 'D'
> A  {B,C,D,E,F}
D is found within the edges increment that path, set that as new node

> D  {E,F,C}
C is found within the edges increment that path, we have built the string

If there is a case where D or A did not contain any of the characters within the word
then return null or cannot be found, so:

> D  {E,F}
C is not found, cannot go any further

If you can, try checking the previous nodes and read from there if you cannot find a
certain character/node within the edges

"""

#Seperate function here to act as traversing through the graph

#Traverse through graph to build the word

#previousIndex = 0

strFile = open('strFile.txt','r').read().split(" ")

WORD = strFile[2]
startIndex = 0
wl = 0
print("Very Linear Graph Search")
print("WORD TO LOOK FOR:",WORD,"\n")

#Iterate through the word that we're looking for and reach each character by character
while wl < len(WORD):
    #Here reads from the dictionary which contains our tuples both containing our
    #linked list class

    #'t' stores values that look like this: ('a' : {'b','d','f'})
    t = dictionary.IndexOf(startIndex)
    #Here we need to obtain the edges from the vertex we're looking at 
    #edges will now equal {'b','d','f'}
    edges = t[1]

    #Word we're lookng for is 'hello'
    #So we need to grab the characters while we iterate
    #charFind at the beginning of the loop will equal 'h'
    #Then next time it loops it goes to 'e' then next loop would be 'l' and so on...
    charFind = WORD[wl]

    print("LOOK FOR",charFind)

    #t[0] is the 'a' from our dictionary
    #Here we need to compare the first element in our dictionary to the current character we're looking for
    #If not jump to the else statement
    if t[0] == charFind:
        print(t[0],"-->",t[0])
    else:
        #Declare variables for our next iteration
        q = 0
        canFindChar = False
        #Store the startIndex (current dictionary) to prev so we can keep track of our path
        prev = startIndex

        #Here we need to iterate and search through out our edges
        #Remember edges is {'b','d','f'}
        for j in range(edges.size):
            #Check if our current edges contain the character we are looking for
            #charFind is the character we want to look for
            #edges.IndexOf(j) is each iteration through out our linked list class
            if edges.IndexOf(j) == charFind:
                #If we found the character we're looking for jump here
                canFindChar = True

                #Grab the current index (which we'll change) 
                prev_dict = dictionary.IndexOf(prev)[0] 

                #Iteration through out our entire graph and set the 'startIndex' (which is our current)
                #to the new character
                for m in range(dictionary.size):
                    if dictionary.IndexOf(m)[0] == charFind:
                        startIndex = m
                
                #Print our final path
                print(prev_dict,"-->",dictionary.IndexOf(startIndex)[0])
            else:
                q += 1 

        #If the value 'canFindChar' is not true or it is false
        #then we break out of our while loop and print that we cannot find the character
        if not canFindChar:
            print("Can't find char!!")
            break
    #We want to iterate through out the word 'hello' we start with wl = 0 and then iterater wl
    #through out our loop
    wl += 1

