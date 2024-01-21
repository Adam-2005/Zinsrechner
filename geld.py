#-import--------------
import tkinter as tk

#-def-----------------
def berechnung():
    try:
        #-dim-Block-----------
        Anlagsbetrag = float(rootAnlagsbetrag.get())
        zinssatz = float(rootZinssatz.get())
        minJahre = int(rootmMinJahre.get())

        #-Zahlen-formatiren---
        Anlagsbetrag = round(Anlagsbetrag,2)
        zinssatz = zinssatz/100

        #-Berechnung
        zinsertrag = Anlagsbetrag * (1 + zinssatz) ** minJahre
        ergebnisLabel.config(text=f"Zinsertrag nach {minJahre} Jahren: {zinsertrag:.2f} Euro")
    
    except ValueError:
        ergebnisLabel.config(text="erro")

#-Eingabe-------------
root = tk.Tk()
root.title("Zinsrechnung")

rootAnlagsbetrag = tk.Entry(root)
rootZinssatz = tk.Entry(root)
rootmMinJahre = tk.Entry(root)

btnBerechnen =tk.Button(root, text="Berechnen", command=berechnung)

#-Ausgabe-------------
ergebnisLabel = tk.Label(root, text="Ergebnis wird hier angezeigt")

#-Grid----------------
tk.Label(root,text="Anlagsbetrag:").grid(row=1, column=0)
rootAnlagsbetrag.grid(row=1, column=1)
tk.Label(root,text="Zinssatz:").grid(row=2, column=0)
rootZinssatz.grid(row=2, column=1)
tk.Label(root,text="MinJahre:").grid(row=3, column=0)
rootmMinJahre.grid(row=3, column=1)
tk.Label(root,text="Berechnen:").grid(row=4, column=0)
btnBerechnen.grid(row=4, column=1)
tk.Label(root,text="ergebnis:").grid(row=5, column=0)
ergebnisLabel.grid(row=5, column=1)

root.mainloop()