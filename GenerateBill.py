from tkinter import *
from tkinter import ttk 
import random,os,tempfile
from tkinter import messagebox

class Generate_Bill:
    
     
    def __init__(self,root):
        self.root = root
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

        self.BtnExit=Button(Btn_Frame,command=self.root,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",height=2,width=12)
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
        self.custnam=StringVar()
        self.custnam.set("tushar")
        self.custid=StringVar()
        self.custid.set("54321")
        self.pno=StringVar()
        self.pno.set("123456789")
        self.pnt=StringVar()
        self.pnt.set("987654321")
        self.price=StringVar() #Tushar's variable type was StringVar()
        self.price.set("12000")
        self.var_email=StringVar() #This Variable from Pranay Login
        self.var_email.set("tushari12345@gmail.com")
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        # self.search_bill=StringVar()
        self.prdnam=StringVar()
        self.prdnam.set("Colgate")
        self.prdid=StringVar()
        self.prdid.set("12345")
        self.tim=StringVar() #Quantity = Disc = Tim
        self.tim.set("50")
        self.taxPercent=StringVar()
        self.taxPercent.set(18)
        self.sub_total=StringVar()
        self.tax=StringVar()
        self.total=StringVar()

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
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
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
        self.textarea.insert(END,f"\n Email ID : {self.var_email.get()}")     

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
            f1=open('Bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved!!",f"Bill No. : {self.bill_no.get()} Saved Successfully!!!")
            f1.close()

    def print_bill(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"Print")

    def search_bill(self):
        self.textarea.config(state='normal')
        found = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.entryRecieptNo.get():
                f1=open(f'Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found == "no":
            messagebox.showerror("Error!!",f"Bill No. {self.entryRecieptNo.get()} Not Found!!!")
        self.textarea.config(state='normal')
    


if __name__ == "__main__":
    root = Tk()
    obj = Generate_Bill(root)
    root.mainloop()        