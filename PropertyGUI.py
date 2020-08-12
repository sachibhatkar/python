"""
    * Class: CS 3A
    * Description: This program creates a window with an entry box where the user enters
    * an amount. After clicking the caluclate button, the program displays the property
    * tax and tax value
    * Sachi Bhatkar
    * PropertyGUI.py
    * 20383783
"""

import tkinter

class PropertyGUI():
    def __init__(self):
        # create root window
        # put title,
        self.root_window = tkinter.Tk(className='Property Tax Calculator')
        # add frames, divide into 4 top, 2 middle(upper and lower), and bottom frame
        self.top_frame = tkinter.Frame()
        self.upper_center_frame = tkinter.Frame()
        self.lower_center_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        # prompt for user entering the property value in entry box
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a property value: $')
        # create entry box
        self.actual_user_entered_value = tkinter.Entry(self.top_frame, width=15)

        # asset value labels
        self.assess_title = tkinter.Label(self.upper_center_frame, text='Assessment Value: ')
        self.assess_value = tkinter.StringVar()
        self.assess_value_label = tkinter.Label(self.upper_center_frame, textvariable=self.assess_value)
        # pack side by side
        self.assess_title.pack(side='left')
        self.assess_value_label.pack(side='left')

        # property tax labels

        self.property_tax_title = tkinter.Label(self.lower_center_frame, text='Property Tax: ')
        self.tax_value = tkinter.StringVar()
        self.property_tax_label = tkinter.Label(self.lower_center_frame, textvariable=self.tax_value)

        # packing property labels
        self.property_tax_title.pack(side='left')
        self.property_tax_label.pack(side='left')

        # Create buttons

        self.calculate_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.cal_property_tax)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.root_window.destroy)

        # pack Buttons

        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the label and entry
        self.prompt_label.pack(side='left')
        self.actual_user_entered_value.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.upper_center_frame.pack()
        self.lower_center_frame.pack()
        self.bottom_frame.pack()

        # geometry (width, height of window)
        self.root_window.geometry("500x200")
        # initialize mainloop
        tkinter.mainloop()
    # calculate the property tax and assessment value based on entered value and formula
    def cal_property_tax(self):
        entered_value = float(self.actual_user_entered_value.get())
        assessment_value = 0.6 * entered_value
        assessment_value_str = format(assessment_value, ',.2f')
        # setting assessment_value_str value
        self.assess_value.set('$'+assessment_value_str)
        tax_value = assessment_value * 0.0075
        tax_value_str = format(tax_value, ',.2f')
        # setting property tax value
        self.tax_value.set('$'+tax_value_str)


property_gui = PropertyGUI()