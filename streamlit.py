import streamlit as st
import pandas as pd
import numpy as np
st.logo("photo.jpg",size="large")
st.title("MyAPP")
st.divider()
a= pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
st.sidebar.write("Hello")
st.sidebar.divider()
mean = a.mean()
mean

c=st.container(border=25)
c.write("This is container")
st.write("The End!")