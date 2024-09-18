import tkinter 
from time import strftime


m = tkinter.Tk()
m.title("Digital Clock")
m.geometry("500x100")
m.config(bg='black')

label1 = tkinter.Label(m,text="DIGITAL CLOCK",font=("TT Norms" ,100 ) , bg='grey')
label1.place(relx=0.5,rely=0.1,anchor='center')
label2 = tkinter.Label(m,text="HRS : MIN : SEC" , font=("Courier",90),bg='brown')
label2.place(relx=0.5 , rely=0.3 ,anchor='center')
label = tkinter.Label(m, text="", font=("Courier", 100), bg='#96DED1')
label.place(relx=0.5, rely=0.5, anchor='center')
label_date = tkinter.Label(m,text="",font=("Courier",90) , bg='#239b56')
label_date.place(relx=0.5 , rely=0.7 , anchor='center')



def digital_clock():
    time = strftime('%H : %M : %S ')
    date = strftime('%d-%m-%Y')
    label.config(text=time)
    label_date.config(text=date)
    label.after(1000, digital_clock)
    
digital_clock()
m.mainloop()