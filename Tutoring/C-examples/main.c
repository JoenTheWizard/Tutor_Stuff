//To compile the program we simply run 'gcc main.c -o main' and execute the output executable with './main'
//Include 'stdio.h' for standard input and outputfunctionalities
#include <stdio.h>

//Declare main (which returns int)
int main() {
    //Store an int array
    int arr[] = {2,4,6,7};

    //Iterate through array. We use sizeof() to obtain the length of array 
    //Using sizeof(), we get the size of a variable in terms of bytes
    //Size of int array that stores 4 ints = (4 bytes * 4) = 16 bytes
    //Size of int is 4 bytes. Divide the two (16 / 4) to get size of 4 which is the amount our array holds
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
        //Print each character. '%i' is used in our print format for integer type
        printf("%i\n", i);
    }

    //Create char array (which is a string) and print it
    char str[] = "Hello World\n";
    printf("%s", str);

    //Create a pointer to a character (which is a string) and print it
    char* str1 = "Hello World\n";
    printf("%s", str1);

    //Get the first character of the string using dereference and print it
    //When we dereference we get the current value pointed by the str1 pointer 
    char ch = *(str1);
    printf("%c\n", ch);

    //We can use '&' to obtain the reference/memory address of the variable 'j' and store that
    //memory address to int pointer 'k'

    //Declare 'j' variable
    int j = 10;
    //Get the reference from 'j' (memory address) and store into pointer 'k'
    int* k = &j;
    //Print the address of the variable 'j' using 'k' pointer
    printf("%p\n", k);

    //Return 0 status (success)
    return 0;
}
