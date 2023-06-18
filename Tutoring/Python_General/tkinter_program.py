import tkinter as tk

#Event handler for button click
def on_button_click():
    #Grab the user input from the textbox and print it
    user_input = textbox.get("1.0", "end-1c") 
    print(user_input)

def create_window():
    #Define the 'textbox' to be global so we can access it in other functions/event handlers
    global textbox

    #Create the window instance
    window = tk.Tk()

    #Set the title
    window.title("First program")

    #Define the button that we want to initialize within our GUI program
    button = tk.Button(window, text="Click here", command=on_button_click)
    button.pack(padx=10,pady=10)

    #Define the textbox that we want to add within our GUI program
    textbox = tk.Text(window, height=4, width=50)
    textbox.pack(padx=10,pady=10)

    #We will make the window loop continously until we close
    window.mainloop()

    #Everything after the mainloop() is after we close the window
    print("Program ended")

#Call create_window
create_window()

#Question 1:
#Create 4 buttons that use the same event handler/function so when you click it prints "Hello, World!" to the terminal

#Question 2:
#Make the program read the user input and make it so it parses simple mathematical expressions after clicking the button.
#For example:
#If the textbox has something like '5 + 9' the output to the terminal should be '14' or '6 - 3' output should be '3'
