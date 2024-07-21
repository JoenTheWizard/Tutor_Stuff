#include "list.h"

/*
Initialize the list of nodes
 */
List* createList() {
    List* list = (List*)malloc(sizeof(List));
    if (!list)
        return NULL;

    list->head = NULL;
    return list;
}

/*
Create our node
*/
node_l* newNode(int x, int y) {
    node_l* new = (node_l*)malloc(sizeof(node_l));

    if (!new)
        return NULL;
    
    new->x = x;
    new->y = y;
    new->next = NULL;

    return new;
}

/*
Add to our list
*/
void add_l(List* list, int x, int y) {
    node_l* cur = NULL;
    /*
    If our list is empty, then just initialize the head node to a new node
    */
    if (list->head == NULL) {
        list->head = newNode(x, y);
    }
    /*
    Otherwise the list is not empty jump here
    */
    else {
        cur = list->head;
        while (cur->next != NULL)
            cur = cur->next;
        /*
        Put our new node in here as we traverse through the list
        */
        cur->next = newNode(x, y);
    }
}


/*
Display our list
*/
void display(List* list) {
    node_l* cur = list->head;

    if (list->head == NULL)
        return;
    
    while (cur != NULL) {
        printf("X: %i  Y: %i\n", cur->x, cur->y);
        cur = cur->next;
    }
}

void push_l(List* list, int x, int y) {
    node_l* tmp = newNode(x, y);
    tmp->next = list->head;
    list->head = tmp;
}

int pop_l(List* list) {
    if (list->head == NULL)
        return -1;
    
    node_l* h = list->head;
    list->head = list->head->next;

    free(h);
    return 0;
}

/*
Deallocate the list
*/
void free_list(List* list) {
    node_l* cur = list->head;
    node_l* next = cur;

    while (cur != NULL) {
        next = cur->next;
        free(cur);
        cur = next;
    }

    free(list);
}