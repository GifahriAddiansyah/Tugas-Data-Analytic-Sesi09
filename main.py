import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("data_mancanegara.xlsx", sheet_name="Gender Age")
data2 = pd.read_excel("data_mancanegara.xlsx", sheet_name="Usia")
kebangsaan = data["Kebangsaan"].unique()

test = st.sidebar.radio("Navigation", ['Home','Tabel Diagram','Pie Chart'])


st.title('Tugas Sesi 09')
st.subheader('Mohamad Gifahri Addiansyah - 4IFP - 240434005')
st.subheader('Vinny Lindawaty - 4IFP - 240434007')

if st.button( 'Klik saya' , help = "Klik untuk melihat perubahan teks" ): 
    st.write( 'Selamat datang di Kelompok 1' ) 
else : 
    st.write( 'Hai!' )

if test == "Home":

    st.subheader("DISTRIBUSI WISATAWAN MANCANEGARA MENURUT JENIS KELAMIN 'BULAN JANUARI TAHUN 2024")
    st.table(data) 

    st.subheader("DISTRIBUSI WISATAWAN MANCANEGARA MENURUT KELOMPOK USIA 'BULAN JANUARI TAHUN 2024")
    st.table(data2)  

if test == "Tabel Diagram":
    perempuan = "Perempuan"  
    laki = "Laki-Laki"
    
    data.dropna(axis=0, inplace=True)
    kebangsaan = data['Kebangsaan']

    x = np.arange(len(kebangsaan))
    width = 0.35

    fig, ax = plt.subplots(figsize=(40, 7))

    lklk = ax.bar(x - width/2, data['Laki-Laki'], width, label='Laki-laki', color='steelblue')
    prpn = ax.bar(x + width/2, data['Perempuan'], width, label='Perempuan', color='lightcoral')

    ax.set_title('Data Distribusi Wisatawan Menurut Jenis Kelamin', size=16)
    ax.set_ylabel('Jumlah Persentase', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(kebangsaan, size=12)
    ax.legend(fontsize=14)

    plt.show()

    st.subheader("Data Distribusi Wisatawan Menurut Jenis Kelamin Laki - laki")
    fig, ax = plt.subplots(figsize=(30, 7))
    ax.bar(data["Kebangsaan"], data[laki], color="steelblue")
    ax.set_title("Data Distribusi Wisatawan Menurut Jenis Kelamin Laki - laki")
    ax.set_xlabel("Kebangsaan")
    ax.set_ylabel("Laki-laki")
    st.pyplot(fig)

    st.subheader("Data Distribusi Wisatawan Menurut Jenis Kelamin Perempuan")
    fig, ax = plt.subplots(figsize=(30, 7))
    ax.bar(data["Kebangsaan"], data[laki], color="lightcoral")
    ax.set_title("Data Distribusi Wisatawan Menurut Jenis Kelamin Perempuan")
    ax.set_xlabel("Kebangsaan")
    ax.set_ylabel("Laki-laki")
    st.pyplot(fig)

    st.subheader("Data Distribusi Wisatawan Menurut Jenis Kelamin Usia")
    fig, ax = plt.subplots(figsize=(30, 7))
    ax.bar(data2["Kebangsaan"], data2['<25'], color="red")
    ax.set_title("Data Distribusi Wisatawan Menurut Usia")
    ax.set_xlabel("Kebangsaan")
    ax.set_ylabel("Laki-laki")
    st.pyplot(fig)

if test == "Pie Chart": 
    st.subheader("Data Distribusi Wisatawan Menurut Jenis Kelamin Perempuan")
    data = pd.read_excel("data_mancanegara.xlsx", sheet_name="Gender Age")

    if 'Kebangsaan' in data.columns:
        
        kebangsaan = data['Kebangsaan']
        perempuan = data['Perempuan']
        laki = data['Laki-Laki']

        # Membuat pie chart
        fig, ax = plt.subplots()
        ax.pie(
            perempuan,
            labels=kebangsaan,
            # autopct='%1.1f%%',
            # startangle=90,
            colors=['steelblue','lightcoral']  # Warna untuk laki-laki dan perempuan
        )
        ax.axis('equal')  # Membuat pie chart berbentuk lingkaran sempurna
        st.pyplot(fig)

        fig, ax = plt.subplots()
        ax.pie(
            laki,
            labels=kebangsaan,
            # autopct='%1.1f%%',
            # startangle=90,
            colors=['steelblue','lightcoral']  # Warna untuk laki-laki dan perempuan
        )
        ax.axis('equal')  # Membuat pie chart berbentuk lingkaran sempurna
        st.pyplot(fig)