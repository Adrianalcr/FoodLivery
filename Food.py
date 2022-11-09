from cProfile import label
from cgitb import text
from tkinter import*
import time
import random
from tkinter import messagebox
from turtle import bgcolor, color

class Food:
    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr=Tk()
        except:
            try:
                sf.scr=Tk()   
            except:
                pass 

        # Ícone do Sistema
        sf.scr.geometry("1366x768")
        sf.scr.title("Pizzaria FoodLivery :")
        sf.scr.iconbitmap('p.ico')

        # Logo
        sf.mainf1 = Frame(sf.scr,height=150,width=1366)
        sf.logo = PhotoImage(file="logo.png")
        sf.l = Label(sf.mainf1,image=sf.logo)
        sf.l.place(x=0,y=0)
        sf.mainf1.pack(fill=BOTH,expand=1)

        # Backgrround Fundo
        sf.mainf2 = Frame(sf.scr, height=618,width=1366)
        sf.c = Canvas(sf.mainf2, height=618,width=1366)        
        sf.c.pack()
        sf.back = PhotoImage(file="pizza3.png")        
        sf.c.create_image(683,284,image=sf.back)

        # Botão Menu
        sf.input = Button(sf.mainf2,text="MENU",command=lambda:sf.Login(),cursor='hand2',bd=2,font=("coooper black", 10,'bold'),fg="white",bg="black")
        sf.input.place(x=250,y=15)
        sf.mainf2.pack(fill=BOTH,expand=1)

        sf.scr.mainloop()

    def Login(sf):
        sf.scr.destroy()
        sf.scr=Tk()

        sf.scr.geometry("1366x768")
        sf.scr.title("Pizzaria FoodLivery :")
        sf.scr.iconbitmap('p.ico')

        sf.loginf1 = Frame(sf.scr,height=150,width=1366)
        sf.logo = PhotoImage(file="logo.png")
        sf.log = Label(sf.loginf1,image=sf.logo, height=150).place(x=0,y=0)  

        sf.home = Button(sf.loginf1,text="Home",command=lambda:sf.main(),cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="white",bg="blue")
        sf.home.place(x=800,y=100) 

        sf.adm = Button(sf.loginf1,text="Administração",cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="black",bg="white")
        sf.adm.place(x=925,y=100) 

        sf.about = Button(sf.loginf1,text="Sobre Nós",cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="black",bg="white")
        sf.about.place(x=1210,y=100) 

        sf.localtime  = time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.loginf1,text=sf.localtime,fg="white",font=("default",16),bg="#0b1335")
        sf.tim.place(x=925,y=50) 
        sf.loginf1.pack(fill=BOTH,expand=1) 

        sf.loginf2 = Frame(sf.scr, height=618,width=1366)
        sf.c = Canvas(sf.loginf2, height=618,width=1366)        
        sf.c.pack()

        #sf.back = PhotoImage(file="pizza4.png")        
        #sf.c.create_image(683,284,image=sf.back)


        #sf.logo2 = PhotoImage(file="pizza3.png")        
        #sf.c.create_image(683,309,image=sf.logo2)


x=Food()
x.main()