from tkinter import*
from tkinter import ttk
import random,os,tempfile
from PIL import Image,ImageTk
from pathlib import Path
from tkinter import messagebox
# import mysql.connector
import pymysql


import smtplib as s
from pdf_mail import sendpdf
from time import strftime

BASE_DIR = Path(__file__).resolve().parent

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

        # Initialize database tables
        self.initialize_database()

        #====================================================================================

        lbltitle=Label(self.root,text="E-Mart Management System",bd=15,relief=RIDGE
                       ,bg='white',fg='darkblue',font=("time new roman",50,"bold"),padx=2,pady=4)
        
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open(BASE_DIR/"images"/"logos.jpg")
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

        #==========================Images================================
        img2=Image.open(BASE_DIR/"images"/"drink.jpg")
        img2=img2.resize((270,113),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b2=Button(self.root,image=self.photoimg2,borderwidth=0)
        b2.place(x=48,y=350)

        img3=Image.open(BASE_DIR/"images"/"grocery.jpg")
        img3=img3.resize((250,113),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(self.root,image=self.photoimg3,borderwidth=0)
        b3.place(x=280,y=350)

        img4=Image.open(BASE_DIR/"images"/"grocery2.jpg")
        img4=img4.resize((300,113),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b4=Button(self.root,image=self.photoimg4,borderwidth=0)
        b4.place(x=500,y=350)

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
                                         ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
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
        self.store_table.column("subtotal",width=100)
        self.store_table.column("tax",width=100)
        self.store_table.column("total",width=100)
        
        self.fetch_dataprd()
        self.fetch_data()
        self.store_table.bind("<ButtonRelease-1>",self.get_curssor)

#=======================Database Initialization Method=======================
    #=======================Database Initialization Method=======================
    def initialize_database(self):
        """Initialize database tables with correct schema"""
        try:
            conn = pymysql.connect(
                host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
                port=21390,
                user="avnadmin",
                password="AVNS_flfS-xIQA4vHQtH_z4h",
                database="defaultdb"
            )
            my_cursor = conn.cursor()
            
            # First, drop all existing tables to start fresh
            my_cursor.execute("DROP TABLE IF EXISTS stordata")
            my_cursor.execute("DROP TABLE IF EXISTS category_table")
            my_cursor.execute("DROP TABLE IF EXISTS order_detail")
            my_cursor.execute("DROP TABLE IF EXISTS cust_data")
            
            # Create stordata table with correct schema
            my_cursor.execute("""
                CREATE TABLE stordata (
                    prdid VARCHAR(45) PRIMARY KEY,
                    prdnam VARCHAR(45),
                    categ VARCHAR(45),
                    expirydat DATE,
                    disct INT,
                    price DECIMAL(10, 2)
                )
            """)
            
            # Create category_table
            my_cursor.execute("""
                CREATE TABLE category_table (
                    prod_id VARCHAR(45) PRIMARY KEY,
                    prod_name VARCHAR(45),
                    category_name VARCHAR(45)
                )
            """)
            
            # Create order_detail table
            my_cursor.execute("""
                CREATE TABLE order_detail (
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
                    total DECIMAL(10, 2)
                )
            """)
            
            # Create cust_data table
            my_cursor.execute("""
                CREATE TABLE cust_data (
                    custid VARCHAR(45),
                    custnam VARCHAR(45),
                    custadd VARCHAR(255),
                    pno VARCHAR(15),
                    gmail VARCHAR(100)
                )
            """)
            
            conn.commit()
            conn.close()
            print("Database tables recreated successfully with correct schema")
        except Exception as e:
            print(f"Error initializing database: {str(e)}")
            # If the above fails, try a simpler approach
            self.initialize_database_simple()

    def initialize_database_simple(self):
        """Alternative simpler database initialization"""
        try:
            conn = pymysql.connect(
                host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
                port=21390,
                user="avnadmin",
                password="AVNS_flfS-xIQA4vHQtH_z4h",
                database="defaultdb"
            )
            my_cursor = conn.cursor()
            
            # Simple table creation without complex checks
            tables = [
                """CREATE TABLE IF NOT EXISTS stordata (
                    prdid VARCHAR(45), prdnam VARCHAR(45), categ VARCHAR(45),
                    expirydat DATE, disct INT, price DECIMAL(10, 2))""",
                """CREATE TABLE IF NOT EXISTS category_table (
                    prod_id VARCHAR(45), prod_name VARCHAR(45), category_name VARCHAR(45))""",
                """CREATE TABLE IF NOT EXISTS order_detail (
                    cust_id VARCHAR(45), cust_nam VARCHAR(45), address VARCHAR(255),
                    phon_o VARCHAR(15), gmail VARCHAR(100), prod_id VARCHAR(45),
                    prod_nam VARCHAR(45), categ VARCHAR(45), expdat DATE, tim INT,
                    price DECIMAL(10, 2), subtotal DECIMAL(10, 2), tax DECIMAL(10, 2),
                    total DECIMAL(10, 2))""",
                """CREATE TABLE IF NOT EXISTS cust_data (
                    custid VARCHAR(45), custnam VARCHAR(45), custadd VARCHAR(255),
                    pno VARCHAR(15), gmail VARCHAR(100))"""
            ]
            
            for table_sql in tables:
                try:
                    my_cursor.execute(table_sql)
                except Exception as e:
                    print(f"Table creation warning: {e}")
                    continue
            
            conn.commit()
            conn.close()
            print("Database tables initialized with simple method")
        except Exception as e:
            print(f"Error in simple database initialization: {str(e)}")
#=======================add prouct functionality Declaration =======================
    def generate_id(self):
        # Generate a random 4-digit customer ID
        customer_id = random.randint(1000, 9999)
        self.custid.set(str(customer_id))
        
    def genrate_prdid(self):
        addprdid_var = random.randint(1000, 9999)
        self.addprdid_var.set(str(addprdid_var))

    def add_prd(self):
        try:
            conn = pymysql.connect(
                host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
                port=21390,
                user="avnadmin",
                password="AVNS_flfS-xIQA4vHQtH_z4h",
                database="defaultdb"
            )
            my_cursor = conn.cursor()
            
            my_cursor.execute("INSERT INTO stordata(prdid, prdnam, categ, expirydat, disct, price) VALUES (%s, %s, %s, %s, %s, %s)", (
                self.addprdid_var.get(),
                self.addprdnam_var.get(),
                self.addcat_var.get(),
                self.expdat_var.get(),
                self.disc_var.get(),
                self.pric_var.get()
            ))
            
            my_cursor.execute("INSERT INTO category_table(prod_id, prod_name, category_name) VALUES (%s, %s, %s)", (
                self.addprdid_var.get(),
                self.addprdnam_var.get(),
                self.addcat_var.get()
            ))

            conn.commit()
            self.fetch_dataprd()
            conn.close()
            messagebox.showinfo("Success", "Product Added")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fetch_dataprd(self):
        conn = pymysql.connect(
            host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
            port=21390,
            user="avnadmin",
            password="AVNS_flfS-xIQA4vHQtH_z4h",
            database="defaultdb"
        )
        my_cursor = conn.cursor()
        
        my_cursor.execute("SELECT prdid, prdnam, categ, expirydat, disct, price FROM stordata")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.product_table.delete(*self.product_table.get_children())
            for i in rows:
                self.product_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def Prdget_cursor(self, event=""):
        cursor_row = self.product_table.focus()
        content = self.product_table.item(cursor_row)
        row = content["values"]
        if row and len(row) >= 6:  
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

    def UpdateStr(self):
        try:
            if self.addprdid_var.get() == "" or self.addprdnam_var.get() == "" or self.addcat_var.get() == "" or self.expdat_var.get() == "" or self.disc_var.get() == "" or self.pric_var.get() == "":
                messagebox.showerror("Error", "All fields are Required")
            else:
                conn = pymysql.connect(
                    host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
                    port=21390,
                    user="avnadmin",
                    password="AVNS_flfS-xIQA4vHQtH_z4h",
                    database="defaultdb"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE stordata SET prdnam=%s, categ=%s, expirydat=%s, disct=%s, price=%s WHERE prdid=%s", (
                    self.addprdnam_var.get(),
                    self.addcat_var.get(),
                    self.expdat_var.get(),
                    self.disc_var.get(),
                    self.pric_var.get(),
                    self.addprdid_var.get()
                ))
                my_cursor.execute("UPDATE category_table SET prod_name=%s, category_name=%s WHERE prod_id=%s",(
                    self.addprdnam_var.get(),
                    self.addcat_var.get(),
                    self.addprdid_var.get(),
                ))
                conn.commit()
                self.fetch_dataprd()
                conn.close()
                messagebox.showinfo("Success", "Product has been Updated")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def DeletePrd(self):
        conn = pymysql.connect(
            host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
            port=21390,
            user="avnadmin",
            password="AVNS_flfS-xIQA4vHQtH_z4h",
            database="defaultdb"
        )
        my_cursor = conn.cursor()

        if self.addprdid_var.get() == "":
            messagebox.showerror("Error", "Data not Found in database")
        else:
            sql = "DELETE FROM stordata WHERE prdid=%s"
            val = (self.addprdid_var.get(),)
            my_cursor.execute(sql, val)
            
            sql = "DELETE FROM category_table WHERE prod_id=%s"
            val = (self.addprdid_var.get(),)
            my_cursor.execute(sql, val)
        
            conn.commit()
            self.fetch_dataprd()
            conn.close()
            messagebox.showinfo("Success", "Data Of Product is Deleted !!!")

    def ClearPrd(self):
        self.addprdid_var.set("")
        self.addprdnam_var.set("")
        self.addcat_var.set("")
        self.expdat_var.set("")
        self.disc_var.set("")
        self.pric_var.set("")

#===================================================== Main table ============================================
    def Add_data(self):
        if self.custid.get() == "" or self.prdid.get() == "":
            messagebox.showerror("Error", "All fields are properly required")
        elif len(self.pno.get()) != 10:
            messagebox.showerror("Error", "Phone No. Must be of Length 10")
        elif self.pnt.get().find("@") == -1:
            messagebox.showerror("Error", "Email Must Contain '@' ")
        else:
            try:        
                # Bill calculation
                self.l = []  # sub-total
                self.n = int(self.price.get())
                self.m = int(self.tim.get()) * self.n
                self.l.append(self.m)
                self.sub_total.set(self.m)
                self.tax.set((((sum(self.l)) - int(self.price.get())) * int(self.taxPercent.get())) / 100)
                self.total.set((sum(self.l) + ((((sum(self.l)) - int(self.price.get())) * int(self.taxPercent.get())) / 100)))
                
                conn = pymysql.connect(
                    host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
                    port=21390,
                    user="avnadmin",
                    password="AVNS_flfS-xIQA4vHQtH_z4h",
                    database="defaultdb"
                )
                my_cursor = conn.cursor()
                
                if int(self.disc_var.get()) >= int((self.tim.get())):
                    self.disc_var.set(str(int(self.disc_var.get()) - int(self.tim.get())))
                    my_cursor.execute("UPDATE stordata SET disct=%s WHERE prdid=%s", (self.disc_var.get(), self.addprdid_var.get()))

                    my_cursor.execute("INSERT INTO order_detail(cust_id, cust_nam, address, phon_o, gmail, prod_id, prod_nam, categ, expdat, tim, price, subtotal, tax, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
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
                    
                    my_cursor.execute("INSERT INTO cust_data(custid, custnam, custadd, pno, gmail) VALUES (%s, %s, %s, %s, %s)", (
                        self.custid.get(),
                        self.custnam.get(),
                        self.add.get(),
                        self.pno.get(),
                        self.pnt.get(),
                    ))
                    
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Data has been inserted")
                else:
                    messagebox.showerror("Error", "Insufficient Quantity in Store !!!")
            except Exception as e:
                messagebox.showerror("Error", str(e))    

    def fetch_data(self):
        conn = pymysql.connect(
            host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
            port=21390,
            user="avnadmin",
            password="AVNS_flfS-xIQA4vHQtH_z4h",
            database="defaultdb"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM order_detail")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.store_table.delete(*self.store_table.get_children())
            for i in rows:
                self.store_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    
    def get_curssor(self, ev=""):
        cursor_row = self.store_table.focus()
        content = self.store_table.item(cursor_row)
        row = content["values"]
        if row and len(row) >= 11: 
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
            if len(row) >= 13:
                self.sub_total.set(row[11])
                self.tax.set(row[12])
                self.total.set(row[13])

    def Update(self):
        try:
            if self.custid.get() == "" or self.prdid.get() == "":
                messagebox.showerror("Error", "All fields are Required")
            else:
                # Bill calculation
                self.l = []  # sub-total
                self.n = int(self.price.get())
                self.m = int(self.tim.get()) * self.n
                self.l.append(self.m)
                self.sub_total.set(self.m)
                self.tax.set((((sum(self.l)) - int(self.price.get())) * int(self.taxPercent.get())) / 100)
                self.total.set((sum(self.l) + ((((sum(self.l)) - int(self.price.get())) * int(self.taxPercent.get())) / 100)))
                
                conn = pymysql.connect(
                    host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
                    port=21390,
                    user="avnadmin",
                    password="AVNS_flfS-xIQA4vHQtH_z4h",
                    database="defaultdb"
                )
                my_cursor = conn.cursor()
                
                my_cursor.execute("UPDATE order_detail SET cust_nam=%s, address=%s, phon_o=%s, gmail=%s, prod_id=%s, prod_nam=%s, categ=%s, expdat=%s, tim=%s, price=%s, subtotal=%s, tax=%s, total=%s WHERE cust_id=%s", (
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
                    self.custid.get()
                ))
                
                my_cursor.execute("UPDATE cust_data SET custnam=%s, custadd=%s, pno=%s, gmail=%s WHERE custid=%s", (
                    self.custnam.get(),
                    self.add.get(),
                    self.pno.get(),
                    self.pnt.get(),
                    self.custid.get()
                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Order has been Updated")
                
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
    def delete(self):
        try:
            if self.custid.get() == "":
                messagebox.showerror("Error", "Please enter customer id")
            else:
                conn = pymysql.connect(
                    host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
                    port=21390,
                    user="avnadmin",
                    password="AVNS_flfS-xIQA4vHQtH_z4h",
                    database="defaultdb"
                )
                my_cursor = conn.cursor()

                sql = "DELETE FROM order_detail WHERE cust_id=%s"
                val = (self.custid.get(),)
                my_cursor.execute(sql, val)

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data of product is Deleted !!!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reset(self):
        self.custnam.set("")
        self.add.set("")
        self.pno.set("")
        self.pnt.set("")
        self.prdid.set("")
        self.prdnam.set("")
        self.catg.set("")
        self.expdt.set("")
        self.tim.set("")
        self.price.set("")
        self.custid.set("")

    def search_data(self):
        conn = pymysql.connect(
            host="mysql-26b47ad6-jprashik42-fa1a.c.aivencloud.com",
            port=21390,
            user="avnadmin",
            password="AVNS_flfS-xIQA4vHQtH_z4h",
            database="defaultdb"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM order_detail WHERE " + str(self.search_var.get()) + " LIKE '" + str(self.searchTxt_var.get()) + "%'")

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.store_table.delete(*self.store_table.get_children())
            for i in rows:
                self.store_table.insert("", END, values=i)
        conn.commit()
        conn.close()

#========================bill genrator================================
    def gen_bill(self):
        self.root.geometry("550x720+500+25")
        self.root.title("Bill Generator")

        # Main Frame
        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=0, width=550, height=720)

        # Billing Section Frame
        Billing_Section_Frame = LabelFrame(Main_Frame, text="BILLING SECTION", font=("times new roman", 12, "bold"), bg="white", fg="green")
        Billing_Section_Frame.place(x=22, y=125, width=500, height=500)
        scroll_y = Scrollbar(Billing_Section_Frame, orient=VERTICAL)
        self.textarea = Text(Billing_Section_Frame, yscrollcommand=scroll_y.set, bg="white", fg="blue", font=("times new roman", 12, "bold"), state='disabled')
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter LabelFrame
        Bill_Counter_Frame = LabelFrame(Main_Frame, text="BILL COUNTER", font=("times new roman", 12, "bold"), bg="white", fg="green")
        Bill_Counter_Frame.place(x=255, y=0, width=275, height=125)

        self.lblSubTotal = Label(Bill_Counter_Frame, font=('arial', 11, 'bold'), bg="white", fg="brown", text="SUB-TOTAL :-", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entrySubTotal = ttk.Entry(Bill_Counter_Frame, font=('arial', 11, 'bold'), width=24, state='readonly')
        self.entrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lblTax = Label(Bill_Counter_Frame, font=('arial', 11, 'bold'), bg="white", fg="brown", text="GOV. TAX :-", bd=4)
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.entryTax = ttk.Entry(Bill_Counter_Frame, font=('arial', 11, 'bold'), width=24, state='readonly')
        self.entryTax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblTotal = Label(Bill_Counter_Frame, font=('arial', 11, 'bold'), bg="white", fg="brown", text="TOTAL :- ", bd=4)
        self.lblTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.entryTotal = ttk.Entry(Bill_Counter_Frame, font=('arial', 11, 'bold'), width=24, state='readonly')
        self.entryTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Button Frames
        Btn_Frame = Frame(Main_Frame, bd=2, bg="white")
        Btn_Frame.place(x=25, y=630)

        self.BtnSaveBill = Button(Btn_Frame, command=self.save_bill, text="Save Bill", font=('arial', 15, 'bold'), bg="orangered", fg="white", height=2, width=12)
        self.BtnSaveBill.grid(row=0, column=0, padx=5)

        self.BtnPrint = Button(Btn_Frame, command=self.print_bill, text="Print", font=('arial', 15, 'bold'), bg="orangered", fg="white", height=2, width=12)
        self.BtnPrint.grid(row=0, column=1, padx=5)

        self.BtnExit = Button(Btn_Frame, command=self.send_BillPdf, text="E-mail", font=('arial', 15, 'bold'), bg="orangered", fg="white", height=2, width=12)
        self.BtnExit.grid(row=0, column=2, padx=5)

        # Reciept LabelFrame
        Reciept_Frame = LabelFrame(Main_Frame, text="SEARCH SECTION", font=("times new roman", 12, "bold"), bg="white", fg="green")
        Reciept_Frame.place(x=0, y=0, width=252, height=125)

        self.lblRecieptNo = Label(Reciept_Frame, font=('arial', 11, 'bold'), bg="white", fg="brown", text="RECIEPT NO. :-", bd=4)
        self.lblRecieptNo.grid(row=0, column=0, sticky=W, padx=0, pady=10)

        self.entryRecieptNo = ttk.Entry(Reciept_Frame, font=('arial', 11, 'bold'), width=15)
        self.entryRecieptNo.grid(row=0, column=1, sticky=W, padx=0, pady=10)

        # Search Frame
        Search_Frame = LabelFrame(Reciept_Frame)
        Search_Frame.place(x=58, y=50, width=136, height=48)

        self.BtnSearch = Button(Search_Frame, command=self.search_bill, text="Search", font=('arial', 15, 'bold'), bg="orangered", fg="white", height=1, width=10)
        self.BtnSearch.grid(row=0, column=0)

        # Variables
        self.bill_no = StringVar()
        z = random.randint(1000, 9999)
        self.bill_no.set(z)
        
        # Creating List
        self.l = []

        # Function Calling
        self.welcome()
        self.priceCalc()
        
    def priceCalc(self):
        self.n = int(self.price.get())
        self.m = int(self.tim.get()) * self.n
        self.l.append(self.m)
        if self.prdnam.get() == "":
            messagebox.showerror("Error", "Please Enter Product Name.")
        elif self.prdid.get() == "":
            messagebox.showerror("Error", "Please Enter Product ID.")
        elif self.tim.get() == "":
            messagebox.showerror("Error", "Please Enter Product Quantity Purchased.")
        elif self.price.get() == "":
            messagebox.showerror("Error", "Please Enter Product Price.")
        else:
            self.textarea.config(state='normal')
            self.entrySubTotal.config(state='normal')
            self.entryTax.config(state='normal')
            self.entryTotal.config(state='normal')
            self.textarea.insert(END, f"\n {self.prdid.get()}\t\t{self.prdnam.get()}\t\t{self.tim.get()}\t\t{self.price.get()}")    
            self.sub_total.set('Rs.%.2f' % (sum(self.l)))
            self.tax.set(str('Rs.%.2f' % ((((sum(self.l)) - int(self.price.get())) * int(self.taxPercent.get())) / 100)))
            self.total.set(str('Rs.%.2f' % ((sum(self.l)) + ((((sum(self.l)) - int(self.price.get())) * int(self.taxPercent.get())) / 100))))
            self.entrySubTotal.delete(0, 'end')
            self.entrySubTotal.insert(0, self.sub_total.get())
            self.entryTax.delete(0, 'end')
            self.entryTax.insert(0, self.tax.get())
            self.entryTotal.delete(0, 'end')
            self.entryTotal.insert(0, self.total.get())
            self.textarea.insert(END, f"\n====================================================")
            self.textarea.insert(END, f"\n\n====================================================")
            self.textarea.insert(END, f"\n Sub-Amount :\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax-Amount :\t\t\t{self.tax.get()}")
            self.textarea.insert(END, f"\n-----------------------------------------------------------------------------------------------")
            self.textarea.insert(END, f"\n Total-Amount :\t\t\t{self.total.get()}")
            self.textarea.insert(END, f"\n====================================================")
            self.entrySubTotal.config(state='readonly')
            self.entryTax.config(state='readonly')
            self.entryTotal.config(state='readonly')
            self.textarea.config(state='disabled')

    def welcome(self):
        self.textarea.config(state='normal')
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\n\t\t       Welcome to E-Mart Mall")
        self.textarea.insert(END, f"\n\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.custnam.get()}")
        self.textarea.insert(END, f"\n Customer ID : {self.custid.get()}")
        self.textarea.insert(END, f"\n Phone No. : {self.pno.get()}")
        self.textarea.insert(END, f"\n E-Mail : {self.pnt.get()}")

        self.textarea.insert(END, f"\n\n====================================================")
        self.textarea.insert(END, f"\n Product\t\tProduct\t\tQuantity\t\tPrice of ")
        self.textarea.insert(END, f"\n   ID.  \t\tName.  \t\t        \t\t Product ")
        self.textarea.insert(END, f"\n        \t\t       \t\t\t\t(1 Quantity)")
        self.textarea.insert(END, f"\n====================================================\n")
        self.textarea.config(state='disabled')

    def save_bill(self):
        try:
            op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
            if op:
                self.bill_data = self.textarea.get(1.0, END)
                # Create bills directory if it doesn't exist
                bills_dir = 'C:/Tushar/StoreMag/Bills/'
                if not os.path.exists(bills_dir):
                    os.makedirs(bills_dir)
                f1 = open(bills_dir + str(self.bill_no.get()) + ".txt", 'w')
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved!!", f"Bill No. : {self.bill_no.get()} Saved Successfully!!!")
        except Exception as e: 
            messagebox.showerror("Error", str(e))

    def print_bill(self):
        try:
            q = self.textarea.get(1.0, "end-1c")
            filename = tempfile.mktemp('.txt')
            open(filename, 'w').write(q)
            os.startfile(filename, "Print")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def search_bill(self):
        try:
            self.textarea.config(state='normal')
            found = "no"
            bills_dir = 'C:/Tushar/StoreMag/Bills/'
            if os.path.exists(bills_dir):
                for i in os.listdir(bills_dir):
                    if i.split('.')[0] == self.entryRecieptNo.get():
                        f1 = open(f'{bills_dir}{i}', 'r')
                        self.textarea.delete(1.0, END)
                        for d in f1:
                            self.textarea.insert(END, d)
                        f1.close()
                        found = "yes"
            if found == "no":
                messagebox.showerror("Error!!", f"Bill No. {self.entryRecieptNo.get()} Not Found!!!")
            self.textarea.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def send_BillPdf(self):
        try:
            cust_name = self.custnam.get()

            def mailToUser():
                subject = "Your E-mart purchase bill"
                body = f'''Dear {cust_name},
This is the system generated bill from E-mart Management System.   
Your order is successfully dispatched.
Thank you!
'''
                key = sendpdf("mimayurmahajan@gmail.com", self.pnt.get(), "zmuv azck rjxo fnqt", subject, body, self.bill_no.get(), r"C:/Tushar/StoreMag/Bills/")
                key.email_send()

            mailToUser()
            messagebox.showinfo("Success", "Mail Sent Successfully!!!") 
        except Exception as e:
            messagebox.showerror("Error", str(e))

# if __name__ == "__main__":
#     root = Tk()
#     obj = StoreManagementSystem(root)
#     root.mainloop()