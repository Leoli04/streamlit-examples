

import streamlit as st

st.title('st.form')

with st.expander('about this app'):
    st.write('''
    `st.form` 创建一个将内容组合起来的表单，并且带有一个 "Submit" 提交按钮。
    通常情况下，当用户与组件交互的时候，Streamlit 应用就会重新运行一遍。
    表单是是一个视觉上将元素和组件编组的容器，并且应当包含一个提交按钮。在此之中，用户可以与一个或多个组件进行任意次交互都不会触发重新运行。直到最后提交按钮被按下时，所有表单内组件的数值会一次性更新并传给 Streamlit。
    你可以使用 `with` 语句来向表单对象添加内容（推荐），或者也可以将其作为一个对象直接调用其对象方法（即首先将表单组件存入一个变量，随后调用该变量的 Streamlit 方法）。可见样例应用。
    表单有一些限制：
    - 所有表单都应当包含一个 `st.form_submit_button` 对象
    - `st.button` 和 `st.download_button` 将无法在表单中使用
    - 表单能够出现在你应用的任何地方（包括侧边栏、列等等），唯独不能嵌入另一个表单之中
    更多有关表单的信息，详见我们的 博客帖。
    ''')

st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')

else:
    st.write('☝️ Place your order!')

# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)