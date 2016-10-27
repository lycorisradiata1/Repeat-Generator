# coding=UTF-8
__author__ = 'yanxiaoshuang'
import os
import sys
type = sys.getfilesystemencoding()
def circlesame(space,num1,str1,name,path = 'd://'):
    #num1为循环多少个；str1为基字符串；name为要保存的文件名称;path为保存文件的路径
    #生成num1个相同的字符串
    i=0
    a=[]
    allpath = path+name+'.txt'
    print allpath

    if(os.path.exists(allpath)):
        fp = open(allpath,'a+')
        fp.write('\n')
        fp.write('\n')
    else:
        fp = open(allpath,'a+')
    strstart = (str(num1)+'个：\n').decode('utf-8').encode(type)
    fp.write(strstart)
    while(i<num1):
        fp.write(str1)
        if(space):
            fp.write('\n')
        else:
            pass
        s=str1
        i+=1
    fp.close()


def circlediff(space,num1,str1,name,path = 'd://'):
    #num1为循环多少个；str1为基字符串；name为要保存的文件名称;path为保存文件的路径
    #生成num1个不同的字符串
    print(path)
    i=0
    a=[]
    s =str1
    print s
    allpath = path+name+'.txt'
    print allpath

    if(os.path.exists(allpath)):
        fp = open(allpath,'a+')
        fp.write('\n')
        fp.write('\n')
    else:
        fp = open(allpath,'a+')
    strstart = (str(num1)+'个：\n').decode('utf-8').encode(type)
    fp.write(strstart)
    while(i<num1):
        s+=str(i)
        fp.write(s)
        if(space):
            fp.write('\n')
        else:
            pass
        s=str1
        i+=1 
    fp.close()
