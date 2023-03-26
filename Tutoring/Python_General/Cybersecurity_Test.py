'''
Test conditions: 

* Each function must return the appropriate answer.
* You must make a legitimate response. Simply copying and pasting the test condition is not legitimate.

Marking schema: 

Completion : 0 - 1 - 2 
Solution:    0 - 1 - 2 - 3 - 4 (only for intermediate and hard questions)

T students have multipliers on the solutions for hard questions
A students have multipliers on the completion for all questions


'''
def question1(cash, exchange_rate, fee):
    '''
    Given an exchange rate, exchange money from one currency to another. For example, 
    the country of 1 US dollar can be exchanged for $1.5 Australian. 

    Fees are calculated before exchange, so 1 US dollar would be reduced to 0.9 US dollars. 

    '''
    cash_after_fee = cash * (1 - fee)
    total = cash_after_fee * exchange_rate
    return total

print(question1(1, 1.5, 0.1),'\n')

def question2(file_in):
    '''this question is given a file. In this file are thousands of lines of text. 
    The format of each line of text looks like this: 

    [filter]:[flag]

    Modify this function to return only the flag for the only filter that is duplicated. 

    For example: 
    CATS:BOTH_LOVE_AND_HATE_YOU
    DOGS:ARE_ALL_GOOD_PUPPIES
    CATS:BOTH_LOVE_AND_HATE_YOU

    You must return "BOTH_LOVE_AND_HATE_YOU" as CATS are the only duplicated filter in the list
    ''' 
    
    

def question3(list_in):
    ''' 
    modify this function so it accepts a list of non-negative integers and 
    strings and then return a new list with the strings filtered out
    '''
    empty_list = []
    for i in list_in:
        if type(i) == int:
            empty_list.append(i)
    
    return empty_list
    

print(question3([10,34,'hello',23,'world']),'\n')

def question4(list_in, nth_number):
    '''
    modify this function so it accepts a list of non-negative integers. 
    This list must be filtered for duplicate numbers. 
    The number of duplicate numbers that is allowed in any given list is 
    defined by the 'nth_number'. Return a list containing the filtered numbers. 

    For example:
    question4([1, 1, 2, 2, 3, 3, 3], 2) returns [1, 1, 2, 2, 3, 3]
    question4([1, 1, 2, 2, 2, 3, 3, 3, 4], 1) returns [1, 2, 3, 4]
    question4([1, 1, 1, 1, 1], 2) returns [1, 1]
    '''
    #Remove duplicates
    list_in = list(dict.fromkeys(list_in))

    #Initialize the empty list
    new_list = []

    #Iterate through the list
    for i in list_in:
        #Iterate through the range from the nth_number
        for j in range(0,nth_number):
            new_list.append(i)  #Append the list through each iteration
    
    #Return the final new list
    return new_list
    
print(question4([1, 1, 2, 2, 3, 3, 3], 2), '\n')

def question5(file_name):
    '''
    modify this function so it accepts a filename. 
    The file contains details about students. The details flow as follows: 
    student_id; given_name; family_name; mark1, mark2, mark3, mark4

    return: only students who's student_ids start with a number greater 4

    return a dictionary of dictionaries in the following format: 

    {
        "876543210" : {
            "given_name": "ada",
            "family_name": "lovelace",
            "mean_mark": 75.5
        }
    }
    '''
    #Store the empty dictionary
    dictionary = {}

    #Read through each line
    with open(file_name, 'r') as f:
        for i in f.readlines():
            student_data = i.split(';')

            #Start total mean_mark at 0
            mean_mark = 0
            for j in student_data[3].split(','):
                val = int(j)
                mean_mark += val

            #Divide total by length of array (to get the average)
            mean_mark /= len(student_data[3].split(','))

            #Store the internal dictionary (the dictionary data that stores the info within the parent dictionary)
            student_info = {
                "given_name" : student_data[1].strip(),
                "family_name" : student_data[2].strip(),
                "mean_mark" : mean_mark
            }
            dictionary[student_data[0].strip()] = student_info #Store the final dictionary

    #Return the final dictionary
    return dictionary

print(question5('example_file'), '\n')

def question6(floors_traveled):
    ''' 
    Elevator Madness! 
    modify this function so it accepts a name of a file. Open the file and read it. 

    Each integer describes the number of floors and which direction the lift has traveled. 
    So, for example, if the lift is currently on floor 0 and the number is 3, the 
    elevator has traveled 0 -> 1 -> 2 -> 3
    Now the elevator is on floor 3, if the number is -2 the elevator travels 3 -> 2 -> 1
    and is now on floor 1.

    The elevator starts each day at floor 0

    You must return a dictionary which contains following keys and values: 
    {
        'highest_floor': the_highest_floor_reached, 
        'lowest_floor' : the_lowest_floor_reached,
        'most_frequent' : the_floor_most_frequently_stopped_at,
        'frequency_of_most_frequent': how_many_times_lift_stopped_at_most_frequent_floor
        'floors_traveled': absolute_number_of_floors_traveled, 
        'current_floor': the_current_floor_the_elevator_is_on_at_the_end,
    }
    if there are multiple floors that are the most_frequent return a list of all of them
    '''
    #Initialize empty list to later store values
    floors_traveled_list = []
    current_floor = 0
    stops = {}

    #Open the input file and read each line
    with open(floors_traveled, 'r') as f:
        for line in f:
            floor_change = int(line.strip()) #Convert the line from a string to an integer
            floors_traveled_list.append(abs(floor_change)) #Add the absolute value of the floor change to the list of floors traveled
            current_floor += floor_change #Update the current floor based on the floor change
            stops[current_floor] = stops.get(current_floor, 0) + 1 #Add the current floor to the stops dictionary and increment the count
    
    #Calculate the highest and lowest floors based on the keys in the stops dictionary
    highest_floor = max(stops.keys()) #Gets the max from the dictionary (keys)
    lowest_floor = min(stops.keys()) #Gets the min from the dictionary (keys)

    #Find the most frequent floor by looking for the floors with the highest count in the stops dictionary
    most_frequent = [floor for floor, count in stops.items() if count == max(stops.values())]
    frequency_of_most_frequent = max(stops.values()) #Calculate the frequency of the most frequent floor by finding the highest value in the stops dictionary
    absolute_floors_traveled = sum(floors_traveled_list) #Calculate the absolute number of floors traveled by summing the list of floors traveled

    #Return the total dictionary of the values
    return {
        'highest_floor': highest_floor,
        'lowest_floor': lowest_floor,
        'most_frequent': most_frequent[0],
        'frequency_of_most_frequent': frequency_of_most_frequent,
        'floors_traveled': absolute_floors_traveled,
        'current_floor': current_floor
    }

print(question6('floors.txt'))

# import unittest
# class TestQuestions(unittest.TestCase):
#     def test_question1(self):
#         self.assertEqual(question1(1, 1.5, 0.1), 1.35)
#         self.assertNotEqual(question1(1, 2, 0.1), 1.35)

#     def test_question2(self):
#         self.assertEqual(question2('question.2.data'), "fc957dc4a4d8be8abaa2eab25af8576a")

#     def test_question3(self):
#         self.assertEqual(question3([1,2,'a','b']),[1,2])
#         self.assertEqual(
#             question3(['m', 8, 'B', 'O', 'h', 5, 'c', 2, 2, 'C', 8, 7, 'i', 'N', 'l', 'h', 'C', 'g', 'i', 'f', 'e', 'M', 'a', 'd', 'X', 'M', 'K', 'C', 1, 'o', 'X', 'P', 'J', 'S', 'E', 'd', 'b', 'k', 'a', 'G', 'G', 'v', 9, 'L', 'u', 'o', 'I', 'W', 3, 7, 5, 2, 'j', 'U', 'I', 4, 'D', 'B', 's', 'm', 'G', 'H', 'G', 'd', 'H', 'O', 'T', 'B', 'O', 2, 'b', 'o', 't', 'i', 9, 's', 'q', 'm', 'c', 4, 'X', 9, 'S', 'u', 'd', 0, 'H', 'X', 'X', 2, 'x', 1, 4, 'l', 'h', 'e', 'R', 'a', 'P', 'P']),
#             [8, 5, 2, 2, 8, 7, 1, 9, 3, 7, 5, 2, 4, 2, 9, 4, 9, 0, 2, 1, 4]
#         )

#     def test_question4(self):
#         self.assertEqual(question4([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
#         self.assertEqual(question4([1,1,3,3,7,2,2,2,2], 1), [1, 3, 7, 2])

#     def test_question5(self):
#         self.assertEqual(question5('question.5.data'),  {'907938119': {'given_name': ' Regina', 'family_name': ' Walker', 'mean_mark': 46.5}, '904417131': {'given_name': ' Kelly', 'family_name': ' Mayes', 'mean_mark': 37.0}, '906641569': {'given_name': ' Lisa', 'family_name': ' Winkler', 'mean_mark': 68.25}, '903496120': {'given_name': ' Kenneth', 'family_name': ' Zombory', 'mean_mark': 64.0}, '904893024': {'given_name': ' Shawn', 'family_name': ' Peragine', 'mean_mark': 19.0}, '903534557': {'given_name': ' Yolanda', 'family_name': ' Rector', 'mean_mark': 19.5}, '904313736': {'given_name': ' Jessie', 'family_name': ' Wright', 'mean_mark': 76.25}})

# def test_question6(self):
#     self.assertEqual(question6('question.6.data'), {'highest_floor': 30, 'lowest_floor': -5, 'most_frequent': 27, 'frequency_of_most_frequent': 40, 'floors_traveled': 12601, 'current_floor': 9})

# if __name__ == "__main__":
#     unittest.main()
