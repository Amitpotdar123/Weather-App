from tkinter import *
from tkinter import ttk
import requests

def data_get():

    city=city_name.get()
    # used Api
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=53a8ae8cfb736d5ef7d29dfded1a3645").json()
    #  fetaching the details in the our data boxes
    w1_label.config(text=data["weather"][0]["main"])
    des1_label.config(text=data["weather"][0]["description"])
    temp1_label.config(text=str(data["main"]["temp"]-273.15))
    pre1_label.config(text=data["main"]["pressure"])

    
win = Tk()

win.title("Weather Information")
win.config(bg="blue")
win.geometry("500x580")

name_label=Label(win,text="Weather App",font=("Times New Roman",35,"bold"))
name_label.place(x=25,y=50,height=50,width=450)


list_state=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

# dropdown city box
city_name=StringVar()
com= ttk.Combobox(win,text="Weather App",values=list_state,font=("Times New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)


# information box
w_label=Label(win,text="Weather App",font=("Times New Roman",10))
w_label.place(x=25,y=260,height=50,width=100)

w1_label=Label(win,text="",font=("Times New Roman",10))
w1_label.place(x=245,y=260,height=50,width=200)


des_label=Label(win,text="discription",font=("Times New Roman",10))
des_label.place(x=25,y=330,height=50,width=100)

des1_label=Label(win,text="",font=("Times New Roman",10))
des1_label.place(x=245,y=330,height=50,width=200)

temp_label=Label(win,text="Tempreature",font=("Times New Roman",10))
temp_label.place(x=25,y=400,height=50,width=100)

temp1_label=Label(win,text=" ",font=("Times New Roman",10))
temp1_label.place(x=245,y=400,height=50,width=200)

pre_label=Label(win,text="Pressure",font=("Times New Roman",10))
pre_label.place(x=25,y=470,height=50,width=100)

pre1_label=Label(win,text="",font=("Times New Roman",10))
pre1_label.place(x=245,y=470,height=50,width=200)


# Button
button=Button(win,text="Done",font=("Times New Roman",20,"bold"),command=data_get)
button.place(y=190,height=50,width=100,x=200)
win.mainloop()