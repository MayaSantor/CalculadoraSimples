import tkinter as tk
from tkinter import *
from tkinter import ttk

janela = tk.Tk()

cor1 = "#F4DEB3" 
cor2 = "#F0EAAC"
cor3 = "#CCE0AC"
cor4 = "#FF8A8A"
janela.config(bg=cor1)
janela.geometry("235x310")

frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=5, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor2, fg=cor4)
app_label.place(x=0, y=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

def entrar_valores():
    resultado = eval('9/9')
    valor_texto.set(resultado)



b1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0,y=0)
b2 = Button(frame_corpo, command=lambda:entrar_valores('%'), text="%", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118,y=0)
b3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177,y=0)


b4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0,y=52)
b5 = Button(frame_corpo, text="8", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59,y=52)
b6 = Button(frame_corpo, text="9", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118,y=52)
b7 = Button(frame_corpo, text="*", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=177,y=52)

b8 = Button(frame_corpo, text="4", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0,y=104)
b9 = Button(frame_corpo, text="5", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59,y=104)
b10 = Button(frame_corpo, text="6", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118,y=104)
b11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x=177,y=104)


b12 = Button(frame_corpo, text="1", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0,y=156)
b13 = Button(frame_corpo, text="2", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59,y=156)
b14 = Button(frame_corpo, text="3", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118,y=156)
b15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=177,y=156)

b16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0,y=208)
b17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118,y=208)
b17 = Button(frame_corpo, text="=", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=177,y=208)




janela.mainloop()
