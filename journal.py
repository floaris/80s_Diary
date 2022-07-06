
from tkinter import * 
import tkinter as tk
import tkinter as Tkinter
from tkinter.font import Font
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

def save():
	file=filedialog.asksaveasfile(defaultextension='.txt',
	filetypes=[
		("Text file",".txt"),
		("All files", ".*"),
	]

	)
	filetext=str(text.get(1.0, END))
	file.write(filetext)
	file.close()
    

root=tk.Tk()
root.geometry('1000x900')
save=Tkinter.Button(root,text="ENREGISTRER", command=save)
save.pack()
text=tk.Text(width=1000, height=900, font=("Times New Roman", 15), bg='black',fg='green')
text.pack()    
root.mainloop()
