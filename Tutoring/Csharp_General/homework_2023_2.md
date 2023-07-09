## Note
The following tasks may require you to research certain subjects on your own. You will apply your current understanding of the C# programming languages, but certain tasks (such as certain algorithms, mathematical equations etc) will be done via researching maybe through online sources, documentation or books. Part of what makes software engineering, or engineering as a whole is to continously learn about new topics frequently. As technologies evolve, you will be required to learn more and more as a software/cybersecurity engineer.

If you are having troubles with some of the questions, it's fine to skip some of them and work on another question then come back to it when you feel ready.

# Task 1
## Sum values
Write a C# function that takes an integer input and calculates the sum of all numbers from 1 up to that input number.
Make sure to display the calculated sum as the output and check for values of 0 or smaller, if so print 'Invalid' and return.
Example
```cs
using System;
					
public class Program
{
  //Write your function here

	public static void Main()
	{
		CalculateSum(5); //Would output to the console '15' (1 + 2 + 3 + 4 + 5)
	}
}
```

# Task 2
## Reverse a String
Write a C# function that takes a string as input and returns the string reversed.

Example:
```cs
using System;
				
public class Program
{
  //Write your function here

	public static void Main()
	{
		Console.WriteLine(ReverseString("Hello, world!")); // Output: "!dlrow ,olleH"
	}
}
```

# Task 3
## Calculate the Factorial of a Number
Write a C# function that takes an integer input and calculates the factorial of that number.

Example:
```cs
using System;
				
public class Program
{
  //Write your function here

	public static void Main()
	{
		Console.WriteLine(Factorial(5)); // Output: 120
	}
}
```

# Task 4
## Bank account class
Write a C# class that simulates a basic bank account. The class should have properties for the account number, account holder name, and balance. Implement methods to deposit, withdraw, and display the account details, including the account balance.

# Task 5
## Enums
Create an enum called Color representing different colors: Red, Green, Blue, Yellow, and White. Write a program that prompts the user to enter their favorite color and displays a message based on the entered color. If the color is Red, display "Red is a vibrant color!". If the color is Green, display "Green represents nature and freshness.". If the color is Blue, display "Blue symbolizes calmness and serenity.". If the color is Yellow, display "Yellow is associated with happiness and energy.". If the color is White, display "White signifies purity and innocence.". For any other color, display "Your favorite color is unique!".

# Task 6
## Dictionaries
Use the following data stored from a file
```
Alice: 85
Bob: 73
Charlie: 92
Dave: 68
```
And store them into dictionaries (it should be of types <string,int>). Then output the user with the highest score from the dictionary


# Task 7
## Linked list
Write a linked list class for strings in C#. It should be able to append, push and pop strings from the list. Also implement a 'printList()' function in order to print the contents from the list
Example of using the list in a prgoram
```cs
MyLinkedList list = new MyLinkedList();
list.add("a");
list.add("b");
list.add("c");

list.pop()
list.pop()

list.push("hello");

list.printList();
```

# Task 8
## Multithreading
## This task might require you research more on Threads in C#
Write a C# program that creates a user-defined number of threads within a Console environment. Each thread should execute concurrently and print a message indicating its thread number. The program should prompt the user to enter the number of threads and then create the specified number of threads. Each thread should print a message stating its thread number. Additionally, introduce a random delay (between 1 and 10 seconds) using the Thread.Sleep method to simulate some processing time before printing the message.
Note:
If you want to get a random delay amount in C# between 1-10 seconds use `new Random().Next(1000,10000)` (in terms of milliseconds)

# Task 9
## Temperature converter GUI
## This task might require you research more on the other WPF controls (such as RadioButtons)
Create a simple WPF application that allows users to convert temperatures between Celsius and Fahrenheit. The application should have the following components:
- One TextBox for the input value
- Two RadioButton controls to select the conversion direction: Celsius to Fahrenheit or Fahrenheit to Celsius.
- One label to display the result from the converted value
- A button to trigger the temperature conversion event

Requirements:
- The conversion formula from Celsius to Fahrenheit is: Fahrenheit = (Celsius * 9/5) + 32.
- The conversion formula from Fahrenheit to Celsius is: Celsius = (Fahrenheit - 32) * 5/9.
- The result should be rounded to two decimal places.
- Orientation does not matter (You can split the grid into sections if you want)
