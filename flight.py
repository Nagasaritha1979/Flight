from tkinter import *
from tkinter import ttk
import tkcalendar

win=Tk()
win.title('TRIP')

win.config(bg='blue')
travel_from=''
travel_to=''
def date_range(start,stop):
    
    global travel_from
    global travel_to
    
    date1=str(start)
    date2=str(stop)
    
    diff=(stop-start).days
    
    label2.config( text="You are travelling from "+ travel_from + ' to ' + 
                  travel_to + ' Departure date being '+ date1+ ' and ' + ' Arrival date being '+ date2)
    

    label3.config(text='No of days of travel is: '+ str(diff) )

def hotel():
    pass

def flight():
    pass

def train():
    pass

def car():
    pass

def opt1():
    global travel_from
    
    menu_button1.config(text='Bangalore')
    
    travel_from='Bangalore'
    
def opt2():
    global travel_from
    menu_button1.config(text='Singapore')
    travel_from='Singapore'
    
def opt3():
    global travel_from    
    menu_button1.config(text='Dubai')
    travel_from='Dubai'
    
def optr1():
    
    global travel_to

    menu_button2.config(text='Frankfurt')
    travel_to='Frankfurt'    
def optr2():
    global travel_to
    menu_button2.config(text='Paris')
    travel_to='Paris'
    
    
def optr3():
    global travel_to
    menu_button2.config(text='Rome')
    travel_to='Rome'
    
    
heading=Label(win, text="Your Trip Begins Here", justify=CENTER,font=("Arial Bold",25),bg='blue',fg='white')
heading.place(x=400,y=20)

btn_hotels=Button(win, bg='navy blue', fg='white',activebackground='navy blue',text='HOTELS', width=10, command=hotel,font=("Arial",20))
btn_hotels.place(x=100,y=100)

btn_flights=Button(win, bg='navy blue', fg='white',activebackground='navy blue',text='FLIGHTS', width=10, command=flight,font=("Arial",20))
btn_flights.place(x=300,y=100)

btn_trains=Button(win, bg='navy blue', fg='white',activebackground='navy blue',text='TRAINS', width=10, command=train,font=("Arial",20))
btn_trains.place(x=500,y=100)

btn_cars=Button(win, bg='navy blue', fg='white',text='CARS',activebackground='navy blue', width=10, command=car,font=("Arial",20))
btn_cars.place(x=700,y=100)

var1=StringVar()
var1.set("Round-Trip")
option_menu1=OptionMenu(win, var1,'Round-Trip','One-Way','Multi-City')
option_menu1.place(x=75,y=190) 

option_menu1.config(bg='blue',fg='white')
option_menu1['menu'].config(bg='blue')

var2=StringVar()
var2.set("Economy")
option_menu2=OptionMenu(win, var2,'Economy','Premium Economy','Business','First')
option_menu2.place(x=350,y=190)

option_menu2.config(bg='blue',fg='white')
option_menu2['menu'].config(bg='blue')
text=StringVar()

menu_button1=Menubutton(win,text='Leaving From',bg='white',width=40)
menu_button1.menu=Menu(menu_button1)
menu_button1['menu']=menu_button1.menu

menu_button1.menu.add_command(label = "Bangalore", 
                                command = opt1)
menu_button1.menu.add_command(label='Singapore',command=opt2)
menu_button1.menu.add_command(label='Dubai',command=opt3)
menu_button1.place(x=75,y=250)

                       
menu_button2=Menubutton(win,text='Going to',bg='white',width=40)
menu_button2.menu=Menu(menu_button2)
menu_button2['menu']=menu_button2.menu

menu_button2.menu.add_command(label = "Frankfurt", 
                                command = optr1)
menu_button2.menu.add_command(label='Paris',command=optr2)
menu_button2.menu.add_command(label='Rome',command=optr3)
menu_button2.place(x=375,y=250)

start_date=tkcalendar.DateEntry(win)
start_date.place(x=700,y=250)

end_date=tkcalendar.DateEntry(win)
end_date.place(x=800,y=250)



search_btn=Button(win,text='SEARCH',fg='white',bg='navy blue',command=lambda: date_range(start_date.get_date(),end_date.get_date()))
search_btn.place(x=1000,y=250)                      
                        
label2=Label(win,text=' ',fg='white',bg='navy blue',font=("Arial",15))
label2.place(x=50,y=350)

label3=Label(win,text=' ',fg='white',bg='navy blue',font=("Arial",15))
label3.place(x=100,y=500)



win.mainloop()
