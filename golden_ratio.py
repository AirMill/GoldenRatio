import tkinter as tk
import ttkbootstrap as ttk
from math import sqrt
from decimal import Decimal, getcontext

# Function to convert


def convert():
    # Set the precision to 20 decimal places 3 extra for intermediate calculations
    getcontext().prec = 23
    # add to give an answer correct way!)
    number_input = Decimal(entry_decimal.get())
    phi_value = (1 + Decimal(5).sqrt()) / Decimal(2)
    goldenratio_output = number_input * phi_value
    output_string.set(goldenratio_output) # type: ignore

# Function to handle entry click


def on_entry_click(event):
    if entry_decimal.get() == 0.0:
        entry_decimal.set('') # type: ignore

# Function to exit the application


def exit_application():
    window.destroy()


# window
window = ttk.Window(themename='journal')  # darkly change for stile for ttk
window.title('Golden Ratio Calculator')
# window.iconbitmap(default='C:\Users\user\Desktop\Programs\Python\Course 2 - GUIs in Python\Lesson 1\golden_ratio.py\icon.ico')
window.geometry('300x220')

# title
title_label = ttk.Label(
    master=window, text='Golden Ratio', font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)

# use it to define updated value for the form to acquire
entry_decimal = tk.DoubleVar()
entry = ttk.Entry(master=input_frame, foreground="Green",
                  textvariable=entry_decimal)
button = ttk.Button(master=input_frame, text='Convert', command=convert)

# to delete when click on the populated field
entry.bind("<FocusIn>", on_entry_click)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font='Calibri 24',
    textvariable=output_string  # overwrites text "Output"
)
output_label.pack(pady=5)

# exit button with Calibri font
exit_button = ttk.Button(
    master=window, text='Exit', command=exit_application, style='Primary.TButton'
)

# Set Calibri font directly on the Style object
exit_button_style = ttk.Style()
exit_button_style.configure('Primary.TButton', font=('Calibri', 12, 'bold'))

exit_button.pack(side='top', pady=20, anchor='center', padx=10)

# run
window.mainloop()
