//Include 'stdio.h' for standard input and output functionalities
#include <stdio.h>
//Include 'stdlib.h' for dynamic memory allocation functionalities
#include <stdlib.h>

//If you want an optional and extra read on good 'style' for C programming here is:
//https://felipec.github.io/good-taste/parts/1.html (https://github.com/mkirchner/linked-list-good-taste)
//https://felipec.wordpress.com/2024/03/03/c-skill-issue-how-the-white-house-is-wrong/

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

    //Store array 'arr1'
    int arr1[] = {3, 2, 1};
    //Create pointer to 'arr1'
    int* pointer = arr1;
    //Print integer from memory address (added by 1, so this will print the second value of the array)
    printf("%i\n", *(pointer + 1));

    //Segmentation fault here
    //This is because we are attempting to modify a string literal which is read only.
    //Segmentation faults are caused when we attempt to access memory in which we are not allowed to modify
    // char* str2 = "Hello C";
    // *(str2) = 'Y';

    //Undefined behaviour
    //C doesn't check for bounds in arrays and this is defined as undefined behaviour
    //Undefined behaviour simply means that the behaviour of the program can be random
    //For example it still run correctly, could randomly crash, overwrite other data or something else (depending on compiler or system it can be differently handled)
    int carr[3];
    carr[15] = 5;

    //Dynamic memory allocation is a method to allocate memory during runtime.
    //You can use tools like Valgrind to check for any memory leaks that is caused by the program (You can install it with: sudo apt-get install valgrind)
    printf("Enter memory allocation: ");

    //Here we use scanf to take user input for the size of dynamically allocated array
    int amount;
    scanf("%i", &amount);

    //Allocate memory for 'amount' number of integers. malloc() takes in amount of bytes and will return a void* type
    //void* is a type where the value it's pointing to is unknown.
    //You can cast the void* return, but usually it's not quite necessary. It's up to you if you need to cast the result depending on your implementation
    //You can read more on void* casting here: https://stackoverflow.com/questions/605845/should-i-cast-the-result-of-malloc
    int* dynamicarr = malloc(amount * sizeof(int));

    //Assign a value to each of the elements in the dynamically allocated array
    for (int i = 0; i < amount; i++) {
        dynamicarr[i] = i;
        printf("%i\n", i);
    }

    //We need to free the dynamically allocated memory ourselves
    free(dynamicarr);

    //Return 0 status (success)
    return 0;
}
