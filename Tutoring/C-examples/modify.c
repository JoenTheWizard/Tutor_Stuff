#include <stdio.h>

//Call modify function. This function requires a pointer argument, so it can modify the variable
//using its reference (the memory address of the variable)
void modify_value(int* a) {
    //Dereference the pointer passed in so we can modify that value stored in that memory address
    *a = 10;
}

int main() {

    //'c' is stored as a value 2
    int c = 2;

    //Pass in the reference of variable 'c', so we get the memory address of that variable to later modify
    modify_value(&c);

    //After calling 'modify_value()' we print the variable 'c' to see if the value has been modified after
    //it has been called.
    printf("%d", c);

    return 0;
}
