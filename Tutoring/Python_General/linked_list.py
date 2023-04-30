#Node class
class Node:
    def __init__(self, data, next=None):
        self.data = data #Stores data
        self.next = next #Stores the next node (Node or NONE/NULL)

class LinkedList:
    def __init__(self):
        self.head = None #We need to start with a head node
        self.size = 0 #Specify size of list

    def add(self, data):
        newNode = Node(data) #Create the new node we are going to add
        if self.head: #This checks if the head node is not null/none/empty
            current = self.head #We will start with the head node
            while current.next: #Traverse to the end of the list until we reach none
                current = current.next #This will set current to the next node
            current.next = newNode #Set the next node to the new node we want to add at the end of the list
        else:
            self.head = newNode
        
        self.size += 1 #Append size
    
    #I have defined 'push' and 'pop' for you to look into yourself if you'd want
    #Some image references to help with the following I have defined:
    #https://i0.wp.com/masterdotnet.com/wp-content/uploads/2020/09/Stack.png?fit=751%2C430&ssl=1

    #Push - This pushes data to the top of the list
    def push(self, data):
        newNode = Node(data) #Create the new node
        newNode.next = self.head #Make the newNode's next equal to the head
        self.head = newNode #Now the new head is the newNode we made
        self.size += 1
    
    #Pop - This removes the top node from the list
    def pop(self):
        if self.head: #If the head node is not null
            self.head = self.head.next #Then we make the head node equal to the next node
            self.size -= 1 #Decrement size

    #Printing the list
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    #=== QUESTION ===
    #Define a method 'sum()' that iterates through out the list and sums all the numbers within that list
    #The 'printList()' method should help you with this task



ll = LinkedList()

# Add to the top of the list the even numbers ranging from 0 - 50

# The linked list with the values.
ll.add(34)
ll.add(30)
ll.push(12)
ll.push(45)
ll.push(78)

# sumInList = ll.sum()
# print(sumInList) #Should return the sum of all values in the list

# #ll.pop()
# #ll.pop()

#ll.printList()
