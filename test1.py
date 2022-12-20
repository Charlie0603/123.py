import streamlit as st
st.title ("2022年最新發票兌獎程式")
st.text_input('輸入您的發票號碼')
ns = '05701942' 
n1 = '97718570'                        
n2 = ['88400675','73475574','53038222'] 
if num == ns: st.write("對中 1000 萬元！")  
if num == n1: st.write("對中 200 萬元！")
# 頭獎判斷
for i in n2:
    if num == i:
        st.write("對中 20 萬元！")   
        break
    if num[-7:] == i[-7:]:
        st.write("對中 4 萬元！")   
        break
    if num[-6:] == i[-6:]:
        st.write("對中 1 萬元！")    
        break
    if num[-5:] == i[-5:]:
        st.write("對中 4000 元")    
        break
    if num[-4:] == i[-4:]:
        st.write("對中 1000 元！")   
        break
    if num[-3:] == i[-3:]:
        st.write("對中 200 元！")    
        break
    else:
      st.write("再接再厲下次加油")
      break
