#MY minesweeper
from tkinter import *
from random import randrange
field=[]
frame=[]
button=[]
def create(xsize, ysize):                        #создаем пустое поле
    field = [[0] * xsize for b in range(ysize)]
    return (field)
moves=0
def fielding(*args):           #minen - колво мин, xsize и ysize, длина
    xsize=int(x_entry.get())
    ysize=int(y_entry.get())
    minen=int(m_entry.get())
    field = create(xsize,ysize)
    size=xsize*ysize
    if minen <= size:
        i=minen                                  #ставим мины
        while i!=0:
            j=randrange(1,size+1)
            if j%xsize==0:
                y = j//xsize
            else:
                y = j//xsize +1
            x=j-xsize*(y-1)
            if field[y-1][x-1]!=-1:
                field[y-1][x-1]=-1
                i-=1
    else:                                        #ошибка, если слишком много
        raise ValueError('Too many mines!')
    for i in range(0,xsize):                     #длинная проверка и расстановка чисел
        for j in range(0,ysize):
            if (j!=0 and j!=ysize-1) and (i!=0 and i!=xsize-1):
                if field[j][i]!=-1:
                    k=0
                    if field[j-1][i-1]==-1:
                        k+=1
                    if field[j-1][i]==-1:
                        k+=1
                    if field[j][i-1]==-1:
                        k+=1
                    if field[j][i+1]==-1:
                        k+=1
                    if field[j+1][i]==-1:
                        k+=1
                    if field[j+1][i+1]==-1:
                        k+=1
                    if field[j+1][i-1]==-1:
                        k+=1
                    if field[j-1][i+1]==-1:
                        k+=1
                    field[j][i]=k
            if j==0 and (i!=0 and i!=xsize-1):
                if field[j][i]!=-1:
                    k=0
                    if field[j][i-1]==-1:
                        k+=1
                    if field[j][i+1]==-1:
                        k+=1
                    if field[j+1][i]==-1:
                        k+=1
                    if field[j+1][i+1]==-1:
                        k+=1
                    if field[j+1][i-1]==-1:
                        k+=1
                    field[j][i]=k
            if j==ysize-1 and (i!=0 and i!=xsize-1):
                if field[j][i]!=-1:
                    k=0
                    if field[j-1][i-1]==-1:
                        k+=1
                    if field[j-1][i]==-1:
                        k+=1
                    if field[j][i-1]==-1:
                        k+=1
                    if field[j][i+1]==-1:
                        k+=1
                    if field[j-1][i+1]==-1:
                        k+=1
                    field[j][i]=k
            if (j!=0 and j!=ysize-1) and i==0:
                if field[j][i]!=-1:
                    k=0
                    if field[j-1][i]==-1:
                        k+=1
                    if field[j][i+1]==-1:
                        k+=1
                    if field[j+1][i]==-1:
                        k+=1
                    if field[j+1][i+1]==-1:
                        k+=1
                    if field[j-1][i+1]==-1:
                        k+=1
                    field[j][i]=k
            if (j!=0 and j!=ysize-1) and i==xsize-1:
                if field[j][i]!=-1:
                    k=0
                    if field[j-1][i-1]==-1:
                        k+=1
                    if field[j-1][i]==-1:
                        k+=1
                    if field[j][i-1]==-1:
                        k+=1
                    if field[j+1][i]==-1:
                        k+=1
                    if field[j+1][i-1]==-1:
                        k+=1
                    field[j][i]=k
            if i==0 and j==0:
                if field[j][i]!=-1:
                    k=0
                    if field[j][i+1]==-1:
                        k+=1
                    if field[j+1][i]==-1:
                        k+=1
                    if field[j+1][i+1]==-1:
                        k+=1
                    field[j][i]=k
            if j==0 and i==xsize-1:
                if field[j][i]!=-1:
                    k=0
                    if field[j][i-1]==-1:
                        k+=1
                    if field[j+1][i]==-1:
                        k+=1
                    if field[j+1][i-1]==-1:
                        k+=1
                    field[j][i]=k
            if j==ysize-1 and i==0:
                if field[j][i]!=-1:
                    k=0
                    if field[j-1][i]==-1:
                        k+=1
                    if field[j][i+1]==-1:
                        k+=1
                    if field[j-1][i+1]==-1:
                        k+=1
                    field[j][i]=k
            if j==ysize-1 and i==xsize-1:
                if field[j][i]!=-1:
                    k=0
                    if field[j-1][i]==-1:
                        k+=1
                    if field[j][i-1]==-1:
                        k+=1
                    if field[j-1][i-1]==-1:
                        k+=1
                    field[j][i]=k 
    return field                                #создано поле в виде массива
def CH(i,field):
    def click():
        xsize=int(x_entry.get())
        ysize=int(y_entry.get())
        k=i//xsize
        j=i-k*xsize
        button[i].config(text=field[k][j])         # Отображаем игровую ситуацию
        if field[k][j] == 0:
            button[i].config(text=' ', bg='#ccb', state=DISABLED)
        elif field[k][j] == -1:
            button[i].config(text='\u2665')
            loss=Label(text='Вы проиграли.')
            loss.pack()
            for b in range(xsize*ysize):
                button[b].config(state=DISABLED)
                k=b//xsize
                j=b-k*xsize
                if field[k][j]==-1:
                    button[b].config(text='\u2665')

    return click

def game(*args):
    xsize=int(x_entry.get())
    ysize=int(y_entry.get())
    field=fielding()
    for i in range(0, ysize):                         # Размещаем кнопки
        frame.append(Frame())
        frame[i].pack(expand=YES, fill=BOTH)
        for j in  range(0, xsize):
            button.append(Button(frame[i], text=' ',
                            font=('mono', 16, 'bold'),
                            width=3, height=1))
            button[i*xsize+j].pack(side=LEFT, expand=NO, fill=Y)
            button[i*xsize+j].bind('<Button-3>', lambda event, n=i*xsize+j: marker(n))
    for i in range(0,xsize*ysize):
        button[i].config(command=CH(i,field))
def marker(n):
    button[n].config(text='\u2661')
xsize=0
ysize=-1
minen=2
tk = Tk()
tk.title('Sweeper')
mframe = Frame(tk)
greet=Label( text=' Добро пожаловать в Сапер!')
ch1=Label(text='Размеры поля:')
x_entry = Entry( width=7, textvariable=xsize)
xsize=StringVar()
y_entry = Entry( width=7, textvariable=ysize)
ysize=StringVar()
ch2=Label( text='Количество мин:')
m_entry = Entry( width=7, textvariable=minen)
minen=StringVar()
greet.pack()
ch1.pack()
x_entry.pack()
y_entry.pack()
ch2.pack()
m_entry.pack()

but=Button( text="Создать", command=game)
but.pack()
tk.mainloop()
