#include <stdio.h>
#include "list.h"

int main(int argc, char** argv) {
    
    
    //Allocate the memory and create list
    List* list = createList();

    //Add the nodes to list
    add_l(list, 10);
    for (int i = 0; i < 10; i++)
        add_l(list, i);

    //Pop from list
    pop_l(list);

    //Push to list
    push_l(list, 40);
    //Print the list
    print_list(list);

    //Deallocate the list
    free_list(list);

    return 0;
}
