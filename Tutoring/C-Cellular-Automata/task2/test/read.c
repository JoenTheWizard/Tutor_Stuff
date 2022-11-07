#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../includes/color.h"
#include "../includes/newSleep.h"
#include "../includes/random.h"

FILE* fp;
char* line = NULL;
size_t len = 0;
size_t read;

char first_ant;
char second_ant;

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

/*
typedef enum {
    FIRST_ANT,
    SECOND_ANT,
    FILE
} TILE_SET_BY;

typedef struct {
    char tile_type;
    TILE_SET_BY set_by;
} TILE;
*/

/*
For coloring the grid:
Specifiy the struct and the enum to store each of the values.
Change 'image' variable to TILE**.
Then allocate that to the 2D array (eg. (TILE**)malloc(sizeof(TILE*) * cur_y)
and the same for x (eg.  image[i] = (TILE*)malloc(sizeof(TILE) * cur_x+1)).

Change the way we store variables (eg. image[LineNo - 3][alloc_x].tile_type = *c)

Change 'image' array to something like: image[first_ant_.y][first_ant_.x].tile_type

*/

ANT first_ant_;

/* Implement the second ant */
ANT second_ant_;

int x;
int y;

float time;
int steps;

char** image;
/*
TILE** image;
*/

char return_ant_look(ANT* ant);

void return_ant_turn(ANT* ant, char isClockwise);

int main(int argc, char** argv) {
    if (argc >= 3) {
        fp = fopen(argv[1], "r");
        steps = atoi(argv[2]);
        time = atof(argv[3]);
        if (fp == NULL)
            exit(EXIT_FAILURE);

        int LineNo = 0;
        while ((read = getline(&line, &len, fp)) != -1) {
            /*printf("%s", line);*/
            line[strcspn(line, "\n")] = '\0';

            char* c = strtok(line, " ");
            int a = 0;

            int cur_x = 0, cur_y = 0;

            /*
            Read from each string within the following while loop
            seperated by a space.
            Then we can determine the arguments specified within the file.
            */
            int alloc_x = 0;
            while (c != NULL) {
                /*
                Read for the first two arguments (which will be integers for the first 3 lines
                everything after the first three lines will be the grid)
                */
                if (a < 2 && LineNo < 3) {
                    /*printf("%i ", atoi(c));*/
                    if (a==0) cur_y = atoi(c);
                    if (a==1) cur_x = atoi(c);
                }
                else {
                    /*First ant will be stored at line number 1*/
                    if (LineNo == 1) {
                        first_ant = *c;
                        first_ant_.x = cur_x;
                        first_ant_.y = cur_y;
                        if (first_ant == '^')
                            first_ant_.look = UP;
                        else if (first_ant == '<')
                            first_ant_.look = LEFT;
                        else if (first_ant == '>')
                            first_ant_.look = RIGHT;
                        else if (first_ant == 'v')
                            first_ant_.look = DOWN;
                        
                        printf("\n== ANT 1 X: %i ANT 1 Y: %i ANT: %c == ", cur_x, cur_y, first_ant);
                    }
                    /*Second ant will be stored at line number 2*/
                    else if (LineNo == 2) {
                        second_ant = *c;
                        printf("\n== ANT 2 X: %i ANT 2 Y: %i ANT: %c == \n", cur_x, cur_y, second_ant);
                    }
                    else {
                        if (image != NULL) {
                            /*
                            Store each of the chacters within the array
                            */
                            image[LineNo - 3][alloc_x] = *c;
                            /*
                            image[LineNo - 3][alloc_x].tile_type = *c;
                            image[LineNo - 3][alloc_x].set_by = FILE;
                            */
                            alloc_x++;
                        }
                    }
                }

                c = strtok(NULL, " ");
                a++;
            }
            if (a < 3 && LineNo == 0) {
                /*Line Number 0 is where the size of the grid is displayed
                So we have to malloc for the 2d array
                */
                x = cur_x;
                y = cur_y;

                image = (char**)malloc(sizeof(char*) * cur_y);
                int i;
                for (i = 0; i < cur_y; i++)
                    image[i] = (char*)malloc(sizeof(char) * cur_x+1);

                /*
                image = (TILE**)malloc(sizeof(TILE*) * cur_y);
                int i;
                for (i = 0; i < cur_y; i++)
                    image[i] = (TILE*)malloc(sizeof(TILE) * cur_x+1);
                */
                printf("== Map X: %i Map Y: %i == ", cur_x, cur_y);
            }

            /*Increment the Line Number after each getline() call*/
            LineNo++;
        }

        char TILE_TYPE;
        TILE_TYPE = image[first_ant_.y][first_ant_.x];
        /*
        TILE_TYPE = image[first_ant_.y][first_ant_.y].tile;
        */

        /* Deploy the ant */
        if (first_ant_.y >= 0 && first_ant_.y <= y &&
            first_ant_.x >= 0 && first_ant_.x <= x)
            {
                image[first_ant_.y][first_ant_.x] = return_ant_look(&first_ant_);
                /*
                image[first_ant_.y][first_ant_.x].tile = return_ant_look(&first_ant_);
                */
            }

        int gameRun = 1;

        int gameRunSteps = 0;
        int k,j;
        while (gameRun) {
            system("clear");
            for (j = 0; j < y; j++) {
                    for (k = 0; k < x; k++) {
                        printf("%c ", image[j][k]);
                        /*
                        For the printing stuff here:
                        if (image[j][k].tile == '1' && image[j][k].set_by == FILE) {
                            setBackground("green");
                            printf(" ");
                            setBackground("reset")
                        }
                        else if (image[j][k].tile == '1' && image[j][k].set_by == FIRST_ANT) {
                            setBackground("red");
                            printf(" ");
                            setBackground("reset")
                        }
                        else {

                        }
                        */
                    }
                    printf("\n");
                }

            printf("CURRENT TILE: %c\n", TILE_TYPE);
            printf("GRID X: %i  GRID Y: %i\n", x, y);
            printf("X: %d  Y: %d\n", first_ant_.x, first_ant_.y);
            printf("STEPS: %i\n", gameRunSteps);

            newSleep(time);

            image[first_ant_.y][first_ant_.x] = TILE_TYPE == '0' ? '1' : '0';
            /*
            Replace the line above this with:
            image[first_ant_.y][first_ant_.x].tile_type = TILE_TYPE == '0' ? '1' : '0';
            image[first_ant_.y][first_ant_.x].set_by = FIRST_ANT;
            */
            return_ant_turn(&first_ant_, TILE_TYPE);
            TILE_TYPE = image[first_ant_.y][first_ant_.x];
            image[first_ant_.y][first_ant_.x] = return_ant_look(&first_ant_);
            /*
            Replace the line above this with:
            TILE_TYPE = image[first_ant_.y][first_ant_.x].tile;
            image[first_ant_.y][first_ant_.x].tile = return_ant_look(&first_ant_);
            */

            /* 
            FOR THE SECOND ANT STUFF BELOW:
            Initialize random 
            initRandom();

            //Second ant flipping the tiles
            image[second_ant.y][second_ant.x].tile = TILE_TYPE_2 == '0' ? '1' : '0';
            image[second_ant.y][second_ant.x].set_by = SECOND_ANT;

            //Returns a random direction the ant must go
            //Manage second ant's direction and position
            second_ant.look = random_val(LEFT, DOWN);
            if (second_ant.look == LEFT)
                second_ant.x--;
            else if (second_ant.look == RIGHT)
                second_ant.x++;


            //Obtain the tile for the second ant
            TILE_TYPE_2 = image[second_ant.y][second_ant.x].tile;

            //Deploy the second ant to the new direction
            image[second_ant.y][second_ant.x] = return_ant_look(&second_ant);
        */

            if (gameRunSteps == steps)
                gameRun = 0;

            gameRunSteps++;
        }

        int freeBufs;
        for (freeBufs = 0; freeBufs < y; freeBufs++)
            free(image[freeBufs]);
        
        free(image);

        /*
        You can set the above to this as well
        if (image) {
            free(image);
            image = NULL;
        }
        */

        fclose(fp);
        if (line)
            free(line);
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
            if (ant->x < x - 1)        
                ant->x++;
            ant->look = RIGHT;
        }
        else if (ant->look == LEFT) {
            if (ant->y > 0)
                ant->y--;
            ant->look = UP;
        }
        else if (ant->look == RIGHT) {
            if (ant->y < y - 1)
                ant->y++;
            ant->look = DOWN;
        }
    }
    /* Anti-clockwise */
    else if (isClockwise == '1') {
        if (ant->look == DOWN) {
            if (ant->x < x - 1)
                ant->x++;
            ant->look = RIGHT;
        }
        else if (ant->look == UP) {
            if (ant->x > 0)
                ant->x--;
            ant->look = LEFT;
        }
        else if (ant->look == LEFT) {
            if (ant->y < y - 1)
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