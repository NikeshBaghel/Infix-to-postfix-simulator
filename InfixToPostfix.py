from tkinter import *

from PIL import ImageTk,Image
root = Tk()
root.title("Infix to postfix converter")

root.geometry("1114x704")
root.maxsize(1114,704)
root.config(bg = "black")

image5 = Image.open("Hello world.jpeg")
image5 = image5.resize((500,500),Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image5)
Label(image  = photo5,bg = "black").place(x = 320,y=110)


image1 = Image.open("python2.jpg")
image1 = image1.resize((600,330),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image1)
Label(image = photo,bg = "black").place(x = 300,y = 0)


#TODO: Execution window code
def Execution_win():
    window = Tk()
    window.config(bg = "violet")
    window.title("Execution window")
    window.geometry("1080x1080")
    def reset():
        window.destroy()
        Execution_win()



    #Labels
    Label(window,text = "Infix: ",relief = SUNKEN,borderwidth = 3,font = ("comicsanms",18,"bold")).place(x = 430 ,y = 30)

    #Userinput
    UserInput = StringVar()
    userentry = Entry(window,textvariable = UserInput,font = ("comicsanms",18,"bold"),borderwidth = 3)
    userentry.place(x = 540,y= 30)

    #TODO: STACK CODE
    def stack():
        Label(window,bg = "grey").grid(row = 0,column = 1)
        Label(window,bg = "grey").grid(row = 1,column = 1)
        Label(window,bg = "grey").grid(row=2, column=1)
        Label(window,bg = "grey").grid(row=3, column=1)
        Label(window,bg = "grey").grid(row=4, column=1)
        Label(window,bg = "grey").grid(row=5, column=1)
        Label(window,bg = "grey").grid(row=6, column=1)
        Label(window,bg = "grey").grid(row=7, column=1)
        Label(window, bg='yellow', text="Symbol", width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8, column=2)
        Label(window, bg='yellow', text="Stack", width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8, column=3)
        Label(window, bg='yellow', text="Postfix", width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8, column=5)


        postfix = []
        temp = []
        operator = -10
        operand = -20
        leftparentheses = -30
        rightparentheses = -40
        empty = -50

        def precedence(s):
            if s is '(':
                return 0
            elif s is '+' or s is '-':
                return 1
            elif s is '*' or s is '/' or s is '%':
                return 2
            else:
                return 99

        def typeof(s):
            if s is '(':
                return leftparentheses
            elif s is ')':
                return rightparentheses
            elif s is '+' or s is '-' or s is '*' or s is '%' or s is '/':
                return operator
            elif s is ' ':
                return empty
            else:
                return operand

        infix = userentry.get()
        j = 1
        k = 1
        l = 1
        for i in infix:
            type = typeof(i)
            Label(window, text=i, width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8 + j, column=2)

            j += 1
            if type is leftparentheses:
                temp.append(i)

                Label(window,text = temp,width = 15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row = 8+l,column = 3)
                l+=1
                Label(window,text = postfix,width = 15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row = 8+k,column = 5)
                k+=1
            elif type is rightparentheses:
                Label(window,text = postfix,width = 15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row = 8+k,column = 5)
                k+=1
                next = temp.pop()
                Label(window,text = temp,width = 15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row = 8+l,column = 3)
                l+=1
                while next is not '(':
                    postfix.append(next)
                    Label(window, text=postfix, width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8 + k, column=5)
                    k += 1
                    next = temp.pop()
                    Label(window, text=temp, width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8 + l, column=3)
                    l += 1
            elif type is operand:
                postfix.append(i)
                Label(window, text=temp, width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8 + l, column=3)
                l += 1
                Label(window,text = postfix,width = 15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row = 8+k,column = 5)
                k+=1
            elif type is operator:
                p = precedence(i)
                while len(temp) is not 0 and p <= precedence(temp[-1]):
                    postfix.append(temp.pop())
                    Label(window, text=postfix, width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8 + k, column=5)
                    k += 1
                temp.append(i)
                Label(window,text = temp,width = 15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row = 8+l,column = 3)
                l+=1
            elif type is empty:
                continue

        while len(temp) > 0:
            Label(window, text=temp, width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8 + l, column=3)
            l += 1
            postfix.append(temp.pop())
            Label(window, text=temp, width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8 + l, column=3)
            l += 1
            Label(window, text=postfix, width=15,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",14,"bold")).grid(row=8 + k, column=5)
            k += 1


        ans = "".join(postfix)
        c = 0
        for i in ans:
            if(i.isalpha() == True):
                break
            else:
                c = c + 1



        if(c == len(ans)):
            obj = eval(infix)
            print("Value of ", ans, "is", obj)
            EvaluatedAns = obj
            Label(window,text = "Evaluated answer is: ",font=("italics", 19, "bold"),borderwidth = 3,relief = SUNKEN,width = 17).place(x =600,y = 200)
            Label(window, text=EvaluatedAns, font=("italics", 19, "bold"), borderwidth=3, relief=SUNKEN,
                ).place(x=900, y=200)
        else:
            Label(window, text="Cannot Evaluate strings ", font=("italics", 19, "bold"), borderwidth=3, relief=SUNKEN,
                  ).place(x=700, y=200)

        print("It's postfix notation is ",ans)
        Label(window, text="Postfix: ", font=("italics", 19, "bold"),borderwidth = 3,relief = SUNKEN).place(x = 430, y=118)
        Label(window, text=ans,font=("italics", 19, "bold"),borderwidth = 3,relief = SUNKEN,width = 17).place(x = 540,y = 118)


        Reset = Button(window, text="reset", command=reset, relief=SUNKEN, borderwidth=3,
                        font=("comicsanms", 10, "bold"))
        Reset.place(x=650, y=82)








    #TODO:  submission of input
    Submit = Button(window, text="Submit",command = stack,relief = SUNKEN,borderwidth = 3,font = ("comicsanms",10,"bold"))
    Submit.place(x = 540,y = 82)


#TODO: Help Window
def Help():
    window_2 = Tk()
    window_2.title("Conversion rules")
    window_2.geometry("900x600")
    window_2.config(bg = "PeachPuff")  #color = Moccasin
    Label(window_2,text = "STEP 1",bg = "Peachpuff",fg = "red",font = ("Helvetica",15,"bold italic")).place(x = 12,y = 34)
    Label(window_2,text = "Scan the infix expression from left to right for tokens(Operators,Operands and Parantheses).",bg = "Peachpuff",fg = "black",font = ("Helvetica",15,"")).place(x=12,y = 64)
    Label(window_2, text="STEP 2", bg="Peachpuff", fg="red", font=("Helvetica", 15, "bold italic")).place(x=12, y=99)
    Label(window_2,text = "If token is operand,append it in postfix expression.",bg = "Peachpuff",fg = "black",font = ("Helvetica",15,"")).place(x=12,y = 128)
    Label(window_2, text="STEP 3", bg="Peachpuff", fg="red", font=("Helvetica", 15, "bold italic")).place(x=12, y=160)
    Label(window_2, text="If token is a left parantheses '(',push it in stack.", bg="Peachpuff", fg="black",font=("Helvetica", 15, "")).place(x=12, y=188)
    Label(window_2, text="STEP 4", bg="Peachpuff", fg="red", font=("Helvetica", 15, "bold italic")).place(x=12, y=220)
    Label(window_2, text="If token is an OPERATOR - \n1.Pop all the operators which are of higher or equal precedence then the incoming token\n and append them to the output expression."
                         "\n2.After poping out such operators, push the new token on stack.", bg="Peachpuff", fg="black",font=("Helvetica", 15, "")).place(x=12, y=248)
    Label(window_2, text="STEP 5", bg="Peachpuff", fg="red", font=("Helvetica", 15, "bold italic")).place(x=12, y=347)
    Label(window_2, text="If ')' right parantheses is found -\n1. Pop all the operators from the stack and append them to the output string,\n till"
                         "you encounter the Opening parantheses '('.\n2. Pop the left parantheses but don't append it to the output string.", bg="Peachpuff", fg="black",font=("Helvetica", 15, "")).place(x=12, y=377)
    Label(window_2, text="STEP 6", bg="Peachpuff", fg="red", font=("Helvetica", 15, "bold italic")).place(x=12, y=480)
    Label(window_2,
          text="When all tokens of Infix expression have been scanned.Pop all the elements \nfrom the stack and append them to the output string.",
          bg="Peachpuff", fg="black", font=("Helvetica", 15, "")).place(x=12, y=520)
    window_2.mainloop()


image2 = Image.open("rightarrow(correct).png")
image2 = image2.resize((100,30),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
Label(image = photo2,bg = "black").place(x = 210,y = 482)

image3 = Image.open("rightarrow(correct).png")
image3 = image3.resize((100,30),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)
Label(image = photo3,bg = "black").place(x = 210,y= 570)




Exe_but = Button(root,bg = "green",fg = "black",text = "Infix to Postfix converter",font = ("italics",19,"bold"),width = 14,padx = 60,pady = 10,borderwidth = 9,command = Execution_win,relief = SUNKEN)
Exe_but.place(x = 378,y = 452)
Rules_but = Button(root,bg = "green",fg = "black",text = "Help",width = 14,font = ("italics",19,"bold"),padx = 60,pady = 10,borderwidth = 9,relief = SUNKEN,command = Help)
Rules_but.place(x = 378,y = 540)

Label(root,bg = "green",fg = "black",text = "made by: ",font = ("italics",13,"bold")).place(x=900,y = 555)
Label(root,bg = "green",fg = "black",text = "Nikeshsingh Baghel",font = ("italics",15,"bold")).place(x=900,y = 580)



root.mainloop()
