import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

st.header('Jumlah Tip')

# reading the database
url = "https://raw.githubusercontent.com/wdyprtiwi/davis-2024/main/tips.csv"
data = pd.read_csv(url)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Bar chart with day against tip
plt.bar(data['day'], data['tip'])

# plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# Show plot
st.pyplot()


# diagram lineplot
st.header('Total Tagihan Berdasarkan Jenis Kelamin')

# draw lineplot
sns.lineplot(x="sex", y="total_bill", data=data)

st.pyplot(bbox_inches='tight')
