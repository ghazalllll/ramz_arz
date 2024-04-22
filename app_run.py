#Library for body code
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from PIL import Image, ImageTk
import requests
import os
from datetime import datetime
import pytz
import smtplib
from email.mime.text import MIMEText
# Library for Bitcoin price
import requests as rq
from bs4 import BeautifulSoup as sp
from unidecode import unidecode
import time
from app import (get_webpage_btc,get_webpage_btc2,get_webpage_btc3,get_webpage_btc4,
                 get_webpage_eth,get_webpage_eth2,get_webpage_eth3,get_webpage_eth4)                                                                   

# def send_imail():
    # purchase_price = 42.50
    # Check if the purchase price reaches $43
    # get_webpage_btc2()
    # if price2 >= 43.00:
    # # Set up your email details
    #     sender_email = " sender_email"  # Your Gmail address
    #     recipient_email = "recipient_email"  # Recipient's email address
    #     subject = "Purchase Price Alert"
    #     message = "The purchase price has reached $43. Consider taking action!"

    # # Create the email content
    #     email_content = MIMEText(message)
    #     email_content["Subject"] = subject
    #     email_content["From"] = sender_email
    #     email_content["To"] = recipient_email

    # # Establish a secure connection to the SMTP server (Gmail in this case)
    #     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    #         server.login(sender_email, "gmail")  # Replace with your Gmail password
    #         server.sendmail(sender_email, [recipient_email], email_content.as_string())
    #         print("Email sent successfully!")
    # else:
    #     print("Purchase price is below $43. No email sent.")

def update_image2():

    canvas.itemconfig(image_container, image=img2)

def update_image3():

    canvas.itemconfig(image_container, image=img3)    
def update_btc_price():
    for i in get_webpage_btc():              
        btc_lable.config(text=f"{i}")
        for j in get_webpage_btc2():  
            buy_lable.config(text=f"{j}")
            for x in get_webpage_btc3():  
                sell_lable.config(text=f"{x}")

    # Schedule the next update after  seconds
                root.after(1, update_btc_price)
def update_eth_price():
    for i in get_webpage_eth():              
        btc_lable.config(text=f"{i}")
        for j in get_webpage_eth3():  
            buy_lable.config(text=f"{j}")
            for x in get_webpage_eth4():  
                sell_lable.config(text=f"{x}")
                # for y in get_webpage_eth2():  
                #     ravand_lable.config(text=f"{y}")
    # Schedule the next update after  seconds
                root.after(1, update_eth_price)  
def get_price_of():
    coin = textfield.get()
    # try:
    if coin == "btc":
            #change icon
        update_image2()
            # Use the after method to periodically update the price
        root.after(1000, update_btc_price)
        

    if coin == "eth":
            #change icon 
        update_image3()  
            # Use the after method to periodically update the price
        root.after(1000, update_eth_price)
    elif(coin != "btc" and coin != "eth"):
        messagebox.showerror("price app","Invalid Entry!!!")
    # except Exception as error:  
    #     error = messagebox.showerror("price app","Invalid Entry!!!")


#Graphic body using tkinter library
root = tk.Tk()
root.title("price app")
root.geometry("900x500+300+200")
root.resizable(False,False)
#search box
working_dir = "C:\\Users\\asus\\Desktop\\ramz_arz\\ramz_arz\\media"
os.chdir(working_dir)
a = Image.open("search.png")
photo = ImageTk.PhotoImage(a)
tk.Label(root, image=photo).pack(pady=20,side=tk.TOP)

textfield = tk.Entry(root, justify="center" , width=17 ,
                      font=("poppins",25,"bold"),
                      bg="#404040",fg="white", border=0)
textfield.place(x=290,y=40)

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_button = tk.Button(root, image=search_icon, border=0,
                               cursor="hand2", bg="#404040", command=get_price_of)
search_icon_button.place(x=590,y=34)

#logo

canvas = tk.Canvas(root, width=128, height=128)
canvas.pack(side=tk.TOP)
img1 = Image.open("C:\\Users\\asus\\Desktop\\ramz_arz\\ramz_arz\\media\\icon.png")
img1 = ImageTk.PhotoImage(img1)
image_container = canvas.create_image(0,0, anchor="nw", image=img1)
# Load the second image
img2 = Image.open("C:\\Users\\asus\\Desktop\\ramz_arz\\ramz_arz\\media\\btc2.png")
img2 = ImageTk.PhotoImage(img2)
# Load the Third image
img3 = Image.open("C:\\Users\\asus\\Desktop\\ramz_arz\\ramz_arz\\media\\ethereum2.png")
img3 = ImageTk.PhotoImage(img3)

#bottom box
bottom_box = "C:\\Users\\asus\\Desktop\\ramz_arz\\ramz_arz\\media"
os.chdir(bottom_box)
box = Image.open("box.png")
picture2 = ImageTk.PhotoImage(box)
tk.Label(root, image=picture2).pack(pady=10,side=tk.BOTTOM)

#city name:
# city_Label = tk.Label(root, font=("arial", 40, "bold"), fg="#e355cd")
# city_Label.place(x=120, y=160)

# #time:

# time_label = tk.Label(root, font=("arial", 20, "bold"), fg="#4b4bcc")
# time_label.place(x=120, y=230)

# Clock = tk.Label(root, font=("Helvetica",20), fg="#4b4bcc")
# Clock.place(x=120, y=270)



# labels:
label1 = tk.Label(root, text="قیمت به دلار", font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = tk.Label(root, text="تغییرات", font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
label2.place(x=290, y=400)

label3 = tk.Label(root, text="قیمت خرید(تومان)", font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
label3.place(x=450, y=400)

label4 = tk.Label(root, text=("قیمت فروش(تومان)"), font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
label4.place(x=670, y=400)

# value

btc_lable = tk.Label(root, text="...", font=("arial",14,"bold"),
                     bg="#1ab5ef", fg="#404040")
btc_lable.place(x=120, y=430)

ravand_lable = tk.Label(root, text="...", font=("arial",14,"bold"),
                     bg="#1ab5ef", fg="#404040")
ravand_lable.place(x=290, y=430)

buy_lable = tk.Label(root, text="...", font=("arial",14,"bold"),
                     bg="#1ab5ef", fg="#404040")
buy_lable.place(x=460, y=430)

sell_lable = tk.Label(root, text="...", font=("arial",14,"bold"),
                     bg="#1ab5ef", fg="#404040")
sell_lable.place(x=680, y=430)

         
root.mainloop()