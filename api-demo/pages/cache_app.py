import streamlit as st
import numpy as np
import pandas as pd
from time import time

with st.expander('About this app'):
    st.write('''
    `st.cache` 使得你可以优化 Streamlit 应用的性能。
    Streamlit 提供了一个缓存机制，使你的应用即便是在从互联网加载数据、操作大数据集或者进行大开销的计算时仍可以保持高性能。这主要通过 `@st.cache` 装饰器来实现。
    当你用 `@st.cache` 装饰器标记一个函数时，它将告诉 Streamlit 在该函数执行前需要做如下一些检查：
    - 函数的输入参数是否发生了变化
    - 函数中使用的外部变量是否发生了变化
    - 函数的主体是否发生了变化
    - 函数中用到的所有函数的主体是否发生了变化
    - 如果以上任意一项不满足，即 Streamlit 第一次见到这四者的这种顺序组合时，它将会执行这个函数，并且将结果存储于本地缓存中。然后当下一次该带缓存的函数被调用时，如果以上四项均未发生改变，则 Streamlit 会直接跳过函数执行，而直接从缓存中调用先前的结果并返回。
    Streamlit 通过哈希散列来追踪这些条件的变化。你可以把缓存当成一种存储在内存之中的键值对结构，其中上述四项总和的哈希值为键，以函数实际返回的引用为值。
    ''')


st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache_data
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)