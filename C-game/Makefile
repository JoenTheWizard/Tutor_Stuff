#Oprional flag for GDB debugging
#GDBDB = -g
#Assignment requires C89
C89_F = -std=c89
make:
	gcc -fsanitize=leak $(C89_F) escape.c includes/terminal.c includes/random.c -o escape

#Make running it easier
run:
	./escape 45 20 2 2 10 10

#Borderless mode
borderless:
	./escape 45 20 2 2 10 10 --borderless