import requests
from bs4 import BeautifulSoup
import time
import re

# 爬取信息部分
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Cookie': '_ga=GA1.3.1855477254.1590192930; JSESSIONID=0000edq_PfRDzKh4gYgYrSJwWPo:18f1dopuc'
}

url='http://news.fzu.edu.cn/html/fdyw/1.html'

import pymysql

def connect(host,user,password,port):
    db=pymysql.connect(host=host,user=user,password=password,port=port)
    cursor=db.cursor()
    cursor.execute("SELECT VERSION()")
    data=cursor.fetchone()
    print("Connect successfully!Here is the version:",data)
    create_a_database(db=db)

def create_a_database(db):
    basename=input("Please input the basename you want to create.\n")
    cursor=db.cursor()
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET utf8".format(basename))
    print("Create {} successfully".format(basename))
    create_a_database_table(basename=basename)

def create_a_database_table(basename):
    tablename=input("Please input the table you want to create.\n")
    db=pymysql.connect(host=host,user=user,password=password,port=port,db=basename)
    cursor=db.cursor()
    # fieldlist=input("Please input the field you want to add\n")
    fieldlist="Title VARCHAR(255) NOT NULL,Date VARCHAR(255) NOT NULL,Author VARCHAR(255) NOT NULL,TotalRead VARCHAR(255) NOT NULL,Body TEXT NOT NULL"
    sql='CREATE TABLE IF NOT EXISTS {0} ({1})'.format(tablename,fieldlist)
    cursor.execute(sql)
    insert_a_data_into_table(db=db,tablename=tablename)

def insert_a_data_into_table(db,tablename):
    
    def main(i):
        url2=url.replace('1',str(i))    
        html=requests.get(url=url2, headers=headers)
        parsing_html_(html.text)

    def parsing_html_(html):#翻页后的网页，要从中提取二级网页
        soup=BeautifulSoup(html,'lxml')
        add="http://news.fzu.edu.cn"
        for i in soup.find_all(attrs={'class':'list_time'}):
            # print(list(i.next_siblings)[1].attrs['href'])
            next_html=add+(list(i.next_siblings)[1].attrs['href'])
            process(next_html)

    def process(html):#已经获取二级网页，要对其提取信息
        url2=html
        # time.sleep(1)
        html2=requests.get(url=url2,headers=headers).text
        
        soup=BeautifulSoup(html2,'lxml')
        
        head_info=soup.find(attrs={"class","detail_main_content"})
        head_info2=soup.find(attrs={"class","detail_content_display"})
        try:
            Body=(list(head_info2.next_siblings)[1].contents[0].contents[1])
        except IndexError:
            Body=""
        for i in range(1,len((list(head_info2.next_siblings)[1].contents))):
            try:
                Body+=list(head_info2.next_siblings)[1].contents[i].string
            except TypeError:
                break
        # print(Body)
        base_url="http://news.fzu.edu.cn/interFace/getDocReadCount.do?id=" 
        try:
            readcount_source=str(head_info.contents[3].contents[12].string)
        except IndexError:
            readcount_source=str(head_info.contents[5].contents[12])
        readcount_url=re.findall("id=(.*?)',timeout:",readcount_source,re.S)
        url_read_cout=base_url+readcount_url[0]
        request2=requests.get(url=url_read_cout)

        Title=head_info.contents[1].string
        try:
            Date=head_info.contents[3].contents[3].string
        except IndexError:
            Date=head_info.contents[5].contents[3].string
        try:
            Author=head_info.contents[3].contents[7].string
        except IndexError:
            Author=head_info.contents[5].contents[7].string
        TotalRead=request2.text
        

        cursor=db.cursor()
        sql='INSERT INTO {}(Title,Date,Author,TotalRead,Body) values(%s,%s,%s,%s,%s)'.format(tablename)
        try:
            cursor.execute(sql,(Title,Date,Author,TotalRead,Body))
            db.commit()
        except:
            db.rollback()
            # print("insertwrong")

    for i in range(1,16):
        print("longding page",i)
        main(i)
    db.close()

if __name__ == "__main__":
    host=input("Please input your host name.(localhost)\n")
    user=input("Please input your user name.(root)\n")
    password=input("Please input your password.\n")
    port=int(input("Please input a port you need(3306).\n"))
    connect(host=host,user=user,password=password,port=port)