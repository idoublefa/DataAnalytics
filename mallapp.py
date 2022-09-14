import streamlit as st
import numpy as np
import pandas as pd

st.header("K Means Clustering")
st.write(pd.DataFrame("mall_customer.csv"))

features = ['Annual_Income_(k$)', 'Spending_Score']
X = df[features]

step_size = 0.01

x_min, x_max = min(X.iloc[:,0]) - 1, max(X.iloc[:,0]) + 1
y_min, y_max = min(X.iloc[:,1]) - 1, max(X.iloc[:,1]) + 1
x_values, y_values = np.meshgrid(np.arange(x_min,x_max,step_size), np.arange(y_min,y_max,step_size))

predictions = kmeans.predict(np.c_[x_values.ravel(), y_values.ravel()])
predictions = predictions.reshape(x_values.shape)
st.figure(figsize=(8,6))
st.imshow(predictions, interpolation='nearest', extent=(x_values.min(), x_values.max(), y_values.min(), y_values.max()), 
           cmap=plt.cm.Spectral, aspect='auto', origin='lower')

st.scatter(X.iloc[:,0],X.iloc[:,1], marker='o', facecolors='grey',edgecolors='w',s=30)
centroids = kmeans.cluster_centers_
st.scatter(centroids[:,0], centroids[:,1], marker='o', s=200, linewidths=3, 
           color='k', zorder=10, facecolors='black')
st.show()
