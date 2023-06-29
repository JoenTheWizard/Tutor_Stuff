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
  // Write your function here

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
  // Write your function here

	public static void Main()
	{
		Console.WriteLine(Factorial(5)); // Output: 120
	}
}
```

# Task 4
## 
Write a C# class that simulates a basic bank account. The class should have properties for the account number, account holder name, and balance. Implement methods to deposit, withdraw, and display the account details, including the account balance.
