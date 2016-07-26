from tkinter import *
from tkinter import ttk

root=Tk()
root.title('Circuit Simulator')

mainframe=ttk.Frame(root, width=600,height=400,borderwidth=2, relief='sunken')
mainframe.grid(column=0,row=0, padx=5, pady=5)

circuitframe=ttk.Frame(mainframe, width=300,height=300,relief='raised')
circuitframe.grid(column=0,row=0)

componentframe=ttk.Frame(mainframe, width=200, height=300, relief = 'raised')
componentframe.grid(column=1, row=0)

detailsframe=ttk.Frame(mainframe, width=510, height=75, relief='raised')
detailsframe.grid(column=0, row=1, columnspan=2, sticky=W)


cifheader=ttk.Label(mainframe, text='Circuit Diagram')
cofheader=ttk.Label(mainframe, text='Components')
defheader=ttk.Label(mainframe, text='Circuit Details')

cifheader.grid(column=0, row=0, sticky=(N,W))
cofheader.grid(column=1, row=0, sticky=(N,W))
defheader.grid(column=0, row=1, sticky=(N,W))

for child in mainframe.winfo_children():
	if child.winfo_class() == 'TLabel':
		child.grid_configure(padx=10,pady=10)
	else:
		child.grid_configure(padx=5,pady=5)
root.mainloop()
