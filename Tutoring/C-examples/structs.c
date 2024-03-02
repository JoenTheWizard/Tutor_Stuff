#include <stdio.h>
#include <string.h>

//We can specify our Student struct with name and age.
// struct Student {
//     char name[50]; //50 bytes
//     int age; //4 bytes
// };

//We can also create the struct in this case we can specify it with typedef to provide user defined struct types (and prevent from typing 'struct Student' as the type)
typedef struct {
    char name[50]; //50 bytes
    int age; //4 bytes
} Student;


int main() {
    //Initialize students struct
    Student students;

    //Specify the students by copying the string to the destination
    strcpy(students.name, "John");

    //Specify the age
    students.age = 17;

    //Print our Student struct's data
    printf("%s: %d\n", students.name, students.age);

    return 0;

}
