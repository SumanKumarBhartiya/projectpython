# Python program to create a simple GUI
# calculator using Tkinter

from tkinter import * # import everything from tkinter module

expression = "" # globally declare the expression variable

def press(num):
    
    global expression # point out the global expression variable
    
    expression = expression + str(num) # concatenation of string
    
    equation.set(expression) # update the expression by using set method

def equalpress(): # Function to evaluate the final expression
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
	#expression=""
    except ZeroDivisionError:
        equation.set(" error ")
        expression=""
def clear(): # Function to clear the expression
    global expression
    expression = ""
    equation.set("")
    expression_field.insert(0, '0')
# Driver code
if __name__ == "__main__":
    
    gui = Tk() # create a GUI window
    
    gui.configure(background="") # set the background colour of GUI window
    
    gui.title("Suman's Calculator") # set the title of GUI window
    
    gui.geometry("513x296")  # set the configuration of GUI window
    
    equation = StringVar() # StringVar() is the variable class, we create an instance of this class
    
    expression_field = Entry(gui,font=("Arial",14),textvariable=equation) # create the text entry box for showing the expression .
    expression_field.insert(0, '0')
    expression_field.grid(columnspan=4,ipadx=145, ipady=10) # grid method is used for placing the widgets at respective positions  in table like structure .

    # create a Buttons and place at a particular location inside the root window .
    # when user press the button, the command or function affiliated to that button is executed .
    
    b1=Button(gui,text=' 1 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(1),height=2,width=13)
    b1.grid(row=2, column=0)

    b2 = Button(gui,text=' 2 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(2),height=2,width=13)
    b2.grid(row=2, column=1)

    b3 = Button(gui,text=' 3 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(3),height=2,width=13)
    b3.grid(row=2, column=2)

    b4 = Button(gui,text=' 4 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(4),height=2,width=13)
    b4.grid(row=3, column=0)

    b5 = Button(gui,text=' 5 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(5),height=2,width=13)
    b5.grid(row=3, column=1)

    b6 = Button(gui,text=' 6 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(6),height=2,width=13)
    b6.grid(row=3, column=2)

    b7 = Button(gui,text=' 7 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(7),height=2,width=13)
    b7.grid(row=4, column=0)

    b8 = Button(gui,text=' 8 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(8),height=2,width=13)
    b8.grid(row=4, column=1)

    b9 = Button(gui,text=' 9 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(9),height=2,width=13)
    b9.grid(row=4, column=2)

    b0 = Button(gui,text=' 0 ',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda: press(0),height=2,width=13)
    b0.grid(row=5, column=1)

    divide=Button(gui,text=' % ',font=("Arial",12),fg='#202124',bg='#dadce0',command=lambda: press("%"),height=2,width=13)
    divide.grid(row=2, column=3)

    multiply=Button(gui,text=' / ',font=("Arial",12),fg='#202124',bg='#dadce0',command=lambda: press("/"),height=2,width=13)
    multiply.grid(row=3, column=3)

    minus=Button(gui,text=' * ',font=("Arial",12),fg='#202124',bg='#dadce0',command=lambda:press("*"),height=2,width=13)
    minus.grid(row=4, column=3)

    plus=Button(gui,text=' - ',font=("Arial",12),fg='#202124',bg='#dadce0',command=lambda: press("-"),height=2,width=13)
    plus.grid(row=5, column=3)

    clear = Button(gui,text='Clear',font=("Arial",12),fg='#202124',bg='#dadce0',command=clear,height=2,width=13)
    clear.grid(row=5, column='2')

    Decimal=Button(gui,text='.',font=("Arial",12),fg='black',bg='#f1f3f4',command=lambda:press('.'),height=2,width=13)
    Decimal.grid(row=5, column=0)
    
    modulo=Button(gui,text='+',font=("Arial",12),fg='#202124',bg='#dadce0',command=lambda:press('+'),height=2,width=13)
    modulo.grid(row=6, column=3)

    equal = Button(gui,text=' = ',font=("Arial",12),fg='#fff',bg='#4285f4',command=equalpress,height=2,width=13)
    equal.grid(row=6,column=2)

    bracket1 = Button(gui,text=' ( ',font=("Arial",12),fg='#202124',bg='#dadce0',command=lambda:press('('),height=2,width=13)
    bracket1.grid(row=6,column=0)
    
    bracket2 = Button(gui,text=' ) ',font=("Arial",12),fg='#202124',bg='#dadce0',command=lambda:press(')'),height=2,width=13)
    bracket2.grid(row=6,column=1)

    
    gui.mainloop() # start the GUI
