import platform
import os

global arc

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

def check_python_architecture():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 32BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING HARRYv6 ')
        import data.HARRY32
        data.HARRY32
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 64BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING HARRYv6 ')
        import data.HARRY64
        data.HARRY64
    else:
        arc = "INVALID"


if __name__ == "__main__":


check_python_architecture()

check_python2_architecture()
arc ="32BIT"


check_python_architecture() 

arc = "82bit"
