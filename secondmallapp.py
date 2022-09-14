import streamlit as st
import numpy as np
import pandas as pd

st.header("K Means Clustering")
st.write(pd.read_csv("mall_customer.csv"))

st.area_chart("mall_customer.csv")
