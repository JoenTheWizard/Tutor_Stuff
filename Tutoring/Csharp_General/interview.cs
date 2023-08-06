using System;

public class Program
{
    //Initialize the enum 'Days' which stores the days of week in order
    //Enums provide a natural way to represent and work with a finite set of related values.
    //By default, the type of an enum is `int`, but you can specify a different integral type if needed.
    //In this enum, the underlying values are automatically assigned starting from 0 and incrementing by 1 for each subsequent value.
    //For example, Monday has the integer value of 0, Tuesday has 1, and so on.
    enum Days
    {
        Monday,
        Tuesday, 
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday
    }
    //Defines the 'Student' struct. A struct in C# is a value type that stores small groups of related variables.
    //Unlike classes, structs cannot inherit from other structs or classes, but they can implement interfaces.
    //The difference between structs and classes is that structs are value types and classes are reference types.
    //This means that when a struct is assigned to a new variable, a copy of the actual value is made, whereas with a class, 
    //the memory address of the value is copied, not the actual value itself.
    struct Student
    {
        public int Id;
        public string Name;

        public Student(int Id, string Name)
        {
            this.Id = Id;
            this.Name = Name;
        }

        public void printInfo() {
            Console.WriteLine("{0}, {1}", Id, Name);
        }
    }
    
    public static void Main()
    {
        //Initialize a value from the enum 'Days'
        Days days = Days.Saturday;

        //This casts '1' to 'Days' enum. It is equivalent to saying Days.Tuesday
        //Days days1 = (Days)1;

        //Print the value from 'days' that it stores
        Console.WriteLine("The day today is " + days);

        //Enums are stored as if they were integer values with specific uses/values.
        //So in our case Days enum at '0' represents 'Monday' or '1' represents 'Tuesday'

        //So if we have a day that's greater than 'Friday' then it is a weekend otherwise it is a weekday
        if (days > Days.Friday)
        {
            Console.WriteLine("It is a weekend");
        }
        else
        {
            Console.WriteLine("It is a weekday");
        }

        //Reasons to use switch case over if else/else if is simply because we can minimize the verbosity
        //if we have a lot of conditional checks/statements.
        string name = "John";

        switch (name)
        {
            case "John":
                Console.WriteLine("Hello John");
                break;
            case "Tom":
                Console.WriteLine("Hello Tom");
                break;
            case "Jim":
                Console.WriteLine("Hello Jim");
                break;
            default:
                Console.WriteLine("I do not know who you are.");
                break;
        }

        //2D arrays
        //4 columns 4 rows
        int[,] vals = { { 1 , 2, 3, 4 }, 
                    { 2 , 3, 4, 5 }, 
                    { 3 , 4, 5, 6 },
                    { 4, 5, 6, 7 } };

        //2 rows 1 Column
        int[,] vals1 = new int[2, 1] { { 1 },
                                       { 2 } };

        //Dictionary Initialization
        Dictionary<int, string> dictionary = new Dictionary<int, string>();
        //Append/add value to the dictionary
        dictionary.Add(1, "value1");

        //Print each value from the dictionary
        foreach (var val in dictionary.Values) {
            Console.WriteLine(val);
        }

        //Lists are dynamic, in the way that we can dynamically add values to the list during run-time
        //of the program, unlike arrays.
        List<string> list = new List<string>();
        list.Add("Val");

        //Queues
        //Queues rely on a first-in-first-out structure (FIFO)
        Queue<string> queue = new Queue<string>();
        //Enqueue adds to the end of the queue
        queue.Enqueue("Hello");
        queue.Enqueue("World");
        queue.Enqueue("!");

        //Dequeue removes the start of the queue
        queue.Dequeue();

        //Print each value within the queue
        foreach (var obj in queue)
            Console.Write("{0} ", obj);
        Console.WriteLine();

        //Stacks are last-in-first-out (LIFO). The last element that is appended to the stack will be the last one
        //removed.
        Stack<string> stack = new Stack<string>();
        //Push adds to the top of the list
        stack.Push("Hello");
        stack.Push("World");
        stack.Push("!");

        //Pops the top of the list (which is our recently pushed value in the stack '!')
        stack.Pop();

        //Print each value within the stack
        foreach (var obj in stack)
            Console.Write("    {0}", obj);
        Console.WriteLine();

        //This would initialize a new instance of student struct (which should initialize its fields)
        //You can initialize the struct like: 'Struct student;' but you would need to assign the fields
        Student student = new Student();
        student.Name = "Tom";
        student.Id = 1;

        student.printInfo();

        //String manipulation
        string str1 = "Hello World!";

        //string sub = str1.Substring(6, 5); //Obtain substring
        //str1 += "! Welcome to C#"; //Append to text
        //string replaced = str1.Replace("World", "C#"); //Replaces all occurences of the word
        //int index = str1.IndexOf("World"); //Gets index of the first occurence of the specified substring
        //string trimmed = str1.Trim(); //Trims all whitespaces

        //Print the 'str1' value after manipulation
        Console.WriteLine(str1);

        //'.Equal()' checks if the string object's value and other string object's value are equal
        if (str1.Equals("Hello World!"))
        {
            Console.WriteLine("Hi");
        }

        //Replacing a character in a string using char[]
        char[] chr_arr = str1.ToArray(); //Convert the string and get the char array
        chr_arr[0] = 'h'; //Get the first index of the char array and replace the value with 'h'

        //To obtain the final string from the char array you can initialize a new string object with the char array
        //Or you can use the .Join() method using an empty separator with the char array
        string value = new string(chr_arr); //string.Join("", chr_arr);

        Console.WriteLine(value);
    }
}
