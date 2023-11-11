#Note

The following tasks may require you to research certain subjects on your own. You will apply your current understanding of the C# programming languages, but certain tasks (such as certain algorithms, mathematical equations etc) will be done via researching maybe through online sources, documentation or books. Part of what makes software engineering, or engineering as a whole is to continously learn about new topics frequently. As technologies evolve, you will be required to learn more and more as a software/cybersecurity engineer.

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

    //Change the value here using 'p'

    printf("After change: %i\n", num);

    return 0;
}
```
