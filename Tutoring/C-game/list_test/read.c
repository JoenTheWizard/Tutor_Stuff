#include <stdio.h>
#include <stdlib.h>
#include <string.h>
FILE* fp;
char* line = NULL;
size_t len = 0;
size_t read;

int main(int argc, char** argv) {
    /*
    This part here should be at the beginning of the program
    */
    fp = fopen(argv[1], "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        /*printf("%s", line);*/
        line[strcspn(line, "\n")] = '\0';

        char* c = strtok(line, " ");
        int a = 0;

        int cur_x = 0, cur_y = 0;
        while (c != NULL) {
            if (a < 2) {
                printf("%i ", atoi(c));
                if (a==0) cur_x = atoi(c);
                if (a==1) cur_y = atoi(c);
            }
            else {
                printf("%s ", c);
                if (!strcmp(c,"X")) {
                    printf("\n== Obstacle X: %i Obstacle Y: %i == ", cur_x, cur_y);
                }
                else if (!strcmp(c,"P")) {
                    printf("\n== Player X: %i Player Y: %i == ", cur_x, cur_y);
                }
                else if (!strcmp(c,"G")) {
                    printf("\n== Goal X: %i Goal Y: %i == ", cur_x, cur_y);
                }
            }
            c = strtok(NULL, " ");
            a++;
        }
        if (a < 3) {
            printf("\n== Map X: %i Map Y: %i == ", cur_x, cur_y);
        }
        /*printf("\n== X: %i Y: %i == ", cur_x, cur_y);*/
        printf("\n");
    }

    /*
    This here should be at the end of the main function of the program
    It closes the file buffer and deallocates the buffer
    */
    fclose(fp);
    if (line)
        free(line);

    return 0;
}