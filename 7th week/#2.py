#2
from tkinter import *
def ans():
    ans_label.config(text='Blade of Miquella')
fr = Tk()
fr.geometry('200x100')
fr.title('Отринь свои глупые амбции')
label=Label(fr, text='I am Malenia')
button=Button(fr, text='who?', command=ans)
ans_label=Label(fr, text='')
label.pack()
button.pack()
ans_label.pack()
fr.mainloop()