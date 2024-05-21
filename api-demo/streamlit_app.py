import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
from datetime import time, datetime


st.header('st.button')

if st.button('say hello'):
    st.write('why hello there')
else:
    st.write('goodbye')

st.markdown("---")

st.header('st.write')

# 样例 1
st.write('Hello, *World!* :sunglasses:')

st.markdown("***")

# 样例 2
st.write(1234)

st.markdown("___")

# 样例 3
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

st.markdown("---")

# 样例 4
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.markdown("---")

# 样例 5
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.markdown("---")

st.header('st.slider')

st.code("Display a slider widget to select items from a list.\n"
        "This also allows you to render a range slider by passing a two-element tuple or list as the value.\n"
        "The difference between st.select_slider and st.slider is that select_slider accepts any datatype and takes an iterable set of options,\n "
        "while st.slider only accepts numerical or date/time data and takes a range as input.\n"
        "st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility='visible')\n"
        )

#样例1
st.subheader('slider')
age =st.slider('How old are you?', 0, 130, 25)
st.write("I'm " ,age ,"years old")

# 样例 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 样例 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# 样例 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="YYYY/MM/DD - hh:mm")
st.write("Start time:", start_time)

st.markdown("---")

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.markdown("---")

st.header('st.selectbox')

st.write("`st.selectbox` 显示一个选择组件")

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

st.markdown("---")

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

st.markdown("---")

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

st.markdown("---")

st.header('st.latex')

st.write("`st.latex` 以 LaTeX 语法显示数学公式")

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.markdown("---")
st.title('st.secrets')
st.write("`st.secrets` 使你可以存储一些秘密信息，例如 API 密钥、数据库密码等其他验证信息。")

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

st.markdown("---")

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')

