import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

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