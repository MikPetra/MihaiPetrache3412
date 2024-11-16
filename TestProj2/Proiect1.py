from tkinter import *
from tkinter import messagebox

afisaj = Tk()
afisaj.title("Salutare")
#afisaj.geometry("350x200")
Label(afisaj,text="Nume", font=('Times New Roman',12)).grid(row=0)
Label(afisaj, text="Prenume", font=('Arial',12),justify="left").grid(row=1)
nume = Entry(afisaj,bg="red", fg="blue",font=('Times New Roman',12,"bold"))
nume.grid(row=0, column=1)
prenume = Entry(afisaj,bg="blue", fg="red",font=('Times New Roman',12,"bold"))
prenume.grid(row=1, column=1)

def intampinare():
    nume_intampinare = nume.get()
    prenume_intampinare = prenume.get()
    messagebox.showinfo("Intampinare", f"Salut, {nume_intampinare} {prenume_intampinare}")

Button(afisaj, text = "Intampinare", command= intampinare).grid(row=2, columnspan=2)

mainloop()