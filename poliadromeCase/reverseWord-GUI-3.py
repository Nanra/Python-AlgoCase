from tkinter import *
from tkinter import messagebox

## Section For Init
window = Tk()
window.title("Poliandrom Checker")
window.geometry('350x200')
lbl = Label(window, text="Input Word : ")
lbl.grid(column=0, row=2)
txt = Entry(window, width=20)
txt.grid(column=3, row=2)

## Button Checker
def clicked():
    val = txt.get()

    ## Section for Reverse Word
    wordReversed = ''
    for i in val:
        wordReversed = i + wordReversed
    if val.lower() == wordReversed.lower():
        note = 'Polindrome'
    else:
        note = 'Bukan Polindrome'

    ## Show Message Box
    messagebox.showinfo('Result Check', 'Keterangan : ' + note)

## Init Button Action
btn = Button(window, text="Check", command=clicked)
btn.grid(column=3, row=5)
 
window.mainloop()
