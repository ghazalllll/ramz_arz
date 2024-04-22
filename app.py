#Library for body code
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from PIL import Image, ImageTk
import requests
import os
from datetime import datetime
import pytz
import smtplib,ssl
from email.mime.text import MIMEText
# Library for Bitcoin price
import requests as rq
from bs4 import BeautifulSoup as sp
from unidecode import unidecode
import time
import numpy as np


def message():
    get_webpage_btc()


def get_webpage_btc():
    
    
    #قیمت بیت کوین به دلار
    url = "https://kifpool.me/wallet/bitcoin-BTC"
    response1 = rq.get(url)
    response1 = response1.text
    suap = sp (response1, 'html.parser')
    price1 = suap.find(id="coin-upricenit-price")
    price1=price1.text
    price1 = price1.replace('$','')
    price1 = price1.replace(',','')
    
    purchase_price = int(price1)
    #قابلیت ارسال ایمیل
    if purchase_price >= 47000:
        smtp_server ='smtp.gmail.com'
        port = 465

        sender = 'sender_email'  
        receiver = 'recipient_email' 
        password = " password"

        message =''' \
        subject:Test

        Hi, this message is from app price.
        BITCOIN(BTC) has reached the price you want    
        '''
        context = ssl.create_default_context()


        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender,password)  # Replace with your Gmail password
            server.sendmail(sender, receiver, message)
             
    # Set up your email details
    #     sender_email = "sender_email"  # Your Gmail address
    #     recipient_email = "recipient_email"  # Recipient's email address
    #     subject = "Purchase Price Alert"
    #     message = "The purchase price has reached $43000. Consider taking action!"

    # # Create the email content
    #     email_content = MIMEText(message)
    #     email_content["Subject"] = subject
    #     email_content["From"] = sender_email
    #     email_content["To"] = recipient_email

    # # Establish a secure connection to the SMTP server (Gmail in this case)
    #     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    #         server.login(sender_email, "sender_gmail")  # Replace with your Gmail password
    #         server.sendmail(sender_email, [recipient_email], email_content.as_string())
            # print("Email sent successfully!")
    price1 = sp(price1, 'html.parser')
    return price1

def get_webpage_btc2():
    # قیمت خرید بیت کوین به تومان
    url = "https://kifpool.me/wallet/bitcoin-BTC"
    response2 = rq.get(url)
    response2 = response2.text
    suap = sp (response2, 'html.parser')
    price2 = suap.find(id="coin-price-buy")
    
    return price2
    
    
def get_webpage_btc3():
# قیمت فروش بیت کوین به تومان
    url = "https://kifpool.me/wallet/bitcoin-BTC"
    response3 = rq.get(url)
    response3 = response3.text
    suap = sp (response3, 'html.parser')
    price3 = suap.find(id="coin-price-sell")

    return price3
    

def get_webpage_btc4():
#  تغییرات بیت کوین 
    url = "https://www.iranjib.ir/showgroup/23/realtime_price/"
    response4 = rq.get(url)
    response4 = response4.text
    suap = sp (response4, 'html.parser')
    price4 = suap.find(id="f_8277_99")
    price4 =price4.txt
    
    price4 = sp(price4, 'html.parser')

    return price4
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#اتریوم
def get_webpage_eth():
    
    
    #قیمت اتریوم به دلار
    url = "https://kifpool.me/wallet/ethereum-eth"
    response1 = rq.get(url)
    response1 = response1.text
    suap = sp (response1, 'html.parser')
    price1 = suap.find(id="coin-upricenit-price")
    price1=price1.text
    price1 = price1.replace('$','')
    price1 = price1.replace(',','')
    

    purchase_price = int(price1)
    #قابلیت ارسال ایمیل
    if purchase_price >= 46000:
        smtp_server ='smtp.gmail.com'
        port = 465

        sender = 'sender_email'  
        receiver = 'recipient_email' 
        password = " password"

        message =''' \
        subject:Test

        Hi, this message is from app price.
        ETHEREUM(ETH) has reached the price you want    
        '''
        context = ssl.create_default_context()


        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender,password)  # Replace with your Gmail password
            server.sendmail(sender, receiver, message)
             
    # Set up your email details
    #     sender_email = "sender_email"  # Your Gmail address
    #     recipient_email = "recipient_email"  # Recipient's email address
    #     subject = "Purchase Price Alert"
    #     message = "The purchase price has reached $43000. Consider taking action!"

    # # Create the email content
    #     email_content = MIMEText(message)
    #     email_content["Subject"] = subject
    #     email_content["From"] = sender_email
    #     email_content["To"] = recipient_email

    # # Establish a secure connection to the SMTP server (Gmail in this case)
    #     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    #         server.login(sender_email, "sender_email")  # Replace with your Gmail password
    #         server.sendmail(sender_email, [recipient_email], email_content.as_string())
            # print("Email sent successfully!")
    price1 = sp(price1, 'html.parser')
    return price1

def get_webpage_eth2():
    # تغییرات اتریوم
    url = "https://www.iranjib.ir/showgroup/23/realtime_price/"
    response2 = rq.get(url)
    response2 = response2.text
    suap = sp (response2, 'html.parser')
    price2 = suap.find(id="f_8278_99")
    price2 = unidecode(price2.text)
    price2 = sp(price2, 'html.parser')

    return price2
    
def get_webpage_eth3():
# قیمت خرید اتریوم به تومان
    url = "https://kifpool.me/wallet/ethereum-eth"
    response3 = rq.get(url)
    response3 = response3.text
    suap = sp (response3, 'html.parser')
    price3 = suap.find(id="coin-price-buy")

    return price3
    

def get_webpage_eth4():
# قیمت فروش اتریوم به تومان 
    url = "https://kifpool.me/wallet/ethereum-eth"
    response4 = rq.get(url)
    response4 = response4.text
    suap = sp (response4, 'html.parser')
    price4 = suap.find(id="coin-price-sell")
    
    return price4