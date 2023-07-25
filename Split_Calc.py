# Imports #
from tkinter import Tk, StringVar, ttk,Scrollbar, LEFT, RIGHT, Y
from tkinter import *

# Window Start #
window = Tk()
window.title("Sprint Split Calculator")
window.geometry('600x510')
window.configure(background='#B2BEB5')
window.resizable(False,False)

# Functions # 
def calculate():
    distance_map = {
        '10m': 10,
        '20m': 20,
        '30m': 30,
        '40m': 40,
        '50m': 50,
        '60m': 60,
        '100m': 100,
        '200m': 200,
        '300m': 300,
        '400m': 400
    }

    selected_distance = distancebox.get()
    selected_time = timeentry.get()
    selected_interval = intervalentry.get()

    if selected_distance in distance_map and selected_time and selected_interval:
        try:
            distance_in_meters = distance_map[selected_distance]
            time_in_seconds = float(selected_time)
            interval_in_meters = distance_map[selected_interval]

            # Calculate the total number of intervals
            num_intervals = distance_in_meters // interval_in_meters

            if num_intervals > 0:
                split_time = time_in_seconds / num_intervals
                conversionentry.config(text=f"{split_time:.2f} seconds per {selected_interval}")

                # Display intervals in the table with accumulated split times
                interval_table.delete(*interval_table.get_children())  # Clear previous data

                accumulated_time = 0.0
                for i in range(1, num_intervals + 1):
                    accumulated_time += split_time
                    interval_distance = i * interval_in_meters
                    interval_table.insert("", "end", values=(f"{interval_distance}m", f"{accumulated_time:.2f} seconds"))

                # Resize the table based on the number of intervals
                interval_table["height"] = num_intervals

                # Center the text in each cell of the table
                for col in interval_table["columns"]:
                    interval_table.column(col, anchor="center")

                # Display the table
                interval_table.pack()
            else:
                conversionentry.config(text="Invalid Interval")
                interval_table.pack_forget()  # Hide the table if no valid intervals

        except ValueError:
            conversionentry.config(text="Invalid Time (Enter a number)")
            interval_table.pack_forget()  # Hide the table if invalid time input
    else:
        conversionentry.config(text="Select Distance, Interval, and Enter Time")
        interval_table.pack_forget()  # Hide the table if input is missing
    interval_table.grid(row=5, column=0, columnspan=2,padx=180, pady=260)  # Adjust row and column values as needed

# Labels #
title = Label(font=('arial',35, 'bold'),text='Sprint Split Calculator', 
                    justify='center',padx=1,pady=1,bd=2,fg="black",background='#B2BEB5')
#title_width = len(title["text"])  # Get the width of the title text
#title.place(x=(600 - title_width*19) / 2, y=2)  # Center the title horizontally
title.place(x=50)
distance = Label(window, text="Distance:", font="arial,15", background='#B2BEB5')
distance.place(x=50,y=75)
time = Label(window, text="Time:", font="arial,15",background='#B2BEB5')
time.place(x=50,y=200)
interval = Label(window, text="Interval:", font="arial,15",background='#B2BEB5')
interval.place(x=50,y=140)
conversion = Label(window, text="Split Time:", font="arial,15", background='#B2BEB5')
conversion.place(x=50,y=260)

# Entry Fields #
distancevalue = StringVar(window)
distancevalue.set('Select Distance')
distancebox = ttk.Combobox(textvariable=distancevalue, state='readonly',font=('arial',13,'bold'),width=24, justify='center')
distancebox['values'] = ('Select Distance','100m','200m','300m','400m')
distancebox.current(0)

helplabel = Label(window, font=('arial', 9, 'bold') ,text="Read the Help before use:", background='#B2BEB5')
timevalue=StringVar()
timeentry = Entry(window, textvariable=timevalue, font="arial 13",justify='center', width=24)

intervalvalue=StringVar()
intervalvalue.set('Select Interval')
intervalentry = ttk.Combobox(textvariable=intervalvalue, state='readonly',font=('arial',13,'bold'),width=24, justify='center')
intervalentry['values'] = ('Select Interval','10m','20m','30m','40m','50m','60m','100m','200m','300m','400m')
intervalentry.current(0)

conversionvalue = StringVar()
conversionentry = Label(window, font="arial,10", width=24, relief='sunken')

distancebox.place(x=180,y=75)
helplabel.place(x=180, y=110)
intervalentry.place(x=180, y=140)
timeentry.place(x=180, y=200)
#conversionentry.place(x=220, y=260)

# Table to display intervals
interval_table = ttk.Treeview(window, columns=("Interval", "Accumulated Time"), show="headings")
interval_table.heading("Interval", text="Interval")
interval_table.heading("Accumulated Time", text="Accumulated Time")
#interval_table.place(x=220, y=260)
interval_table.grid(row=5, column=1, columnspan=2,padx=220, pady=260)  # Adjust row and column values as needed
interval_table.grid_remove()
# Add scrollbar to the table
scrollbar = Scrollbar(window, orient=VERTICAL, command=interval_table.yview)
interval_table.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=5, column=1, sticky=(N, S), padx=400, pady=260)  # Adjust the column value as needed
# Buttons #
Button(text="Calculate", command=calculate, font="arial 15", width=12).place(x=430, y=75)
Button(window, text="Exit", command=lambda:exit(), font="arial 15", width=12).place(x=430, y=140)
Button(window, text="Help", font="arial 15", width=12).place(x=430, y=200)

window.mainloop()