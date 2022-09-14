import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_csv("mall_customer.csv")
st.header("K Means Clustering")
st.write(data)

st.area_chart(data)
