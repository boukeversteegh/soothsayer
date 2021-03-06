import os

try:
    # Windows variant
    import msvcrt
    
    def get_character():
        """Reads a single character from user input"""
        return str(msvcrt.getch().decode())

except ImportError:
    # Unix variant
    import sys, tty, termios

    def get_character():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return str(ch)

def clear():
    """Clears the screen"""
    os.system(['clear','cls'][os.name == 'nt'])


def command(command,piped = False):

    if piped:
        result = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE).communicate()[0].decode()
    else:
        f = open('TiMBL_output','w')
        result = subprocess.Popen(command, shell=True,stdout=f,stderr=f)
        result.wait()

    return(result)