import streamlit as st
import time

st.title('st.progress')



with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
     st.write("`st.progress` 显示一个随着循环进度更新的进度条。")

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()