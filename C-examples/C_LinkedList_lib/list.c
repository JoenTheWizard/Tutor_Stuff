#include "list.h"

List* createList() {
    List* list = (List*)malloc(sizeof(List));
    if (!list)
        return NULL;
    list->head = NULL;
    return list;
}

node_l* newNode(int data) {
    node_l* new = (node_l*)malloc(sizeof(node_l));

    if (!new)
        return NULL;
    new->data = data;
    new->next = NULL;
    return new;
}

void add_l(List* list, int data) {
    node_l* cur = NULL;
    if (list->head == NULL)
        list->head = newNode(data);
    else {
        cur = list->head;
        while (cur->next != NULL)
            cur = cur->next;
        
        cur->next = newNode(data);
    }
}

void push_l(List* list, int data) {
  node_l* tmp = newNode(data);
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

void print_list(List* list) {
    node_l* cur = list->head;

    if (list->head == NULL)
        return;

    while (cur != NULL) {
        printf("%i\n", cur->data);
        cur = cur->next;
    }
}

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
