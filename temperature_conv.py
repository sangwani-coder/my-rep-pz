import tkinter as tk

#main window
root = tk.Tk()
root.title('Temperature Converter')

# Declare global variables
temp_c = None
temp_f = None
temp_f =None

############ Function definitions to be called when buttons are pressed
def convert_c():
    global temp_c
    global temp_f
    global temp_k
    global method

    
    #Convert Celsius to Fahrenheit and update (through textvariable)
    try:
        val = temp_c.get()
        temp_f.set((val*9.0/5) + 32)
        ans = (val*9.0/5) + 32
        ans = round(ans, 4)
                
        method.set('Temp °F =  ' + '(' + str(val)+ '°C ' + '* ' + '9/5 '  ')' + '+ 32 \n' + '= ' + str(ans)+ '°F')
    except:
            pass

def convert_f ():
        try:
            val_1 = temp_f.get()
            temp_c.set((val_1-32) * 5/9)
            ans_1 = (val_1-32) * 5/9
            ans_1 = round(ans_1, 4)
           
            method.set('Temp °C =  ' + '(' + str(val_1)+ '°F ' + '- ' + '32 '  ')' + '* 5/9 \n' + '= ' + str(ans_1) + '°C')
        except:
            pass

def clear ():
    entry_celsius.delete(0, 20)
    entry_fahrenheit.delete(0, 20)     
              

frame = tk.Frame(root)
frame.pack()

#Allow middle cell of grid to grow when window is resized

frame.columnconfigure(1, weight=1)
frame.rowconfigure(1,weight=1)

#variables for holding temperature data

temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()
method =tk.StringVar()

######################################Create widgets for Celsius to Fahrenheit and ViceVersa################

entry_celsius = tk.Entry(frame, width=30, textvariable=temp_c)
label_unitc = tk.Label(frame, text="°C", font=('arial', 12, 'bold'))
label_equal_F =tk.Label(frame, text= "is equal to ==>", font=('arial', 8, 'bold'),)
label_fahrenheit =tk.Label(frame, textvariable=temp_f, relief='raised', bg='white', fg='green', font=('arial', 8, 'bold'))
label_unitf = tk.Label(frame, text="°F" , font=('arial', 12, 'bold'))

entry_fahrenheit = tk.Entry(frame, width=30, textvariable=temp_f)
label_unit_f = tk.Label(frame, text="°F", font=('arial', 12, 'bold'))
label_equal_C =tk.Label(frame, text="is equal to ==>", font=('arial', 8, 'bold'),)
label_celsius=tk.Label(frame, textvariable=temp_c, relief='groove', bg='white', fg='green', font=('arial', 8, 'bold'))
label_unitc= tk.Label(frame, text="°C", font=('arial', 12, 'bold'))


#####################################l Laying out the widgets
entry_celsius.grid(row=1, column=1)
label_unitc.grid(row=1, column=2)
label_equal_F.grid(row=2, column=0)
label_fahrenheit.grid(row=2, column=1)
label_unitf.grid(row=2, column=2)


entry_fahrenheit.grid(row=4, column=1)
label_unit_f.grid(row=4, column=2)
label_equal_C.grid(row=5, column=0)
label_celsius.grid(row=5, column=1)
label_unitc.grid(row=5, column=2)



############################ Buttons ###############

button_convert_C = tk.Button(frame, text="Convert °C to Fahrenheit", font=('arial', 12, 'bold'), relief='raised', command=convert_c)
button_convert_C.grid(row=0, column=1)
button_convert_F = tk.Button(frame, text="Convert °F to Celsius", font=('arial', 12, 'bold'), relief='raised', command=convert_f)
button_convert_F.grid(row=3, column=1)

button_clear = tk.Button(frame, text="Reset", relief='raised', font=('arial', 12, 'bold'), bg='orange', command=clear)
button_clear.grid(row=6, column=1)

#''############### Calculation display widget ############

label_display =tk.Label(frame, width=30, height=4,textvariable=method, fg='blue', bg='white', relief="sunken", font=('arial', 10, 'bold'))
label_calc =tk.Label(frame, text="Calculation", font=('arial', 12, 'bold'))
label_display.grid(row=8, column=1, sticky='S')
label_calc.grid(row=8, column=0)



entry_celsius.focus()
root.mainloop()
