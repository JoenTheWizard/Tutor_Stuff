#Open and read file
with open('example_file', 'r') as file:
    #Iterate through the file and read each line
    for i in file.readlines():
        line = i.rstrip() #Read line and remove any newline characters and store in variable line
        split_line = line.split(',') #Split the string by comma and store in variable split_line

        #Create the dictionary and store the values within their appropriate key
        dictionary = {
            'age' : split_line[0],
            'name': split_line[1],
            'post': split_line[2]
        }

        #This should print the values from the specified keys from the dictionary
        print(dictionary['age'], dictionary['name'], dictionary['post'])
