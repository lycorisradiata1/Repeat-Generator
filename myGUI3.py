# -*- coding: UTF-8 -*-
__author__ = 'yanxiaoshuang'

from Tkinter import *
import ctypes
import circlebase
RESULT={}
def Mbox(title,text,style):
    ctypes.windll.user32.MessageBoxA(0,text,title,style)
def on_click(num,str1,path,name,v1,v):
    global RESULT
    n = int(num.get())
    s = str(str1.get())
    p = str(path.get())
    na = str(name.get())
    RESULT = {'num':n,'string':s,'path':p,'name':na}
    string = str('Success!!\nSee your result in the file of %s%s.txt'%(p,na))
    titleb = 'result'
    Mbox(titleb,string,1)
    if(v1.get()==0):
        space = 0
    else:
        space = 1
    print(space)
    if(v.get()==0):
        sameclick(space)
    else:
        diffclick(space)
    return

def myui():
    global  RESULT
    root = Tk()
    root.title('重复文件生成器')
    v = IntVar()
    v.set(0)
    m = PanedWindow(orient=HORIZONTAL)
    m.pack(fill=BOTH,expand=1)
    Radiobutton(m,text = '相同文字生成器',variable = v,value = 0).pack()
    Radiobutton(m,text = '不同文字生成器',variable = v,value = 1).pack()

    mm = PanedWindow(orient=VERTICAL)
    mm.pack(fill=BOTH,expand=1)



    head = Label(mm,text='请输入以下内容：')
    head.pack(side=LEFT)
    mm.add(head)


    m0 = PanedWindow(orient=HORIZONTAL)
    m0.pack(fill=BOTH,expand=1)
    left1 = Label(m0,text='循环个数：')
    left1.pack(side=LEFT)
    m0.add(left1)
    text1 = StringVar()
    right1 = Entry(m0,textvariable=text1)
    text1.set("")
    right1.pack()
    m0.add(right1)
    mm.add(m0)

    m2 = PanedWindow(orient=HORIZONTAL)
    m2.pack(fill=BOTH,expand=1)
    left2 = Label(m2,text='基串：')
    m2.add(left2)
    right2 = Entry()
    m2.add(right2)
    mm.add(m2)

    m3 = PanedWindow(orient=HORIZONTAL)
    m3.pack(fill=BOTH,expand=1)
    left = Label(m3,text='路径：')
    m3.add(left)
    right3 = Entry()
    m3.add(right3)
    mm.add(m3)

    m4 = PanedWindow(orient=HORIZONTAL)
    m4.pack(fill=BOTH,expand=1)
    left4 = Label(m4,text='文件名：')
    m4.add(left4)
    right4 = Entry()
    m4.add(right4)
    mm.add(m4)


    bottom = Label(root,text='重复词之间是否需要添加回车符')
    bottom.pack(side=LEFT)
    mm.add(bottom)

    v1 = IntVar()
    v1.set(0)
    Radiobutton(root,text = '不添加',variable = v1,value = 0).pack()
    Radiobutton(root,text = '添加',variable = v1,value = 1).pack()

    Button(root,text='提交',command=lambda:on_click(right1,right2,right3,right4,v1,v)).pack()
    mainloop()


def sameclick(space):#字符串重复生成
    circlebase.circlesame(space,RESULT['num'],RESULT['string'],RESULT['name'],RESULT['path'])

def diffclick(space):#字符串区别化生成
    circlebase.circlediff(space,RESULT['num'],RESULT['string'],RESULT['name'],RESULT['path'])


if __name__ == '__main__':
    myui()

