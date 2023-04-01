#This here is an infinite while loop
i = 0
while True: #While True represents an infinite loop because the statement is always true
    i += 1
    if i == 5: #If 'i' is equal to 5 then we skip everything ahead of it
        continue #Continue here represents to skip everything else within the loop

    if i == 10: #If 'i' is equal to 10 then we 'break' which means to break out of a loop
        break #break out of loop at i == 10
    print(i)


#Lambda functions
def func1():
    func = lambda a: a + 1
    return func

print(func1()(4))

#Classes
class NewClass:
    #Initialize constructor, which creates the instance of an object
    def __init__(self, string_variable):
        self.hello = string_variable
    
    #Initialize print hello
    def print_hello(self):
        print(self.hello)


classNew = NewClass("hello world")
classNew.print_hello()
