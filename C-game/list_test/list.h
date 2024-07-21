#pragma once
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int x;
    int y;
    struct node* next;
} node_l;


typedef struct {
    node_l* head;
} List;


List* createList();


node_l* newNode(int x, int y);


void add_l(List* list, int x, int y);


int pop_l(List* list);


void push_l(List* list, int x, int y);

void display(List* list);

void free_list(List* list);