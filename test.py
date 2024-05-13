import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="sakila",
        cursorclass=pymysql.cursors.DictCursor
    )

def get_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT c.customer_id as cus_id, count(r.rental_id) as jml_order FROM customer c join rental r on c.customer_id = r.customer_id group by c.customer_id order by jml_order")
    data = cursor.fetchall()
    conn.close()
    return data

data = get_data()

st.write("Data dari database:")
st.write(data)
