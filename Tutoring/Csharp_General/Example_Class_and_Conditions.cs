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

	}
}
