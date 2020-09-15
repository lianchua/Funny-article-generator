# python3 使用 tkinter
from tkinter import *

def startfun():
    print("hello ~ !")
    a = input_main.get()
    b = input_main2.get()
    c = input_main3.get()
    print(a)
    print(b)
    print(c)
    result='    '+a+b+'是怎么回事呢？'+a+'相信大家都很熟悉，但是'+a+b+'是怎么回事呢？下面就让小编带大家一起了解吧。'+' '+a+b+'，其实就是'+c+'，大家可能会很惊讶'+a+'怎么会'+b+'呢？但事实就是这样，小编也感到非常惊讶。'+'  '+'这就是关于'+a+b+'的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'
    print(result)
    return result

def out_result():
    result_info.delete('1.0','end')
    result_info.insert('end',startfun())
   
root = Tk()
w = 600 # width for the Tk root
h = 366 # height for the Tk root
# root.geometry('640x480')
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
root.title("沙雕营销号文章生成器")
label = Label(frame1, text="主体", justify=LEFT)
input_main = Entry(frame1, text="Label", justify=LEFT)
label.pack(side=LEFT)
input_main.pack(side=LEFT)
label2 = Label(frame1, text="行为", justify=LEFT)
input_main2 = Entry(frame1, text="Label2", justify=LEFT)
label2.pack(side=LEFT)
input_main2.pack(side=LEFT)
label3 = Label(frame1, text="另一个说法", justify=LEFT)
input_main3 = Entry(frame1, text="Label3", justify=LEFT)
label3.pack(side=LEFT)
input_main3.pack(side=LEFT)
hi_there = Button(frame2, text="生成文章", command=out_result)
hi_there.pack()
result_info = Text(frame3)
result_info.pack(side=LEFT)
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)
frame3.pack(padx=10, pady=10)

root.mainloop()