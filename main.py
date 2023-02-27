from datetime import datetime
from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox
from abc import ABC, abstractmethod

try:
    #LabeledEntry is to decorate the entry boxes as their default grey text inorder to enhance the user understanding.
    class LabeledEntry(tk.Entry):
        def __init__(self, master=None, label="Type here", **kwargs):
            tk.Entry.__init__(self, master, **kwargs)
            self.label = label
            self.on_exit()
            self.bind('<FocusIn>', self.on_entry)
            self.bind('<FocusOut>', self.on_exit)
    #This function erases the default grey text when the entry button is clicked. 
        def on_entry(self, event=None):
            if self.get() == self.label:
                self.delete(0, tk.END)
    #This function again filled the default text if we don't enter anything.
        def on_exit(self, event=None):
            if not self.get():
                self.insert(0, self.label)
    #This page shows the user the terms and conditions inorder to proceed to the store.
    class introductory_page:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1000x600")
            self.root.title("ONLINE SHOPPING STORE ")
            self.image2 = PhotoImage(file = "BGGG.png")
            self.intro = Frame(self.root,width=950,height=609,bg= "light green")
            self.contacts = Frame(self.root,width=1099,height = 20, bg = "grey")
            #The application window is no more resizeable.
            self.root.resizable(False,False)
            self.label3 = Label(self.intro,text=" "*20)
            self.label3.config(image = self.image2 ,width = 1300, height = 750)
            self.label3.pack()
            self.label1=Label(self.intro,text="                  "+"                CONTACT US                               "+"                    ",bg = "#363636", fg = "#C71585" ,font = "consolas 17 bold")
            self.label1.place(x=0,y=0)
            self.label2=Label(self.intro,text="☎:+923122211828     "+"          ✉:bilalarif1666@gmail.com           "+"       📌:Karachi          ",bg = "#363636", fg = "#C71585" ,font = "consolas 15")
            self.label2.place(x=0,y=28)
            self.image1 = PhotoImage(file = "LOGO.png")
            self.cont = Label(self.intro,image = self.image1)
            self.cont.place(x=20,y=70)
            self.label=Label(self.intro,text= "➡Welcome!! This site really helps you in shopping with ease and reasonable prices.",bg='#ff9342',fg = "#fff5db",font="lato 13 bold")
            self.label.place(x=20,y=310)
            self.label=Label(self.intro,text= "➡You acknowledge and recognize that we are a private commercial enterprise and reserve the right to conduct business \n  to achieve our objectives in a manner we deem fit.",bg='#ff9342',fg = "#fff5db",font="lato 13 bold")
            self.label.place(x=20,y=345)
            self.label=Label(self.intro,text= "➡The entire contents of the Site also are protected by copyright as a collective work under Pakistani copyright laws and \n international conventions. All rights are reserved..",bg='#ff9342',fg = "#fff5db",font="lato 13 bold")
            self.label.place(x=20,y=400)
            self.label4=Label(self.intro,text= "➡We shall neither be liable or responsible for any actions or inactions of any other service provider as listed on our Site"+"\n"+ "which includes but is not limited to payment providers, instalment offerings, warranty services amongst others.",bg='#ff9342',fg = "#fff5db",font="lato 13 bold")
            self.label4.place(x=20,y=460)
            self.agreement=Label(self.intro,text="➡BY PROCEDING TO NEXT PAGE ,YOU ARE ACCEPTING TO OUR ALL TERMS AND CONDITIONS.",fg="black",bg="#ff9342",font="lato 13 bold")
            self.agreement.place(x=20,y=515)
        #Thia class contains the login and sigup GUI widgets and their functions.
    class user_account:
        def __init__(self,obj1):
            self.root = obj.root
            self.obj1=obj1
            #This image is the background image.
            self.image2 = PhotoImage(file = "BGGG.png")
            self.f1_introductory = tk.Frame(self.root)

            self.label3 = Label(self.f1_introductory,text=" "*20)
            self.label3.config(image = self.image2 ,width = 1300, height = 750)
            self.label3.pack()
            self.LOGINLABEL=Label(self.f1_introductory,text="LOGIN/SIGNUP",fg="black",bg="#b5928e",font="consolas 20 bold").place(x=405,y=40)
            self.username = tk.Label(self.f1_introductory, text="USERNAME:", font="Consolas 15 bold",bg = "grey").place(x=450,y=110)
            self.username_entry = LabeledEntry(self.f1_introductory, label="Type username", font="Times 15", fg="grey")
            self.username_entry.place(x=400,y=150)
            self.password = tk.Label(self.f1_introductory, text="PASSWORD:", font="Consolas 15 bold",bg = "grey").place(x=450,y=190)
            self.pass_entry = LabeledEntry(self.f1_introductory, label="Type Password",show="*", font="Times 15", fg="grey")
            self.pass_entry.place(x=400,y=230)
            self.loginbutton = tk.Button(self.f1_introductory, text="Login", font="Consolas 15 bold", bg="blue", fg="yellow",command=self.login).place(x=470,y=280)
            #signup buttton stored all the personal information to the file.
            signupbutton=tk.Button(self.f1_introductory, text="Don't have an account(Sign Up)",font="Consolas 15 bold",bg="blue" ,fg="yellow",command=self.login_signup).place(x=330,y=330)
            #The f2_Signup frame contains all the signup entry boxes and the signup algorithm. 
            self.f2_Signup = tk.Frame(self.root)
            self.label4 = Label(self.f2_Signup,text=" "*20)
            self.label4.config(image = self.image2 ,width = 1300, height = 750)
            self.label4.pack()
            self.image3 = PhotoImage(file = "SAKO.png")
            self.sale = Label(self.f2_Signup,image = self.image3)
            self.sale.place(x=20,y=120)
            Label(self.f2_Signup, text="SIGNUP", font="Consolas 20 bold",bg="#b5928e",fg = "black").place(x=440,y=25)
            Newuser = tk.Label(self.f2_Signup, text="First name:", font="Consolas 15 bold",bg="grey",fg="black").place(x=430,y=70)
            self.Newuserfname = LabeledEntry(self.f2_Signup, label="Type Firstname", font="Times 15", fg="grey")
            self.Newuserfname.place(x=400,y=105)
            Newuserlname = tk.Label(self.f2_Signup, text="Last Name:", font="Consolas 15 bold",bg="grey",fg="black").place(x=433,y=140)
            self.Newuserlnameentry = LabeledEntry(self.f2_Signup, label="Type Last name", font="Times 15", fg="grey")
            self.Newuserlnameentry.place(x=400,y=175)
            Newuseradress = tk.Label(self.f2_Signup, text="Address:", font="Consolas 15 bold",bg="grey",fg="black").place(x=445,y=210)
            self.Newuseraddressentry = LabeledEntry(self.f2_Signup, label="Type Address", font="Times 15", fg="grey")
            self.Newuseraddressentry.place(x=400,y=245)
            self.back = tk.Button(self.f2_Signup, text="BACK", font="Consolas 15 bold", bg="blue", fg="yellow",command=self.f2tof1).place(x=10,y=10)
            self.Newuseremail = tk.Label(self.f2_Signup, text="Email adress:", font="Consolas 15 bold",bg="grey",fg="black").place(x=420,y=280)
            self.Newuseremailentry = LabeledEntry(self.f2_Signup, label="Type Your e-mail", font="Times 15", fg="grey")
            self.Newuseremailentry.place(x=400,y=315)
            Newuserph = tk.Label(self.f2_Signup, text="Phone number:", font="Consolas 15 bold",bg="grey",fg="black").place(x=415,y=350)
            self.Newuserphentry = LabeledEntry(self.f2_Signup, label="eg:03*********", font="Times 15", fg="grey")
            self.Newuserphentry.place(x=400,y=385)

            Newuseruname = tk.Label(self.f2_Signup, text="Username:", font="Consolas 15 bold",bg="grey",fg="black").place(x=443,y=420)
            self.usernameentry = LabeledEntry(self.f2_Signup, label="Type username", font="Times 15", fg="grey")
            self.usernameentry.place(x=400,y=455)
            Newuserpass = tk.Label(self.f2_Signup, text="Password:", font="Consolas 15 bold",bg="grey",fg="black").place(x=443,y=490)
            self.Newuserpassentry = LabeledEntry(self.f2_Signup, label="Type Password", show="*",font="Times 15", fg="grey")
            self.Newuserpassentry.place(x=400,y=525)
            signupbutton2 = tk.Button(self.f2_Signup, text="Sign Up", font="Consolas 15 bold", bg="blue", fg="yellow",
                                      command=self.saveinfo).place(x=448,y=555)
            self.label=Label(self.f2_Signup,text= '''"NOTE:ALL THE FOLLOWING INFORMATION \n IS MANDATORY FOR SIGNUP"''',bg="#b50000",fg = "white",font="lato 13 bold")
            self.label.place(x=600,y=45)
            C1 = Checkbutton(self.f2_Signup, text = "Keep notify me for upcoming discounts", font = "lato 12",
                     onvalue = "yes", offvalue = "no").place(x=38,y=80)

            self.font = ("Consolas", 14, "bold")
            #self.file = open("user_account_information.txt", "a+")
    
            self.image1 = PhotoImage(file = "proced.png")
            self.btn2=Button(self.obj1.intro,image = self.image1,command=self.turn_to_product).place(x=400,y=555)
            self.usernameofperson=""
        #This fnction is linked with the shopnow button and then proceed to the login window.
        def turn_to_product(self):
            obj.intro.pack_forget()
            self.f1_introductory.pack()
        #This function is linked with the back button which switches the signup window to login window.
        def f2tof1(self):
            self.f2_Signup.pack_forget()
            self.f1_introductory.pack()
        #This function is linked with the signup button which changes the login window to signup window.
        def login_signup(self):
            self.f1_introductory.pack_forget()
            self.f2_Signup.pack()
        #This function is linked with login button also verify the entered credentials and proceed to the store.
        def login(self):
            #user_account_information.txt contains all the credentials of all the existting users that have been regisered.
            mfile = open("user_account_information.txt", "r")
            myfile = mfile.readlines()
            self.my=mfile.readlines()
            username = self.username_entry.get()
            self.usernameofperson=username
            password = self.pass_entry.get()
            self.O = ''
            I = 'hg'
            #the following for loop is to compare each saved credentials with the input ones to login.
            for items in myfile:
                self.myfilesplit = items.split(";")
                for names in self.myfilesplit:
                    if username == self.myfilesplit[2] and password==self.myfilesplit[4] :
                        self.O = self.myfilesplit[2]
                        self.nameuser=names
                        # for passw in self.myfilesplit:
                        #     if password==self.myfilesplit[4]:
                        I=self.myfilesplit[4]
                        has.header.pack()
                        has.bottom.pack()
                        has.electronic_frame.pack()
                        has.usernamelogin["text"] = '''"Hello '''+(loginpage.usernameofperson).title()+'''🙂"'''
                        self.f1_introductory.pack_forget()
                        break
            #The following if else statements cecking the validity of inputs.
            if username == "" and password == "":
                messagebox.showerror("warning", "please enter user id and password")
            elif username != "" and password == "":
                messagebox.showerror("warning", "please insert password")
            elif username == "" and password != "":
                messagebox.showerror("warning", "enter user ID")
            elif I!=password and self.O!=username:
                messagebox.showerror("warning", "please enter correct password and user id")
        #is function is linked with the signup button and saves all the entered information to the user_account_information.txt  file in paricular format.

        def saveinfo(self):
            fname=self.Newuserfname.get()
            lname=self.Newuserlnameentry.get()
            useraddress=self.Newuseraddressentry.get()
            usrname=self.usernameentry.get()
            useremail=self.Newuseremailentry.get()
            password=self.Newuserpassentry.get()
            phonenumber=self.Newuserphentry.get()
            cr=0
            if fname!="Type Firstname" and lname!="Type Last name" and useraddress!="Type Address" and usrname!="Type username" and useremail!="Type Your e-mail" and password!="Type Password" and phonenumber!="Type Phonenumber":
                if ("@gmail.com" in useremail or "@hotmail.com" in useremail or "cloud.neduet.edu.pk" in useremail) and len(phonenumber)==11:
                    with open("user_account_information.txt", "r") as file:
                        filename = file.readlines()
                        for i in filename:
                            filesplitting = i.split(";")
                            for k in filesplitting:
                                if k == usrname:
                                    cr+=1
                                    messagebox.showerror("username exist",
                                                         "please use another username as it's already used by someone")
                    if cr==0:
                        with open("user_account_information.txt", "a+") as file:
                            file.write(f"{fname};{lname};{usrname};{useremail};{password};{phonenumber};{useraddress}; \n")

                        messagebox.showinfo("YOUR ACCOUNT CREATED SUCCESSFULLY🙂","username:"+usrname+"\npassword:"+password)
                        self.f2_Signup.pack_forget()
                        self.f1_introductory.pack()
                else:
                    messagebox.showerror("ATTENTION🥺","PLEASE INPUT A VALID E-MAIL ADDRESS AND PHONE NUMBER")
            else:
                messagebox.showerror("ATTENTION🥺","PLEASE FILL ALL THE REQUIRED INFORMATION")
            # print(fname,lname,useraddress,usrname,useremail,password,phonenumber)



    root=Tk()
    obj=introductory_page(root)
    obj.intro.pack()
    loginpage = user_account(obj)


    root.configure(background="grey")



    class Shopping_store(ABC):
        def __init__(self,root):
            self.root=root
            self.root.geometry("1000x600")
            self.header = Frame(self.root,width=1000,height=70,bg="#c60d2f")
            # self.header.pack()
            self.bottom=Frame(self.root,width=1000,height=200,bg="#15151d")
            # self.bottom.pack()
            self.imagge = PhotoImage(file = "LOGOO.png")
            self.logo = Label(self.header,image=self.imagge).place(x=10,y=10)
            self.introabel=Label(self.header,text="WELCOME TO THE E-COMMERCE STORE APPLICATION.",font="consolas 18 bold",fg="white",bg="#c60d2f")
            self.introabel.place(x=113,y=23)
            self.usernamelogin=Label(self.header,bg="#c60d2f",fg = "black",font="consolas 17 bold")
            self.usernamelogin.place(x=345,y=0)
            #self.usernamelogin["text"]= "hello"+loginpage.usernameofperson

            appliance = tk.Button(self.bottom,command=self.switch_to_garments)
            image = ImageTk.PhotoImage(file="APPLIANCES.jpg")
            appliance.config(image=image, width=200, height=100, bg="grey")
            appliance.image = image
            appliance.place(x=30,y=35)
            appliancelabel=Label(self.bottom,text="APPLIANCES",fg ="black",bg = "#c60d2f" ,font = "bold 12").place(x=50+25,y=150)

            electronic = tk.Button(self.bottom,command=self.switch_to_groccery)
            image = ImageTk.PhotoImage(file="ELECROLOGO.png")
            electronic.config(image=image, width=200, height=100, bg="grey")
            electronic.image = image
            electronic.place(x=280,y=35)
            electronic=Label(self.bottom,text="ELECTRONICS",fg ="black",bg = "#c60d2f",font = "bold 12").place(x=300+28,y=150)

            SPORTS = tk.Button(self.bottom, command=self.switch_to_electronic)
            image = ImageTk.PhotoImage(file="download.jpg")
            SPORTS.config(image=image, width=200, height=100, bg="grey")
            SPORTS.image = image
            SPORTS.place(x=280+250,y=35)
            SPORTS=Label(self.bottom,text="SPORTS",fg ="black",bg = "#c60d2f",font = "bold 12").place(x=550+50,y=150)

            GARMENT = tk.Button(self.bottom,command=self.switch_to_sports)
            image = ImageTk.PhotoImage(file="garment.jpg")
            GARMENT.config(image=image, width=200, height=100, bg="grey",font = "bold 12")
            GARMENT.image = image
            GARMENT.place(x=280+500,y=35)
            GARMENT=Label(self.bottom,text="GARMENTs",fg ="black",bg = "#c60d2f",font = "bold 12").place(x=760+80,y=150)
            self.sport_frame=Frame(self.root, width=1000, height=500, bg="white")
            self.image5 = PhotoImage(file = "SPORTSS.png")
            self.label3 = Label(self.sport_frame,text=" "*20)
            self.label3.config(image = self.image5 ,width = 1000, height = 500)
            self.label3.pack()
            # self.sport_frame.pack()
            self.garment_frame=Frame(self.root, width=1000, height=500, bg="white")
            self.image = PhotoImage(file = "GARMENTT.png")
            self.label4 = Label(self.garment_frame,text=" "*20)
            self.label4.config(image = self.image ,width = 1000, height = 500)
            self.label4.pack()
            # self.garment_frame.pack()
            self.electronic_frame = Frame(self.root, width=1000, height=500, bg="white")
            self.image6 = PhotoImage(file = "ELECTROO.png")
            self.label5 = Label(self.electronic_frame,text=" "*20)
            self.label5.config(image = self.image6 ,width = 1000, height = 500)
            self.label5.pack()
            # self.electronic_frame.pack()
            self.appliance_frame = Frame(self.root, width=1000, height=500, bg="white")
            self.image7 = PhotoImage(file = "APLIANCE.png")
            self.label7 = Label(self.appliance_frame,text=" "*20)
            self.label7.config(image = self.image7 ,width = 1100, height = 500)
            self.label7.pack()
            # self.appliance_frame.pack()

        #This Button is linked with the sports item when you selected the sports category to view. 
        def switch_to_electronic(self):
            self.sport_frame.pack()
            self.appliance_frame.pack_forget()
            self.electronic_frame.pack_forget()
            self.garment_frame.pack_forget()
        #This Button is linked with the garment item when you selected the garment category to view. 
        def switch_to_sports(self):
            self.sport_frame.pack_forget()
            self.appliance_frame.pack_forget()
            self.electronic_frame.pack_forget()
            self.garment_frame.pack()
        #This Button is linked with the elecronic item when you selected the electronic category to view. 
        def switch_to_groccery(self):
            self.sport_frame.pack_forget()
            self.appliance_frame.pack_forget()
            self.electronic_frame.pack()
            self.garment_frame.pack_forget()
        #This Button is linked with the appliance item when you selected the appliance category to view. 
        def switch_to_garments(self):
            self.sport_frame.pack_forget()
            self.appliance_frame.pack()
            self.electronic_frame.pack_forget()
            self.garment_frame.pack_forget()
        @abstractmethod
        def log_outbtn(self):
            pass
    #This class only worked for saving and viewing the sopping history.
    class shopping_history(Shopping_store):
        def __init__(self,root):
            super().__init__(root)
            self.payment_process=Frame(self.root,width=1000,height=500,bg= "grey")
            self.canvasforbill = Canvas(self.payment_process, width=500, height=450,bg="white")
            self.totalamount = Label(self.canvasforbill, text=" ",font="bold 25")
            self.totalamount.place(x=100, y=350)
            self.pop = 0
            self.negativel=0
            self.canvasforbill.place(x=190, y=35)
            self.canvasforbill.create_text(100, 100)

            self.loguotbtn=Button(self.header,text="log out",font ="bold",bg = "blue",fg = "yellow",command=self.log_outbtn)
            self.loguotbtn.place(x=730,y=20)

            shoppingcart_label=Label(self.header,text="Your Cart",font = "arial 10",fg = "yellow",bg = "black" ).place(x=898,y=46)
            self.asus = tk.Button(self.header,command=self.shoppn_cartfunc)
            image = ImageTk.PhotoImage(file="icons8-trolley-64.png")
            self.asus.config(image=image, width=50, height=35, bg="grey")
            self.asus.image = image
            self.asus.place(x=900,y=5)

            #This buton contains the command of viewing history.
            self.history=Button(self.payment_process,text="My history",command=self.user_history,font ="bold",bg = "blue",fg = "yellow")
            self.history.place(x=800,y=250)
            file=open("customer_shopping_history.txt","r")
            self.files=file.readlines()
        #This funcion is linked with the view hisory button and showing the viewer his shopping history..
        def user_history(self):
            p = ''
            for l in self.files:
                listing_inh = l.split(";")
                if listing_inh[2]==loginpage.usernameofperson:
                    for k in range(len(listing_inh)):
                        p+=listing_inh[k] +" "
                    p+="\n"
            ws=Tk()
            ws.geometry("1000x600")
            ws.resizable(False,False)
            ws.title("YOUR HISTORY")
            v = Scrollbar(ws, orient='vertical')
            v.pack(side=RIGHT, fill='y')

            textbox=Text(ws,height=150,width=1000,yscrollcommand=v.set)

            textbox.insert('end', p)
            textbox.config(state='disabled')
            v.config(command=textbox.yview)
            textbox.pack(expand=True)
        #This function is linked with the shopping cart icon which shows the user his current shopping cart and also the user able to edit them. 
        def shoppn_cartfunc(self):
            self.sport_frame.pack_forget()
            self.appliance_frame.pack_forget()
            self.electronic_frame.pack_forget()
            self.garment_frame.pack_forget()
            self.bottom.pack_forget()
            self.payment_process.pack()

    #This class contains functions related to checkout and logout. 
    class final_payment_lock(shopping_history, Shopping_store):
        shoppeddata = []
        def finalprocess(self):
            self.payment_locked=Frame(self.root ,width=1000,height=700)
            self.image2 = PhotoImage(file = "CARTT.png")
            self.label3 = Label(self.payment_locked,text=" "*20)
            self.label3.config(image = self.image2 ,width = 1000, height = 700)
            self.label3.pack()
            self.buttnpayment = Button(self.payment_process,text= "BACK TO STORE",font ="bold",bg = "blue",fg = "yellow",command=self.backtopayment).place(x=32,y=350)

            self.proceedbtn=Button(self.payment_process,text= "CONFIRM ORDER",font ="bold",bg = "blue",fg = "yellow",command=self.payment).place(x=32,y=455)
        #This funcion is linked with the back to store button which enables the user to back to store and add itms to cart.
        def backtopayment(self):
            self.payment_process.pack_forget()
            self.bottom.pack()
            self.electronic_frame.pack()
        #This function is linked with the logout button which logged out the user.
        def log_outbtn(self):
            a=messagebox.askquestion("log_out","do you want to log out")
            if a =="yes":
                loginpage.f1_introductory.pack()
                self.header.pack_forget()
                self.electronic_frame.pack_forget()
                self.sport_frame.pack_forget()
                self.bottom.pack_forget()
                self.appliance_frame.pack_forget()
                self.garment_frame.pack_forget()
                self.payment_process.pack_forget()
                self.payment_locked.pack_forget()
                self.calculation=0
                self.initializer=0
                # try:
                #     self.cardin['text']=''
                # except AttributeError as p:
                #     messagebox.showerror(type(p),p)
                loginpage.username_entry.delete(0,END)
                loginpage.pass_entry.delete(0,END)
                self.placement_y=0
                has.totalamount['text']=''
##                has.pop=0
        def __str__(self):
            return str(has.pop)
        #This funcion is linked with the confirm order button after which the confirmaion and order relevan details displayed to the user. 
        def payment(self):
            self.payment_process.pack_forget()
            ofile=open("user_account_information.txt", "r+")
            userfile=ofile.readlines()
            lo=""
            lst_ind=''

            rit = ''
            po = ''
            now = datetime.now()
            for k in self.shoppeddata:
                po += k + "\n"
                rit += ";" + k
            for k in userfile:
                us=k.split(";")

                for j in us:

                    if loginpage.usernameofperson==j :
                        lo=f"{us[0]};{us[1]};{us[2]}"
                        Label(self.payment_locked, text=f"dear {us[0] +  us[1] }" ,bg='#ff9342',fg = "#fff5db",font="lato 13 bold").place(x=50, y=50)
                        Label(self.payment_locked, text=f"your email {us[3]}",bg='#ff9342',fg = "#fff5db",font="lato 13 bold").place(x=50, y=80)
                        Label(self.payment_locked, text=f"Your contact number {us[5]}",bg='#ff9342',fg = "#fff5db",font="lato 13 bold").place(x=50, y=110)
                        Label(self.payment_locked, text=f"YOUR ORDERED WILL BE PLACED AT {us[6]} in few days",bg='#ff9342',fg = "#fff5db",font="lato 13 bold").place(x=50,
                                                                                                                     y=140)
                        Label(self.payment_locked, text=f"your order\n {po}\n{has.pop}").place(x=680, y=50)

                        Label(self.payment_locked, text=now,bg='#ff9342',fg = "#fff5db",font="lato 13 bold").place(x=50, y=25)



            self.payment_locked.pack()
            myfile=open("customer_shopping_history.txt","a")
            myfile.write(lo+""+rit+ " "+ ",total amount = "+str(has.pop) + " ,"+ str(now) + "\n")
    #This class contains all the products.
    class products:
        class sports:
            xi=60
            def __init__(self,imaging,A,B):
                #working for electronic side
                self.A=A
                image = ImageTk.PhotoImage(file=A)
                re = Button(imaging, text="i'm here ", fg="black", borderwidth=10, command=B)
                re.config(image=image, width=130, height=180, bg="black")
                re.image = image
                re.place(x=products.sports.xi , y=40)
                products.sports.xi += 180

        class garments:
            xi=60
            def __init__(self,imaging,A,B):
                #working for sports side
                image = ImageTk.PhotoImage(file=A)
                re = Button(imaging,text = "I am here",fg="black",borderwidth=10,command=B)
                re.config(image=image, width=130, height=180, bg="black")
                re.image = image

                re.place(x=products.garments.xi , y=40)
                products.garments.xi += 180

        class electronic:
            xi=60
            def __init__(self,imaging,A,B):
                #working for sports side
                re = Button(imaging,fg="black",borderwidth=10,command=B)
                image = ImageTk.PhotoImage(file=A)
                re.config(image=image, width=130, height=180, bg="black")
                re.image = image

                re.place(x=products.electronic.xi , y=40)
                products.electronic.xi += 180

        class appliance:
            xi=60
            def __init__(self,imaging,A,B):
                #working for electronic side

                re = Button(imaging,text="i'm here ",fg="red",borderwidth=10,command=B)
                self.A=A
                image = ImageTk.PhotoImage(file=A)
                re = Button(imaging, text="i'm here ", fg="black", borderwidth=10, command=B)
                re.config(image=image, width=130, height=180, bg="black")
                re.image = image


                re.place(x=products.appliance.xi , y=40)
                products.appliance.xi += 180


    has=final_payment_lock(root)
    has.finalprocess()

    #This class is for displaying the producs and details.
    class shopping_products(Shopping_store):

        placement_x=20
        placement_y = 25

        def __init__(self,product_name,frame_name,price):
            super().__init__(root)
            self.price=price

            self.product_name=product_name
            self.calculation = 0
            self.bulletl=Label(frame_name, font="bold 10",text = "Quantity: "+"0",bg = "grey",fg = "white")
            self.bulletl.place(x=shopping_products.placement_x+75, y=300)

            self.label1 = Label(frame_name,text = self.product_name,font = "arial 12 bold",bg = "black",fg = "white")
            self.label1.place(x=shopping_products.placement_x+58+5, y=13)

            self.label2 = Label(frame_name,text = "Rs."+str(self.price),font = "arial 12 bold",bg = "black",fg = "white")
            self.label2.place(x=shopping_products.placement_x+70+5, y=248)


            self.cardburn=Button(frame_name, text="Add To Cart",font = "bold 10", bg="orange",command=self.cartinfo)
            self.cardburn.place(x=shopping_products.placement_x+70, y=275)

            self.cardin = Label(has.canvasforbill, text="",bg="white")
            shopping_products.placement_x += 180

            if shopping_products.placement_x>820:
                shopping_products.placement_x=20

        def yeht(self):

            self.calculation+=1
            self.bulletl["text"]="Quantity: "+str(self.calculation)
        #This function associated with the Add to Cart algorithm. 
        def cartinfo(self):
            self.initializer = self.calculation
            if self.initializer==0:
                messagebox.showinfo("select item","please click on pictures to select the quantity")
            if self.initializer>0:


                #This funcion is linked with the addition of items to the cart.
                def positivebtn():
                    if self.initializer >=1:
                        self.initializer+=1
                        has.pop+=self.price
                        has.totalamount["text"] = "Total Amount = "+str(has.pop)
                        self.cardin["text"] = f"{self.product_name} " + "  quantity   " + str(
                            self.initializer) + f" amount = {self.price * self.initializer} "
                        o=0
                        b=0

                        for pr in has.shoppeddata:

                            if self.product_name in pr:
                                has.shoppeddata.pop(o)
                            o += 1

                            if self.product_name not in pr:
                                b+=1

                        if b<=len(has.shoppeddata):
                            has.shoppeddata.append(f"{self.product_name} " + "  quantity   " + str(self.initializer) + f" amount = {self.price * self.initializer} ")
                #This funcion is linked with the removal of items to the cart.
                def negativebtn():
                    self.initializer -= 1

                    if self.initializer == 0:
                        has.pop -= self.price
                        has.totalamount["text"] = "Total Amount = "+str(has.pop)
                        self.cardin["text"]=''
                        self.cardburn["state"]="active"
                        has.shoppeddata.pop(has.shoppeddata.index(f"{self.product_name} " + "  quantity   " + str(1) + f" amount = {self.price * 1} "))

                        self.positivebutton.destroy()
                        self.negativebutton.destroy()
                        if has.pop==0:
                            has.totalamount["text"] = ""
                            has.totalamount["bg"] = "white"
                    elif self.initializer >=1:

                        has.pop -= self.price
                        has.totalamount["text"] = "Total Amount = "+str(has.pop)
                        self.cardin["text"] = f"{self.product_name} " + "  quantity   " + str(
                            self.initializer) + f" amount = {self.price * self.initializer} "

                        o = 0
                        b = 0
                        self.oi=0
                        for pr in has.shoppeddata:

                            if self.product_name in pr:
                                has.shoppeddata.pop(o)
                                break
                            o += 1
                            self.oi=o

                        for pr in has.shoppeddata:
                            if self.product_name not in pr:
                                b += 1
                        if b <= len(has.shoppeddata):

                            has.shoppeddata.append(f"{self.product_name} " + "  quantity   " + str(
                            self.initializer) + f" amount = {self.price * self.initializer} ")



                self.cardin["text"]=f"{self.product_name} " + "  quantity   " + str(self.calculation) + f" amount = {self.price*self.calculation} "
                has.pop+=self.price*self.calculation

                has.shoppeddata.append(f"{self.product_name} " + "  quantity   " + str(1) + f" amount = {self.price * 1} ")
                has.totalamount["text"] ="Total Amount = "+str(has.pop)
                self.cardin.place(x=120, y=shopping_products.placement_y)
                self.cardburn["state"]= "disabled"
                self.initializer=self.calculation

                self.rate=0

                self.negativebutton = Button(has.canvasforbill,command=negativebtn)
                image1 = ImageTk.PhotoImage(file="MINUS.png")
                self.negativebutton.config(image=image1, width=13, height=13, bg="grey")
                self.negativebutton.image = image1
                self.negativebutton.place(x=400,y=shopping_products.placement_y - 5)

                self.positivebutton = Button(has.canvasforbill,command=positivebtn)
                image2 = ImageTk.PhotoImage(file="PLUS.png")
                self.positivebutton.config(image=image2, width=13, height=13, bg="yellow")
                self.positivebutton.image = image2
                self.positivebutton.place(x=430,y=shopping_products.placement_y -
                                                  5)

            #xtra
    ##        self.negativebutton = Button(has.canvasforbill, text ="-",command=negativebtn).place(x=400,
    ##3                                                                                            y=shopping_products.placement_y - 5)
    ##        self.positivebutton = Button(has.canvasforbill, text = "+" ,command=positivebtn).place(x=430,
    ##                                                                                            y=shopping_products.placement_y - 5)
                shopping_products.placement_y += 20
        #This button associated with logou algorihm. 
        def log_outbtn(self):
            self.cardin.destroy()
            has.totalamount.destroy()
             


    football_in=shopping_products("Football", has.sport_frame, 1313)
    batcr_in=shopping_products("Cricket Bat", has.sport_frame, 1234)
    basketball_in=shopping_products("Basketball", has.sport_frame, 3213)
    hockey_in=shopping_products("Hockey", has.sport_frame, 5000)
    ball_in=shopping_products("Tennis Ball", has.sport_frame, 500)

    footballs=products.sports(has.sport_frame, "FoOTBALL.png", football_in.yeht)
    batcr=products.sports(has.sport_frame, "BAT.png", batcr_in.yeht)
    basketball=products.sports(has.sport_frame, "BASKET.png", basketball_in.yeht)
    hockey=products.sports(has.sport_frame, "HOCKEY.png", hockey_in.yeht)
    ball=products.sports(has.sport_frame, "BALL.png", ball_in.yeht)

    # extra = additions(3,2)
    kurta_in=shopping_products("Longcoat", has.garment_frame, 2433)
    coat_in=shopping_products("Men Blazer", has.garment_frame, 3455)
    longcoat_in=shopping_products("Cool Hoody", has.garment_frame, 3411)
    tshirt_in=shopping_products("T-SHIRT", has.garment_frame, 900)
    pent_in=shopping_products("Men Jeans", has.garment_frame, 1500)


    kurta=products.garments(has.garment_frame, "LONGCOAT.png", kurta_in.yeht)
    coat=products.garments(has.garment_frame, "SIUT.png", coat_in.yeht)
    longcoat=products.garments(has.garment_frame, "HOODY.png", longcoat_in.yeht)
    tshirt=products.garments(has.garment_frame, "SHIRT.png", tshirt_in.yeht)
    pent=products.garments(has.garment_frame, "JEANS.png", pent_in.yeht)


    
    laptop=shopping_products("HP Laptop", has.electronic_frame, 50000)
    mobile=shopping_products("Mobile Phone", has.electronic_frame, 15000)
    desktop=shopping_products("LED 55 inch", has.electronic_frame, 1500)
    headphones=shopping_products("Headphones", has.electronic_frame, 788)
    speaker=shopping_products("DSLR Camera", has.electronic_frame, 15700)

    laptop_in=products.electronic(has.electronic_frame, "LAPTOP.png", laptop.yeht)
    mobile_in=products.electronic(has.electronic_frame, "MOBILE.png", mobile.yeht)
    desktop_in=products.electronic(has.electronic_frame, "TV.png", desktop.yeht)
    headphones_in=products.electronic(has.electronic_frame, "HEADPHONES.png", headphones.yeht)
    speaker_in=products.electronic(has.electronic_frame, "CAMERA.png", speaker.yeht)

    toaster=shopping_products("Bread Toaster", has.appliance_frame, 20000)
    tv=shopping_products("Vaccum Cleaner", has.appliance_frame, 20000)
    fridge=shopping_products("Automatic Fridge", has.appliance_frame, 20000)
    washer=shopping_products("Smart Washer", has.appliance_frame, 20000)
    coffee_maker=shopping_products("Coffee Maker", has.appliance_frame, 20000)

    toaster_in=products.appliance(has.appliance_frame, "TOASTER.png", toaster.yeht)
    tv_in=products.appliance(has.appliance_frame, "VACCUM.png", tv.yeht)
    fridge_in=products.appliance(has.appliance_frame, "FRID.png", fridge.yeht)
    washer_in=products.appliance(has.appliance_frame, "WASHER.jpg", washer.yeht)
    coffer_maker_in=products.appliance(has.appliance_frame, "COFFEE.png", coffee_maker.yeht)
    dunder = final_payment_lock(root)

    loginpage.root.mainloop()

    print(dunder)


except  SyntaxError as e:
    print(type(e),e)
except FileNotFoundError  as i:
    print(type(i),i)
except NameError as l:
    print(type(l),l)
