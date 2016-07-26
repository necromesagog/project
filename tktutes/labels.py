from tkinter import *
from tkinter import ttk

def plusone(*args):
	enterPresses.set(int(enterPresses.get())+1)

root=Tk()
root.title("Label tests")

mainframe=ttk.Frame(root)
mainframe.grid(column=0, row=0, padx=5,pady=5, sticky=(N,W,E,S))

enterPresses = StringVar()
enterPresses.set(0)
textlabel = ttk.Label(mainframe, text='Times pressed Enter:')
textlabel.grid()
numberlabel = ttk.Label(mainframe, textvariable=enterPresses)
numberlabel.grid(column=1, row=0, padx=10)

root.bind('<Return>', plusone)

root.mainloop()
