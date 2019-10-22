import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("srisaiabhishakegopal@gmail.com", "e=mc2blackhole") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("srisaiabhishakegopal@gmail.com", "abhidasari1289@gmail.com", message) 
  
# terminating the session 
s.quit() 
