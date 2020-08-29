# Calculator.py
# Simple Calculator App using Python 3
# Author : Meianandh Kumarasamy

from tkinter import *
from tkinter import ttk
from decimal import Decimal

class CalculatorGUI:

    def __init__(self, master):
        # Variables
        self.labelTextAbove = StringVar()
        self.labelText = StringVar()
        self.prevKey = StringVar()
        self.mathAction = StringVar()
        self.val1 = DoubleVar()
        self.val2 = DoubleVar()
        self.ans = DoubleVar()

        # Set Initial Values for Variables
        self.labelTextAbove.set("")
        self.labelText.set("0")
        self.resetVariables()

        # GUI Frame
        content = ttk.Frame(master, padding=(5,5,5,5))
        style = ttk.Style()
        style.configure("NUMBER.TButton", font = ('Arial', 12))
        style.configure("SYMBOL.TButton", font = ('Arial', 12))

        # Define Widgets
        labelAbove = ttk.Label(content, textvariable=self.labelTextAbove, font=('Arial',12), foreground='gray', background='#D3D3D3', anchor='e')
        label = ttk.Label(content, textvariable=self.labelText, font=('Arial',18), foreground='black', background='#D3D3D3', anchor='e')
        b0 = ttk.Button(content, text="0", command=self.num_0_key, style="NUMBER.TButton")
        b1 = ttk.Button(content, text="1", command=self.num_1_key, style="NUMBER.TButton")
        b2 = ttk.Button(content, text="2", command=self.num_2_key, style="NUMBER.TButton")
        b3 = ttk.Button(content, text="3", command=self.num_3_key, style="NUMBER.TButton")
        b4 = ttk.Button(content, text="4", command=self.num_4_key, style="NUMBER.TButton")
        b5 = ttk.Button(content, text="5", command=self.num_5_key, style="NUMBER.TButton")
        b6 = ttk.Button(content, text="6", command=self.num_6_key, style="NUMBER.TButton")
        b7 = ttk.Button(content, text="7", command=self.num_7_key, style="NUMBER.TButton")
        b8 = ttk.Button(content, text="8", command=self.num_8_key, style="NUMBER.TButton")
        b9 = ttk.Button(content, text="9", command=self.num_9_key, style="NUMBER.TButton")
        bdec = ttk.Button(content, text=".", command=self.num_dot_key, style="NUMBER.TButton")
        bdel = ttk.Button(content, text="DEL", command=self.action_del, style="SYMBOL.TButton")
        bdiv = ttk.Button(content, text="/", command=self.action_div, style="SYMBOL.TButton")
        bmul = ttk.Button(content, text="*", command=self.action_mul, style="SYMBOL.TButton")
        badd = ttk.Button(content, text="+", command=self.action_add, style="SYMBOL.TButton")
        bsub = ttk.Button(content, text="-", command=self.action_sub, style="SYMBOL.TButton")
        beql = ttk.Button(content, text="=", command=self.action_eql, style="SYMBOL.TButton")

        #Grid Layout
        content.grid(row=0, column=0, sticky=(N, S, E, W))

        #Grid Row 1
        labelAbove.grid(row=0, column=0, rowspan=1, columnspan=4, sticky=(N, S, E, W))

        #Grid Row 2
        label.grid(row=1, column=0, rowspan=1, columnspan=4, sticky=(N, S, E, W))

        #Grid Row 3
        bdel.grid(row=2, column=0, sticky=(N, S, E, W))
        bdiv.grid(row=2, column=1, sticky=(N, S, E, W))
        bmul.grid(row=2, column=2, sticky=(N, S, E, W))
        bsub.grid(row=2, column=3, sticky=(N, S, E, W))

        #Grid Row 4
        b7.grid(row=3, column=0, sticky=(N, S, E, W))
        b8.grid(row=3, column=1, sticky=(N, S, E, W))
        b9.grid(row=3, column=2, sticky=(N, S, E, W))
        badd.grid(row=3, column=3, rowspan=2, columnspan=1, sticky=(N, S, E, W))

        #Grid Row 5
        b4.grid(row=4, column=0, sticky=(N, S, E, W))
        b5.grid(row=4, column=1, sticky=(N, S, E, W))
        b6.grid(row=4, column=2, sticky=(N, S, E, W))

        #Grid Row 6
        b1.grid(row=5, column=0, sticky=(N, S, E, W))
        b2.grid(row=5, column=1, sticky=(N, S, E, W))
        b3.grid(row=5, column=2, sticky=(N, S, E, W))
        beql.grid(row=5, column=3, rowspan=2, columnspan=1, sticky=(N, S, E, W))

        #Grid Row 7
        b0.grid(row=6, column=0, rowspan=1, columnspan=2, sticky=(N, S, E, W))
        bdec.grid(row=6, column=2, sticky=(N, S, E, W))

        #Bind KEY to buttons
        master.bind('q', quit)
        master.bind('0', lambda event: self.num_key_press(self, key="0"))
        master.bind('1', lambda event: self.num_key_press(self, key="1"))
        master.bind('2', lambda event: self.num_key_press(self, key="2"))
        master.bind('3', lambda event: self.num_key_press(self, key="3"))
        master.bind('4', lambda event: self.num_key_press(self, key="4"))
        master.bind('5', lambda event: self.num_key_press(self, key="5"))
        master.bind('6', lambda event: self.num_key_press(self, key="6"))
        master.bind('7', lambda event: self.num_key_press(self, key="7"))
        master.bind('8', lambda event: self.num_key_press(self, key="8"))
        master.bind('9', lambda event: self.num_key_press(self, key="9"))
        master.bind('.', self.num_dot_key)
        master.bind('+', self.action_add)
        master.bind('-', self.action_sub)
        master.bind('/', self.action_div)
        master.bind('*', self.action_mul)
        master.bind('<Delete>', self.action_del)
        master.bind('<BackSpace>', self.action_del)
        master.bind('<Return>', self.action_eql)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        content.columnconfigure(2, weight=1)
        content.columnconfigure(3, weight=1)
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)
        content.rowconfigure(2, weight=1)
        content.rowconfigure(3, weight=1)
        content.rowconfigure(4, weight=1)
        content.rowconfigure(5, weight=1)
        content.rowconfigure(6, weight=1)


    def num_key_action(self, keyVal):
        currentData = self.labelText.get()
        if(self.prevKey.get() == "="):
            self.labelText.set("0")
            currentData = self.labelText.get()
        symbolStr = ["+", "-", "/", "*"]
        for sym in symbolStr:
            if(self.prevKey.get() == sym):
                self.labelText.set("0")
                currentData = self.labelText.get()
        if(currentData == "0"):
            currentData = ""
        if(keyVal == "0"):
            self.labelText.set(str(currentData) + "0")
        elif(keyVal == "1"):
            self.labelText.set(str(currentData) + "1")
        elif(keyVal == "2"):
            self.labelText.set(str(currentData) + "2")
        elif(keyVal == "3"):
            self.labelText.set(str(currentData) + "3")
        elif(keyVal == "4"):
            self.labelText.set(str(currentData) + "4")
        elif(keyVal == "5"):
            self.labelText.set(str(currentData) + "5")
        elif(keyVal == "6"):
            self.labelText.set(str(currentData) + "6")
        elif(keyVal == "7"):
            self.labelText.set(str(currentData) + "7")
        elif(keyVal == "8"):
            self.labelText.set(str(currentData) + "8")
        elif(keyVal == "9"):
            self.labelText.set(str(currentData) + "9")
        elif(keyVal == "."):
            self.labelText.set(str(currentData) + ".")

    def resetVariables(self):
        self.prevKey.set("NA")
        self.mathAction.set("NA")
        self.val1.set(0.0)
        self.val2.set(0.0)
        self.ans.set(0.0)

    def calcAction(self):
        self.labelTextAbove.set(str(self.val1.get()) + " " + str(self.mathAction.get())+ " "+ str(self.val2.get()))
        if(self.mathAction.get() == "+"):
            self.ans.set(self.val1.get() + self.val2.get())
        elif(self.mathAction.get() == "-"):
            self.ans.set(self.val1.get() - self.val2.get())
        elif(self.mathAction.get() == "*"):
            self.ans.set(self.val1.get() * self.val2.get())
        elif(self.mathAction.get() == "/"):
            self.ans.set(self.val1.get() / self.val2.get())
        print("val1 : " + str(self.val1.get()))
        print("val2 : " + str(self.val2.get()))
        print("ans : " + str(self.ans.get()))
        self.labelText.set(self.ans.get())
        self.resetVariables()
        self.val1.set(Decimal(self.labelText.get()))

    def action_eql(self, _event=None):
        self.val2.set(Decimal(self.labelText.get()))
        self.calcAction()
        self.resetVariables()
        self.prevKey.set("=")

    def action_actionVal(self, actV):
        self.prevKey.set(actV)
        self.mathAction.set(actV)
        self.labelTextAbove.set(str(self.val1.get()) + " " + str(actV))


    def action_common(self, actVal):
        if(self.val1.get() == 0 and self.mathAction.get() == "NA"):
            self.val1.set(Decimal(self.labelText.get()))
            self.labelTextAbove.set(str(self.val1.get()))
        elif(self.mathAction.get() != "NA"):
            self.val2.set(Decimal(self.labelText.get()))
            self.calcAction()
        self.action_actionVal(actVal)

    def action_add(self, _event=None):
        if(self.prevKey.get() != "+" and self.prevKey.get() != "-" and self.prevKey.get() != "*" and self.prevKey.get() != "/"):
            self.action_common("+")
        else:
            self.action_actionVal(self, str("+"))

    def action_sub(self, _event=None):
        if(self.prevKey.get() != "+" and self.prevKey.get() != "-" and self.prevKey.get() != "*" and self.prevKey.get() != "/"):
            self.action_common("-")
        else:
            self.action_actionVal("-")

    def action_mul(self, _event=None):
        if(self.prevKey.get() != "+" and self.prevKey.get() != "-" and self.prevKey.get() != "*" and self.prevKey.get() != "/"):
            self.action_common("*")
        else:
            self.action_actionVal("*")

    def action_div(self, _event=None):
        if(self.prevKey.get() != "+" and self.prevKey.get() != "-" and self.prevKey.get() != "*" and self.prevKey.get() != "/"):
            self.action_common("/")
        else:
            self.action_actionVal("/")

    def action_del(self, _event=None):
        self.resetVariables()
        self.labelText.set("0")
        self.labelTextAbove.set("")

    def num_key(self, numVal):
        self.num_key_action(numVal)
        self.prevKey.set(numVal)

    def num_key_press(self, event, key):
        self.num_key(key)

    def num_0_key(self, _event=None):
        self.num_key("0")

    def num_1_key(self, _event=None):
        self.num_key("1")

    def num_2_key(self, _event=None):
        self.num_key("2")

    def num_3_key(self, _event=None):
        self.num_key("3")

    def num_4_key(self, _event=None):
        self.num_key("4")

    def num_5_key(self, _event=None):
        self.num_key("5")

    def num_6_key(self, _event=None):
        self.num_key("6")

    def num_7_key(self, _event=None):
        self.num_key("7")

    def num_8_key(self, _event=None):
        self.num_key("8")

    def num_9_key(self, _event=None):
        self.num_key("9")

    def num_dot_key(self, _event=None):
        self.num_key(".")


if __name__ == "__main__":
    root = Tk()
    calculatorGUI = CalculatorGUI(root)
    root.geometry("250x300")
    root.title("Calculator")
    root.mainloop()