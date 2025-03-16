     import smtplib
     import random
     def read_data_send_mail():
     try:
     f=open("MAILS.txt","r")
     MAILS=f.read()
     MAILS=MAILS.split(",")
     print(MAILS)
     except:
     print("file not available")
     sender_email="sirishashalivahana2573@gmail.com"
     for i in MAILS:
     otp_number=random.randint(00000,9999)
     print(otp_number)
     s = smtplib.SMTP('smtp.gmail.com', 587)
     s.starttls()
     s.login(sender_email, "mpdv agem bizx yxes")
     message = f"Hello user your otp number is{ otp_number}"
     try:
     s.sendmail(sender_email, i, message)
     print("The mail is Sent Sucessfully")
     s.quit()
     except:
     print("The mail was not send")
     read_data_send_mail()
