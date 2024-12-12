from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("550x600")
root.title("Catatan")
root.config(bg="orange")
root.resizable(False,False)

def simpan_file():
    buka_file=filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if buka_file is None:
        return
    teks=str(entry.get(1.0,END))
    buka_file.write(teks)
    buka_file.close()

def buka_file():
    file=filedialog.askopenfile(mode="r",filetypes=[("text files", "*.txt")])
    if file is not None:
        konten=file.read()
    entry.insert(INSERT, konten)

t1=Button(root,width="20",height="2",bg="white",text="Simpan",command=simpan_file).place(x=100,y=5)
t2=Button(root,width="20",height="2",bg="white",text="Buka File",command=buka_file).place(x=300,y=5)

entry=Text(root,height="33",width="66",wrap=WORD)
entry.place(x=10,y=60)


root.mainloop()