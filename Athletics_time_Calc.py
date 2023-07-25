from tkinter import Tk, StringVar, ttk
from tkinter import *

window = Tk()
window.title("Athletics Time Calculator")
window.geometry('670x300+0+0')
window.configure(background='black')
window.resizable(False,False)

#--------------------FRAMES--------------------------
Top= Frame(window, width=1000,height=50,bd=16, relief="raise")
Leftinframe= Frame(window, width=150,height=300,bd=8, relief="raise")
Leftmainframe= Frame(window, width=150,height=300,bd=8, relief="raise")
Rightmainframe= Frame(window, width=300,height=300,bd=8, relief="raise")

Top.pack(side=TOP)
Leftinframe.pack(side=LEFT)
Leftmainframe.pack(side=LEFT)
Rightmainframe.pack(side=RIGHT)

#--------------------Variables-----------------------
value0 = StringVar()
check1 = StringVar()
check2 = StringVar()
check3 = StringVar()
convert = StringVar()
sixtymeter = StringVar()
hundredmeter= StringVar()
twohundredmeter= StringVar()
fourhundredmeter= StringVar()
num1 = float(1.53)
num2 = float(2.024375)
num3 = float(2.218625)
Time = StringVar()

#----------------Time calcluations---------------------
def Convert():
    if(value0=='100m'):
        time = int(float(Time.get()))
        Calc1 = time*num1
        print("Your 100m time will be: ", Calc1)

    elif(value0=='200m'):
        time = int(float(Time.get()))
        Calc2 = time*num2
        print("Your 200m time will be: ", Calc2)

    elif(value0=='400m'):
        time = int(float(Time.get()))
        Calc3 = time*num3
        print("Your 400m time will be: ",Calc3)

#----------------Title----------------------------
title = Label(Top, font=('arial', 40, 'bold'),text='Athletics Time Calculator', 
                    padx=2,pady=2,bd=2,fg="black",)
title.grid(row=0, column=2,sticky=W)

#---------------Objects-----------------------------
box = ttk.Combobox(Leftmainframe,textvariable=value0,state='normal',
                        font=('arial',20,'bold'),width=13)
box['values'] = ('','60m','100m','200m','400m')
box.current()
box.grid(row=0,column=0)

title2 = Label(Leftmainframe, font=('arial', 20, 'bold'),text='Select Distance', 
                    padx=2,pady=2,bd=2,fg="black",)
title2.grid(row=1, column=0,sticky=W)

Entertime=Entry(Leftmainframe,font=('arial',20,'bold'),textvariable=Time,bd=2,
                    width=15,justify='center')
Entertime.grid(row=3,column=0)

title3 = Label(Leftmainframe, font=('arial', 20, 'bold'),text='Enter Time:', 
                    padx=2,pady=2,bd=2,fg="black",)
title3.grid(row=2, column=0,sticky=W)

Convert1 = Label(Leftmainframe, font=('arial', 20, 'bold'),textvariable=hundredmeter,bd=2,
                        width=13,bg="white",padx=2,pady=2, relief='sunken')
Convert1.grid(row=4,column=0)

#----------------------Label Objects----------------------
lblSpace = Label(Leftinframe, font=('arial', 20, 'bold'), bd=2,width=13,
                    pady=2,padx=2)
lblSpace.grid(row=0,column=0)
lblConvert = Label(Leftinframe, font=('arial', 20, 'bold'),textvariable=check1,bd=2,
                        width=13,padx=2,pady=2, relief='sunken')
lblConvert.grid(row=1,column=0, sticky=W)
lblConvert = Label(Leftinframe, font=('arial', 20, 'bold'),textvariable=check2,bd=2,
                        width=13,padx=2,pady=2, relief='sunken')
lblConvert.grid(row=2,column=0, sticky=W)
lblSpace = Label(Leftinframe, font=('arial', 20, 'bold'),textvariable=check3,bd=2,
                        width=13,padx=2,pady=2, relief='sunken')
lblSpace.grid(row=3,column=0, sticky=W)

#----------------------Buttons----------------------
btnConvert=Button(Rightmainframe, text='Convert', padx=2,pady=2, bd=2,fg="black",
                    font=('arial', 18, 'bold'),command = Convert,width=10, height=0).grid(row=1,column=0)
btnReset=Button(Rightmainframe, text='Reset', padx=2,pady=2, bd=2,fg="black",
                    font=('arial', 18, 'bold'),width=10, height=0).grid(row=2,column=0)
btnExit=Button(Rightmainframe, text='Exit', padx=2,pady=2, bd=2,fg="black",
                    font=('arial', 18, 'bold'),width=10, height=0).grid(row=3,column=0)
window.mainloop()