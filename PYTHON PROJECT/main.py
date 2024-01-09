from tkinter import *
from tkinter import messagebox

root =Tk()

root.title('my convertor')
root.iconbitmap('cal.ico')
root.geometry("1500x1700")
root.configure(background="#F5D0F7")


my_topic=Label(root,text='CURRENCY   CONVERTOR   CALCULATOR', bg='#F0D31E', fg='#FB5908', width=60,height=3)
my_topic.grid(padx=40,pady=30)
lab4= Label(root, text='currency from' , bg='#9EFA51',fg="#1B1B1A", width=20,height=2 )
lab4.grid(padx=100,pady=10)
options1 =[
    'IND',
    'USD',
    'PKR',
    'UAE'
]
clicked1 =StringVar()
clicked1.set(options1[0])
drop1 = OptionMenu(root,clicked1,*options1)
drop1.grid()
lab5= Label(root, text='currency to',bg='#9EFA51',fg="#1B1B1A", width=20,height=2)
lab5.grid(padx=30,pady=10)
options2 =[
    'USD',
    'IND',
    'PKR',
    'UAE'
]
clicked2 =StringVar()
clicked2.set(options2[0])
drop2 = OptionMenu(root,clicked2,*options2)
drop2.grid()

def dis():
    global lab1
    global lab2
    val=int(e.get())
    if(val!=0):
      str1=clicked1.get()
      str2=clicked2.get()
      if str1=='IND' and str2=='USD':
        res = (val *0.12)
        lab2=Label(root, text=' Currency from '+ str1 +' to '+ str2 +' is')
        lab2.grid()
        lab1 = Label(root, text= float(res), width = 40 , height=4, borderwidth = 2,fg='black',bg='gray')
        lab1.grid( pady=10)
        b1['state']=DISABLED
      elif str1=='USD' and str2=='IND' :
        res = (val *82.42)
        lab2=Label(root, text=' Currency from '+ str1 +' to '+ str2 +' is')
        lab2.grid()
        lab1 = Label(root, text= float(res),width = 40 , height=3, borderwidth = 2,fg='black',bg='gray',)
        lab1.grid()
        b1['state']=DISABLED
      elif str1=='IND' and str2=='PKR' :
         res = (val *2.65)
         lab2=Label(root, text=' Currency from '+ str1 +' to '+ str2 +' is')
         lab2.grid()
         lab1 = Label(root, text= float(res),width = 40 , height=4, borderwidth = 2,fg='black',bg='gray')
         lab1.grid()
         b1['state']=DISABLED
      elif str1=='PKR' and str2=='IND' :
         res = (val *0.38)
         lab2=Label(root, text=' Currency from '+ str1 +' to '+ str2 +' is')
         lab2.grid()
         lab1 = Label(root, text= float(res),width = 40 , height=4, borderwidth = 2,fg='black',bg='gray')
         lab1.grid()
         b1['state']=DISABLED
      elif str1=='IND' and str2=='UAE' :
         res = (val *0.045)
         lab2=Label(root, text=' Currency from '+ str1 +' to '+ str2 +' is')
         lab2.grid()
         lab1 = Label(root, text= float(res),width = 40 , height=4, borderwidth = 2,fg='black',bg='gray')
         lab1.grid()
         b1['state']=DISABLED
      elif str1=='UAE' and str2=='IND' :
         res = (val *22.44)
         lab1 = Label(root, text= float(res),width = 40 , height=4, borderwidth = 2,fg='black',bg='gray')
         lab1.grid()
         b1['state']=DISABLED
      elif str1=='USD' and str2=='UAE' :
         res = (val *3.67)
         lab1 = Label(root, text= float(res),width = 40 , height=4, borderwidth = 2,fg='black',bg='gray')
         lab1.grid()
         b1['state']=DISABLED     
      elif str1=='UAE' and str2=='USD' :
         res = (val *0.27)
         lab1 = Label(root, text= float(res),width = 40 , height=4, borderwidth = 2,fg='black',bg='gray')
         lab1.grid()
         b1['state']=DISABLED    
      elif str1==str2:
        root.iconbitmap("warning.ico")
        messagebox.showwarning("warning","please don't provide same currency for both input  ")               
    else:    
      messagebox.showinfo("new message","please enter valid number!!")  
def delete ():
    lab2.destroy()
    lab1.destroy()
    b1['state']=NORMAL
        
       
amt = Label(root, text='AMOUNT TO CONVERT', activeforeground='green')
amt.grid(pady=20 ,padx=20)

e = Entry(root, width=40,  font=('arial',15),fg='black')
e.grid( padx=30,pady=30)

b1 = Button(root, text='click it', command= dis,bg='#33FFE0', width=10, height=2, borderwidth='0' )
b1.grid()

dele= Button(root, text='clear',command=delete,bg='#33FFE0', width=10, height=2, borderwidth='0')
dele.grid(pady=20)

root.mainloop()