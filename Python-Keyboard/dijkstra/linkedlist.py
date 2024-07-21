#Library for the single linked list

#Create the node class (then we must created the linked list class)
class Node:
  #Initialize the constructor
  def __init__(self, data, next=None): 
    self.data = data
    self.next = next

#Now for the linked list class
class LinkedList:
  #Constructor
  def __init__(self):  
    self.head = None
    self.size = 0
  
  #This will add a new node to the list
  def add(self, data):
    newNode = Node(data)
    if self.head:
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
    else:
        self.head = newNode
    
    self.size += 1
  
  #Print method for the Linked list
  def printList(self):
    current = self.head
    while current:
        print(current.data)
        current = current.next

  #THis is just for formatting the printing
  def printFormat(self, atIndex):
    current = self.head
    i = 0
    while current:
        if i % 6 == 5:
            print("\u001b[7m"+current.data+"\u001b[0m\n" if i == atIndex else current.data+"\n",end='')
        else:
            print("\u001b[7m"+current.data+"\u001b[0m " if i == atIndex else current.data+" ",end='')
            #print(current.data + " ",end='')
        #print(current.data + "\n" if i % 6 == 5 else current.data+" "*2,end='')
        i += 1
        current = current.next
    print("")

  #Get value from index
  def IndexOf(self, index):
    current = self.head
    if index > self.size - 1 or index < 0:
        raise IndexError
    i = 0
    while current:
        if i == index:
            return current.data
        current = current.next
        i += 1
    return -1
  
  #Clear the nodes
  def clear(self):
    while self.head != None:
      temp = self.head
      self.head = self.head.next
      temp = None
    self.size = 0

  def remove(self,position):
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1 and self.head != None):
      nodeToDelete = self.head
      self.head = self.head.next
      nodeToDelete = None
      self.size -= 1
    else:    
      temp = self.head
      for i in range(1, position-1):
        if(temp != None):
          temp = temp.next   
      if(temp != None and temp.next != None):
        nodeToDelete = temp.next
        temp.next = temp.next.next
        nodeToDelete = None 
        self.size -= 1
      else:
        print("\nThe node is already null.")

    