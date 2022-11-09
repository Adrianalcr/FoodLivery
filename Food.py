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
        sf.input = Button(sf.mainf2,text="ENTRAR NO SISTEMA",command=lambda:sf.Login(),cursor='hand2',bd=2,font=("coooper black", 10,'bold'),fg="white",bg="black")
        sf.input.place(x=250,y=15)
        sf.mainf2.pack(fill=BOTH,expand=1)

        sf.scr.mainloop()

    #Área de Login
    def Login(sf):
        sf.scr.destroy()
        sf.scr=Tk()

        sf.scr.geometry("1366x768")
        sf.scr.title("Pizzaria FoodLivery :")
        sf.scr.iconbitmap('p.ico')

        # Logo
        sf.loginf1 = Frame(sf.scr,height=150,width=1366)
        sf.logo = PhotoImage(file="logo.png")
        sf.log = Label(sf.loginf1,image=sf.logo, height=150).place(x=0,y=0)  

        #Botões
        sf.home = Button(sf.loginf1,text="Home",command=lambda:sf.main(),cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="white",bg="blue")
        sf.home.place(x=800,y=100) 

        sf.adm = Button(sf.loginf1,text="Administração",cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="black",bg="white")
        sf.adm.place(x=925,y=100) 

        sf.about = Button(sf.loginf1,text="Sobre Nós",cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="black",bg="white")
        sf.about.config(command=lambda:sf.sobre())
        sf.about.place(x=1210,y=100) 

        #Data e Hora
        sf.localtime  = time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.loginf1,text=sf.localtime,fg="white",font=("default",16),bg="#0b1335")
        sf.tim.place(x=925,y=50) 
        sf.loginf1.pack(fill=BOTH,expand=1) 

        # Backgrround Fundo
        sf.loginf2 = Frame(sf.scr, height=618,width=1366)
        sf.c = Canvas(sf.loginf2, height=618,width=1366)        
        sf.c.pack()    
        sf.bkground = PhotoImage(file="pizza3.png")        
        sf.c.create_image(683,309,image=sf.bkground)

        #Formulário Login
        sf.c.create_rectangle(50,100,700,450,fill="#d3ede6",outline="white",width=5)
        sf.log=Label(sf.loginf2,text="Administração: Login",fg="white",bg="#0b1335",width=31,font=("cooper black",26))
        sf.log.place(x=59,y=105) 

        sf.lab1=Label(sf.loginf2,text="Usuário :",bg="#d3ede6",font=("cooper black",22))
        sf.lab1.place(x=100,y=180)        
        sf.user=Entry(sf.loginf2,bg="white",font=("cooper black",22),bd=1,justify='left')
        sf.user.place(x=320,y=180)     

        sf.lab2=Label(sf.loginf2,text="Senha :",bg="#d3ede6",font=("cooper black",22))
        sf.lab2.place(x=105,y=250) 
        sf.pasd=Entry(sf.loginf2,bg="white",font=("cooper black",22),bd=1,justify='left')
        sf.pasd.place(x=320,y=250) 

        sf.lg = Button(sf.loginf2,text="ENTRAR",fg="white",bg="black",cursor='hand2',font=("coooper black", 20),bd=1)
        sf.lg.place(x=310,y=320) 

        sf.reg = Button(sf.loginf2,text="REGISTRAR",command=lambda:sf.Form(),fg="white",bg="black",cursor='hand2',font=("coooper black", 20),bd=1)
        sf.reg.place(x=450,y=320)  

        sf.loginf2.pack(fill=BOTH,expand=1)   
        sf.scr.mainloop() 

    #Informação Sobre
    def sobre(sf):
        sf.scr1=Tk()
        sf.scr1.geometry("400x550")
        sf.scr1.config(bg="light pink")
        sf.scr1.title("Sobre Nós")
        sf.scr1.iconbitmap('p.ico')
        sf.la=Label(sf.scr1,font=("cooper black",20),bg="light pink",text="\n Pizzaria FoodLivery \n Seja Bem-vindo\n\n Telefone de Contato\n (00)0000-0000\n\n Ligue para fazer seu pedido.\n\n Abrimos de segunda à sexta\n 9:00 AM as 22:00 PM.\n\n Sábado e Domingo \n 10:00 AM as 3:00 AM.\n\n by: Adriana Lima")
        sf.la.pack() 
        sf.scr1.mainloop()

    #Área de Cadastro
    def Form(sf):
        sf.scr.destroy()
        sf.scr=Tk()

        #Ícone
        sf.scr.geometry("1366x768")
        sf.scr.title("Pizzaria FoodLivery :")
        sf.scr.iconbitmap('p.ico')

        #Logo
        sf.form = Frame(sf.scr,height=150,width=1366)
        sf.logo = PhotoImage(file="logo.png")
        sf.log = Label(sf.form,image=sf.logo, height=150).place(x=0,y=0)  
        
        #Botões 
        sf.home = Button(sf.form,text="Home",command=lambda:sf.main(),cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="white",bg="blue")
        sf.home.place(x=800,y=100) 

        sf.adm = Button(sf.form,text="Administração",cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="black",bg="white")
        sf.adm.place(x=950,y=100) 

        sf.about = Button(sf.form,text="Sobre Nós",cursor='hand2',bd=2,font=("coooper black", 16,'bold'),fg="black",bg="white")
        sf.about.config(command=lambda:sf.sobre())
        sf.about.place(x=1210,y=100) 

        #Data e Hora
        sf.localtime  = time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.form,text=sf.localtime,fg="white",font=("default",16),bg="#0b1335")
        sf.tim.place(x=950,y=50) 
        sf.form.pack(fill=BOTH,expand=1) 

        #Formulário Cadastro
        sf.form2 = Frame(sf.scr, height=618,width=1366)
        sf.c = Canvas(sf.form2, height=618,width=1366)        
        sf.c.pack()

        #Background Fundo
        sf.logo2 = PhotoImage(file="pizza3.png")        
        sf.c.create_image(683,309,image=sf.logo2)

        #Fomrulário Registro
        sf.c.create_rectangle(150,100,1216,450,fill="#d3ede6",outline="white",width=5)
        sf.log=Label(sf.form2,text="Registrar Usuário:",fg="white",bg="#0b1335",width=53,font=("cooper black",26))
        sf.log.place(x=150,y=105) 

        sf.lab1=Label(sf.form2,text="Nome :",bg="#d3ede6",font=("cooper black",18))
        sf.lab1.place(x=190,y=200)  
        sf.name=Entry(sf.form2,bg="white",width=15,font=("cooper black",18),bd=1)
        sf.name.place(x=430,y=200)     

        sf.lab2=Label(sf.form2,text="Sobrenome :",bg="#d3ede6",font=("cooper black",18))
        sf.lab2.place(x=730,y=200) 
        sf.sobrenome=Entry(sf.form2,bg="white",width=15,font=("cooper black",18),bd=1)
        sf.sobrenome.place(x=920,y=200) 

        sf.lab3=Label(sf.form2,text="Usuário :",bg="#d3ede6",font=("cooper black",18))
        sf.lab3.place(x=190,y=250) 
        sf.usern=Entry(sf.form2,bg="white",width=15,font=("cooper black",18),bd=1)
        sf.usern.place(x=430,y=250) 
        
        sf.lab4=Label(sf.form2,text="Senha :",bg="#d3ede6",font=("cooper black",18))
        sf.lab4.place(x=730,y=250) 
        sf.passwd=Entry(sf.form2,bg="white",width=15,font=("cooper black",18),bd=1)
        sf.passwd.place(x=920,y=250) 

        sf.lab5=Label(sf.form2,text="Email :",bg="#d3ede6",font=("cooper black",18))
        sf.lab5.place(x=190,y=300) 
        sf.email=Entry(sf.form2,bg="white",width=15,font=("cooper black",18),bd=1)
        sf.email.place(x=430,y=300) 

        
        sf.lab6=Label(sf.form2,text="Telefone :",bg="#d3ede6",font=("cooper black",18))
        sf.lab6.place(x=730,y=300) 
        sf.tel=Entry(sf.form2,bg="white",width=15,font=("cooper black",18),bd=1)
        sf.tel.place(x=920,y=300) 

        #Botões 
        sf.vt = Button(sf.form2,text="VOLTAR",command=lambda:sf.Login(),fg="white",bg="black",cursor='hand2',font=("coooper black", 20),bd=1)
        sf.vt.place(x=370,y=370)

        sf.lg = Button(sf.form2,text="CADASTRAR",fg="white",bg="black",cursor='hand2',font=("coooper black", 20),bd=1)
        sf.lg.place(x=610,y=370)

        sf.clear = Button(sf.form2,text="LIMPAR",fg="white",bg="black",cursor='hand2',font=("coooper black", 20),bd=1)
        sf.clear.place(x=910,y=370)              
        
        sf.form2.pack(fill=BOTH,expand=1)   
        sf.scr.mainloop()




x=Food()
x.main()