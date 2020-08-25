import smtplib
import enchant
from google_apis_speech_text_conversion import SpeechToText as stt
from google_apis_speech_text_conversion import TextToSpeech as tts
from email.mime.text import MIMEText

dictionary = enchant.Dict("en_US")

def get_recipients_id(assistant_name):
    print("{}: Whom do you want to send email? If there are more than one recipients separate them using 'and'.".format(assistant_name))
    tts.speak("Whom do you want to send email? If there are more than one recipients separate them using 'and'.")
    recipients = stt.speechToText()
    lst = recipients.split('and')
    for s in range(len(lst)):
        lst[s] = lst[s].replace(" ", "")

    return lst

def get_message(assistant_name):
    print("{}: What is the message sir!".format(assistant_name))
    tts.speak("What is the message.")
    message = stt.speechToText()
    
    return message

def get_subject(assistant_name):
    print("{}: What is the subject sir!".format(assistant_name))
    tts.speak("What is the subject.")
    subject = stt.speechToText()
    
    return subject

def send_email(assistant_name, sender_email_id, sender_email_id_password):
    recipient_list = get_recipients_id(assistant_name)
    fromx = sender_email_id
    to  = recipient_list
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
    