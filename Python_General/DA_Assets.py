#!/usr/bin/python
# "responses.py" v1.0
# Author: Mick Arrogante
# 2023 S1 Digital Assets
# Assessment Item #2

# SCHEDULE OF EVENTS
#
# FIRST 10 MINUTES:
# - Take seat, open Google Classroom (GC) and Visual Studio (VS), login, hardware check
# - Ask questions about the item, request online interpreter IF technical issues with VS
# - Place keyboard well in front of you, underneath monitor
#
# NEXT 3 MINUTES
# - Download the code from GC, open it in Visual Studio (VS), read through it
# - Last chance to ask questions about item rules or format
#
# NEXT 90 MINUTES
# - Complete the item
# 
# NEXT 2 MINUTES
# - Stop coding, submit your *py file to GC
# - Coding at this time may result in penalties
# - Submitting late to GC may result in penalties

# ITEM CONDITIONS
#
# This is an OPEN-BOOK item: you may refer to your notebook or notes printed from our GC
# This is a CLOSED-COMPUTER item: you may only use an IDE (e.g. Visual Studio)
# You will be allowed 90 minutes to complete this code
# You must submit this *py file ONLY to the Item 2 post on our Google Classroom
# If you are having issues accessing/using your IDE, REQUEST to use an online interpreter ASAP
# The only website you may visit is Google Classroom (to collect AND submit this when done)

# The BSSS requires that you substantially complete this item
# If you do not make a reasonable attempt to answer all questions, you may be deemed
# to have NOT completed this item for the purposes of assessment

# HINTS
#
# 0. Do not change the name nor arguments for any of the provided functions
# 1. You do not need to use the input() function for any of the below functions
# 2. You can write your own print() statments to call and test your functions
# 3. All of the below functions need to RETURN values
# 4. Assume that any code outside of the given functions will be ignored

# MARKING TOTALS
#
# There are 7 functions to implement
# These are the mark totals for each question (depending on your package type)
#
# You will be marked for CORRECTNESS, CONCISENESS and STYLE
#	- Correctness: does your function do what it is meant to do?
#	- Conciseness: did you use the least amount of lines/functions/variables to do it?
#	- Style: did you achieve the above with code that is easy to read and understand?
#
#					TERTIARY		ACCREDITED
#	FUNCTION 1		2 marks			3 marks
#	FUNCTION 2		2 marks			3 marks
#	FUNCTION 3		3 marks			3 marks
#	FUNCTION 4		3 marks			3 marks
#	FUNCTION 5              4 marks			3 marks
#	FUNCTION 6		4 marks			3 marks
#	FUNCTION 7		4 marks			4 marks
#	TOTAL			22 marks		22 marks
#
# Do your best to write relevant code.
# Partial correctness may still allow you to score partial marks.

#
# THE QUESTIONS (FUNCTIONS) BEGIN AFTER THIS LINE

'''	Function 1.
	Implement this function to: 
		- Subtract 1/3 (one third) of x from 42
		- Return the result of this calculation
'''
def question_1(x):
	# DELETE THESE TWO LINES AND TYPE YOUR CODE IN HERE
	x = int(x)
	return 42 - (x/3)

print(question_1(15)) # Should output 37



'''	Function 2.
	Implement this function to:
		- Check if a string, s, is read the same forwards and backwards
		- If it is read the same forwards and backwards, return True (the bool type)
		- Else, return False (the bool type)

	Examples of input : output:-
		- 'radar'  : True
		- 'posix' : False
		- 'malayalam' : True
'''

def question_2(s):
	# DELETE THESE TWO LINES AND TYPE YOUR CODE IN HERE
	# if s: # if the string is read the same forwards and backwards, return True
	#     return True
	# else:
	#     return False
    #rev_s = s[::-1]
    return s[::-1] == s

print(question_2('racecar'))


'''	Function 3. (4 marks)
	Implement this function to: 
		- Count the number of upper case words in a string, s
		- If there is ONE OR LESS, the function should return -1
		- If there are MORE THAN ONE:
			- If there is an ODD number the function should return 0
			- If there is an EVEN number the function should return 1

		- Examples of input : output:-
			- 'DIGITAL ASSETS is on' : 1
			- 'DiGiTAL aSSeTs is on' : -1
			- 'DIGITAL asets IS ON' : 0
'''


def question_3(s):
    #We need count the amount of uppercase characters
    total = 0 #Start from 0
    #Iterate through each character
    for i in s:
        if i.isupper(): #If the character is an uppercase character then increment total by 1
            total += 1
    
    #Conditonal statements to give the return value
    if total <= 1:
        return -1
    else:
        if total % 2 == 1:
            return 0
        else:
            return 1

print(question_3('HELlo'))

'''	Function 4. (4 marks)
	Implement this function to: 
		- Search a space-separated string, s, for any words three letters or less long
		- No string passed to this function will have punctuation (just letters and spaces)
		- Return a LIST of these words WITHOUT DUPLICATES (case-sensitive)

		- Examples of input : output:-
			- 'I study CAD at college' : ['I', 'CAD', at]
			- 'There is a red cat' : ['is','a','red','cat']
			- 'There is a red red cat' : ['is','a','red','cat']
			- 'There is IS a red RED cat' : ['is', 'IS','a','red', 'RED', 'cat']
'''

def question_4(s):
    list_arr = []
    
    s_ = s.split(' ')
    for i in s_:
        if len(i) <= 3:
            list_arr.append(i)
    
    #Remove duplicates
    list_arr = list(dict.fromkeys(list_arr))
    return list_arr


print(question_4('I study CAD at college'))


'''	Function 5.
	Implement this function to: 
		- Receive a LIST OF LISTS OF NUMBERS, l
		- Total all of the numbers and divide by the number of sublists in the main list
		- It is okay to return numbers with decimal points (floats)

		- Examples of input : output:-
			- [[1],[2],[3]] : 2.0
			- [[0,2,3],[2,1],[1,3]] : 4.0
			- [[0,0,3],[0],[0,0]] : 1.0
'''
def question_5(l):
	# DELETE THESE TWO LINES AND TYPE YOUR CODE IN HERE
	# l = int[]
	# elements = [0][1][2]
	# total_index = [l]
	# return elements/total_index

    total = 0
    for sublist in l:
        for j in sublist:
            total += j
    
    return total/len(l)

print(question_5([[1],[2],[3]]))

'''	Function 6.
	Implement this function to:
		- Receive a tuple containing two numbers, t
		- Return a dictionary with a single entry
		- The single entry in the returned dictionary should have:
			- a tuple KEY made up on the first number, and the string 'foo'
			- a tuple VALUE made up of the second number, and the string 'bar'
			- In both cases, the string should be last in the tuples

	Examples of input : output:-
		- (1,2) : {(1,'foo'):(2,'bar')}
		- (0,0) : {(0,'foo'):(0,'bar')}
		- (-2,3) : {(-2,'foo'):(3,'bar')}
'''

def question_6(t):
    dictionary = {} #Declare empty dictionary
    first_elem = (t[0], 'foo') #Declare the first tuple value (key)
    second_elem = (t[1], 'bar') #Declare the second tuple value (value)

    dictionary[first_elem] = second_elem

    return dictionary


print(question_6((1,2)))


'''	Function 7.
	Implement this function to:
		- Receive a LIST OF TUPLES OF NUMBERS, l
		- The tuples will contain two numbers e.g., (5,6)
		- Return the number of tuples where one of the numbers is 0 and the other is EVEN
		- NOTE: 0 is an even number
	Examples of input : output:-
		- [(2,2),(0,2),(2,0),(0,1)] : 2
		- [(2,2),(0,0)] : 1
		- [(0,1),(0,0)] : 1
'''

def question_7(l):
    total = 0 #Start at 0 (which we'll increment )
    for i in l:
        #If the first value is 0 and second is even OR If the first value is even and the second is 0
        #Then we increment the amount we have if the latter was the case
        if (i[0] == 0 and i[1] % 2 == 0) or (i[1] == 0 and i[0] % 2 == 0):
            total += 1
    #Return total
    return total

#Print the final
print(question_7([(0,1),(1,0)]))
