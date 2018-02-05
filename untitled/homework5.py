import tkinter


class TaxConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.middle1_frame = tkinter.Frame()
        self.middle2_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter the actual value of the property :  $')
        self.tax_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.tax_entry.pack(side='left')
        self.mid_label1 = tkinter.Label(self.middle1_frame, text='Assessment value  is :  $')
        self.mid_label2 = tkinter.Label(self.middle2_frame, text='Property tax is :  $')
        self.value1 = tkinter.StringVar()
        self.value2 = tkinter.StringVar()
        self.assessment_label = tkinter.Label(self.middle1_frame, textvariable=self.value1)
        self.tax_label = tkinter.Label(self.middle2_frame, textvariable=self.value2)
        self.mid_label1.pack(side='left')
        self.mid_label2.pack(side='left')
        self.assessment_label.pack(side='left')
        self.tax_label.pack(side='left')
        self.convert_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        property_value = float(self.tax_entry.get())
        property_assessment_value = property_value * 0.60
        property_tax = property_assessment_value * 0.0075
        self.value1.set(property_assessment_value)
        self.value2.set(property_tax)


tax_convert = TaxConverterGUI()
