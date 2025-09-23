from tkinter import*
from tkinter import ttk
import random,os,tempfile
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import smtplib as s
from pdf_mail import sendpdf
from time import strftime
def main():
   win=Tk()
   app=Login_Window(win)
   #app=StoreManagementSystem(win)
   win.mainloop()





class Login_Window:
     def __init__(self,root):
       self.root=root
       self.root.title("Login")
       self.root.geometry("1550x800+0+0")

       self.bg=ImageTk.PhotoImage(file=r"C:\Tushar\StoreMag\pexels-simon-berger-1323550.jpg")

       lbl_bg=Label(self.root,image=self.bg)
       lbl_bg .place(x=0,y=0,relwidth=1,relheight=1)
       self.new_window = None  # Initialize new_window attribute

       frame=Frame(self.root,bg='black')
       frame.place(x=610,y=170,width=340,height=450)

       img1=Image.open(r"C:\Tushar\StoreMag\kisspng-computer-icons-user-profile-person-5abd85306ff7f7.0592226715223698404586.jpg")
       img1=img1.resize((100,100),Image.LANCZOS)
       self.photoimg1=ImageTk.PhotoImage(img1)
       lblimg1=Label(image=self.photoimg1,borderwidth=0,bg="black")
       lblimg1.place(x=730,y=175,width=100,height=100)


       get_str=Label(frame,text="GET STARTED",font=("times new roman",20,"bold"),fg="white",bg="black")
       get_str.place(x=70,y=100)

       #=======Label========
       username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
       username.place(x=70,y=155)

       self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
       self.txtuser.place(x=40,y=180,width=270)

       password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
       password.place(x=70,y=225)

       self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
       self.txtpass.place(x=40,y=250,width=270)

       #======================Icon   Images========================

       
       img2=Image.open(r"C:\Tushar\StoreMag\username logo.jpg")
       img2=img2.resize((25,25),Image.LANCZOS)
       self.photoimg2=ImageTk.PhotoImage(img2)
       lblimg2=Label(image=self.photoimg2,borderwidth=0,bg="black")
       lblimg2.place(x=650,y=323,width=25,height=25)

       
       img3=Image.open(r"C:\Tushar\StoreMag\password logo.png")
       img3=img3.resize((25,25),Image.LANCZOS)
       self.photoimg3=ImageTk.PhotoImage(img3)
       lblimg3=Label(image=self.photoimg3,borderwidth=0,bg="black")
       lblimg3.place(x=650,y=394,width=25,height=25)
       #=========ButtonS================================ s
       loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
       loginbtn.place(x=110,y=300,width=120,height=35)

       registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
       registerbtn.place(x=15,y=350,width=160)

       foregtpasswordbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
       foregtpasswordbtn.place(x=10,y=370,width=160)

     def register_window(self):
      self.new_window=Toplevel()
      self.app=Register(self.new_window)

   
        






     def login(self):
      try:
              def storain(self):
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=StoreManagementSystem(self.new_window)  
                else:
                    
                    if not open_main:
                        return
                if self.txtuser.get()=="" or self.txtpass.get()=="":
                    messagebox.showerror("Error","all field required")
                elif self.txtuser.get()=="Pranayjha123" and self.txtpass.get()=="Pranayjha@123":
                    messagebox.showinfo("Success","Valid username & password")
                else :
                    conn=mysql.connector.connect(host="localhost",username="root",password="w@2915djkq#",database="store")
                    my_cursor=conn.cursor()
                    my_cursor.execute("SELECT * FROM register where username=%s and password=%s",( 
                                                                                                self.txtuser.get(),
                                                                                                self.txtpass.get()
                                                                                                ))
                    row=my_cursor.fetchone()
                    if row==None:
                     messagebox.showerror("Error","Invalid Username & Password")
                    else:
                        storain(self)
                        conn.commit()
                        conn.close()
      except Exception as e :
                    messagebox.showerror("Error",str(e))
         #================def stomain==================
 
         


     
        #===========reset password=========================
     def reset_pass(self):
         if self.combo_security_Q.get()=="Select":
             messagebox.showerror("Error","Select Security Question",parent=self.root2)
         elif self.txt_security.get()=="":
           messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)  
         elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password",parent=self.root2)
         else :
          conn=mysql.connector.connect(host="localhost",username="root",password="w@2915djkq#",database="store")
          my_cursor=conn.cursor()
          query=("select * from register where username=%s and securityQ=%s and securityA=%s")
          value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())

          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          if row==None:
            messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2)
          else:
             query=("update register set password=%s where username=%s")
             value = (self.txt_newpass.get(), self.txtuser.get())

             my_cursor.execute(query,value)

             conn.commit()
             conn.close()
             messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
             self.root2.destroy()

            
                       


#===================forgot password window====================
     def forgot_password_window(self):
         if self.txtuser.get()=="":
             messagebox.showerror("Error","please enter Email address to Reset Password")
         else:
           conn=mysql.connector.connect(host="localhost",username="root",password="w@2915djkq#",database="store")
           my_cursor=conn.cursor()
           query=("SELECT * FROM register where username=%s")
           value=(self.txtuser.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           print(row)  

           if row==None:
               messagebox.showerror("Error","Please enter the valid User name")
           else:
               conn.close()
               self.root2=Toplevel()
               self.root2.title("Forgot Password")
               self.root2.geometry("340x450+610+170")

               #l=Label(self.root,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
               #l.place(y=10,relwidth=1)

               security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
               security_Q.place(x=50,y=80)
               self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
               self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
               self.combo_security_Q.place(x=50,y=110,width=250)
               self.combo_security_Q.current(0)

               security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
               security_A.place(x=50,y=150)

               self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
               self.txt_security.place(x=50,y=180,width=250)

               new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
               new_password.place(x=50,y=220)

               self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"),show="*")
               self.txt_newpass.place(x=50,y=250,width=250)
               #====resetbutton=========
               btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green",command=self.reset_pass)
               btn.place(x=135,y=300)
    
                   
    
                   
           
                 
              
               
class Register:
     def __init__(self,root):
       self.root=root
       self.root.title("Register")
       self.root.geometry("1600x900+0+0")
       #==============variables====================
       self.var_fname=StringVar()
       self.var_lname=StringVar()
       self.var_contact=StringVar()
       self.var_email=StringVar()
       self.var_SecurityQ=StringVar()
       self.var_SecurityA=StringVar()
       self.var_pass=StringVar()
       self.var_confpass=StringVar()
       
       
     #===========bg image===========
       
       self.bg=ImageTk.PhotoImage(file=r"C:\Tushar\StoreMag\pexels-simon-berger-1323550.jpg")
       lbl_bg=Label(self.root,image=self.bg)
       lbl_bg .place(x=0,y=0,relwidth=1,relheight=1)
       #=============left image======================
       self.bg1=ImageTk.PhotoImage(file=r"C:\Tushar\StoreMag\registration-hand-pressing-button-interface-blue-background-49410297.jpg")
       left_lbl=Label(self.root,image=self.bg1)
       left_lbl .place(x=50,y=100,width=590,height=550)
       #=======main frame======
       frame=Frame(self.root,bg="white")
       frame.place(x=630,y=100,width=800,height=550)


       register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="brown")
       register_lbl.place(x=20,y=20)
       #==========label entery=====
       #=============row1
       fname=Label(frame,text="Frist Name",font=("times new roman",15,"bold"),bg="white")
       fname.place(x=50,y=100)

       fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
       fname_entry.place(x=50,y=130,width=250)

       l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
       l_name.place(x=370,y=100)

       self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
       self.txt_lname.place(x=370,y=130,width=250)
       #=================row2
       contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
       contact.place(x=50,y=170)

       self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
       self.txt_contact.place(x=50,y=200,width=250)

       email=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white",fg="black")
       email.place(x=370,y=170)

       self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
       self.txt_email.place(x=370,y=200,width=250)

       #=====================row3
       security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
       security_Q.place(x=50,y=240)
       self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times new roman",15,"bold"),state="readonly")
       self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
       self.combo_security_Q.place(x=50,y=270,width=250)
       self.combo_security_Q.current(0)

       security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
       security_A.place(x=370,y=240)

       self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
       self.txt_security.place(x=370,y=270,width=250)

       #========================row4
       paswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
       paswd.place(x=50,y=310)

       self.txt_paswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"),show="*")
       self.txt_paswd.place(x=50,y=340,width=250)

       confirm_paswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
       confirm_paswd.place(x=370,y=310)

       self.txt_confirm_paswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"),show="*")
       self.txt_confirm_paswd.place(x=370,y=340,width=250)
       #================checkButton================
       self.var_check=IntVar()
       self.checkbtn=Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.var_check,font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
       self.checkbtn.place(x=50,y=380)
       #==========button==========
       img=Image.open(r"C:\Tushar\StoreMag\efb997aee7e14cf58b989a53866b13d3.jpg")
       img=img.resize((210,50),Image.LANCZOS)
       self.photoimage=ImageTk.PhotoImage(img)
       b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
       b1.place(x=10,y=420,width=200)

       img1=Image.open(r"C:\Tushar\StoreMag\downloadss.jpeg")
       img1=img1.resize((210,50),Image.LANCZOS)
       self.photoimage1=ImageTk.PhotoImage(img1)
       b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
       b2.place(x=330,y=420,width=200)

       #==================Function delcartion=====================


     def register_data(self):
         if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select":
              messagebox.showerror("Error","All fields are required")
         elif self.var_pass.get()!=self.var_confpass.get():
              messagebox.showerror("Error","Password & Confirmpassword must be same")
         elif self.var_check.get()==0:
              messagebox.showerror("Error","Please agree our terms & conditions")
         else:
              conn=mysql.connector.connect(host="localhost",username="root",password="w@2915djkq#",database="store")
              my_cursor=conn.cursor()
              my_cursor.execute("SELECT * FROM store.register where username=%s", (self.var_email.get(),))
              
             
              row=my_cursor.fetchone()

              if row!=None:
                  messagebox.showerror("Error","User already exist,please tey another username")
              else:
                  my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                           self.var_fname.get(),
                                                                                           self.var_lname.get(),
                                                                                           self.var_contact.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_SecurityQ.get(),
                                                                                           self.var_SecurityA.get(),
                                                                                           self.var_pass.get()
                                                                                                               ))     
              conn.commit()
              conn.close()
              messagebox.showinfo("Success","Register Successfully")
      
     def return_login(self):
         self.root.destory()


class StoreManagementSystem:
       def __init__(self,root):
        self.root=root
        self.root.title("E-Mart Management System")
        self.root.geometry("1550x800+0+0")

        #==========================add variable============================================
        self.addprdid_var=StringVar()
        self.addprdnam_var=StringVar()
        self.addcat_var=StringVar()
        self.expdat_var=StringVar()
        self.disc_var=StringVar()
        self.pric_var=StringVar()
        #===========================Main tex variable======================================
        self.custid=StringVar()
        self.custnam=StringVar()
        self.add=StringVar()
        self.pno=StringVar()
        self.pnt=StringVar()
        self.prdid=StringVar()
        self.prdnam=StringVar()
        self.catg=StringVar()
        self.expdt=StringVar()
        self.tim=StringVar()
        self.price=StringVar()
        #==============================bill variable=======================================
        self.taxPercent=StringVar()
        self.taxPercent.set(18)
        self.sub_total=StringVar()
        self.tax=StringVar()
        self.total=StringVar()



        #====================================================================================

        lbltitle=Label(self.root,text="E-Mart Management System",bd=15,relief=RIDGE
                       ,bg='white',fg='darkblue',font=("time new roman",50,"bold"),padx=2,pady=4)
        
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\\Tushar\\StoreMag\\logos.png")
        img1=img1.resize((80,80),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=240,y=17)

#=====================DATA FRAME=========================================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20,bg="brown1")
        DataFrame.place(x=0,y=100,width=1530,height=400)
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Order Information",
                                 fg='darkblue',font=("arial",12,"bold"))
        DataFrameLeft.place(x=-17,y=5,width=830,height=360)
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Product Information",
                                 fg='darkblue',font=("arial",12,"bold"))
        DataFrameRight.place(x=820,y=5,width=650,height=360)
#========================buttonsFrame=====================================
        
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=500,width=1530,height=65)
 #=======================Main Buttin=========================================
        btnAddData=Button(ButtonFrame,text="ADD ORDER",command=self.Add_data,font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)
        btnAddData=Button(ButtonFrame,text="UPDATE",command=self.Update,font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=1)
        btnAddData=Button(ButtonFrame,text="DELETE",command=self.delete,font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=2)
        btnAddData=Button(ButtonFrame,text="RESET",command=self.reset,font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=3)
        btnAddData=Button(ButtonFrame,text="GENERATE BILL",command=self.gen_bill,font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=4) 


        







#===============search===================================================================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search by",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)


        #variable
        self.search_var=StringVar()


        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("cust_id","prod_nam","prod_id")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchTxt_var=StringVar()

        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)
        searchBtn=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8) 
        showAll=Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9) 


#=============================label and entry====================================================
        def time():
            String=strftime('%H:%M:%S %p')
            lbl=Label(DataFrameLeft,font=('time new roam',16,'bold'),background='red',foreground='blue')
            lbl.place(x=0,y=0,width=200)
            lbl.config(text=String) 
            lbl.after(1000,time)
            

            
        time()
#=============================Add product=========================================================
        lblcustno=Label(DataFrameLeft,font=("arial",12,"bold"),text="customer Id:",padx=2,pady=6)
        lblcustno.grid(row=1,column=0,sticky=W)
        #================================ button====================================
        self.generate_button = ttk.Button(DataFrameLeft, text="Generate ID", command=self.generate_id)
        self.generate_button.grid(row=1,column=2)

#==============================Add button==================================================================
        txtcustno=Entry(DataFrameLeft,textvariable=self.custid,font=("arial",12,"bold"),width=25)
        txtcustno.grid(row=1,column=1)
        lblcustnam=Label(DataFrameLeft,font=("arial",12,"bold"),text="Customer Name",padx=2,pady=6)
        lblcustnam.grid(row=2,column=0,sticky=W)
        txtcustnam=Entry(DataFrameLeft,textvariable=self.custnam,font=("arial",12,"bold"),width=27)
        txtcustnam.grid(row=2,column=1)
        lblAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address",padx=2,pady=6)
        lblAddress.grid(row=3,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.add,font=("arial",12,"bold"),width=27)
        txtAddress.grid(row=3,column=1)
        lblphno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Phone Number",padx=2,pady=6)
        lblphno.grid(row=4,column=0,sticky=W)
        txtphno=Entry(DataFrameLeft,textvariable=self.pno,font=("arial",12,"bold"),width=27)
        txtphno.grid(row=4,column=1)
        lblphnnt=Label(DataFrameLeft,font=("arial",12,"bold"),text="E-mail",padx=2,pady=6)
        lblphnnt.grid(row=5,column=0,sticky=W)
        txtphnnt=Entry(DataFrameLeft,textvariable=self.pnt,font=("arial",12,"bold"),width=27)
        txtphnnt.grid(row=5,column=1)
        lblprdid=Label(DataFrameLeft,font=("arial",12,"bold"),text="product Id",padx=2,pady=6)
        lblprdid.grid(row=0,column=3,sticky=W)
        txtprdid=Entry(DataFrameLeft,textvariable=self.prdid,font=("arial",12,"bold"),width=20)
        txtprdid.place(x=590,y=5)
        lblprdname=Label(DataFrameLeft,font=("arial",12,"bold"),text="product Name",padx=2,pady=6)
        lblprdname.grid(row=1,column=3,sticky=W)
        txtprdname=Entry(DataFrameLeft,textvariable=self.prdnam,font=("arial",12,"bold"),width=20)
        txtprdname.place(x=590,y=40)
        lblcat=Label(DataFrameLeft,font=("arial",12,"bold"),text="Catogery",padx=2,pady=6)
        lblcat.grid(row=2,column=3,sticky=W)
        txtcat=Entry(DataFrameLeft,textvariable=self.catg,font=("arial",12,"bold"),width=20)
        txtcat.place(x=590,y=75)
        lblexdat=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expire Date",padx=2,pady=6)
        lblexdat.grid(row=3,column=3,sticky=W)
        txtexdat=Entry(DataFrameLeft,textvariable=self.expdt,font=("arial",12,"bold"),width=20)
        txtexdat.place(x=590,y=110)
        lbldisc=Label(DataFrameLeft,font=("arial",12,"bold"),text="Quantity of order",padx=2,pady=6) # disc=TIME=quantity(use quantity)
        lbldisc.grid(row=4,column=3,sticky=W)
        
        txtdisc=Entry(DataFrameLeft,textvariable=self.tim,font=("arial",12,"bold"),width=20)
        txtdisc.place(x=590,y=145)
        lblprice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price",padx=2,pady=6)
        lblprice.grid(row=5,column=3,sticky=W)
        txtprice=Entry(DataFrameLeft,textvariable=self.price,font=("arial",12,"bold"),width=20)
        txtprice.place(x=590,y=180)
        #==========================actual price=============================
        

        
        #==========================Images================================
        img2=Image.open("C:\\Tushar\\StoreMag\\drink.jpg")
        img2=img2.resize((270,113),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b2=Button(self.root,image=self.photoimg2,borderwidth=0)
        b2.place(x=48,y=350)

        img3=Image.open("C:\\Tushar\\StoreMag\\grocery.jpg")
        img3=img3.resize((250,113),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(self.root,image=self.photoimg3,borderwidth=0)
        b3.place(x=280,y=350)

        img4=Image.open("C:\\Tushar\\StoreMag\\grocery2.jpg")
        img4=img4.resize((300,113),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b4=Button(self.root,image=self.photoimg4,borderwidth=0)
        b4.place(x=500,y=350)


        #===========================Images================================

        #===========================right side================================
        sideframe=Frame(DataFrameRight,bd=4)
        sideframe.place(x=300,y=9,width=100,height=35)
        self.generate_button = ttk.Button(sideframe, text="produc Id", command=self.genrate_prdid)
        self.generate_button.grid(row=0,column=0)



        #=============================right side========================================
        lblprdno=Label(DataFrameRight,font=("arial",12,"bold"),text="Product Id",padx=2,pady=6)
        lblprdno.place(x=-20,y=5)
        txtprdno = Entry(DataFrameRight, textvariable=self.addprdid_var, font=("arial", 12, "bold"), width=20)
        txtprdno.place(x=115, y=11)
        lblprdname=Label(DataFrameRight,font=("arial",12,"bold"),text="Product Name",padx=2,pady=6)
        lblprdname.place(x=-20,y=39)
        txtprdname = Entry(DataFrameRight, textvariable=self.addprdnam_var, font=("arial", 12, "bold"), width=27)
        txtprdname.place(x=115, y=44)
        lblcat=Label(DataFrameRight,font=("arial",12,"bold"),text="Category",padx=2,pady=6)
        lblcat.place(x=-20,y=70)
        txtcat = Entry(DataFrameRight, textvariable=self.addcat_var, font=("arial", 12, "bold"), width=27)
        txtcat.place(x=115, y=75)
        lblexpirdate=Label(DataFrameRight,font=("arial",12,"bold"),text="Expiry Date",padx=2,pady=6)
        lblexpirdate.place(x=-20,y=100)
        txtexpiredate = Entry(DataFrameRight, textvariable=self.expdat_var, font=("arial", 12, "bold"), width=27)
        txtexpiredate.place(x=115, y=105)
        lbldis=Label(DataFrameRight,font=("arial",12,"bold"),text="Quantity",padx=2,pady=6)
        lbldis.place(x=-20,y=130)
        txtdis = Entry(DataFrameRight, textvariable=self.disc_var, font=("arial", 12, "bold"), width=27)
        txtdis.place(x=115, y=135)
        lblprice=Label(DataFrameRight,font=("arial",12,"bold"),text="Selling price",padx=2,pady=6)
        lblprice.place(x=-20,y=160)
        txtprice = Entry(DataFrameRight, textvariable=self.pric_var, font=("arial", 12, "bold"), width=27)#use as selling price
        txtprice.place(x=115, y=165)


        #===========================side frame ================================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="White")
        side_frame.place(x=0,y=210,width=580,height=100)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.product_table=ttk.Treeview(side_frame,columns=("PrdId","PrdName","category","Expirydate","Discount","Price")
                                        ,xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.product_table.xview)
        sc_y.config(command=self.product_table.yview)
     
        self.product_table.heading("PrdId",text="Product Id")
        self.product_table.heading("PrdName",text="Product Name")
        self.product_table.heading("category",text="Category")
        self.product_table.heading("Expirydate",text="Expiry Date")
        self.product_table.heading("Discount",text="quantity")
        self.product_table.heading("Price",text="Selling price")

        self.product_table["show"]="headings"
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.column("PrdId",width=100)
        self.product_table.column("PrdName",width=100)
        self.product_table.column("category",width=100)
        self.product_table.column("Expirydate",width=100)
        self.product_table.column("Discount",width=100)
        self.product_table.column("Price",width=100)

        self.product_table.bind("<ButtonRelease-1>", self.Prdget_cursor)

#=========================product Add Button ============================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=420,y=10,width=135,height=160)

        btnAddprd=Button(down_frame,text="ADD",font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=4,command=self.add_prd)
        btnAddprd.grid(row=0,column=0)

        btnupdtprd=Button(down_frame,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4,command=self.UpdateStr)
        btnupdtprd.grid(row=1,column=0)

        btndelprd=Button(down_frame,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4,command=self.DeletePrd)
        btndelprd.grid(row=2,column=0)

        btnclearprd=Button(down_frame,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4,command=self.ClearPrd)
        btnclearprd.grid(row=3,column=0)

        #==========================================Frame detail==============================================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=570,width=1530,height=210)


        #===========================================Main table scroll bar============================================
        Table_frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame.place(x=0,y=570,width=1530,height=210)


        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.store_table=ttk.Treeview(Table_frame,columns=("cust_id","cust_nam","addrs","pho","pht","prd_id","prd_nam","catg","expdat","disc","price","subtotal","tax","total") 
                                         ,xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        scroll_x.config(command=self.store_table.xview)
        scroll_y.config(command=self.store_table.yview)
        self.store_table["show"]="headings"

        self.store_table.heading("cust_id",text="CUSTOMER ID")
        self.store_table.heading("cust_nam",text="CUSTOMER NAME")
        self.store_table.heading("addrs",text="ADDRESS")
        self.store_table.heading("pho",text="PHONE NO.1")
        self.store_table.heading("pht",text="E-mail")
        self.store_table.heading("prd_id",text="PRODUCT Id")
        self.store_table.heading("prd_nam",text="PRODUCT NAME")
        self.store_table.heading("catg",text="CATEGORY")
        self.store_table.heading("expdat",text="EXPIRYDATE")
        self.store_table.heading("disc",text="Quantity")#change to quantity
        self.store_table.heading("price",text="SELLING PRICE")#change to price
        self.store_table.heading("subtotal",text="Sub total")
        self.store_table.heading("tax",text="tax")
        self.store_table.heading("total",text="total")
        self.store_table.pack(fill=BOTH,expand=1)
        
        self.store_table.column("cust_id",width=100)
        self.store_table.column("cust_nam",width=100)
        self.store_table.column("addrs",width=100)
        self.store_table.column("pho",width=100)
        self.store_table.column("pht",width=100)
        self.store_table.column("prd_id",width=100)
        self.store_table.column("prd_nam",width=100)
        self.store_table.column("catg",width=100)
        self.store_table.column("expdat",width=100)
        self.store_table.column("disc",width=100)
        self.store_table.column("price",width=100)
        self.fetch_dataprd()
        self.fetch_data()
        self.store_table.bind("<ButtonRelease-1>",self.get_curssor)
        print("hii")



        #=======================add prouct functionality Declaration =======================
        print("hello")
        #===================================genrate id========================================
       def generate_id(self):
        # Generate a random 4-digit customer ID
        customer_id = random.randint(1000, 9999)
        self.custid.set(str(customer_id))
       def genrate_prdid(self):
        addprdid_var= random.randint(1000, 9999)
        self.addprdid_var.set(str(addprdid_var))
        #===========================================================================================================
        print("raju")
       def add_prd(self):
      
            print("on")
            conn=mysql.connector.connect(host="localhost",username="root",password="w@2915djkq#",database="store")
            my_cursor=conn.cursor()
            print("t")
            my_cursor.execute("insert into stordata(prdid,prdnam,categ,expirydat,disct,price) values(%s,%s,%s,%s,%s,%s)",(
                self.addprdid_var.get(),
                self.addprdnam_var.get(),
                self.addcat_var.get(),
                self.expdat_var.get(),
                self.disc_var.get(),
                self.pric_var.get()
            ))
            my_cursor.execute("insert into category_table(prod_id,prod_name,category_name) values(%s,%s,%s)",(
               self.addprdid_var.get(),
               self.addprdnam_var.get(),
               self.addcat_var.get()

            ))




            print("m")
            conn.commit()
            self.fetch_dataprd()
            self.Prdget_cursor()
            conn.close()
            print("Yes")
            messagebox.showinfo("Sucess","Product Added")

       def fetch_dataprd(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="w@2915djkq#", database="store")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from stordata")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.product_table.delete(*self.product_table.get_children())
            for i in rows:
                self.product_table.insert("", END, values=i)
            conn.commit()
            print("hi")
        conn.close()



    #===========================predgenrt================================================
       def Prdget_cursor(self,event=""):
         cursor_row=self.product_table.focus()
         print("hi")
         content=self.product_table.item(cursor_row)
         row=content["values"]
         if row:
          if len(row) >= 6:  
           self.addprdid_var.set(row[0])
           self.addprdnam_var.set(row[1])
           self.addcat_var.set(row[2])
           self.expdat_var.set(row[3])
           self.disc_var.set(row[4])
           self.pric_var.set(row[5])
           self.prdid.set(row[0])
           self.prdnam.set(row[1])
           self.catg.set(row[2])
           self.expdt.set(row[3])
           self.price.set(row[5])
           print("done")
    
                 



            #eror def because def rPrdget
       def UpdateStr(self):
         if self.addprdid_var.get()=="" or self.addprdnam_var.get()=="" or self.addcat_var.get()=="" or self.expdat_var.get()=="" or self.disc_var.get()=="" or self.pric_var.get()=="":
              messagebox.showerror("Error","All fild are Required")
         else:
               conn = mysql.connector.connect(host="localhost", username="root", password="w@2915djkq#", database="store")
               my_cursor = conn.cursor()
               my_cursor.execute("UPDATE stordata SET prdnam=%s, categ=%s, expirydat=%s, disct=%s, price=%s WHERE prdid=%s", (
    self.addprdnam_var.get(),
    self.addcat_var.get(),
    self.expdat_var.get(),
    self.disc_var.get(),
    self.pric_var.get(),
    self.addprdid_var.get()  # Add the missing parameter
    ))
               my_cursor.execute("UPDATE category_table SET prod_name=%s, category_name=%s WHERE prod_id=%s",(
                  self.addprdnam_var.get(),
                  self.addcat_var.get(),
                  self.addprdid_var.get(),
               ))
               conn.commit()
               self.fetch_dataprd()
               conn.close()
               messagebox.showinfo("Success","Product has been Updated")


               


       def DeletePrd(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="w@2915djkq#", database="store")
        my_cursor = conn.cursor()

        sql="delete from stordata where prdid=%s"
        val=(self.addprdid_var.get(),)
        my_cursor.execute(sql,val)
        #=============================category==================================
        sql="delete from category_table where prod_id=%s"
        val=(self.addprdid_var.get(),)
        my_cursor.execute(sql,val)
       
        #=======================================================================

        conn.commit()
        self.fetch_dataprd()
        conn.close()
        messagebox.showinfo("Success","Data Of Product is Delete !!!")



       def ClearPrd(self):
        self.addprdid_var.set("")
        self.addprdid_var.set(""),
        self.addprdnam_var.set(""),
        self.addcat_var.set(""),
        self.expdat_var.set(""),
        self.disc_var.set(""),
        self.pric_var.set("")
#===================================================== Main  table ============================================
       def Add_data(self):
      
        if self.custid.get()=="" or self.prdid.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
            try:        
        
                    #========================bill==================================
                    self.l=[]#sub-total
                    self.n=int(self.price.get())
                    self.m=int(self.tim.get())*self.n
                    self.l.append(self.m)
                    print(self.m)
                    self.sub_total.set(self.m)
                    print(((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100))#gov-tax
                    self.tax.set(((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100))
                    print(sum(self.l) + ((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100))#total
                    self.total.set((sum(self.l) + ((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100)))
                    #==============================================================
                    conn = mysql.connector.connect(host="localhost", username="root", password="w@2915djkq#", database="store")
                    my_cursor = conn.cursor()
                    print("work 1")
                    #try:
                    my_cursor.execute("insert into order_detail(cust_id,cust_nam,address,phon_o,phon_t,prod_id,prod_nam,categ,expdat,tim,price,subtotal,tax,total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                                                    self.custid.get(),
                                                                                                                                                                                    self.custnam.get(),
                                                                                                                                                                                    self.add.get(),
                                                                                                                                                                                    self.pno.get(),
                                                                                                                                                                                    self.pnt.get(),
                                                                                                                                                                                    self.prdid.get(),
                                                                                                                                                                                    self.prdnam.get(),
                                                                                                                                                                                    self.catg.get(),
                                                                                                                                                                                    self.expdt.get(),
                                                                                                                                                                                    self.tim.get(),
                                                                                                                                                                                    self.price.get(),
                                                                                                                                                                                    self.sub_total.get(),
                                                                                                                                                                                    self.tax.get(),
                                                                                                                                                                                    self.total.get()
                                                                                                                                                                                    ))
                    my_cursor.execute("insert into cust_data(custid,custnam,custadd,pno,pnt) values(%s,%s,%s,%s,%s)",(
                        self.custid.get(),
                                                                                                                                                                                    self.custnam.get(),
                                                                                                                                                                                    self.add.get(),
                                                                                                                                                                                    self.pno.get(),
                                                                                                                                                                                    self.pnt.get(),
                    ))
                    
                    print("work 2") 

                                                                                                                                                                                    
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","data has been inserted")
            except Exception as e:
               messagebox.showerror("Error",str(e))    
           

       def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="w@2915djkq#", database="store")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from order_detail")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.store_table.delete(*self.store_table.get_children())
            for i in rows:
                 self.store_table.insert("", END, values=i)
            conn.commit()
            print("ok done")
        conn.close()
    
       def get_curssor(self,ev=""):
        cursor_row=self.store_table.focus()
        print("wkkk")
        content=self.store_table.item(cursor_row)
        row=content["values"]
        if row:
          if len(row) >= 6: 
           self.custid.set(row[0]) 
           self.custnam.set(row[1])
           self.add.set(row[2])
           self.pno.set(row[3])
           self.pnt.set(row[4])
           self.prdid.set(row[5])
           self.prdnam.set(row[6])
           self.catg.set(row[7])
           self.expdt.set(row[8])
           self.tim.set(row[9])
           self.price.set(row[10])
           print(self.price.get())
           print("done")
       def Update(self):
         if self.custid.get()=="" or self.prdid.get()=="":
              messagebox.showerror("Error","All fild are Required")
         else:
            
               #========================bill==================================
                self.l=[]#sub-total
                self.n=int(self.price.get())
                self.m=int(self.tim.get())*self.n
                self.l.append(self.m)
                print(self.m)
                self.sub_total.set(self.m)
                print(((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100))#gov-tax
                self.tax.set(((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100))
                print(sum(self.l) + ((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100))#total
                self.total.set((sum(self.l) + ((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100)))
                    #==============================================================
                conn = mysql.connector.connect(host="localhost", username="root", password="w@2915djkq#", database="store")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE order_detail SET cust_nam=%s, address=%s, phon_o=%s, phon_t=%s, prod_id=%s, prod_nam=%s,categ=%s,expdat=%s,tim=%s,price=%s,subtotal=%s,tax=%s,total=%s WHERE cust_id=%s", (
                                                                                                                                                                            self.custnam.get(),
                                                                                                                                                                            self.add.get(),
                                                                                                                                                                            self.pno.get(),
                                                                                                                                                                            self.pnt.get(),
                                                                                                                                                                            self.prdid.get(),
                                                                                                                                                                            self.prdnam.get(),
                                                                                                                                                                            self.catg.get(),
                                                                                                                                                                            self.expdt.get(),
                                                                                                                                                                            self.tim.get(),
                                                                                                                                                                            self.price.get(),
                                                                                                                                                                            self.sub_total.get(),
                                                                                                                                                                            self.tax.get(),
                                                                                                                                                                            self.total.get(),
                                                                                                                                                                            self.custid.get()# Add the missing parameter
                                                                                                                                                                            
    ))
         my_cursor.execute("UPDATE cust_data SET custnam=%s, custadd=%s, pno=%s, pnt=%s WHERE custid=%s", (
                                                                                                                                                                            self.custnam.get(),
                                                                                                                                                                            self.add.get(),
                                                                                                                                                                            self.pno.get(),
                                                                                                                                                                            self.pnt.get(),
                                                                                                                                                                            self.custid.get()# Add the missing parameter
    ))
               
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("Success","order has been Updated")
       
         
                 
       def delete(self):
         try:
            conn = mysql.connector.connect(host="localhost", username="root", password="w@2915djkq#", database="store")
            my_cursor = conn.cursor()

            sql="delete from order_detail where cust_id=%s"
            val=(self.custid.get(),)
            my_cursor.execute(sql,val)

            sql="delete from cust_data where custid=%s"
            val=(self.custid.get(),)
            my_cursor.execute(sql,val)

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","data of product is Deleat !!!")
         except Exception as e:
            messagebox.showerror("Error","",str(e))


       def reset(self):
         self.custnam.set(""),
         self.add.set(""),
         self.pno.set(""),
         self.pnt.set(""),
         self.prdid.set(""),
         self.prdnam.set(""),
         self.catg.set(""),
         self.expdt.set(""),
         self.tim.set(""),
         self.price.set(""),
         self.custid.set("")

       def search_data(self):
         conn = mysql.connector.connect(host="localhost", username="root", password="w@2915djkq#", database="store")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from order_detail where " + str(self.search_var.get()) + " LIKE '" + str(self.searchTxt_var.get()) + "%'")

         
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.store_table.delete(*self.store_table.get_children())
             for i in rows:
                 self.store_table.insert("",END,value=i)
         conn.commit()
         conn.close()

         #========================bill genrator================================

       def gen_bill(self):
            
            
            
            self.root.geometry("550x720+500+25")
            self.root.title("Bill Generator")
        

    


        #Main Frame
            Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
            Main_Frame.place(x=0,y=0,width=550,height=720)

            #Billing Section Frame
            Billing_Section_Frame=LabelFrame(Main_Frame,text="BILLING SECTION",font=("times new roman",12,"bold"),bg="white",fg="green")
            Billing_Section_Frame.place(x=22,y=125,width=500,height=500)
            scroll_y=Scrollbar(Billing_Section_Frame,orient=VERTICAL)
            self.textarea=Text(Billing_Section_Frame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"), state='disabled')
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=self.textarea.yview)
            self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter LabelFrame
            Bill_Counter_Frame=LabelFrame(Main_Frame,text="BILL COUNTER",font=("times new roman",12,"bold"),bg="white",fg="green")
            Bill_Counter_Frame.place(x=255,y=0,width=275,height=125)

            self.lblSubTotal=Label(Bill_Counter_Frame,font=('arial',11,'bold'),bg="white",fg="brown",text="SUB-TOTAL :-",bd=4)
            self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

            self.entrySubTotal=ttk.Entry(Bill_Counter_Frame,font=('arial',11,'bold'),width=24,state='readonly')
            self.entrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

            self.lblTax=Label(Bill_Counter_Frame,font=('arial',11,'bold'),bg="white",fg="brown",text="GOV. TAX :-",bd=4)
            self.lblTax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

            self.entryTax=ttk.Entry(Bill_Counter_Frame,font=('arial',11,'bold'),width=24,state='readonly')
            self.entryTax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

            self.lblTotal=Label(Bill_Counter_Frame,font=('arial',11,'bold'),bg="white",fg="brown",text="TOTAL :- ",bd=4)
            self.lblTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

            self.entryTotal=ttk.Entry(Bill_Counter_Frame,font=('arial',11,'bold'),width=24,state='readonly')
            self.entryTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Button Frames
            Btn_Frame=Frame(Main_Frame,bd=2,bg="white")
            Btn_Frame.place(x=25,y=630)

            self.BtnSaveBill=Button(Btn_Frame,command=self.save_bill,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",height=2,width=12)
            self.BtnSaveBill.grid(row=0,column=0,padx=5)

            self.BtnPrint=Button(Btn_Frame,command=self.print_bill,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",height=2,width=12)
            self.BtnPrint.grid(row=0,column=1,padx=5)

            self.BtnExit=Button(Btn_Frame,command=self.send_BillPdf,text="E-mail",font=('arial',15,'bold'),bg="orangered",fg="white",height=2,width=12)
            self.BtnExit.grid(row=0,column=2,padx=5)

        #Reciept LabelFrame
            Reciept_Frame=LabelFrame(Main_Frame,text="SEARCH SECTION",font=("times new roman",12,"bold"),bg="white",fg="green")
            Reciept_Frame.place(x=0,y=0,width=252,height=125)

            self.lblRecieptNo=Label(Reciept_Frame,font=('arial',11,'bold'),bg="white",fg="brown",text="RECIEPT NO. :-",bd=4)
            self.lblRecieptNo.grid(row=0,column=0,sticky=W,padx=0,pady=10)

            self.entryRecieptNo=ttk.Entry(Reciept_Frame,font=('arial',11,'bold'),width=15)
            self.entryRecieptNo.grid(row=0,column=1,sticky=W,padx=0,pady=10)

        #Search Frame
            Search_Frame=LabelFrame(Reciept_Frame)
            Search_Frame.place(x=58,y=50,width=136,height=48)

            self.BtnSearch=Button(Search_Frame,command=self.search_bill,text="Search",font=('arial',15,'bold'),bg="orangered",fg="white",height=1,width=10)
            self.BtnSearch.grid(row=0,column=0)

            #Variables
             #This Variable from Pranay Login
            
            self.bill_no=StringVar()
            z=random.randint(1000,9999)
            self.bill_no.set(z)
            # self.search_bill=StringVar()
            
            
     

            #Creaating List
            self.l=[]

            #Function Calling
            self.welcome()
            self.priceCalc()
        
       def priceCalc(self) :
        
        
          self.n=int(self.price.get())
          self.m=int(self.tim.get())*self.n
          self.l.append(self.m)
          if self.prdnam.get() == "" :
              messagebox.showerror("Error","Please Enter Product Name.")
          elif self.prdid.get() == "" :
              messagebox.showerror("Error","Please Enter Product ID.")
          elif self.tim.get() == "" :
              messagebox.showerror("Error","Please Enter Product Quantity Purchased.")
          elif self.price.get() == "" :
              messagebox.showerror("Error","Please Enter Product Price.")
          else :
              self.textarea.config(state='normal')
              self.entrySubTotal.config(state='normal')
              self.entryTax.config(state='normal')
              self.entryTotal.config(state='normal')
              self.textarea.insert(END,f"\n {self.prdid.get()}\t\t{self.prdnam.get()}\t\t{self.tim.get()}\t\t{self.price.get()}")    
              self.sub_total.set('Rs.%.2f' % (sum(self.l)))
              self.tax.set(str('Rs.%.2f'%((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100)))
              self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - int(self.price.get()))*int(self.taxPercent.get()))/100)))))
              self.entrySubTotal.delete(0, 'end')
              self.entrySubTotal.insert(0, self.sub_total.get())
              self.entryTax.delete(0, 'end')
              self.entryTax.insert(0, self.tax.get())
              self.entryTotal.delete(0, 'end')
              self.entryTotal.insert(0, self.total.get())
              self.textarea.insert(END,f"\n====================================================")
              self.textarea.insert(END,f"\n\n====================================================")
              self.textarea.insert(END,f"\n Sub-Amount :\t\t\t{self.sub_total.get()}")
              self.textarea.insert(END,f"\n Tax-Amount :\t\t\t{self.tax.get()}")
              self.textarea.insert(END,f"\n-----------------------------------------------------------------------------------------------")
              self.textarea.insert(END,f"\n Total-Amount :\t\t\t{self.total.get()}")
              self.textarea.insert(END,f"\n====================================================")
              self.entrySubTotal.config(state='readonly')
              self.entryTax.config(state='readonly')
              self.entryTotal.config(state='readyonly')
              self.textarea.config(state='disabled')

       def welcome(self):
          self.textarea.config(state='normal')
          self.textarea.delete(1.0,END)
          self.textarea.insert(END,"\n\t\t       Welcome to E-Mart Mall")
          self.textarea.insert(END,f"\n\n Bill Number : {self.bill_no.get()}")
          self.textarea.insert(END,f"\n Customer Name : {self.custnam.get()}")
          self.textarea.insert(END,f"\n Customer ID : {self.custid.get()}")
          self.textarea.insert(END,f"\n Phone No. 1 : {self.pno.get()}")
          self.textarea.insert(END,f"\n Phone No. 2 : {self.pnt.get()}")
          #self.textarea.insert(END,f"\n Email ID : {self.var_email.get()}")     

          self.textarea.insert(END,f"\n\n====================================================")
          self.textarea.insert(END,f"\n Product\t\tProduct\t\tQuantity\t\tPrice of ")
          self.textarea.insert(END,f"\n   ID.  \t\tName.  \t\t        \t\t Product ")
          self.textarea.insert(END,f"\n        \t\t       \t\t\t\t(1 Quantity)")
          self.textarea.insert(END,f"\n====================================================\n")
          self.textarea.config(state='disabled')

       def save_bill(self):
          op = messagebox.askyesno("Save Bill","Do you want to save the bill?")
          if op > 0:
              self.bill_data=self.textarea.get(1.0,END)
              f1=open('C:/Tushar/StoreMag/Bills/'+str(self.bill_no.get())+".txt",'w')
              f1.write(self.bill_data)
              op=messagebox.showinfo("Saved!!",f"Bill No. : {self.bill_no.get()} Saved Successfully!!!")
              f1.close()
              self.new_window=Toplevel()
              self.app=StoreManagementSystem(self.new_window)
          

       def print_bill(self):
          q = self.textarea.get(1.0,"end-1c")
          filename = tempfile.mktemp('.txt')
          open(filename,'w').write(q)
          os.startfile(filename,"Print")
          #self.new_window=Toplevel()
          #self.app=StoreManagementSystem(self.new_window)


       def search_bill(self):
          self.textarea.config(state='normal')
          found = "no"
          for i in os.listdir("C:/Tushar/StoreMag/Bills/"):
              if i.split('.')[0]==self.entryRecieptNo.get():
                  f1=open(f'C:/Tushar/StoreMag/Bills/{i}','r')
                  self.textarea.delete(1.0,END)
                  for d in f1:
                      self.textarea.insert(END,d)
                  f1.close()
                  found="yes"
          if found == "no":
              messagebox.showerror("Error!!",f"Bill No. {self.entryRecieptNo.get()} Not Found!!!")
          self.textarea.config(state='normal')

       def send_BillPdf(self):
    
        
            cust_mail = "mahajanmayur501@gmail.com"
            cust_name = self.custnam.get()

            def mailToUser():
                subject="your E-mart purchase bill" #subject of our mail.
                body= f'''Dear {cust_name} ,
                            this is the system generated bill from E-mart Management System.   
                            your order is successfully dispatched.
                            thank you !
                            '''
                key= sendpdf("mimayurmahajan@gmail.com",self.pnt.get() ,"zmuv azck rjxo fnqt",subject,body,self.bill_no.get(),r"C:/Tushar/StoreMag/Bills/")

                key.email_send()

            mailToUser()
            messagebox.showinfo("Success","Mail Sent Successfully!!!") 
       
                
         

if __name__ == "__main__":
      main()