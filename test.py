import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CONNECTION
conn = st.connection("mydb", type="sql", autocommit=True)

# QUERY
df = conn.query('SELECT EnglishPromotionName, StartDate, EndDate, MaxQty from dimpromotion limit 10;', ttl=600)

st.table(df)
