## Note

The following tasks may require you to research certain subjects on your own. You will apply your current understanding of the C programming languages, but certain tasks (such as certain algorithms, mathematical equations etc) will be done via researching maybe through online sources, documentation or books. Part of what makes software engineering, or engineering as a whole is to continously learn about new topics frequently. As technologies evolve, you will be required to learn more and more as a software/cybersecurity engineer.

If you are having troubles with some of the questions, it's fine to skip some of them and work on another question then come back to it when you feel ready.

# Task 1
## C pointers
Write a program to demonstrate how to use a pointer to change the value of a variable. The following program is a template:
```c
#include <stdio.h>

int main() {
    int num = 10;
    int *p = &num;

    printf("Before change: %i\n", num);

    //Change the value here using 'p'. Hint: Try utilizing dereferences

    printf("After change: %i\n", num);

    return 0;
}
```

# Task 2
## Dynamic memory
Dynamically allocate an array of integers of size 5, assign values to each index (1-5) and print it. Make sure to free the memory afterwards (you can use tools like `valgrind` to help you to detect memory leaks). Remember to use Valgrind by doing `valgrind ./<executable>`, in which you can see the heap summary.

# Task 3
## Makefiles
Write a Makefile that compiles a C program with source file: main.c. The executable should be named `myprogram`, in the makefile store the executable name in a variable called `EXEC`. The Makefile should also include a `clean` target that removes all the generated files.

# Task 4
## Modify array
Make a function `modify_array()` that takes in the array {1,2,3} and modifies the first value ('1') to another value (can be any other value). Make sure to print the array before and after its passed to modify_array()
