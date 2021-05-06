from tkinter import *
import math

class calc:

    def getAndreplace(self):
        self.expression=self.e.get()
        self.new_text=self.expression.replace('/', '/')
        self.new_text=self.new_text.replace('x','*')


    def equals(self):
        self.getAndreplace()
        try:
            self.value=eval(self.new_text)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Out Of Range')
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)

    def sqareRoot(self):
        self.getAndreplace()
        try:
            self.value=eval(self.new_text)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Cannot Get Sqaureroot of a give number')
        else:
            self.sqrtval=math.sqrt(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.sqrtval)

    def Square(self):
        self.getAndreplace()

        try:
            self.value = eval(self.new_text)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,"can't get Square !")
        else:
            self.sqrtval=math.pow(self.value,2)
            self.e.delete(0,END)
            self.e.insert(0,self.sqrtval)

    def clearAll(self):
        self.e.delete(0,END)


    def clear1(self):
        self.txt=self.e.get()[:-1]
        self.e.delete(0,END)
        self.e.insert(0,self.txt)

    def action(self,arg):
        self.e.insert(END,arg)


    def __init__(self,master):
        master.title('Homemade Calculator')
        master.geometry()
        self.e=Entry(master)
        self.e.grid(row=0, column=0, columnspan=6,pady=3)
        self.e.focus_set()

        Button(master,text="=",width=11,height=3,fg="Red",
               bg="Purple",command=lambda: self.equals()).grid(
            row=4,column=4,columnspan=2
        )

        Button(master, text='AC', width=5,height=3,
               fg="Blue", bg="Purple",
               command=lambda: self.clearAll()).grid(row=1,column=4)

        Button(master,text='C', width=5,height=3,
               fg="Red", bg="Purple", command=lambda: self.clear1()).grid(row=1,column=5)

        Button(master,text="+", width=5,height=3,
               fg="red", bg="purple",
               command=lambda: self.action('+')).grid(row=4,column=3)

        Button(master,text="x", width=5,height=3,
               fg="Blue",bg="purple",
               command=lambda: self.action('x')).grid(row=2,column=3)

        Button(master, text="-", width=5, height=3,
               fg="Blue", bg="purple",
               command=lambda: self.action('-')).grid(row=3, column=3)

        Button(master,text="÷",width=5,height=3,
               fg="red", bg="purple",
               command=lambda:self.action('/')).grid(row=1,column=3)

        Button(master, text="%", width=5, height=3,
               fg="Blue", bg="purple",
               command=lambda: self.action('%')).grid(row=4, column=2)

        Button(master,text="7", width=5, height=3,
               fg="red",bg="purple",
               command=lambda:self.action('7')).grid(row=1,column=0)

        Button(master,text="8",width=5,height=3,
               fg="blue",bg="purple",
               command=lambda: self.action(8)).grid(row=1,column=1)

        Button(master, text="9", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(9)).grid(row=1, column=2)

        Button(master, text="4", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(4)).grid(row=2, column=0)

        Button(master, text="5", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(5)).grid(row=2, column=1)

        Button(master, text="6", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(6)).grid(row=2, column=2)


        Button(master, text="1", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(1)).grid(row=3, column=0)

        Button(master, text="2", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(2)).grid(row=3, column=1)



        Button(master, text="3", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(3)).grid(row=3, column=2)

        Button(master, text="0", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(0)).grid(row=4, column=0)

        Button(master, text=".", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action('.')).grid(row=4, column=1)
        Button(master, text="(", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action('(')).grid(row=2, column=4)

        Button(master, text=")", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.action(')')).grid(row=2, column=5)

        Button(master, text="?", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.sqareRoot()).grid(row=3, column=4)

        Button(master, text="x²", width=5, height=3,
               fg="blue", bg="purple",
               command=lambda: self.Square()).grid(row=3, column=5)


root=Tk()
calc(root)

root.mainloop()
