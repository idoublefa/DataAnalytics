import streamlit as st
import numpy as np
import pandas as pd

st.header("K Means Clustering")
st.write(pd.read_csv("mall_customer.csv"))

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

st.map('Annual_Income_(k$)','Spending_Score')
