from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python Aufgaben")
root.geometry("320x250")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill=BOTH)

frames = []
for i in range(5):
    f = ttk.Frame(notebook)
    f.pack(fill=BOTH, expand=True, padx=10, pady=10)
    notebook.add(f, text=f"Aufgabe {i+1}")
    frames.append(f)

Label(frames[0],text="Aufgabe 1:\n""Diese Aufgabe gibt mit einer while-Schleife\n""die Zahlen von 10 bis 1 aus.",
    justify=LEFT).pack(anchor=W, pady=5)

def aufgabe1():
    text1.delete(1.0, END)
    zahl = 10
    while zahl >= 1:
        text1.insert(END, f"{zahl}\n")
        zahl -= 1

Button(frames[0], text="Start", command=aufgabe1).pack(pady=5)
text1 = Text(frames[0], height=10)
text1.pack(fill=BOTH, expand=True)

Label(frames[1],text="Aufgabe 2:\n""Der Benutzer gibt eine Zahl ein.\n""Das Programm berechnet die Fakultät dieser Zahl.",
    justify=LEFT).pack(anchor=W, pady=5)

def fakultaet(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def aufgabe2():
    n = int(entry2.get())
    label2.config(text=f"Fakultät von {n} = {fakultaet(n)}")

entry2 = Entry(frames[1])
entry2.pack(pady=5)

Button(frames[1], text="Berechnen", command=aufgabe2).pack()
label2 = Label(frames[1], text="")
label2.pack(pady=5)

Label(frames[2],text="Aufgabe 3:\n""Der Benutzer gibt einen Satz ein.\n""Das Programm zählt die Anzahl der Vokale (a, e, i, o, u).",
    justify=LEFT).pack(anchor=W, pady=5)

def aufgabe3():
    text3.delete(1.0, END)
    satz = entry3.get().lower()
    vokale = "aeiou"
    count = 0

    for buchstabe in satz:
        if buchstabe in vokale:
            count += 1

    text3.insert(END, f"Anzahl der Vokale: {count}")

entry3 = Entry(frames[2], width=40)
entry3.pack(pady=5)

Button(frames[2], text="Zählen", command=aufgabe3).pack()
text3 = Text(frames[2], height=5)
text3.pack(pady=5)

Label(frames[3],text="Aufgabe 4:\n""Der Benutzer gibt Zahlen ein.\n""Bei Eingabe von 0 wird die Summe aller Zahlen ausgegeben.",
      justify=LEFT).pack(anchor=W, pady=5)

summe = 0

def aufgabe4():
    global summe
    zahl = int(entry4.get())
    entry4.delete(0, END)

    if zahl == 0:
        label4.config(text=f"Summe = {summe}")
        summe = 0
    else:
        summe += zahl

entry4 = Entry(frames[3])
entry4.pack(pady=5)

Button(frames[3], text="Zahl eingeben", command=aufgabe4).pack()
label4 = Label(frames[3], text="")
label4.pack(pady=5)

Label(frames[4],text="Aufgabe 5:\n""In einer gegebenen Liste wird gezählt,\n""wie oft die Zahl 3 vorkommt.",
      justify=LEFT).pack(anchor=W, pady=5)

def aufgabe5():

    liste = [2,2,3,3,1,2,1,1,3,2,2,3,1,3,1,2,3,2,2,1,2,2,1,3,1,1,2,1,1,3,3,1,2,1,1,3,2,3,1,3,1,2,1,3,1,2,2,1,2,3,3,2,3,2,3,3,3,3,1,2,3,2,3,1,3,1,3,3,3,1,2,1,1,3,2,1,2,3,2,1,3,2,3,1,2,3,1,3,3,3,1,1,1,2,2,1,1,2,3,3]
    count = 0

    for n in liste:
        if n == 3:
            count += 1

    label5.config(text=f"Die Zahl 3 kommt {count} mal vor.")

Button(frames[4], text="Zählen", command=aufgabe5).pack(pady=10)
label5 = Label(frames[4], text="")
label5.pack()

root.mainloop()