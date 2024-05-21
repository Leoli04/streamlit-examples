import streamlit as st


st.set_page_config(layout="wide")

st.write('''
- `st.set_page_config(layout="wide")` - 将应用的内容以宽屏模式呈现（默认情况下以一固定宽度的列的形式呈现）
-  `st.sidebar` - 将组件/文字/图片显示在侧边栏中
- `st.expander` - 将组件/文字/图片显示在一个可折叠的容器中
- `st.columns` - 创建表格布局（或列布局）来容纳内容
''')


st.title('How to layout your Streamlit app')
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')