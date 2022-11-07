CC = gcc
CFLAGS = -Wall -pedantic -ansi -g
OBJ = main.o random.o color.o newSleep.o
EXEC = ant

build :
	$(CC) main.c includes/*.c -o ant $(CFLAGS)

#Arguments
#grid X, grid Y, ant1 X, ant1 Y, time/seconds
run:
	./ant 10 15 5 3 0.5

clean :
	rm -f $(EXEC) $(OBJ)
