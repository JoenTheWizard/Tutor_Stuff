#include <stdio.h>
#include <stdlib.h>

#include "includes/color.h"
#include "includes/newSleep.h"
#include "includes/random.h"

/*Init the grid*/
char** image;

/*Init the X and Y size of grid*/
int x;
int y;

/*Time intervals*/
float time;

/*Directions of the Ant*/
typedef enum {
    LEFT,
    RIGHT,
    UP,
    DOWN
} ANT_LOOK;

/*Ant struct to store position and direction*/
typedef struct {
    int x;
    int y;
    ANT_LOOK look;
} ANT;

/*First ant will follow the Langton's Ant algorithm*/
ANT first_ant;

/* Implement the second ant */
ANT second_ant;

/*Steps taken from the ants (should break the while loop after this vaile has been reached)
Implement this*/
int steps;

char return_ant_look(ANT* ant);

void return_ant_turn(ANT* ant, char isClockwise);

int main(int argc, char** argv) {

    if (argc >= 2) {
        /* Store the args.
           Implement reading from the
           file yourself given from
           previously
        */
        x = atoi(argv[1]);
        y = atoi(argv[2]);

        first_ant.x = atoi(argv[3]);
        first_ant.y = atoi(argv[4]);

        first_ant.look = DOWN;

        time = atof(argv[5]);
    
    /*malloc the grid
    First init each row
    */
    image = (char**)malloc(sizeof(char*) * y);
    /*
    Then we malloc each column
    (+1 for null terminator)
    */
    int i;
    for (i = 0; i < y; i++)
        image[i] = (char*)malloc(sizeof(char) * x+1);

    /*Initialize the grid buffer*/
     int j,k;
     for (j = 0; j < y; j++) {
        for (k = 0; k < x; k++) {
            image[j][k] = (j == 2 && k == 5) ? '1' : '0';
        }
     }

    /*Extract the type of tile we are on*/
    char TILE_TYPE;
    TILE_TYPE = image[first_ant.y][first_ant.x];

    char TILE_TYPE_2;
    /* TILE_TYPE_2 = image[second_ant.y][second_ant.x] */

    /* Deploy the ant */
    if (first_ant.y >= 0 && first_ant.y <= y &&
        first_ant.x >= 0 && first_ant.x <= x)
        {
            image[first_ant.y][first_ant.x] = return_ant_look(&first_ant);
        }

     int gameRun = 1;
     while (gameRun) {
        /* Will call the 'clear' 
        unix-command for every time interval
        specified */
        system("clear");
        for (j = 0; j < y; j++) {
            for (k = 0; k < x; k++) {
                printf("%c ", image[j][k]);
            }
            printf("\n");
        }

        printf("CURRENT TILE: %c\n", TILE_TYPE);
        printf("X: %d  Y: %d\n", first_ant.x, first_ant.y);

        /* Sleep at the current thread at
        time intervals */
        newSleep(time);

        /* Handling the direction the ant goes in */
        image[first_ant.y][first_ant.x] = TILE_TYPE == '0' ? '1' : '0';
        return_ant_turn(&first_ant, TILE_TYPE);
        TILE_TYPE = image[first_ant.y][first_ant.x];
        image[first_ant.y][first_ant.x] = return_ant_look(&first_ant);

        /* 
        //Initialize random 
        initRandom();

        //Second ant flipping the tiles
        image[second_ant.y][second_ant.x] = TILE_TYPE_2 == '0' ? '1' : '0';

        //Returns a random direction the ant must go
        //Manage second ant's direction and position
        second_ant.look = random_val(LEFT, DOWN);
        if (second_ant.look == LEFT)
            second_ant.x--;
        else if (second_ant.look == RIGHT)
            second_ant.x++;


        //Obtain the tile for the second ant
        TILE_TYPE_2 = image[second_ant.y][second_ant.x];

        //Deploy the second ant to the new direction
        image[second_ant.y][second_ant.x] = return_ant_look(&second_ant);
        */
     }

    /*Deallocate the buffer
    First deallocate each column then
    each row
    */
    int freeBufs;
    for (freeBufs = 0; freeBufs < y; freeBufs++)
        free(image[freeBufs]);
    
    free(image);
    }
    else
        printf("Incorrect usage of program!\n");

    return 0;
}

/*Return direction of ant
Will default to looking UP*/
char return_ant_look(ANT* ant) {
    if (ant->look == DOWN)
        return 'v';
    else if (ant->look == UP)
        return '^';
    else if (ant->look == LEFT)
        return '<';
    else if (ant->look == RIGHT)
        return '>';
    
    return '^';
}

void return_ant_turn(ANT* ant, char isClockwise) {
    /* Clockwise */
    if (isClockwise == '0') {
        if (ant->look == DOWN) {
            if (ant->x > 0)
                ant->x--;
            ant->look = LEFT;
        }
        else if (ant->look == UP) {
            if (ant->x < x)        
                ant->x++;
            ant->look = RIGHT;
        }
        else if (ant->look == LEFT) {
            if (ant->y > 0)
                ant->y--;
            ant->look = UP;
        }
        else if (ant->look == RIGHT) {
            if (ant->y < y)
                ant->y++;
            ant->look = DOWN;
        }
    }
    /* Anti-clockwise */
    else if (isClockwise == '1') {
        if (ant->look == DOWN) {
            if (ant->x < x)
                ant->x++;
            ant->look = RIGHT;
        }
        else if (ant->look == UP) {
            if (ant->x > 0)
                ant->x--;
            ant->look = LEFT;
        }
        else if (ant->look == LEFT) {
            if (ant->y < y)
                ant->y++;
            ant->look = DOWN;
        }
        else if (ant->look == RIGHT) {
            if (ant->y > 0)
                ant->y--;
            ant->look = UP;
        }
    }

}