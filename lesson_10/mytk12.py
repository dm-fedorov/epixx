import tkinter

def click():
    label.config ( text=entry.get() )
    

window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

entry = tkinter.Entry(frame)
entry.pack()

label = tkinter.Label(frame)
label.pack()

button = tkinter.Button(frame, text='Печать!', command=click) 
button.pack()

window.mainloop()
