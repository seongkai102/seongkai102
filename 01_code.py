from tkinter import *

def calc_add():
    a = entry1.get()
    a = int(a)
    b = entry2.get()
    b = int(b)
    label2['text'] = f'결과: {a + b}'

def calc_sub():
    a = entry1.get()
    a = int(a)
    b = entry2.get()
    b = int(b)
    label2['text'] = f'결과: {a - b}'

def calc_null():
    a = entry1.get()
    a = int(a)
    b = entry2.get()
    b = int(b)
    label2['text'] = f'결과: {a * b}'

def calc_div():
    a = entry1.get()
    a = int(a)
    b = entry2.get()
    b = int(b)
    label2['text'] = f'결과: {a / b}'

root = Tk() #클래스의 인스턴스

root.title('lsy')
root.geometry('500x200')

label1 =  Label(root, text = '계산기', font=(40)) #(창, text = '입력'), font = ('글씨체,크기')
label1.pack() #이걸해야 창에 뜸

entry1 = Entry(root, width=30)
entry1.pack()

entry2 = Entry(root, width=30)
entry2.pack()

butten1 = Button(root, text='더하기', command=calc_add) #더하기
butten1.pack()

butten2 = Button(root, text='빼기', command=calc_sub) #뺴기
butten2.pack()

butten3 = Button(root, text='곱하기', command=calc_null) #곱하기
butten3.pack()

butten4 = Button(root, text='나누기', command=calc_div) #나누기
butten4.pack()

label2 =  Label(root, text = '결과: ', font=(40)) #(창, text = '입력'), font = ('글씨체,크기')
label2.pack() 

root.mainloop() #동작