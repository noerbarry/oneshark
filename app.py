import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Fungsi untuk membaca file CSV dengan delimiter kustom
def read_csv(file):
    data = pd.read_csv(file, delimiter=';')
    return data

# Fungsi untuk membuat Donut Chart menggunakan Plotly
def create_donut_chart(data):
    fig = px.pie(data, names='Labels', values='qty dialog', hole=0.5)
    return fig

# Fungsi untuk membuat Bar Chart menggunakan Plotly
def create_bar_chart(data):
    fig = px.bar(data, x='Labels', y='qty dialog')
    return fig

# Tampilan aplikasi web menggunakan Streamlit
def main():
    st.set_page_config(layout="wide")
    st.title('Aplikasi Data Visualization & Dashboard')
    st.write('Unggah file CSV untuk memvisualisasikan datanya & hanya bisa 2 kolom : label & qty')

    # Upload file CSV
    uploaded_file = st.sidebar.file_uploader('Unggah file CSV', type=['csv'])

    if uploaded_file is not None:
        data = read_csv(uploaded_file)
        st.write('Data yang diunggah:')
        st.write(data.head())

        # Tampilkan Donut Chart
        st.subheader('Donut Chart')
        donut_chart_fig = create_donut_chart(data)
        st.plotly_chart(donut_chart_fig, use_container_width=True)

        # Tampilkan Bar Chart
        st.subheader('Bar Chart')
        bar_chart_fig = create_bar_chart(data)
        st.plotly_chart(bar_chart_fig, use_container_width=True)

    # Tampilkan logo
    logo_image = Image.open('logo.png')
    logo_resized = logo_image.resize((200, 200))  # Ubah ukuran sesuai kebutuhan
    st.image(logo_resized)
    st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()

