//Include 'stdio.h' for standard input and output functionalities
#include <stdio.h>
//Include 'stdlib.h' for dynamic memory allocation functionalities
#include <stdlib.h>

//Add function predefined
int add(int a, int b);

//Danging pointer
//Use malloc
int* getData() {
    //*val = 10;
    int* ptr = (int*)malloc(sizeof(int));
    *ptr = 10;
    return ptr; 
}

//Main function
int main() {
    int* ptr = (int*)malloc(sizeof(int));
    *ptr = 10;

    printf("Value is equal to %i\n", *ptr);

    //Undefined behaviour / Dangling pointer
    free(ptr);

    printf("After free: Value is equal to %i", *ptr);

    //int* t = getData();
    //printf("Value: %i", *t);

    //int t = 3;
    //getData(&t);
    //printf("t is equal to: %i", t);

    int* getVal = getData();
    printf("getVal is equal to: %i", *getVal);
    free(getVal);
    //You can also try setting these pointers to NULL to avoid any further use of the pointer as a dangling pointer
    //getVal = NULL;

    return 0;
}

//Define the main function
int add(int a, int b) { 
    return a + b;
}
