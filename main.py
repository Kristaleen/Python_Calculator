from tkinter import *
from tkinter import messagebox

# creating the login window
window = Tk()
window.title('Login Form')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.config(background='#C7EAFF')

#adding images to the login window

#icon = PhotoImage(file='C:\\Users\\Gulbhar\\Downloads\\icons8-user-80.png')
#img = PhotoImage(file='C:\\Users\\Gulbhar\\Downloads\\Daco_4196836 (1).png')
#Label(window, image=img, bg='#C7EAFF').place(x=50, y=50)


#creating the login function

def login():
    #initializing the username and passwords for four users.

    username1 = "gulbahar"
    password1 = "2327!!"

    username2 = "riya"
    password2 = "2204!!"

    username3 = "kristaleen"
    password3 = "1004!!"

    username4 = "rida"
    password4 = "3101!!"

    #if-condiiton to check if the username and the password matches.

    if username_input.get() == username1 and password_input.get() == password1\
            or username_input.get() == username2 and password_input.get() == password2\
            or username_input.get() == username3 and password_input.get() == password3\
            or username_input.get() == username4 and password_input.get() == password4:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.destroy()
        main_menu()
    else:
        messagebox.showerror(title="Error", message="Invalid login!")
        window.destroy()

def cursor_on_user(e):
    username_input.delete(0, 'end')

def cursor_off_user(e):
    n = username_input.get()
    if n == '':
        username_input.insert(0, 'Username')


def cursor_on_pass(e):
    password_input.delete(0, 'end')


def cursor_off_pass(e):
    n = password_input.get()
    if n == '':
        password_input.insert(0, 'Passwword!')

# creating the login labels and the entry boxes for the login window

login_label = Label(window, text='Welcome Back :)', bg='#C7EAFF', fg="black", font=("Century",27),
                    compound='top')
login_label.place(x=530, y=30)

#Pss = PhotoImage(file='C:\\Users\\Gulbhar\\Downloads\\icons8-password-20.png')
#pss_label = Label(window, image=Pss,bg='#C7EAFF').place(x=500, y=250)

#mail=PhotoImage(file='C:\\Users\\Gulbhar\\Downloads\\icons8-mail-20.png')
#mail_label=Label(window,image=mail,bg='#C7EAFF').place(x=500, y=190)


username_input = Entry(window, width=27, border=0, fg='black', bg='#C7EAFF', font=("FrankRuehl", 13))
username_input.place(x=530, y=195)
username_input.insert(0, 'Username')
username_input.bind('<FocusIn>', cursor_on_user)
username_input.bind('<FocusOut>', cursor_off_user)
Frame(width=322, height=2, bg='black').place(x=504, y=226)

password_input = Entry(window, width=25, fg='black', bg='#C7EAFF', border=0, show="*", font=("FrankRuehl", 12))
password_input.place(x=530, y=256)
password_input.insert(0, 'Password!')
password_input.bind('<FocusIn>', cursor_on_pass)
password_input.bind('<FocusOut>', cursor_off_pass)
Frame(width=322, height=2, bg='black').place(x=504, y=286)

login_button = Button(window, width=34, pady=7, border=0, text="Login", bg='#41A9E6', fg="white", font=("Arial", 16),
                      command=login).place(x=460, y=320)



# Defining function to perform basic  calculation.

output = ''

def Standard_Calculator():

    # Creating calculator window.

    ws = Tk()
    ws.title('Standard Calculator')
    ws.geometry('350x420+570+200')
    ws.resizable(0, 0)

    # Setting output as a global variable.

    output = ''

    # Defining functions.

    def display(number):  # Function to display the output on the screen.
        global output
        output = output + str(number)
        scr_lbl['text'] = output

    def clear_scr():  # Function to clear the output screen.
        global output
        output = ''
        scr_lbl['text'] = output

    def equal_btn():  # Function to display the calculated result.
        global output
        result = str(eval(output))
        scr_lbl['text'] = result
        output = result

    def backspace():   # Function to back space the last number
        global output
        output=output[:-1]
        scr_lbl['text']=output


    # Creating frames to create buttons in.

    Frame1 = Frame(ws)
    Frame1.pack(expand=True, fill=BOTH)

    Frame2 = Frame(ws)
    Frame2.pack(expand=True, fill=BOTH)

    Frame3 = Frame(ws)
    Frame3.pack(expand=True, fill=BOTH)

    Frame4 = Frame(ws)
    Frame4.pack(expand=True, fill=BOTH)

    # Creating the label where the result will be displayed.

    scr_lbl = Label(Frame1, textvariable='', font=('Sitka Banner', 25, 'bold'), anchor=SE, bg='#595954', fg='white')
    scr_lbl.pack(expand=True, fill=BOTH)

    #################################################################################################################################

    # Creating the buttons in Frame 1
    Button_1 = Button(Frame1, text='1', font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(1)).pack(expand=True, fill=BOTH, side=LEFT)

    Button_2 = Button(Frame1, text='2', font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(2)).pack(expand=True, fill=BOTH, side=LEFT)

    Button_3 = Button(Frame1, text='3', font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(3)).pack(expand=True, fill=BOTH, side=LEFT)

    Addition_Button = Button(Frame1, text='+', font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display('+')).pack(expand=True, fill=BOTH, side=LEFT)

    Backspace_Button=Button(Frame1, text='\u232B', font=('Sitka Banner', 13, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=backspace).pack(expand=True, fill=BOTH, side=LEFT)

    ##########################################################################################################################

    # Creating the buttons in Frame 2

    Button_4 = Button(Frame2, text='4', font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(4)).pack(expand=True, fill=BOTH, side=LEFT)

    Button_5 = Button(Frame2, text=5, font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(5)).pack(expand=True, fill=BOTH, side=LEFT)

    Button_6 = Button(Frame2, text=6, font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(6)).pack(expand=True, fill=BOTH, side=LEFT)

    Subtraction_Button = Button(Frame2, text='-', font=('Sitka Banner', 25, 'bold'),
                                border=0, relief=GROOVE, bg='#2E2E2B',
                                fg='white', command=lambda: display('-')).pack(expand=True, fill=BOTH, side=LEFT)

    #######################################################################################################################

    # Creating the buttons in Frame 3

    Button_7 = Button(Frame3, text=7, font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(7)).pack(expand=True, fill=BOTH, side=LEFT)

    Button_8 = Button(Frame3, text=8, font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(8)).pack(expand=True, fill=BOTH, side=LEFT)

    Button_9 = Button(Frame3, text=9, font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(9)).pack(expand=True, fill=BOTH, side=LEFT)

    Multiplication_Button = Button(Frame3, text='*', font=('Sitka Banner', 25, 'bold'),
                                   border=0, relief=GROOVE, bg='#2E2E2B',
                                   fg='white', command=lambda: display('*')).pack(expand=True, fill=BOTH, side=LEFT)

    #####################################################################################################################

    # Creating the buttons in Frame 4

    Button_clr = Button(Frame4, text='C', font=('Sitka Banner', 25, 'bold'),
                        border=0, relief=GROOVE, bg='#2E2E2B',
                        fg='white', command=clear_scr).pack(expand=True, fill=BOTH, side=LEFT)

    Button_0 = Button(Frame4, text=0, font=('Sitka Banner', 25, 'bold'),
                      border=0, relief=GROOVE, bg='#2E2E2B',
                      fg='white', command=lambda: display(0)).pack(expand=True, fill=BOTH, side=LEFT)

    Equal_Button = Button(Frame4, text='=', font=('Sitka Banner', 25, 'bold'),
                          border=0, relief=GROOVE, bg='#2E2E2B',
                          fg='white', command=equal_btn).pack(expand=True, fill=BOTH, side=LEFT)

    Divistion_Button = Button(Frame4, text='/', font=('Sitka Banner', 25, 'bold'),
                              border=0, relief=GROOVE, bg='#2E2E2B',
                              fg='white', command=lambda: display('/')).pack(expand=True, fill=BOTH, side=LEFT)

    #creating back button that takes the user back to the main menu
    def back():
        ws.destroy()
        main_menu()

    button_back = Button(Frame4, text='BACK', font=('Sitka Banner', 15, 'bold'), command=back,
                         border=0, relief=GROOVE,bg='#2E2E2B',fg='white')
    button_back.pack(expand=True, fill=BOTH, side=BOTTOM)

    ###################################################################################################################

    ws.mainloop()
#creating the function to display the main menu of the application

def main_menu():

    #creating the main menu window

    mainmenu = Tk()
    mainmenu.title("Brilliant Education")
    mainmenu.geometry('800x690+360+60')
    mainmenu.config(bg='#C7EAFF')
    frame = Frame(mainmenu, bg="#C7EAFF")
    frame.place(x=225, y=80)

    main_label = Label(mainmenu, text='***MAIN MENU***', bg='#C7EAFF', fg="black", font=("Century", 25, 'bold'),
                       compound='top').place(x=225, y=20)

    #creating buttons to display and access the various functions of the application

    b1 = Button(frame, text="Calculator",
                fg="black", padx=85, pady=18,command=lambda :[mainmenu.destroy(),Standard_Calculator()]
            ,highlightbackground="#0F2345", bg='pink', font=("Courier 12 bold"))
    b1.pack(expand=True, fill=BOTH, pady=4)

    b2 = Button(frame, text="Odd Even",
                fg="black", padx=85, pady=18,command=lambda :[mainmenu.destroy(),oddevencheck()],
    highlightbackground="#0F2345", bg='pink', font=("Courier 12 bold"))
    b2.pack(expand=True, fill=BOTH, pady=4)

    b3 = Button(frame, text="Average",
                fg="black", padx=85, pady=18,command=lambda:[mainmenu.destroy(),average()],
                highlightbackground="#0F2345", bg='pink', font=("Courier 12 bold"))
    b3.pack(expand=True, fill=BOTH, pady=4)

    b4 = Button(frame, text="Factorial",
                fg="black", padx=85, pady=18,command=lambda:[mainmenu.destroy(),fact()],
                highlightbackground="#0F2345", bg='pink', font=("Courier 12 bold"))
    b4.pack(expand=True, fill=BOTH, pady=4)

    b5 = Button(frame, text="Fibonacci",
                fg="black", padx=85, pady=18,command=lambda:[mainmenu.destroy(),fibonacci()],
                highlightbackground="#0F2345", bg='pink', font=("Courier 12 bold"))
    b5.pack(expand=True, fill=BOTH, pady=4)

    b6 = Button(frame, text="Base Conversion",
                fg="black",command=lambda :[mainmenu.destroy(),numeric_base()], padx=85, pady=18,
                highlightbackground="#0F2345", bg='pink', font=("Courier 12 bold"))
    b6.pack(expand=True, fill=BOTH, pady=4)

    b7 = Button(frame, text="Mensuration",
                fg="black", padx=85, pady=18, command=lambda :[mainmenu.destroy(),mensuration()],
                highlightbackground="#0F2345", bg='pink', font=("Courier 12 bold"))
    b7.pack(expand=True, fill=BOTH, pady=4)

    b8 = Button(frame, text="Log out",
                fg="black", padx=85, pady=18, command=lambda:[mainmenu.destroy(),logout()],
                highlightbackground="#0F2345", bg='pink', font=("Courier 12 bold"))
    b8.pack(expand=True, fill=BOTH, pady=4)

    mainmenu.mainloop()

def numeric_base():
    from tkinter import ttk

    # Colors
    co0 = "#FFFFFF"  # white
    co1 = "#000000"  # black
    co2 = "#CCCCFB"  # blue
    co3 = "#E67D38"  # orange
    co4 = "#9BCCDF"  # light blue
    co5 = "#4080E4"  # Safari blue
    co6 = "#99999B"  # Grey

    #creating the window for the numeric base converter

    window = Tk()
    window.title('Number System Conversion')

    window.geometry('450x400+500+200')
    window.resizable(0, 0)
    window.configure(bg='#C7EAFF')

    #creating the function to convert and display from one number system to another

    def convert():
        def number_to_decimal(number, bases):

            '''adding try-except to make sure only valid input is accepted and errors message in case the
            input happens to be invalid'''
            try:
                decimal = int(number,bases)

                binary = bin(decimal)
                octal = oct(decimal)
                hexadecimal = hex(decimal)
                l_binary['text'] = str(binary[2:])
                l_octal['text'] = str(octal[2:])
                l_decimal['text'] = str(decimal)
                l_hexadecimal['text'] = str(hexadecimal[2:]).upper()
                # print("Decimal: ", str(decimal))
                # print("Octal: ", str(octal[2:]))
                # print("Binary: ", str(binary[2:]))
                # print("Hexadecimal: ", str(hexadecimal[2:]))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")


        base = combo.get()
        number = e_value.get()
        if base == 'BINARY':
            base = 2
        elif base == 'OCTAL':
            base = 8
        elif base == 'DECIMAL':
            base = 10
        elif base == 'HEXADECIMAL':
            base = 16
        else:
            print("Error")
        number_to_decimal(number, base)

    # frames
    frame_up = Frame(window, bg='#C7EAFF', pady=0, padx=10)
    frame_up.place(x=10, y=20)

    frame_down = Frame(window, width=400, height=300, bg='#C7EAFF', pady=12, padx=0)
    frame_down.place(x=30, y=90)

    app_name = Label(frame_up, text="NUMERIC BASE CONVERTER", font=('Sitka Banner', 25, 'bold'), bg='#C7EAFF', fg=co1)
    app_name.pack()

    bases = ['BINARY', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
    combo = ttk.Combobox(frame_down, width=13, justify="center", font=('Sitka Banner', 11, 'bold'))
    combo['values'] = (bases)
    combo.place(x=50, y=10)

    e_value = Entry(frame_down, width=10, justify="center", font=("Sitka Banner", 13, 'bold'), highlightthickness=1,
                    relief=SOLID)
    e_value.place(x=184, y=10)

    b_converter = Button(frame_down, text="CONVERT", command=convert, height=1, highlightbackground=co3, fg='black',
                         bg='pink', font=('Sitka Banner', 11, 'bold'), relief=RAISED, overrelief=RIDGE)
    b_converter.place(x=285, y=8)

    l_binary = Label(frame_down, text="BINARY", width=14, height=1, anchor='center', font=('Sitka Banner', 11, 'bold'),
                     bg='pink', fg='black')
    l_binary.place(x=50, y=52)
    l_binary = Label(frame_down, text="", width=13, height=1, anchor='nw', font=('Sitka Banner', 11, 'bold'), bg=co6,
                     fg='black',
                     relief=SOLID)
    l_binary.place(x=175, y=50)

    l_octal = Label(frame_down, text="OCTAL", width=14, height=1, anchor='center', font=('Sitka Banner', 11, 'bold'),
                    bg='pink', fg='black')
    l_octal.place(x=50, y=100)
    l_octal = Label(frame_down, text="", width=13, height=1, anchor='nw', font=('Sitka Banner', 11, 'bold'), bg=co6,
                    fg=co1,
                    relief=SOLID)
    l_octal.place(x=175, y=100)

    l_decimal = Label(frame_down, text="DECIMAL", width=14, height=1, anchor='center',
                      font=('Sitka Banner', 11, 'bold'), bg='pink', fg='black')
    l_decimal.place(x=50, y=150)
    l_decimal = Label(frame_down, text="", width=13, height=1, anchor='nw', font=('Sitka Banner', 11, 'bold'), bg=co6,
                      fg=co1,
                      relief=SOLID)
    l_decimal.place(x=175, y=150)

    l_hexadecimal = Label(frame_down, text="HEXADECIMAL", width=14, height=1, anchor='center',
                          font=('Sitka Banner', 11, 'bold'),
                          bg='pink', fg='black')
    l_hexadecimal.place(x=50, y=200)
    l_hexadecimal = Label(frame_down, text="", width=13, height=1, anchor='nw', font=('Sitka Banner', 11, 'bold'),
                          bg=co6, fg=co1,
                          relief=SOLID)
    l_hexadecimal.place(x=175, y=200)

    #creating back button that lets user go back to the main menu

    def back():
        window.destroy()
        main_menu()

    button_back = Button(frame_down, text='BACK', font=('Sitka Banner', 13, 'bold'), command=back, bg='pink')
    button_back.place(x=160, y=250)

    window.mainloop()

def mensuration():
    from tkinter import ttk

    # Colors
    co0 = "#9E9EA4"  # grey
    co1 = "#000000"  # black
    co2 = "#CCCCFB"  # blue
    co3 = "#E67D38"  # orange
    co4 = "#9BCCDF"  # light blue
    co5 = "#4080E4"  # Safari blue
    co6 = "#FDFDFD"  # white
    co7 = "#474948"  # dark grey

    def openwindow():
        # Calculation of area and perimeter of a circle.
        # Calculation of volume of a sphere
        root1 = Tk()
        root1.title("Circle")
        root1.geometry('450x450+540+190')
        root1.resizable(0, 0)
        root1.config(bg='#C7EAFF')

        def calcVolume(radius):
            # Volume of the sphere
            return round((4 / 3 * 3.14 * radius * radius * radius), 2)

        def clickVolume():
            # function to click volume
            try:
                volume.set(calcVolume(float(radius.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        def calcPerimeter(radius):
            # Perimeter of the circle
            return round((2 * 3.14 * radius), 2)

        def clickPerimeter():
            # function to click perimeter
            try:
                perimeter.set(calcPerimeter(float(radius.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be an intger.")

        def calcArea(radius):
            # Area of the Circle
            return round((radius * radius * 3.14), 2)

        def clickArea():
            # function to click area
            try:
                area.set(calcArea(float(radius.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        Label(root1, text="Radius", font=('Sitka Banner', 18, 'bold'), bg='#C7EAFF').place(x=195, y=50)
        radius = StringVar()
        Entry(root1, textvariable=radius, font=('Sitka Banner', 14, 'bold')).place(x=130, y=100)

        # AREA OF THE CIRCLE
        area = IntVar()
        Label(root1, textvariable=area, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=115, y=140)
        button = Button(root1, text="Area", command=clickArea, width=5, bg='pink',
                        fg="black", bd=8, padx=16, pady=16, highlightbackground="#0F2345")
        button.place(x=75, y=175)

        # PERIMETER OF THE CIRCLE
        perimeter = IntVar()
        Label(root1, textvariable=perimeter, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=210, y=140)
        button = Button(root1, text="Perimeter ", command=clickPerimeter, bg='pink',
                        fg="black", bd=8, padx=16, pady=16, highlightbackground="#78CFD1")
        button.place(x=165, y=175)

        # VOLUME OF THE SPHERE
        volume = IntVar()
        Label(root1, textvariable=volume, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=320, y=140)
        button = Button(root1, text="Volume ", command=clickVolume, bg='pink',
                        fg="black", bd=8, padx=16, pady=16, highlightbackground="#F7CD45")
        button.place(x=275, y=175)

        button1 = Button(root1, text="Close", bd=8, padx=6, pady=6, width=10, height=2, bg='pink',
                         highlightbackground="#ED6C59",
                         command=lambda: [root1.destroy(), menu()])
        button1.place(x=175, y=300)

    def openwindow1():
        # Calculation of area and perimeter of a rectangle.
        # Calculation of volume of a rectangular prism
        root2 = Tk()
        root2.title("Rectangle")
        root2.geometry('450x450+540+190')
        root2.resizable(0, 0)
        root2.config(bg='#C7EAFF')

        def calcVolume1(l, b, h):
            # Volume of the Rectangular prism
            return round((l * b * h), 2)

        def clickVolume1():
            # function to click volume
            try:
                volume1.set(calcVolume1(float(length.get()), float(breadth.get()), float(height.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        def calcPerimeter1(l, b):
            # Perimeter of the rectangle
            return round((2 * (l * b)), 2)

        def clickPerimeter1():
            # function to click perimeter
            try:
                perimeter1.set(calcPerimeter1(float(length.get()), float(breadth.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        def calcArea1(l, b):
            # Area of the rectangle
            return round((l * b), 2)

        def clickArea1():
            # function to click area
            try:
                area1.set(calcArea1(float(length.get()), float(breadth.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        Label(root2, text="Breadth :", font=('Sitka Banner', 13, 'bold'), bg='#C7EAFF').place(x=100, y=40)
        breadth = StringVar()
        Entry(root2, textvariable=breadth, width=15, font=('Sitka Banner', 13, 'bold')).place(x=180, y=45)

        Label(root2, text="Length   : ", font=('Sitka Banner', 13, 'bold'), bg='#C7EAFF').place(x=100, y=75)
        length = StringVar()
        Entry(root2, textvariable=length, width=15, font=('Sitka Banner', 13, 'bold')).place(x=180, y=80)

        Label(root2, text="Height   :", font=('Sitka Banner', 13, 'bold'), bg='#C7EAFF').place(x=100, y=112)
        height = StringVar()
        Entry(root2, textvariable=height, width=15, font=('Sitka Banner', 13, 'bold')).place(x=180, y=115)

        # AREA OF THE RECTANGLE

        area1 = IntVar()
        Label(root2, textvariable=area1, bg='#C7EAFF', font=('Sitka Banner', 13, 'bold')).place(x=115, y=145)
        button1 = Button(root2, text="Area", command=clickArea1,
                         fg="black", bd=8, width=5, bg='pink', padx=16, pady=16, highlightbackground="#0F2345")
        button1.place(x=75, y=180)

        # PERIMETER OF THE RECTANGLE

        perimeter1 = IntVar()
        Label(root2, textvariable=perimeter1, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=210, y=145)
        button = Button(root2, text=" Perimeter ", command=clickPerimeter1,
                        fg="black", bd=8, padx=16, pady=16, bg='pink', highlightbackground="#78CFD1")
        button.place(x=165, y=180)

        # VOLUME OF THE RECTANGULAR PRISM

        volume1 = IntVar()
        Label(root2, textvariable=volume1, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=320, y=145)
        button = Button(root2, text=" Volume ", command=clickVolume1,
                        fg="black", bd=8, padx=16, pady=16, bg='pink', highlightbackground="#F7CD45")
        button.place(x=275, y=180)

        button2 = Button(root2, text="Close", bd=8, padx=6, pady=6, width=10, height=2, bg='pink',
                         highlightbackground="#ED6C59", command=lambda: [root2.destroy(), menu()])
        button2.place(x=175, y=300)

    def openwindow2():
        # Calculation of area and perimeter of the square
        # Calculation of volume of the cube
        root3 = Tk()
        root3.title("SQUARE")
        root3.geometry('450x450+540+190')
        root3.resizable(0, 0)
        root3.config(bg='#C7EAFF')

        def calcPerimeter2(side):
            # Perimeter of the square
            return round((4 * side), 2)

        def clickPerimeter2():
            # Function to click the perimeter
            try:
                perimeter2.set(calcPerimeter2(float(side.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        def calcArea2(side):
            # Area of the square
            return round((side * side), 2)

        def clickArea2():
            # function to click area
            try:
                area2.set(calcArea2(float(side.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        def calcVolume2(side):
            # Volume of the cube
            return round((side * side * side), 2)

        def clickVolume2():
            # fucntion to click volume
            try:
                volume2.set(calcVolume2(float(side.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        Label(root3, text="Side: ", font=('Sitka Banner', 15, 'bold'), bg='#C7EAFF').place(x=100, y=85)
        side = StringVar()
        Entry(root3, textvariable=side, width=15, font=('Sitka Banner', 13, 'bold')).place(x=190, y=90)

        # AREA OF THE SQUARE
        area2 = IntVar()
        Label(root3, textvariable=area2, bg='#C7EAFF', font=('Sitka Banner', 13, 'bold')).place(x=115, y=140)
        button = Button(root3, text="Area", command=clickArea2,
                        fg="black", bd=8, padx=16, pady=16, width=5, bg='pink', highlightbackground="#0F2345")
        button.place(x=75, y=175)

        # PERIMETER OF THE SQUARE
        perimeter2 = IntVar()
        Label(root3, textvariable=perimeter2, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=210, y=140)
        button = Button(root3, text="Perimeter ", command=clickPerimeter2,
                        fg="black", bd=8, padx=16, pady=16, bg='pink', highlightbackground="#78CFD1")
        button.place(x=165, y=175)

        # VOLUME OF THE CUBE
        volume2 = IntVar()
        Label(root3, textvariable=volume2, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=320, y=140)
        button = Button(root3, text="Volume ", command=clickVolume2,
                        fg="black", bd=8, padx=16, pady=16, bg='pink', highlightbackground="#F7CD45")
        button.place(x=275, y=175)

        button2 = Button(root3, text="Close", bd=8, padx=6, pady=6, width=10, height=2, bg='pink',
                         highlightbackground="#ED6C59", command=lambda: [root3.destroy(), menu()])
        button2.place(x=175, y=300)

    def openwindow3():
        # calculation of area and perimeter of a triangle
        # calculation of volume of a triangular prism
        root4 = Tk()
        root4.title("TRIANGLE")
        root4.geometry('450x450+540+190')
        root4.resizable(0, 0)
        root4.config(bg='#C7EAFF')

        def calcPerimeter3(side1, side2, side3):
            # Perimeter of the triangle
            return round((side1 + side2 + side3), 2)

        def clickPerimeter3():
            # function to click perimeter
            try:
                perimeter3.set(calcPerimeter3(float(side1.get()), float(side2.get()), float(side3.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        def calcVolume3(base, height, length):
            return 0.5 * base * height * length

        def clickVolume3():
            try:
                volume3.set(calcVolume3(float(base.get()), float(height.get()), float(length.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        def calcArea3(b, h):
            # Area of the triangle
            return round((b * h / 2), 2)

        def clickArea3():
            # Function to click area
            try:
                area3.set(calcArea3(float(base.get()), float(height.get())))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be a number.")

        Label(root4, text="Base     :", font=('Sitka Banner', 15, 'bold'), bg='#C7EAFF').place(x=100, y=25)
        base = StringVar()
        Entry(root4, textvariable=base, width=15, font=('Sitka Banner', 13, 'bold')).place(x=190, y=30)

        Label(root4, text="Height :", font=('Sitka Banner', 15, 'bold'), bg='#C7EAFF').place(x=100, y=55)
        height = StringVar()
        Entry(root4, textvariable=height, width=15, font=('Sitka Banner', 13, 'bold')).place(x=190, y=60)

        Label(root4, text="Side 1", font=('Sitka Banner', 15, 'bold'), bg='#C7EAFF').place(x=100, y=115)
        side1 = StringVar()
        Entry(root4, textvariable=side1, width=15, font=('Sitka Banner', 13, 'bold')).place(x=190, y=120)

        Label(root4, text="Side 2   :", font=('Sitka Banner', 15, 'bold'), bg='#C7EAFF').place(x=100, y=145)
        side2 = StringVar()
        Entry(root4, textvariable=side2, width=15, font=('Sitka Banner', 13, 'bold')).place(x=190, y=150)

        Label(root4, text="Side 3", font=('Sitka Banner', 15, 'bold'), bg='#C7EAFF').place(x=100, y=175)
        side3 = StringVar()
        Entry(root4, textvariable=side3, width=15, font=('Sitka Banner', 13, 'bold')).place(x=190, y=180)

        Label(root4, text="Length :", font=('Sitka Banner', 15, 'bold'), bg='#C7EAFF').place(x=100, y=85)
        length = StringVar()
        Entry(root4, textvariable=length, width=15, font=('Sitka Banner', 13, 'bold')).place(x=190, y=90)

        # PERIMETER OF THE TRIANGLE
        perimeter3 = IntVar()
        Label(root4, textvariable=perimeter3, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=210, y=210)
        button = Button(root4, text="Perimeter ", command=clickPerimeter3,
                        fg="black", bd=8, padx=16, pady=16, bg='pink', highlightbackground="#78CFD1")
        button.place(x=165, y=245)

        # AREA OF THE TRIANGLE
        area3 = IntVar()
        Label(root4, textvariable=area3, bg='#C7EAFF', font=('Sitka Banner', 13, 'bold')).place(x=115, y=210)
        button = Button(root4, text="Area", command=clickArea3,
                        fg="black", bd=8, padx=16, pady=16, width=5, bg='pink', highlightbackground="#0F2345")
        button.place(x=75, y=245)

        # VOLUME OF THE TRIANGULAR PRISM
        volume3 = IntVar()
        Label(root4, textvariable=volume3, bg='#C7EAFF', font=('Sitka banner', 13, 'bold')).place(x=320, y=210)
        button = Button(root4, text="Volume ", command=clickVolume3,
                        fg="black", bd=8, padx=16, pady=16, bg='pink', highlightbackground="#F7CD45")
        button.place(x=275, y=245)

        button3 = Button(root4, text="Close", highlightbackground="#ED6C59"
                         , bd=8, padx=6, pady=6, width=10, height=2, bg='pink',
                         command=lambda: [root4.destroy(), menu()])
        button3.place(x=175, y=355)

    #creating the function to display the menu for the shapes to be chosen to perform the operations on

    def menu():
        root = Tk()
        root.title("Brilliant Education")
        root.geometry("600x630+450+90")
        wt = 350
        ht = 150
        root.minsize(ht, wt)
        root.resizable(width=False, height=False)
        root.configure(bg="#F6E2E1")
        style = ttk.Style()
        style.theme_use('clam')

        ttk.Separator(root, orient="horizontal").grid(row=0, columnspan=3)
        # frames
        frame_up = Frame(root, width=600, height=60, bg="#F6E2E1", pady=0, padx=10)
        frame_up.grid(row=1, column=0)

        frame_down = Frame(root, width=300, height=300, bg="#F6E2E1", pady=0, padx=0)
        frame_down.grid(row=2, column=0)

        app_name = Label(frame_up, text="MENSURATION CALCULATOR", anchor="center", font=("Courier 25 bold"),
                         bg="#F6E2E1",
                         fg=co1)
        app_name.place(x=70, y=15)

        btn = Button(frame_down, text="CIRCLE", command=lambda: [root.destroy(), openwindow()],
                     fg="black", bd=8, width=8, padx=85, pady=18, highlightbackground="#0F2345",
                     font=("Courier 13 bold"))
        btn.grid(row=6, column=0, padx=50, pady=15, columnspan=3, rowspan=1)

        btn = Button(frame_down, text="RECTANGLE", command=lambda: [root.destroy(), openwindow1()],
                     fg="black", bd=8, width=12, padx=65, pady=18, highlightbackground="#78CFD1",
                     font=("Courier 13 bold"))
        btn.grid(row=7, column=0, padx=50, pady=15, columnspan=3, rowspan=1)

        btn = Button(frame_down, text="SQUARE", command=lambda: [root.destroy(), openwindow2()],
                     fg="black", bd=8, width=9, padx=80, pady=18, highlightbackground="#F7CD45",
                     font=("Courier 13 bold"))
        btn.grid(row=8, column=0, padx=50, pady=15, columnspan=6, rowspan=1)

        btn = Button(frame_down, text="TRIANGLE", command=lambda: [root.destroy(), openwindow3()],
                     fg="black", bd=8, width=10, padx=75, pady=18, highlightbackground="#EDAD5D",
                     font=("Courier 13 bold"))
        btn.grid(row=9, column=0, padx=50, pady=15, columnspan=6, rowspan=1)

        btn = Button(frame_down, text="MAIN MENU", command=lambda: [root.destroy(), main_menu()], fg='black', bd=8,
                     padx=75, pady=18, width=10, highlightbackground='#EDAD5D', font=("Courier 13 bold"))
        btn.grid(row=10, column=0, padx=50, pady=15, columnspan=6, rowspan=1)
        root.mainloop()

    menu()

#function to calculate and display the factorial of the given number.

def fact():

    #creating the window

    import math
    root = Tk()
    root.geometry("450x400+500+170")
    root.title("Factorial calculator")
    root.config(bg="#C7EAFF")
    root.resizable(0, 0)

    #creating the labels and the entry box to enter the values and display the output.
    def tab2():
        label2 = Label(root, text='Factorial', font=('Sitka Banner', 25, 'bold'), bg="#C7EAFF")
        label2.pack()
        enter_value = Label(root, text="Enter Value:", font=('Sitka Banner', 15, 'bold'), bg="#C7EAFF")
        enter_value.place(x=30, y=70)
        result = Label(root, text="Result:", font=('Sitka Banner', 18, 'bold'), bg="#C7EAFF")
        result.place(x=70, y=195)
        answer = Label(root, text="", font=('Sitka Banner', 18, 'bold'), bg="#C7EAFF")
        answer.place(x=180, y=195)

        value = StringVar()
        e = Entry(root, textvariable=value, font=('Sitka Banner', 20, 'bold'), width=9)
        e.place(x=160, y=70)

        #function to calculate the factorial

        def calculation():

            '''adding try-except to make sure only valid input is accepted and errors message in case the
                        input happens to be invalid'''

            try:
                n = int(e.get())
                answer.config(text=math.factorial(n))
            except ValueError:
                messagebox.showerror(title="Wrong Input", message="The input must be an integer.")

        cal_button = Button(root, text="Calculate", font=('Sitka Banner', 16, 'bold'), command=calculation, bg="pink",
                            width=9)
        cal_button.place(x=175, y=125)

        #back button that displays the main menu again

        def back():
            root.destroy()
            main_menu()

        button_back = Button(root, text='BACK', font=('Sitka Banner', 15, 'bold'), command=back,bg='pink')
        button_back.pack(side=BOTTOM)

    tab2()
    root.mainloop()

#function to calcuate and display the min,max and average for the given list of numbers.

def average():

    #creating the window

    root = Tk()
    root.geometry("450x450+500+170")
    root.title("Average calculator")
    root.config(bg="#C7EAFF")
    root.resizable(0, 0)

    def tab3():
        label3 = Label(root, text='Minimum, Maximum, Average', font=('Sitka Banner', 18, 'bold'), bg='#C7EAFF')
        label3.place(x=70, y=10)

        #creating the function to perform the required calculation.
        def calculation():

            a = my_entry.get()
            import re
            b = a.split(',')
            for i in b:

                #adding try-except to make sure only valid input is accepted and display appropriate errors message

                try:
                    data = int(i)
                except ValueError:
                    messagebox.showerror(title="Wrong Input", message="The input must be an integer.")
                else:
                    data = my_entry.get()

                    def minimum(data):
                        return min(map(int, re.findall('\d+', str(data))))

                    def maximum(data):
                        return max(map(int, re.findall('\d+', str(data))))

                    def add(data):
                        return sum(map(int, re.findall('\d+', str(data))))

                    my_sum = add(str(data))
                    my_min = minimum(str(data))
                    my_max = maximum(str(data))

                    def avg(data):
                        return map(int, re.findall('\d+', str(data)))

                    my_total = len(list(i for i in avg(data) if isinstance(i, int)))
                    my_avg = my_sum / my_total
                    a_min.config(text=my_min)
                    b_max.config(text=my_max)
                    c_avg.config(text=my_avg)

        #creating label,entry boxes and display boxes.

        guide = Label(root, text="ex. 1, 2, 3, 4", font=('Sitka Banner', 13, 'italic'), bg='#C7EAFF')
        guide.place(x=140, y=102)
        enter_value = Label(root, text="Enter Value:", font=('Sitka Banner', 15), bg='#C7EAFF')
        enter_value.place(x=30, y=60)
        my_entry = Entry(root, font=('Sitka Banner', 18), width=15)
        my_entry.place(x=140, y=60)

        min_label = Label(root, text="Minimum:", font=('Sitka Banner', 15), bg='#C7EAFF')
        min_label.place(x=30, y=200)
        a_min = Label(root, text="", font=('Sitka Banner', 18), bg='#C7EAFF')
        a_min.place(x=130, y=195)

        max_label = Label(root, text="Maximum:", font=('Sitka Banner', 15), bg='#C7EAFF')
        max_label.place(x=30, y=240)
        b_max = Label(root, text="", font=('Sitka Banner', 18), bg='#C7EAFF')
        b_max.place(x=130, y=235)

        avg_label = Label(root, text="Average:", font=('Sitka Banner', 15), bg='#C7EAFF')
        avg_label.place(x=30, y=280)
        c_avg = Label(root, text="", font=('Sitka Banner', 18), bg='#C7EAFF')
        c_avg.place(x=130, y=275)

        #creating the calculate button

        my_button = Button(root, text="Calculate", font=('Sitka Banner', 15, 'bold'), command=calculation, bg='pink')
        my_button.place(x=180, y=145)

        #back button that exits and displays the main menu again.
        def back():
            root.destroy()
            main_menu()

        button_back = Button(root, text='BACK', font=('Sitka Banner', 15, 'bold'), command=back, bg='pink')
        button_back.pack(side=BOTTOM)

    tab3()
    root.mainloop()

#function to check and display whether the given integer is odd or even

def oddevencheck():

    #function to check if the given integer is odd or even

    def odd_even():

        # adding try-except to make sure only valid input is accepted and display appropriate errors message

        try:
            num=int(entry1.get())
            if num%2==0:
                display=num,"Is Even"
                label2=Label(root,font="Century 18 bold",bg='#C7EAFF',anchor='center')
                label2["text"]=display
                label2.place(x=160,y=300)


            else:
                display=num," Is Odd "
                label3=Label(root,font="Century 18 bold",bg='#C7EAFF',anchor='center')
                label3["text"]=display
                label3.place(x=160,y=300)
        except ValueError:
            messagebox.showerror(title="Wrong Input", message="The input must be an integer.")

    #Creating the window

    root=Tk()
    root.geometry("500x500+490+170")
    root.title("Odd or Even calculator")
    root.config(bg="#C7EAFF")
    root.resizable(0,0)

    #creating the labels, entry boxes and buttons.

    label1=Label(root,text="Odd Even Program",font="Times 24 bold",bg='#C7EAFF')

    entry1=Entry(root,bd="10",width=13,font=("Century", 22, 'bold'))
    button1=Button(root,text="Check",bg="pink",fg="black",bd="5",font=("Century", 20, 'bold'),command=odd_even,
                   height=1,width=10)

    label1.place(x=110,y=95)
    entry1.place(x=125,y=148)
    button1.place(x=145,y=215)

    #back button a=that exits and returns to the main menu.
    def back():
        root.destroy()
        main_menu()

    button_back = Button(root, text='BACK', font=('Sitka Banner', 15, 'bold'), command=back, bg='pink')
    button_back.pack(side=BOTTOM)

    root.mainloop()

#function to calculate and display the fibonacci series up to n number.

def fibonacci():

    #creating the window

    fb = Tk()
    fb.geometry("600x650+430+90")
    fb.title("Fibonacci Series")
    fb.resizable(0, 0)
    fb.config(bg='#C7EAFF')

    global number

    #function that calcultes the series and displays into the display box using a for loop.

    def fibo():
        a = 1
        b = 0
        c = 0
        l = [0]
        global number

        # adding try-except to make sure only valid input is accepted and display appropriate errors message

        try:
            n = int(number.get())
            for i in range(1, n):
                c = a + b
                l.append(c)
                a = b
                b = c

            for i in range(0, len(l)):
                txtDisplay.insert(END, l[i])
                txtDisplay.insert(END, ' ')
        except ValueError:
            messagebox.showerror(title="Wrong Input", message="The input must be an integer.")

    #adding labels,entry boxes,buttons and display boxes in the window.

    IblInfo = Label(fb, font=('Sitka Banner', 30, 'bold'), text="Fibonacci Sequence", bg='#C7EAFF', fg="Black"
                    , bd=10)
    IblInfo.place(x=130, y=20)

    Label(fb, text="Number :", font=('Sitka Banner', 15, 'bold'), bg='#C7EAFF').place(x=165, y=112)
    number = StringVar()
    Entry(fb, textvariable=number, width=15, font=('Sitka Banner', 13, 'bold')).place(x=265, y=120)
    txtDisplay = Text(fb, width=32, height="13", bg='white', bd="16", font=('arial', 12, 'bold'))
    txtDisplay.place(x=140, y=180)

    button = Button(fb, text="Calculate ", command=fibo, font=('Sitka Banner', 12, 'bold'),
                    fg="black", bd=8, padx=16, pady=16, bg='pink', highlightbackground="#78CFD1")
    button.place(x=250, y=475)

    #back button that exits and returns to the main menu.
    def back():
        fb.destroy()
        main_menu()

    button_back = Button(fb, text='BACK', font=('Sitka Banner', 15, 'bold'), command=back, bg='pink')
    button_back.place(x=275, y=590)
    fb.mainloop()

#funtion that stops the program and logs the user out.
def logout():
    messagebox.showinfo(title="Logout Success", message="You successfully logged out.")

window.mainloop()