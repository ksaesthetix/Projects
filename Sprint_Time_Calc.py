from tkinter import Tk, StringVar, ttk, Scrollbar
from tkinter import *

window = Tk()

window.title("Sprint Time Calc")
window.geometry('641x250')
window.configure(background='#c6d2ff')
window.resizable(False,False)

def Help():
    HelpWindow = Toplevel(window)
    HelpWindow.title("Help")
    HelpWindow.geometry("300x200")
    HelpWindow.configure(background='#c6d2ff')
    HelpWindow.resizable(False,False)

    scroll=Scrollbar(HelpWindow, orient='vertical')
    scroll.pack(side=RIGHT, fill='y')

    title = Label(HelpWindow, font=('arial',25, 'bold'),text='Instructions', 
                    justify='center',padx=2,pady=2,bd=2,fg="black",background='#c6d2ff')
    T = Text(HelpWindow, height =3, width = 60, yscrollcommand=scroll.set, background='#c6d2ff')
    Fact = """For 100m - Enter your 60m time
              For 200m - Enter your 100m time
              For 400m - Enter your 200m time"""
    title.pack()
    scroll.config(command=T.yview)
    T.pack()
    T.insert(END, Fact)

    def close_win():
        HelpWindow.destroy()

    Button(HelpWindow, text="Exit", command=close_win, font="arial 15", width=9).place(x=84, y=140)

def Calculate():
    # Get the selected distance
    distance = distancevalue.get()
    conversion_num = 1.53
    if distance == '100m':
        conversion_num = 1.53
    elif distance == '200m':
        conversion_num = 2.024375
    elif distance == '400m':
        conversion_num = 2.218625
    else:
        conversion_num = None
    
    if conversion_num == None:
        conversionentry.config(text="Invalid distance selected")
        return
    # Get the current personal best time
    personal_best = float(timeentry.get())

    # Calculate the prediction time
    prediction = personal_best * conversion_num
    # Display the prediction time
    conversionentry.config(text=f'{prediction:.2f}s')


title = Label(font=('arial',35, 'bold'),text='Sprint Time Predictor', 
                    justify='center',padx=2,pady=2,bd=2,fg="black",background='#c6d2ff')
distance = Label(window, text="Distance:", font="arial,15", background='#c6d2ff')
time = Label(window, text="Time:", font="arial,15",background='#c6d2ff')
conversion = Label(window, text="Predicted Time:", font="arial,15", background='#c6d2ff')


title.place(x=80)
distance.place(x=50,y=75)
time.place(x=50,y=140)
conversion.place(x=50,y=200)

distancevalue = StringVar(window)
distancevalue.set('Select Distance')
distancebox = ttk.Combobox(textvariable=distancevalue, state='readonly',font=('arial',13,'bold'),width=18)
distancebox['values'] = ('Select Distance','100m','200m','400m')
distancebox.current(0)

helplabel = Label(window, font=('arial', 9, 'bold') ,text="Read the Help before use:", background='#c6d2ff')
timevalue=StringVar()
timeentry = Entry(window, textvariable=timevalue, font="arial 13",justify='center', width=18)

conversionvalue = StringVar()
conversionentry = Label(window, font="arial,15", width=15, relief='sunken')

distancebox.place(x=220,y=75)
helplabel.place(x=220, y=110)
timeentry.place(x=220, y=140)
conversionentry.place(x=220, y=200)


Button(text="Calculate", command=Calculate, font="arial 15", width=12).place(x=430, y=75)
Button(window, text="Exit", command=lambda:exit(), font="arial 15", width=12).place(x=430, y=140)
Button(window, text="Help", command=Help, font="arial 15", width=12).place(x=430, y=200)


window.mainloop()