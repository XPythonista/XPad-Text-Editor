#For 32-bit windows os

import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\USER\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\USER\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("XPad.py", base=base, icon="notes.ico")]


cx_Freeze.setup(
    name = "XPad",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["notes.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "2022.0.0",
    description = "Tkinter Application",
    executables = executables
    )