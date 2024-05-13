import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

conn = st.connection("mydb", type="sql", autocommit=True)
