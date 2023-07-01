/*
#Python class equivalent
class Student:
	def __init__(name, age):
		self.name = name
		self.age = age
	def printInfo():
		print("Your name is " + name + " and you are " + age + " years old")
		

student = Student()
student.printInfo()
*/

using System;

//'public' is so that other classes and instances can access this class
public class Student {
	//Specify name and age as the attributes/variables within our class definition
	string name;
	int age;
	
	//Constructor
	public Student(string _name, int _age) {
		name = _name;
		age = _age;
	}
	
	//void no returning 
	public void printInfo() {
		Console.WriteLine("Your name is " + name + " and you are " + age + " years old");
	}
}

public class Program
{
	public static void Main()
	{
		//Student is initialized with "John" as our name specifier and 12 as our age
		Student student = new Student("John", 12);
		
		//Print student info by calling 'printInfo()' specified within our Student class.
		student.printInfo();
		
		//1. Initializing part
		//2. Condition/loop must continue (if it is true)
		//3. Is the iterative part/part we change the value as we go through the loop
		for (int i = 0; i < 5; i++)
			Console.WriteLine(i);
		
		int v = 30;
		
		//If statement
		if (v < 45) {
			Console.WriteLine(v);
		}
		
		//While loop
		while (v < 45) {
			v++;
			Console.WriteLine(v);
		}



		//Array, Lists and dictionaries in C#

		//Python's way of declaring a list: list = ['1',2,True]
		
	        //Array of integers (storing fixed size of 10)
	        int[] arr = new int[10];
	
	        //Assign values within the array
	        for (int i = 0; i < arr.Length; i++) {
	            arr[i] = i;
	        }
	
	        //Use a foreach loop to print the value within the array
	        foreach (int num in arr) {
	            Console.WriteLine(num);
	        }
	
	        //Another way of declaring an array (not a set like in Python)
	        int[] arr_1 = { 3, 4, 5, 6, 7, 8 };
	
	        //List/Linked list
	        List<string> list = new List<string>();
	
	        //Assign values within the array
	        for (int i = 0; i < 10; i++) {
	            list.Add("Hello world");
	        }
	
	        //Print each value from the list
	        foreach (string str in list) {
	            Console.WriteLine(str);
	        }
	
	        //Dictionary Initialization
	        Dictionary<int, string> dictionary = new Dictionary<int, string>();
	        //Append/add value to the dictionary
	        dictionary.Add(1, "value1");
	}
}
