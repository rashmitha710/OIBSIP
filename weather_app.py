# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:26:35 2024

@author: Rashmitha
"""

from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=de6a1eb66ada2fc7cbbc29e5e4885d93").json()

    wc_val.config(text=data["weather"][0]["main"])
    wd_val.config(text=data["weather"][0]["description"])
    wt_val.config(text=str(int(data["main"]["temp"]-273.15)))
    wp_val.config(text=data["main"]["pressure"])


win=Tk()
win.title("Rashmitha")
win.config(bg="blue")
win.geometry("500x560")
name_label=Label(win,text="My Weather app",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()

list_name=["Andhra Pradesh","Arunachal Pradesh ",
           "Assam","Bihar","Chhattisgarh","Goa",
           "Gujarat","Haryana","Himachal Pradesh",
           "Jammu and Kashmir","Jharkhand","Karnataka",
           "Kerala","Madhya Pradesh","Maharashtra","Manipur",
           "Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
           "Rajasthan","Sikkim","Tamil Nadu","Telangana",
           "Tripura","Uttar Pradesh","Uttarakhand",
           "West Bengal","Andaman and Nicobar Islands",
           "Chandigarh","Dadra and Nagar Haveli",
           "Daman and Diu","Lakshadweep",
           "National Capital Territory of Delhi","Puducherry"]


com=ttk.Combobox(win,text="Rashmitha",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

wc_label=Label(win,text="Weather Climate",font=("Time New Roman",10,"italic"))
wc_label.place(x=25,y=270,height=50,width=210)

wc_val=Label(win,text="",font=("Time New Roman",10,"italic"))
wc_val.place(x=250,y=270,height=50,width=210)

wd_label=Label(win,text="Weather Description",font=("Time New Roman",10,"italic"))
wd_label.place(x=25,y=330,height=50,width=210)

wd_val=Label(win,text="",font=("Time New Roman",10,"italic"))
wd_val.place(x=250,y=330,height=50,width=210)

wt_label=Label(win,text="Temperature",font=("Time New Roman",10,"italic"))
wt_label.place(x=25,y=390,height=50,width=210)

wt_val=Label(win,text="",font=("Time New Roman",10,"italic"))
wt_val.place(x=250,y=390,height=50,width=210)


wp_label=Label(win,text="Pressure",font=("Time New Roman",10,"italic"))
wp_label.place(x=25,y=450,height=50,width=210)

wp_val=Label(win,text="",font=("Time New Roman",10,"italic"))
wp_val.place(x=250,y=450,height=50,width=210)

btn=Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get)
btn.place(x=200,y=190,height=50,width=100)

#if __name__ == "__main__":
win.mainloop()
