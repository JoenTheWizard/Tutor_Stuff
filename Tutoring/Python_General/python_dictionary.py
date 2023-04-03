#I will give you a file later, it will contain a large list of names and values.
#Here is an example of what a line of this file would look like

#Bob : 20, 30, 10, 4 (Some of the scores list may vary in length)
#So Bob should be the key. And its corresponding values should be { mean: 16 }
#So the resulting value should be { 'Bob' : { mean : 16 } }

#Optional: 
#At the end of the program it should return the person with the highest 'mean' value
#If for example 'Bob' had the highest mean, at the end print this
#"Bob has the highest mean value"

#Open the file and read its contents
with open('practice_dictionary.txt', 'r') as f:
    lines = f.readlines()

#Initialize a dictionary to store the mean for each name
name_mean = {}

#Loop through each line of the file
for line in lines:
    #Split the line into name and scores
    name, scores_str = line.strip().split(':')

    #Convert scores from string to list of integers
    scores = list(map(int, scores_str.split(',')))

    #Calculate the mean of the scores
    mean = sum(scores) / len(scores)

    #Store the mean in the dictionary
    #Key value: name
    #Value: The other dictionary (which is the mean)
    name_mean[name] = {'mean': mean}
    
#Print each of the students names and the mean values (dictionaries)
for d in name_mean:
    print(d,"has",name_mean[d])

#Find the name with the highest mean value
highest_mean_name = '' #Initialize the highest name here
highest_mean_value = 0 #Initialize the highest value here

#Loop through to see which person has the highest mean value
for i in name_mean:
    if name_mean[i]['mean'] > highest_mean_value:
        highest_mean_value = name_mean[i]['mean']
        highest_mean_name = i
    

#Print the name with the highest mean value
print(f"\n{highest_mean_name} "has the highest mean value")
