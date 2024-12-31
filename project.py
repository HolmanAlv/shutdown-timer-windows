from os import system
from tkinter import *
from tkinter import ttk


def plus_timer():
    ...

def minus_timer():
    ...

def shutdown():
    time = input("tiempo: ")
    try:
        system(f"shutdown -s -t {time}")
    except: ValueError
    

def view():

    root = Tk(screenName="Timer")
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    #ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    #ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frame, text="Prueba", command=shutdown).grid(column=1, row=0)

    root.mainloop()

def main():
    view()
    param = "hola mundo"
    #Apargar windows shutdown -s -t [tiempo para que se apague, en segundos]
    #cancelar apagado shutdown -a
    system(f"echo {param}")

if __name__ == "__main__":
    main()
