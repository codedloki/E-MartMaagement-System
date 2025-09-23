import smtplib as s 

#this is way1 of sending mail to user , but attachments cant be sent.
def MailToUser():
        obj=s.SMTP("smtp.gmail.com",587)
        obj.starttls()
        obj.login("mimayurmahajan@gmail.com","Pass@123") #our official emart email and its password. so that customer will receive the email from our official emart email
        subject="your E-mart purchase bill" #subject of our mail.
        body='''Dear {Cust_name} ,
                this is the system generated bill from E-mart Management System.   
                your order is successfully dispatched.
                thank you !
                '''                                          #this is the main body of our mail.
        message = "Subject:{}\n\n{}".format(subject,body)

        obj.sendmail("mimayurmahajan",Cust_mail,message)       #sending mail from official emartmail to CUSTOMERS MAIL ADDRESS 
        print("Mail sent successfully...!")
        obj.quit()                                             #done \




#"less secure apps acceess" should be yes 



#this is way2 of sending mail to user, here attachments can also be sent .
import pdf-mail import sendpdf
def send_BillPdf():
    subject="your E-mart purchase bill" #subject of our mail.
    body='''Dear {Cust_name} ,
                this is the system generated bill from E-mart Management System.   
                your order is successfully dispatched.
                thank you !
                '''
    key= sendpdf("mimayurmahjan@gmail.com","Cust_mail","Pass@123","subject_of_mail","body_of_mail","file_name","Path_of_file")

    k.email_send()














