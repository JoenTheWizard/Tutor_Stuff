#! /usr/bin/env python3
import os
import argparse
import string
import sys, tty, termios
#My libs
import dijkstra.linkedlist as ll

#This function is from the 'termios' module just to handle with terminal input data
def term():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def interactiveMode(keyboardFile):
    CHARLIST = open(keyboardFile,'r').read()
    #First we're going to initialize the list of characters 
    lnklst = ll.LinkedList()
    for i in CHARLIST:
        lnklst.add(i)

    #Do the node operations here
    #eg lnklst.add(whatever the user inputted)

    os.system('clear')
    listINDEX = 0
    INPUTSTRING = ""
    while True:
         #Then we can print them out
        lnklst.printFormat(listINDEX)
        #You can do lnklst.add() for adding to the list for
        curChar = lnklst.IndexOf(listINDEX)
        print("INDEX:",curChar)
        print(INPUTSTRING)
        ch = term()
        #Check if 'q' has been pressed to exit loop
        if ch == 'q':
            break
        
        #Very hacky way of doing this
        #Get key inputs
        #Right key
        if ord(ch) == 67:
            if listINDEX < lnklst.size - 1:
                listINDEX += 1
        #Left key
        elif ord(ch) == 68:
            if listINDEX > 0:
                listINDEX -= 1
        #Down key
        elif ord(ch) == 66:
            if listINDEX < lnklst.size - 6:
                listINDEX += 6
        #Up key
        elif ord(ch) == 65:
            if listINDEX > 5:
                listINDEX -= 6
        
        #Enter key
        elif ord(ch) == 13:
            INPUTSTRING += curChar
        #Backspace
        elif ord(ch) == 127:
            INPUTSTRING = INPUTSTRING[:-1]
        #Space bar
        elif ch == ' ':
            INPUTSTRING += " "
    
        os.system('clear')

#!!! REPLACE OR REMOVE THIS FUNCTION WITH THE GRAPH THEORY FUNCTIONS !!!
def Array2D():
    CHARLIST = open('files/example.keyboard','r').read()
    #'lnk' is the row linked list
    lnk = ll.LinkedList()
    
    #'tmp' is just each column linked list
    tmp = ll.LinkedList()
    #Initialize i to make sure that we have 6 data nodes within each row
    i = 0
    #Iterate through the file and read each character
    for _ in CHARLIST:
        #Add the characters to each column
        tmp.add(_)
        #If size of 6 is satisfied then we fill the cpy linked list and add it as a row which is 'lnk'
        if i % 6 == 5:
            cpy = ll.LinkedList()
            for __  in range(tmp.size):
                cpy.add(tmp.IndexOf(__))
            lnk.add(cpy)
            tmp.clear()
        #Iterate 'i' for each character in the file
        i += 1
    #If any columns have a size smaller than 6, then make sure to add it to the list since it didn't fulfill the condition within the loop
    if tmp.size < 6:
        lnk.add(tmp)
    
    #Print each data value within the list
    for m in range(lnk.size):
        for n in range(lnk.IndexOf(m).size):
            print(lnk.IndexOf(m).IndexOf(n),"->",end=' ')
        print("")

if __name__ == "__main__":
    #Now for argument parsing
    if sys.argv[1] == "-i":
        #Main menu
        #Interactive mode configurations and main menu
        keyboardFile = ""

        while True:
            print("1. Load Keyboard\n2. Node Operations\n3. Edge Operations\n")
            userInput = input('Please select the following: ')

            keyboardselect_menu = True

            if userInput == '1':
                while keyboardselect_menu:
                    keyboardFile = input("Enter the keyboard file name: ")
                    if not os.path.exists(keyboardFile):
                        print("Please enter a valid file path...")
                    else:
                        keyboardselect_menu = False
            break
        interactiveMode(keyboardFile)
    elif sys.argv[1] == "-s":
        #Replace Array 2D function with the Graph function
        Array2D()