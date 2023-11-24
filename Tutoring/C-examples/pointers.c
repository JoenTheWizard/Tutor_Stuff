#include <stdio.h>
#include <stdlib.h>

// char a[] = "hello";  // array
//
//    +---+---+---+---+---+---+
// a: | h | e | l | l | o |\0 |
//    +---+---+---+---+---+---+
//
//  char *p = "world"; // pointer
//
//    +-----+     +---+---+---+---+---+---+
// p: |  *======> | w | o | r | l | d |\0 |
//    +-----+     +---+---+---+---+---+---+

//Make a function 'modify_array()' that takes in the array {1,2,3} and modifies the first value ('1') to another value. Make sure to print the array before and after its passed to modify_array()

void modify_value(int* a);

int main() {
    int a = 2; //This variable is a standard value type that will be stored in some memory address

    //Referencing to variable 'a'
    int* b = &a; //This is a pointer to the variable 'a' which stores the memory address to variable 'a'

    //Dereferencing to variable 'b'
    int c = *b; //Deference 'b' as it stores the memory address from 'a' to obtain the value from that memory address

    modify_value(&c);

    printf("A is equal to %i\n", a);
    printf("C is equal to %i\n", c);

    //Store array 'arr1'
    int arr1[] = {3, 2, 1};
    //Create pointer to 'arr1'
    int* pointer = arr1;
    //Get the size (in bytes) of the dereferenced pointer of the 'pointer' variable (from arr1)
    printf("Size of array: %d\n", sizeof(*pointer));

    return 0;
}

void modify_value(int* a) {
    *a = 10;
}
