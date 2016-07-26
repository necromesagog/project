from tkinter import *
from tkinter import ttk

root = Tk()

l =ttk.Label(root,text="Starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<l>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<Double-l>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='Right button drag to %d, %d' % (e.x, e.y)))

root.mainloop()
