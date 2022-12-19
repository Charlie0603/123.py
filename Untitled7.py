import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

from requests.api import patch
url1 = 'https://invoice.etax.nat.gov.tw/'
html1 = requests.get(url1)
sp = BeautifulSoup(html1.text, 'lxml')
all1 = sp.find("table", class_="etw-table-bgbox etw-tbig")
#print(all1)

tb = sp.find('span', class_='font-weight-bold etw-color-red')
st.write("特別獎:", tb.text)
#可用replace替代調文本內文字
t = sp.find_all('span', class_='font-weight-bold etw-color-red')[1]
st.write("特獎:", t.text)

head1 = sp.find("p", class_="etw-tbiggest mb-md-4")
head2 = sp.find_all("p", class_="etw-tbiggest mb-md-4")[1]
head3 = sp.find_all("p", class_="etw-tbiggest mb-md-4")[2]
st.write("頭獎:", head1.text, end="")
st.write(head2.text, end="")
st.write(head3.text)

add1 = sp.find_all("span", class_="font-weight-bold etw-color-red")
st.write("增開六獎:", add1[-1].text)
"""
td = "14872301"
tb = "37250799"
t = ["71086085", "53645821", "46626911"]
No6 = "916"
"""
a = str(input("請輸入你的發票號碼:"))
a_3 = a[-3] + a[-2] + a[-1]
headlist = [head1.text.replace("\n", ""), head2.text.replace("\n", ""), head3.text.replace("\n", "")]
while a != "":
    b = 0                       #對發票末數
    b_con = 0                   #發票連續對中號碼
    b_con1 = 0                  #連續對中的最大數
    a_3 = a[-3] + a[-2] + a[-1] #再次更新後三碼
    for i in headlist:
        #print(i)
        b = 0
        for j, k in zip(reversed(i), reversed(a)):
            if j == k:
                b = b + 1
                #print(j, k, b)
            else:
                b_con = b
                if b_con > b_con1:
                    b_con1 = b_con
                break

    #print("最高連續:", b_con1)
    headlistF = False      #判斷頭獎

    if len(a) == 8:
        for l in headlist:
            if l == a:
                print("恭喜中獎二十萬，走吧!吃點好料的!")
                headlistF = True
        if tb.text == a:
            st.write("恭喜中獎一千萬，恭喜乾爹!")
        elif t.text == a:
            st.write("恭喜中獎兩百萬，缺乾兒子嗎?")
        elif b_con1 == 7 :
           st.write("恭喜中獎4萬元~")
        elif b_con1 == 6:
            st.write("恭喜中獎一萬元~")
        elif b_con1 == 5:
            st.write("恭喜中獎四千元~")
        elif b_con1 == 4:
            st.write("恭喜中獎一千元~")
        elif b_con1 == 3 or a_3 == add1[-1].text:
            st.write("恭喜中獎兩百元~")
        elif headlistF == False:
            st.write("殘念~本次貢龜~")
    else:
        st.write("請輸入八位數的發票號碼!")
    a = str(input("再次輸入你的發票號碼(輸入空值為結束):"))
    st.write('謝謝使用，祝您中獎')
    break
