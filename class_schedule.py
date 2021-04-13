from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

Username=input("输入学号\n")
Password=(input("输入密码\n"))
browser=webdriver.Chrome()

url='http://jwch.fzu.edu.cn/login.aspx'
browser.get(url)




input1=browser.find_element_by_id("UserName")
input2=browser.find_element_by_id("passWord")
input1.send_keys(Username)
input2.send_keys(Password)
input2.send_keys(Keys.ENTER)
default=browser.current_url
change=default.replace('default','right')
browser.get(change)

html=browser.page_source
soup=BeautifulSoup(html,'lxml')


tmp=(soup.find_all(text=re.compile("节次"))[0].parent.parent.parent)#父节点！！！！！！！1


# ROW 1
child1=tmp.contents[0]

print('',end='\t')
for i in child1.contents:
    print(i.string,end='\t ')




print('\n')
# # ROW 2
child2=tmp.contents[1]
print(child2.contents[1].contents[2],end='  ')

for cchild in child2.contents:
    try:
        a=str(cchild.contents[0].string)
        if(a=="None"):
            print(child2.contents[3].contents[0].contents[0].string,end='  ')
        else:
            print(cchild.contents[0].string,end='  ')
    except IndexError:
        print("没课",end='  ')




print('\n')
# # ROW 3
child3=tmp.contents[2]
print(child3.contents[0].contents[2],end='  ')

for cchild in child3.contents:
    try:
        a=str(cchild.contents[0].string)
        if(a=="None"):
            print(child3.contents[3].contents[0].contents[0].string,end='  ')
        else:
            print(cchild.contents[0].string,end='  ')
    except IndexError:
        print("没课",end='  ')


print('\n')    
# # ROW 4
child4=tmp.contents[3]
print(child4.contents[0].contents[2],end='  ')

for cchild in child4.contents:
    try:
        a=str(cchild.contents[0].string)
        if(a=="None"):
            print(child4.contents[3].contents[0].contents[0].string,end='  ')
        else:
            print(cchild.contents[0].string,end='  ')
    except IndexError:
        print("没课",end='  ')


print('\n')
# # ROW 5
child5=tmp.contents[4]
print(child5.contents[0].contents[2],end='  ')

for cchild in child5.contents:
    try:
        a=str(cchild.contents[0].string)
        if(a=="None"):
            print(child5.contents[3].contents[0].contents[0].string,end='  ')
        else:
            print(cchild.contents[0].string,end='  ')
    except IndexError:
        print("没课",end='  ')


print('\n')
# # ROW 6
child6=tmp.contents[5]
print(child6.contents[1].contents[2],end='  ')

for cchild in child6.contents:
    try:
        a=str(cchild.contents[0].string)
        if(a=="None"):
            print(child6.contents[3].contents[0].contents[0].string,end='  ')
        else:
            print(cchild.contents[0].string,end='  ')
    except IndexError:
        print("没课",end='  ')



print('\n')
# # ROW 7
child7=tmp.contents[6]
print(child7.contents[0].contents[2],end='  ')
for cchild in child7.contents:
    try:
        a=str(cchild.contents[0].string)
        if(a=="None"):
            print(child7.contents[3].contents[0].contents[0].string,end='  ')
        else:
            print(cchild.contents[0].string,end='  ')
    except IndexError:
        print("没课",end='  ')



print('\n')
# # ROW 8
child8=tmp.contents[7]
print(child8.contents[0].contents[2],end='  ')
for cchild in child8.contents:
    try:
        a=str(cchild.contents[0].string)
        if(a=="None"):
            print(child8.contents[3].contents[0].contents[0].string,end='  ')
        else:
            print(cchild.contents[0].string,end='  ')
    except IndexError:
        print("没课",end='  ')




print('\n')
# # ROW 9
child9=tmp.contents[8]
print(child9.contents[0].contents[2],end='  ')
for cchild in child9.contents:
    try:
        a=str(cchild.contents[0].string)
        if(a=="None"):
            print(child9.contents[3].contents[0].contents[0].string,end='  ')
        else:
            print(cchild.contents[0].string,end='  ')
    except IndexError:
        print("没课",end='  ')

browser.close()