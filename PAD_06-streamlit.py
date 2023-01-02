import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import time
from streamlit_option_menu import option_menu



with st.sidebar:
    selected = option_menu(
        menu_title='Main Menu', # wymagane
        options = ['Ankieta', 'Staty'], # wymagane
        default_index=0
    )

if selected == 'Ankieta':
    st.title("Ankieta")
    firstname = st.text_input("Podaj swoje imię:", "Imię")
    lastname = st.text_input("Podaj swoje nazwisko:", "Nazwisko")
    if st.button("Zapisz"):
        result = firstname.title() + " " + lastname.title() + " - pomyślnie zapisano."
        st.success(result)
if selected == 'Staty':
    st.title("Staty")
    data = st.file_uploader("Wczytaj swoje dane", type=['csv'])
    if data is not None:
        with st.spinner("Proszę czekać..."):
            time.sleep(4)
            st.success("Dane zostały wczytane!")
        df = pd.read_csv(data)
        st.dataframe(df.head(10))

        st.set_option('deprecation.showPyplotGlobalUse', False)
        all_columns_names = df.columns.to_list()
        selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
        plot_data = df[selected_column_names]
        wykres = st.selectbox("Wybierz wykres:", ("Area Chart", "Line Chart"))
        if wykres == "Area Chart":
            st.area_chart(plot_data)
        else:
            st.line_chart(plot_data)
        plot_dataNN = df[selected_column_names].plot(kind='hist')
        st.write(plot_dataNN)
        st.pyplot()

        plot_dataNN = df[selected_column_names].plot(kind='box')
        st.write(plot_dataNN)
        st.pyplot()