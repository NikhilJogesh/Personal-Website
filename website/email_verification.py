import smtplib
import math
import random
import json
import re
import socket
import dns
from flask import flash

"""
# Checks if the email provided by the user is valid
def email_validation(email_address):
    #Step 1: Check email
    #Check using Regex that an email meets minimum requirements, throw an error if not
    addressToVerify = email_address
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

    if match == None:
        #print('Bad Syntax in ' + addressToVerify)
        return False

    #Step 2: Getting MX record
    #Pull domain name from email address
    domain_name = email_address.split('@')[1]

    #get the MX record for the domain
    records = dns.resolver.resolve(domain_name, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    #Step 3: ping email server
    #check if the email address exists

    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail('me@domain.com')
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        print("sucessfully failed")
        return True
    else:
        return False
"""

def send_verification_code(email, username, otp):
    print("joe mama")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    with open("secret_key.json", "r") as f:
        json_file = json.load(f)
        sender_email = json_file["email_address"]
        print(sender_email)
        sender_password = json_file["email_password"]
        server.login(sender_email, sender_password)

    #email_valid = email_validation(email)

    #if not email_valid:
     #   print("abcdefu")
     #   flash("Email Invalid")
     #   return

    message = f"""
Hi {username},
A sign up attempt was made using the your email address, {email} to
www.nikhiljogesh.me 's blog section.
We just need to verify your it before you can access the blog.

Verify your email address by entering this OTP:

    {otp}

Thanks!, {username};
Nikhil Jogesh :)
                """

    server.sendmail(sender_email, email, message)
    server.quit()

# function to generate OTP
def generate_OTP(otp_len=6) :

    # Declare a string variable
    # which stores all string
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # Do not alter
    OTP = ""
    length = len(string)
    for _ in range(otp_len) :
        OTP += string[math.floor(random.random() * length)]

    return OTP



