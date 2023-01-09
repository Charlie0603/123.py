import streamlit as st
import requests
#rom bs4 import BeautifulSoup
import re
#import requirements
import setup.sh

from requests.api import patch
url1 = 'https://invoice.etax.nat.gov.tw/'
html1 = requests.get(url1)
sp = BeautifulSoup(html1.text, 'lxml')
all1 = sp.find("table", class_="etw-table-bgbox etw-tbig")

tb = sp.find('span', class_='font-weight-bold etw-color-red')
st.write("特別獎:", tb.text)
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

st.balloons()
st.sidebar.image("雲端發票.JPG")
st.sidebar.title("電子發票指利用網際網路或其他電子方式，開立、傳輸或接收的統一發票。 它包含雲端發票及電子發票證明聯。")
st.title ("2022年最新發票兌獎程式")
st.image("最新發票號碼.jpg")
num=st.text_input('輸入您的發票號碼')
ns = '11174120' 
n1 = '59276913'                        
n2 = ['18079936','20591738','64500205']
if num == ns: st.success("對中 1000 萬元！")
if num == ns: st.image("恭喜中獎.jpg")
if num == n1: st.success("對中 200 萬元！")
if num == n1: st.image("恭喜中獎.jpg")
if num[-3:] == ns[-3:]: st.warning("注意特別獎喔!")
if num[-3:] == n1[-3:]: st.warning("注意特獎喔!")


for i in n2:

    if num == i:
        st.success("對中 20 萬元！")
        st.image("恭喜中獎.jpg") 
        break
    elif num[-7:] == i[-7:]:
        st.success("對中 4 萬元！")
        st.image("恭喜中獎.jpg")
        break
    elif num[-6:] == i[-6:]:
        st.success("對中 1 萬元！")
        st.image("恭喜中獎.jpg")
        break
    elif num[-5:] == i[-5:]:
        st.success("對中 4000 元")
        st.image("恭喜中獎.jpg")
        break
    elif num[-4:] == i[-4:]:
        st.success("對中 1000 元")
        st.image("恭喜中獎.jpg")
        break
    elif num[-3:] == i[-3:]:
        st.success("對中 200 元")
        st.image("恭喜中獎.jpg")
        break

