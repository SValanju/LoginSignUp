#Login and Sign In without DB

from tkinter import *
from tkinter.ttk import *

class Main():
    def __init__(self,parent):
        self.parent=parent
        self.parent.title("Login")

        self.page=StringVar()
        self.loginName=StringVar()
        self.loginPass=StringVar()
        self.signinName=StringVar()
        self.signinPass=StringVar()
        self.sts=StringVar()

        self.createWidgets()
        self.showLogin()

    def createWidgets(self):
        Label(self.parent,textvariable=self.page,font=("",20)).pack()
        
        frame1=Frame(self.parent)
        Label(frame1,text="Username").grid(sticky=W)
        Entry(frame1,textvariable=self.loginName).grid(row=0,column=1,pady=10)
        Label(frame1,text="Password").grid(sticky=W)
        Entry(frame1,textvariable=self.loginPass,show="*").grid(row=1,column=1,pady=10)
        Button(frame1,text="Login",command=self.login).grid(padx=20,pady=10)
        Button(frame1,text="Sign In",command=self.signIn).grid(row=2,column=1,pady=10)
        frame1.pack(padx=10,pady=10)
        frame2=Frame(self.parent)
        Label(frame2,text="Username").grid(sticky=W)
        Entry(frame2,textvariable=self.signinName).grid(row=0,column=1,pady=10,padx=10)
        Label(frame2,text="Password").grid(sticky=W)
        Entry(frame2,textvariable=self.signinPass,show="*").grid(row=1,column=1)
        Button(frame2,text="Create",command=self.create).grid(padx=20,pady=10)
        Button(frame2,text="Back",command=self.showLogin).grid(row=2,column=1,pady=10)
        frame3=Frame(self.parent)
        Label(frame3,text="Logged In",font=("",50)).pack(padx=10,pady=10)
        self.loginFrame=frame1
        self.signinFrame=frame2
        self.logedFrame=frame3
        Label(self.parent,textvariable=self.sts).pack()

    def login(self):
        name=self.loginName.get()
        password=self.loginPass.get()
        try:
            f=open("savedata","r")
            cname,cpass=f.read().split(",")
            if name==cname and password==cpass:
                self.showLoged()
            else:
                self.sts.set("Wrong Username or Password")
        except:
            self.sts.set("Wrong Username or Password")

    def signIn(self):
        self.page.set("Sign In")
        self.loginFrame.pack_forget()
        self.signinFrame.pack()

    def showLogin(self):
        self.page.set("Login")
        self.signinFrame.pack_forget()
        self.loginFrame.pack()

    def showLoged(self):
        self.loginFrame.pack_forget()
        self.logedFrame.pack()

    def create(self):
        name=self.signinName.get()
        password=self.signinPass.get()
        f=open("savedata","w")
        f.write("{0},{1}".format(name,password))
        f.close()
        self.showLogin()

if __name__=="__main__":
    root=Tk()
    root.title("Login")
    root.geometry("810x350+200+200")
    root.resizable(width=FALSE, height=FALSE)
    Label(root, text="Developed By Webmaster Guru",
            foreground="white",
            background="dark Red",
            font="Helvetica 30 bold").pack(pady=10)
    Main(root)
    root.mainloop()
