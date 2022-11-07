#include <stdio.h>
#include <stdlib.h>
/*This is the includes from the given template*/
#include "includes/terminal.h"
#include "includes/random.h"

#define MAX_BORDER_SIZE 100

#define RESET \u001b[0m
/*Remember we can use a pointer as an array as they store values at certain
memory addresses.*/
char** image;

/* Is borderless mode? */
int BORDERLESS = 0;

/*Function to check if player hit the goal*/
int check_if_got_goal(int p_x, int p_y, int g_x, int g_y);

/*Function to check if player hit an obstacle*/
void check_if_hit_obstacle(char** img, int p_x, int p_y, int* gameState);

int main(int argc, char** argv) {
    /*First convert the char array input to integer*/
    if (argc >= 5) {
        int x = atoi(argv[1]) > MAX_BORDER_SIZE ? MAX_BORDER_SIZE : atoi(argv[1]);
        int y = atoi(argv[2]) > MAX_BORDER_SIZE ? MAX_BORDER_SIZE : atoi(argv[2]);

        int player_x = atoi(argv[3]);
        int player_y = atoi(argv[4]);

        int goal_x = atoi(argv[5]);
        int goal_y = atoi(argv[6]);

        if (argc >= 8) {
            if (!strcmp(argv[7],"--borderless"))
                BORDERLESS = 1;
        }

        /*Implement the goal coordinates argument when running the program*/
        if (x < 5 || y < 5) {
            printf("Error: Please enter a valid width or height (must be 5 or greater)\n");
            return 1;
        }
        
        /*First create the rows. Each row will have a column allocated within it*/
        image = (char**)malloc(sizeof(char*)*y);

        /*Now we make more arrays within each row, these will be the columns*/
        int i;
        for (i = 0; i < y; i++)
            image[i] = (char*)malloc(sizeof(char)*x+1);

        int j,k;
            for (j = 0; j < y; j++) {
                for (k = 0; k < x; k++) {
                    /*Create the border*/
                    if (j == 0 || j == y - 1)
                        image[j][k] = BORDERLESS ? ' ' : '*';
                    else if ((k == 0 || k == x - 1))
                        image[j][k] = BORDERLESS ? ' ' : '*';
                    else if (k == player_x && j == player_y)
                        image[j][k] = 'P';
                    else if (k == goal_x && j == goal_y)
                        image[j][k] = 'G';
                    else
                        image[j][k] = ' ';
                }
            }

        int gameRun = 1;
        while (gameRun) {
            /*Clear the screen and display image*/
            system("clear");
            for (j = 0; j < y; j++) {
                for (k = 0; k < x; k++)
                    printf("%c", image[j][k]);
                printf("\n");
            }
            printf("X: %i Y: %i\n",player_x,player_y);
            printf("GOAL X: %i GOAL Y: %i\n",goal_x,goal_y);
            printf("W to up\nA to go left\nS to go down\nD to go right\nQ to quit\n");

            if (check_if_got_goal(player_x, player_y, goal_x, goal_y)) {
                printf("\e[42m!!! YOU WON !!!\e[0m\n");
                gameRun = 0;
            }

            /*Deal with the player movement */
            disableBuffer();
            char in = getchar();
            if (in == 'q')
                gameRun = 0;
            else {
                switch (in) {
                    /*Player movement key inputs and then deal with modifying the buffer*/
                    case 'd':
                        image[player_y][player_x] = ' ';
                        if (player_x < x - 2)
                            player_x++;
                        check_if_hit_obstacle(image, player_x, player_y, &gameRun);
                        image[player_y][player_x] = 'P';
                        /*
                        Push into the list after the player has moved
                        push_l(list, player_x, player_y);
                        */
                        break;
                    case 'w':
                        image[player_y][player_x] = ' ';
                        if (player_y > 1)
                            player_y--;
                        check_if_hit_obstacle(image, player_x, player_y, &gameRun);
                        image[player_y][player_x] = 'P';
                        break;
                    case 's':
                        image[player_y][player_x] = ' ';
                        if (player_y < y - 2)
                            player_y++;
                        check_if_hit_obstacle(image, player_x, player_y, &gameRun);
                        image[player_y][player_x] = 'P';
                        break;
                    case 'a':
                        image[player_y][player_x] = ' ';
                        if (player_x > 1)
                            player_x--;
                        check_if_hit_obstacle(image, player_x, player_y, &gameRun);
                        image[player_y][player_x] = 'P';
                        break;
                    case 'u':
                        /*
                        pop from the list
                        and make the player x and player y
                        equal to the list's head node

                        Get the head node's current X and Y pos:
                        list->head->x
                        list->head->y
                        */
                        break;
                }
            }
            /*Randomly place obstacles*/
            initRandom();
            int rand_y = random_(1,y-2);
            int rand_x = random_(1,x-2);
            image[rand_y][rand_x] = 'X';
        }

        enableBuffer();
        /*Now to deallocate the buffers.
        Because we created a double pointer we would need to also deallocated
        the buffers within the double pointer array*/
        int freeBuffers;
        for (freeBuffers = 0; freeBuffers < y; freeBuffers++)
            free(image[freeBuffers]);

        free(image);
    }
    else
        printf("Error: Not enough given arguments\nUsage: ./escape <row_map> <col_map> <row_player> <col_player> <row_goal> <col_goal>\n");
    
    /*
    Deallocate the list here
    */
    return 0;
}

int check_if_got_goal(int p_x, int p_y, int g_x, int g_y) {
    return (p_x == g_x && p_y == g_y) ? 1 : 0;
}

void check_if_hit_obstacle(char** img, int p_x, int p_y, int* gameState) {
    if (img[p_y][p_x] == 'X') {
        printf("\e[43m!!! GAME OVER !!!\e[0m");
        *gameState = 0;
    }
}
