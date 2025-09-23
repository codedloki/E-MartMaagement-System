from tkinter import *
import pyotp
from tkinter import ttk
import random,os,tempfile
from PIL import Image,ImageTk
from pathlib import Path
from tkinter import messagebox
from StoreManagement import StoreManagementSystem
# import mysql.connector
import pymysql
from qrcodegenerator import QRGenerate
import pyqrcode
import png
import smtplib as s
from pdf_mail import sendpdf
from time import strftime,sleep


BASE_DIR = Path(__file__).resolve().parent

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        #==============variables====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_username=StringVar()
        self.var_email=StringVar()
        self.var_secret_key=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        #===========bg image===========
        self.bg=ImageTk.PhotoImage(file=BASE_DIR/"images"/"pexels-simon-berger-1323550.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg .place(x=0,y=0,relwidth=1,relheight=1)
        #=============left image======================
        self.bg1=ImageTk.PhotoImage(file=BASE_DIR/"images"/"registration-hand-pressing-button-interface-blue-background-49410297.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl .place(x=50,y=100,width=590,height=550)
        #=======main frame======
        frame=Frame(self.root,bg="white")
        frame.place(x=630,y=100,width=800,height=550)


        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="brown")
        register_lbl.place(x=20,y=20)
        #==========label entery=====
#===========================TOp row ===========================#
        email_label=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email_label.place(x=50,y=70,width=500)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=50,y=100,width=580)
        
        #=============row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=150)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=180,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=150)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=180,width=250)
        #=================row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=240)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=280,width=250)

        email=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=240)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_username ,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=280,width=250)

        #=====================row3

    #    security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
    #    security_Q.place(x=50,y=240)
    #    self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times new roman",15,"bold"),state="readonly")
    #    self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
    #    self.combo_security_Q.place(x=50,y=270,width=250)
    #    self.combo_security_Q.current(0)

    #    security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
    #    security_A.place(x=370,y=240)

    #    self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
    #    self.txt_security.place(x=370,y=270,width=250)
    
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
        img=Image.open(BASE_DIR/"images"/"efb997aee7e14cf58b989a53866b13d3.jpg")
        img=img.resize((210,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)

    #    img1=Image.open(r"C:\Tushar\StoreMag\downloadss.jpeg")
    #    img1=img1.resize((210,50),Image.LANCZOS)
    #    self.photoimage1=ImageTk.PhotoImage(img1)
    #    b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
    #    b2.place(x=330,y=420,width=200)

        #==================Function delcartion=====================
    def qr_window(self):
        qr_root = Toplevel(self.root)
        qr_app = QRGenerate(qr_root)
        qr_root.mainloop()

    def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()==""  or len(self.var_contact.get())!=10:
                messagebox.showerror("Error","All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password & Confirmpassword must be same")
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms & conditions")
            else:
                conn=pymysql.connect(host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",port=21390,user="avnadmin",password="AVNS_flfS-xIQA4vHQtH_z4h",database="defaultdb")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT * FROM register where username=%s", (self.var_username.get()))
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please tey another username")
                else:
                    secret_key = pyotp.random_base32()
                    # Generate QR code first
                    otp_con = pyotp.totp.TOTP(secret_key).provisioning_uri(name=self.var_email.get(),issuer_name="Emart System")
                    print(otp_con)

                    # Create qrcodes directory if it doesn't exist
                    qr_dir = BASE_DIR / "qrcodes"
                    qr_dir.mkdir(exist_ok=True)
                    
                    # Generate QR code
                    url = pyqrcode.create(otp_con)
                    qr_path = qr_dir / "code.png"
                    url.png(str(qr_path), scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
                    
                    # Insert data into database AFTER generating QR code
                    try:
                        my_cursor.execute("INSERT INTO register (email, fname, lname, contact, username, password, secret_key) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                                        (self.var_email.get(), self.var_fname.get(), self.var_lname.get(), 
                                         self.var_contact.get(), self.var_username.get(), self.var_pass.get(), secret_key))
                        conn.commit()
                        
                        # Verify the QR code was created successfully
                        if qr_path.exists():
                            print("QR code generated successfully")
                            # Open QR code window
                            self.root.after(100, self.qr_window)  # Small delay to ensure file is written
                            messagebox.showinfo("Success","Registered successfully! Please scan the QR code for 2FA setup.")
                        else:
                            messagebox.showerror("Error", "QR code generation failed")
                            
                    except Exception as e:
                        conn.rollback()
                        messagebox.showerror("Error", f"Database error: {str(e)}")
                    finally:
                        conn.close()

    def return_login(self):
        self.root.destroy()