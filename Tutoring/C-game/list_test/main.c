#include "list.h"

int main() {
    
    List* list = createList();
    add_l(list, 10, 5);
    add_l(list, 10, 15);

    add_l(list, 30, 10);
    
    push_l(list, 100, 10);
    
    pop_l(list);
    display(list);

    free_list(list);
    return 0;
}