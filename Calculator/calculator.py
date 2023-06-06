from tkinter import *


calc=Tk()

expression=""

var=StringVar()
e=Entry(calc,textvariable=var,width=25)
e.grid(row=0,column=0,columnspan=4)

def press(num):
    global expression

    if expression in ["0","+","-","*","/"]:
        clear()

    def rip():
        try:
            if expression[-1] in ["+","-","*","/","."]:
                backsp()
        except:
            pass           

    if str(num)=='+':
        rip()
    elif str(num)=='-':
        rip()
    elif str(num)=='*':
        rip()
    elif str(num)=='/':
        rip()
    elif str(num)=='.':
        rip()
    else:
        pass

    expression = expression + str(num)


 
    var.set(expression)

def equalsto():

    try:
 
        global expression

        total = str(eval(expression))
 
        var.set(total)
 
        expression = ""
 
    except:
 
        var.set(" error ")
        expression = ""

def backsp():
    global expression
    expression=expression[0:len(expression)-1]
    var.set(expression)
    
def clear():
    global expression 
    expression =""
    var.set("")


bf7=Button(calc,text=7, height=2,width=4,command=lambda: press(7))
bf7.grid(row=1,column=0)
bf8=Button(calc,text=8, height=2,width=4,command=lambda: press(8))
bf8.grid(row=1,column=1)
bf9=Button(calc,text=9, height=2,width=4,command=lambda: press(9))
bf9.grid(row=1,column=2)
bclr=Button(calc,text="CLEAR",height=2,width=15, command=clear,background='red',foreground='white')
bclr.grid(row=5,columnspan=3)
bf4=Button(calc,text=4, height=2,width=4,command=lambda: press(4))
bf4.grid(row=2,column=0)
bf5=Button(calc,text=5, height=2,width=4,command=lambda: press(5))
bf5.grid(row=2,column=1)
bf6=Button(calc,text=6, height=2,width=4,command=lambda: press(6))
bf6.grid(row=2,column=2)
bplus=Button(calc,text='+', height=2,width=4,command=lambda: press('+'))
bplus.grid(row=2,column=3)
bf1=Button(calc,text=1, height=2,width=4,command=lambda: press(1))
bf1.grid(row=3,column=0)
bf2=Button(calc,text=2 ,height=2,width=4,command=lambda: press(2))
bf2.grid(row=3,column=1)
bf3=Button(calc,text=3 ,height=2,width=4,command=lambda: press(3))
bf3.grid(row=3,column=2)
bminus=Button(calc,text='-', height=2,width=4,command=lambda: press('-'))
bminus.grid(row=3,column=3)
bf0=Button(calc,text=0, height=2,width=4,command=lambda: press(0))
bf0.grid(row=4,column=0)
bdec=Button(calc,text=".", height=2,width=4,command=lambda: press('.'))
bdec.grid(row=4,column=1)
bmul=Button(calc,text='*', height=2,width=4,command=lambda: press('*'))
bmul.grid(row=4,column=2)
bdiv=Button(calc,text='/', height=2,width=4,command=lambda: press('/'))
bdiv.grid(row=4,column=3)
beq=Button(calc,text='=',height=2,width=4,command=equalsto)
beq.grid(row=5,column=3)
bback=Button(calc,text='C',height=2,width=4,command=backsp,foreground='red')
bback.grid(row=1,column=3)

calc.mainloop()