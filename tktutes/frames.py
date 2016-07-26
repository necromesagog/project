from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Frames")

frame = ttk.Frame(root, width=200, height=200)
frame['borderwidth'] = 2
frame['relief'] = 'sunken'
frame.grid(column=0, row=0, padx=10, pady=10, sticky=(N,W,E,S))

frame2 = ttk.Frame(root, width = 300, height=100)
frame2['borderwidth'] = 10
frame2['relief'] = 'groove'
frame2.grid(column=0,row=1, padx=5,pady=5, sticky=(N,W,E,S))


frame3 = ttk.Frame(frame, width=20, height=20)
frame3['relief'] = 'raised'
frame3.grid(column=0,row=0, sticky=N)

root.mainloop()
