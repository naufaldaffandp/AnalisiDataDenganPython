import streamlit as st
import pandas as pd
import plotly.express as px

# Membaca data dari file CSV
day_data = pd.read_csv('/content/day.csv')
hour_data = pd.read_csv('/content/hour.csv')

st.title('Analisis Penggunaan Sepeda')
# Pertanyaan 1: Distribusi penggunaan sepeda berdasarkan jam dan musim
st.header('Distribusi Penggunaan Sepeda Berdasarkan Jam dan Musim')
fig1 = px.box(hour_data, x='hr', y='cnt', color='season', title='Distribusi Penggunaan Sepeda Berdasarkan Jam dan Musim')
st.plotly_chart(fig1)

# Pertanyaan 2: Korelasi antara faktor cuaca dan jumlah pemakaian sepeda
st.header('Korelasi antara Faktor Cuaca dan Jumlah Pemakaian Sepeda')
corr_matrix = day_data[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
fig2 = px.imshow(corr_matrix, text_auto=True, aspect="auto", title='Korelasi antara Faktor Cuaca dan Jumlah Pemakaian Sepeda')
st.plotly_chart(fig2)
