import math
import random
import smtplib



digit= "0123456789"
otp=""

for i in range(4):
    otp=otp+digit[math.floor(random.random()*10)]
msg=otp
s=smtplib.SMTP_SSL('smtp.gmail.com',465) 
mail_id=input("Enter Mail Id:")
password='ygaomoyakiuczzdi'
s.login(mail_id,password)   
send_to=input("select sender:")
s.sendmail(mail_id,send_to,msg)

my_otp=input("Enter Your OTP:")

if my_otp==msg:
    print('you entered correct otp')

else:
    print('please enter correct otp') 
