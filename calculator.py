from tkinter import *

root=Tk()

Label(root,text="Enter the number 1").pack()
num1=Entry(root)
num1.pack()
Label(root,text="Enter the Operation").pack()
opt=Entry(root)
opt.pack()
Label(root,text="Enter the number 2").pack()
num2=Entry(root)
num2.pack()

def cal():
    if(opt.get()=="+"):
        ans=int(num1.get())+int(num2.get())
    elif(opt.get()=="-"):
        ans=int(num1.get())-int(num2.get())
    elif(opt.get()=="*"):
        ans=int(num1.get())*int(num2.get())
    elif(opt.get()=="/"):
        if(num2.get()=="0"):
            error=Label(root,text="Can not divide by zero")
            error.pack()
        else:
            ans=int(num1.get())+int(num2.get())
    else:
        invalid=Label(root,text="invalid oparation")
        invalid.pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    answer=Label(root,text="The answer is "+str(ans))
    answer.pack()

Button(root,command=cal,text="Calculate").pack()

root.mainloop()