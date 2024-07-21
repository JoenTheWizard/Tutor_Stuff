using System;

public class Program
{
    public static void Main()
    {
        //Reading from a file in C#
      
        //Try and catch
        try {
            //Define path for StreamReader to read
            string path = "example.txt";

            //Define a StreamReader to read within our new scope
            //Using a new scope ensures that '.ReadToEnd()' returns the data we want to read from the file
            using (StreamReader sr = new StreamReader(path))
            {
                //String data stores our stream from the file
                string data = sr.ReadToEnd();

                //Split by new line. Splitting returns a string array
                string[] data_array = data.Split('\n');

                Console.WriteLine(data_array[0]); //Print contents from file
            }
        }
        //If any exception were to be raised then call our exception handler
        catch (Exception exception) {
            //Print the exception message
            Console.WriteLine("ERROR: " + exception.Message);
        }
    }
}
