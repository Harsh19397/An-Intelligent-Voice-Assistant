import smtplib
from nltk.tokenize import word_tokenize
import enchant
import re
from email.mime.text import MIMEText

dictionary = enchant.Dict("en_US")

def get_recipients_id(text):
    lst = re.findall('\S+@+\S', text)
    return lst

def get_message():
    pass

def get_subject():
    pass

def send_email(text, sender_email_id, sender_email_id_password):
    text="Send an email to Swati Sharma saying How are you didi"
    word_tokens = word_tokenize(text)
    fromx = sender_email_id
    to  = get_recipients_id(text)
    msg = MIMEText(get_message())
    msg['Subject'] = get_subject()
    msg['From'] = fromx
    msg['To'] = to
    
    #Creating SMTP session
    smtp_session = smtplib.SMTP(host='smtp.gmail.com', port=587)
    #Starting TLS for security
    smtp_session.starttls()
    # Authentication 
    smtp_session.login(sender_email_id, sender_email_id_password) 
        
    # sending the mail 
    smtp_session.sendmail(fromx, to, msg.as_string()) 
      
    # terminating the session 
    smtp_session.quit() 
    
send_email("harshparashar19@gmail.com", "Papasabseachhe1957!", "Hello Swati Didi!","Swati")