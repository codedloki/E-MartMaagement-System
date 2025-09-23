from tkinter import*
from Otptake import OTPWindow
from tkinter import ttk
import random,os,tempfile
from PIL import Image,ImageTk
from pathlib import Path
from tkinter import messagebox
from StoreManagement import StoreManagementSystem
import pymysql
from registration import Register
import smtplib as s
from pdf_mail import sendpdf
from time import strftime

BASE_DIR = Path(__file__).resolve().parent

class EMARTSYSTEM:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(True, True)

        self.store_management_system_instance = None
        self.bg = ImageTk.PhotoImage(file=BASE_DIR / "images" / "pexels-simon-berger-1323550.jpg")

        self.login_frame = Frame(self.root)
        self.login_frame.pack(fill=BOTH, expand=True)

        lbl_bg = Label(self.login_frame, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.login_frame, bg='black')
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text="SIGN IN", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=70, y=50)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=125)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # Icon Images
        img2 = Image.open(BASE_DIR / "images" / "username logo.jpg")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.login_frame, image=self.photoimg2, borderwidth=0, bg="black")
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(BASE_DIR / "images" / "password logo.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.login_frame, image=self.photoimg3, borderwidth=0, bg="black")
        lblimg3.place(x=650, y=394, width=25, height=25)

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 10, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        foregtpasswordbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=("times new roman", 10,"bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        foregtpasswordbtn.place(x=15, y=400, width=160)

    def login(self):
        try:
            if self.txtuser.get() == "" or self.txtpass.get() == "":
                messagebox.showerror("Error", "All fields required")
            else:
                conn = pymysql.connect(
                    host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com", 
                    port=21390, 
                    user="avnadmin", 
                    password="AVNS_flfS-xIQA4vHQtH_z4h", 
                    database="defaultdb"
                )
                my_cursor = conn.cursor()
                
                # Initialize database tables only if they don't exist
                self.initialize_database_tables(my_cursor)

                # Check if user exists and get secret_key
                my_cursor.execute("SELECT secret_key FROM register WHERE username=%s AND password=%s", (
                    self.txtuser.get(),
                    self.txtpass.get()
                ))

                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username & Password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main:
                        self.login_frame.destroy()
                        OTPWindow(self.root, row[0], self.show_store_management)
                
                conn.commit()
                conn.close()
                
        except Exception as e:
            messagebox.showerror("Error", f"Login failed: {str(e)}")

    def initialize_database_tables(self, cursor):
        """Initialize all required database tables with proper primary keys"""
        try:
            # Register table - with proper primary key
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS register (
                    email VARCHAR(100) UNIQUE,
                    fname VARCHAR(100) NOT NULL,
                    lname VARCHAR(100) NOT NULL,
                    contact VARCHAR(15) NOT NULL,
                    username VARCHAR(100) PRIMARY KEY,
                    password VARCHAR(255) NOT NULL,
                    secret_key VARCHAR(255) NOT NULL
                )
            """)
            
            # Stordata table - with proper primary key
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stordata (
                    prdid VARCHAR(45) PRIMARY KEY,
                    prdnam VARCHAR(45),
                    categ VARCHAR(45),
                    expirydat DATE,
                    disct INT,
                    price DECIMAL(10, 2)
                )
            """)
            
            # Category table - with proper primary key
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS category_table (
                    prod_id VARCHAR(45) PRIMARY KEY,
                    prod_name VARCHAR(45),
                    category_name VARCHAR(45)
                )
            """)
            
            # Order detail table - no primary key needed (can have multiple orders per customer)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS order_detail (
                    order_id INT AUTO_INCREMENT PRIMARY KEY,
                    cust_id VARCHAR(45),
                    cust_nam VARCHAR(45),
                    address VARCHAR(255),
                    phon_o VARCHAR(15),
                    gmail VARCHAR(100),
                    prod_id VARCHAR(45),
                    prod_nam VARCHAR(45),
                    categ VARCHAR(45),
                    expdat DATE,
                    tim INT,
                    price DECIMAL(10, 2),
                    subtotal DECIMAL(10, 2),
                    tax DECIMAL(10, 2),
                    total DECIMAL(10, 2),
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Customer data table - with proper primary key
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cust_data (
                    custid VARCHAR(45) PRIMARY KEY,
                    custnam VARCHAR(45),
                    custadd VARCHAR(255),
                    pno VARCHAR(15),
                    gmail VARCHAR(100)
                )
            """)
            
            print("Database tables initialized successfully")
            
        except Exception as e:
            print(f"Table creation warning: {e}")
            # If tables already exist with different structure, continue without error

    def show_store_management(self):
        """This method is called ONLY after successful OTP verification"""
        try:
            # Clear any existing widgets in root
            for widget in self.root.winfo_children():
                widget.destroy()
            
            # Create new instance of StoreManagementSystem
            self.store_management_system_instance = StoreManagementSystem(self.root)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load store management: {str(e)}")
            # Fallback: show login again
            self.__init__(self.root)

    def register_window(self):
        try:
            register_root = Toplevel(self.root)
            Register(register_root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open registration: {str(e)}")

    def forgot_password_window(self):
        messagebox.showinfo("Forgot Password", "Forgot password functionality not yet implemented.")


if __name__ == "__main__":
    root = Tk()
    app = EMARTSYSTEM(root)
    root.mainloop()
    