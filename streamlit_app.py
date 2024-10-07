import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.title("Hallo")
st.write("Saya menggunakan Streamlit untuk menampilkan grafik")

# Input data dari pengguna
name = st.text_input("Masukkan nama Anda:")
nim = st.text_input("Masukkann nim Anda")

if st.button("Tampilkan Informasi"):
    st.write(f"Nama: {name}")
    st.write(f"Nim: {nim}")
# Bagian untuk memuat dan menampilkan dataset
uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

# Cek apakah ada file yang diunggah
if uploaded_file is not None:
    # Membaca file CSV yang diunggah
    df_sales = pd.read_csv(uploaded_file, encoding="iso-8859-1")
    
    # Menampilkan data dari file CSV
    st.write("Dataframe dari file CSV yang diunggah:")
    st.write(df_sales)
    
    # Memeriksa apakah kolom yang dibutuhkan ada dalam file CSV
    if 'PRODUCTLINE' in df_sales.columns and 'ORDERDATE' in df_sales.columns and 'QUANTITYORDERED' in df_sales.columns:
        
        # Mendapatkan unique product lines
        product_lines = df_sales["PRODUCTLINE"].unique()
        
        # Membuat DataFrame dengan ORDERDATE sebagai index dan product lines sebagai kolom
        df_productline_sales = df_sales.pivot_table(values='QUANTITYORDERED', index='ORDERDATE', columns='PRODUCTLINE', fill_value=0)
        
        # Menampilkan DataFrame yang dihasilkan
        st.write("Data penjualan berdasarkan product line dan tanggal order:")
        st.write(df_productline_sales)
        
        # Membuat Area Chart
        st.title("Area Chart")
        st.area_chart(df_productline_sales)

        # Membuat Line Chart
        st.title("Area Chart")
        st.line_chart(df_productline_sales)

        # Membuat Bar Chart
        st.title("Bar Chart")
        st.bar_chart(df_productline_sales)
        
    else:
        st.write("File CSV tidak memiliki kolom yang sesuai: 'PRODUCTLINE', 'ORDERDATE', atau 'QUANTITYORDERED'.")
else:
    st.write("Silakan unggah file CSV untuk melihat data dan grafiknya.")
