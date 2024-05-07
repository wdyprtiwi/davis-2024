import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header('Tip yang diterima pada setiap harinya')

# reading the database
url = "https://raw.githubusercontent.com/wdyprtiwi/davis-2024/main/tips.csv"
data = pd.read_csv(url)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Scatter plot with day against tip
plt.plot(data['tip'], label='Tip')
plt.plot(data['size'], label='Size')

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Value')

# Show legend
plt.legend()

# Show plot
st.pyplot()
