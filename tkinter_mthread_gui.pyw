#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Trying to create a multithreaded app with Tk. Main module
"""

import sys
import select

#check Python version:
if sys.version.split()[0][0] == '2':
    import Tkinter as tk
elif sys.version.split()[0][0] == '3':
    import tkinter as tk
else:
    print "Невозможно определить установленную версию интерпретатора Python"
    exit()
#---------------------
root = tk.Tk()

S = tk.StringVar()
S.set("TEXT")

S2 = tk.StringVar()
S2.set("TEXT")

L = tk.Label(root, textvariable=S, width=50, height=3)
L.pack()

L2 = tk.Label(root, textvariable=S2)
L2.pack()

B = tk.Button(root, text = "НАЖМИ МЕНЯ")
B.pack()
B.bind("<Button-1>", shift_lbl)

root.mainloop()
