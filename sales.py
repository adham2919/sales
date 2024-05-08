import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv("Sales_Store_Preprocessed.csv")
df

st.metric(label="Total Sales in M$" , value=(df["Sales"]. sum() / 1000000). round (3))

st.header('relation between sales and ship mode ')
fig=px.histogram(data_frame=df,x="Ship Mode",y="Sales")
st.plotly_chart(fig)

st.header("bar plot ")

fig_1=px.bar(data_frame=df,x="Product Name",y="Sales")
st.plotly_chart(fig_1)


