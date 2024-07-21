import sys, tty, termios

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setraw(sys.stdin.fileno())

ch = sys.stdin.read(1)

termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
print(ord(ch))
