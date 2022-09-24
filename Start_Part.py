import tkinter
import os

if __name__ == '__main__':
    OS_TYPE = os.name
    if  OS_TYPE== 'nt':
        Windows_Forensics.start_forensics()
    elif OS_TYPE == 'posix':
        Linux_Forensics.start_forensics()
    else:
        quit()