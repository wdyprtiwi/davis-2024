import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# reading the database
url = "https://raw.githubusercontent.com/wdyprtiwi/davis-2024/main/tips.csv"
data = pd.read_csv(url)

# Scatter plot with day against tip
fig = px.scatter(data, x='day', y='tip', title='Scatter Plot', labels={'day': 'Day', 'tip': 'Tip'})

# Show plot
st.plotly_chart(fig)
