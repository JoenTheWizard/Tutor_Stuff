using System;

//Parent class or Base class
public abstract class A {
	public int val;
	public A() {
		val = 20;
	}
	
	public void Method1() {
		Console.WriteLine("Method1 from A");
	}
	
	public void Method2() {
		Console.WriteLine("Method2 from A");
	}
}

public class B : A {
	public B() {
		Console.WriteLine("B initialized");
	}
	
	//Polymorphism example
	//Method1() is redefined for class 'B'
	public void Method1() {
		Console.WriteLine("Method1 from B");
	}
	//Method1() is also redefined for class 'B' but takes in parameters
	public void Method1(string vals) {
		Console.WriteLine("Method1 from " + vals);
	}
	
	public void Method3() {
		Console.WriteLine("Method3 from B");
	}
	
	//Method4() is static which means it cannot be called from an instance of this class' object.
	public static void Method4() {
		Console.WriteLine("Method4 from B");
	}
}

public class Program
{
	public static void Main()
	{
		//Initialize B object which is derived from A base class.
		//A is an abstract class which means it cannot be initialized itself but it can be derived to a child class inheriting it
		B obj = new B();
		obj.Method1("hello");
		obj.Method2();
		obj.Method3();
		
		//Calling a static method
		B.Method4();
		
		Console.WriteLine(obj.val);
	}
}
