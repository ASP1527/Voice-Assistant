from tkinter import *


def runCalculator():
    root = Tk()
    root.title("Calculator")

    def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_input.set(operator)

    def btnClearDisplay():
        global operator
        operator = ""
        text_input.set("")

    def btnEquals():
        global operator
        sums = str(eval(operator))
        text_input.set(sums)
        operator = ""
        global ans
        ans = sums

    def showAns():
        global operator
        try:
            operator = ""
            text_input.set(ans)
        except:
            operator = ""
            text_input.set("")

    global operator
    operator = ""

    text_input = StringVar()

    e = Entry(root, textvariable=text_input, width=25,
              bg="powder blue", justify='left').grid(row=0, column=0, columnspan=4, padx=0, pady=0)

    button1 = Button(root, text="1", padx=20, pady=5,
                     command=lambda: btnClick(1))
    button2 = Button(root, text="2", padx=20, pady=5,
                     command=lambda: btnClick(2))
    button3 = Button(root, text="3", padx=20, pady=5,
                     command=lambda: btnClick(3))
    button4 = Button(root, text="4", padx=20, pady=5,
                     command=lambda: btnClick(4))
    button5 = Button(root, text="5", padx=20, pady=5,
                     command=lambda: btnClick(5))
    button6 = Button(root, text="6", padx=20, pady=5,
                     command=lambda: btnClick(6))
    button7 = Button(root, text="7", padx=20, pady=5,
                     command=lambda: btnClick(7))
    button8 = Button(root, text="8", padx=20, pady=5,
                     command=lambda: btnClick(8))
    button9 = Button(root, text="9", padx=20, pady=5,
                     command=lambda: btnClick(9))
    button0 = Button(root, text="0", padx=20, pady=5,
                     command=lambda: btnClick(0))
    buttonC = Button(root, text="C", padx=20, pady=5, command=btnClearDisplay)
    buttonAns = Button(root, text="ANS", padx=8, pady=5, command=showAns)
    buttonAdd = Button(root, text="+", padx=20, pady=5,
                       command=lambda: btnClick("+"))
    buttonSubtract = Button(root, text="-", padx=22, pady=5,
                            command=lambda: btnClick("-"))
    buttonMultiply = Button(root, text="*", padx=20, pady=5,
                            command=lambda: btnClick("*"))
    buttonDivide = Button(root, text="/", padx=20, pady=5,
                          command=lambda: btnClick("/"))
    buttonCalculate = Button(root, text="=", padx=20,
                             pady=5, command=btnEquals)
    buttonDecimal = Button(root, text=".", padx=23, pady=5,
                           command=lambda: btnClick("."))
    buttonExp = Button(root, text="^", padx=20, pady=5,
                       command=lambda: btnClick("**"))

    button0.grid(row=5, column=0)
    buttonDecimal.grid(row=5, column=1)
    buttonAns.grid(row=5, column=2)
    buttonCalculate.grid(row=5, column=3)

    button1.grid(row=4, column=0)
    button2.grid(row=4, column=1)
    button3.grid(row=4, column=2)
    buttonSubtract.grid(row=4, column=3)

    button4.grid(row=3, column=0)
    button5.grid(row=3, column=1)
    button6.grid(row=3, column=2)
    buttonAdd.grid(row=3, column=3)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    buttonMultiply.grid(row=2, column=3)

    buttonC.grid(row=1, column=1)
    buttonExp.grid(row=1, column=2)
    buttonDivide.grid(row=1, column=3)

    root.mainloop()
