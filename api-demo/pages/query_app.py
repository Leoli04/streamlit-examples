import streamlit as st

st.title('st.query_params')

with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.\n"
           "访问：http://localhost:8501/query_app/?firstname=Jack&surname=Beanstalk 查看效果")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://localhost:8501/`
such that it becomes
`http://localhost:8501/?firstname=Jack&surname=Beanstalk`
''')


# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.query_params.to_dict())


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

params = st.query_params

if params:
    firstname = st.query_params['firstname']
    surname = st.query_params['surname']

    st.write(f'Hello **{firstname} {surname}**, how are you?')

else:
    st.write("params is empty")