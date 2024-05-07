import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header('Hari yang Paling Banyak Menerima Tip')
# Bar chart with day against tip
plt.bar(data['day'], data['tip'])

plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# Show legend
plt.legend()

# Show plot
st.pyplot()
