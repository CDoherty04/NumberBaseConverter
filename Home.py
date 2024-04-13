"""
Created by: Charlie Doherty and Jonathan Gott
HackKU - University of Kansas
4/12/2024

In the terminal, input "streamlit run Home.py" to run the program
"""
from baseconverter import base_converter
import streamlit as st

if __name__ == "__main__":

    st.set_page_config(layout="wide", page_title="Base Converter")

    # Write the Title at the top of the page
    st.markdown("<p style='text-align: right;'>Created by Charlie Doherty and Jonathan Gott</p>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: right;'>University of Kansas</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: right;'>April 12th, 2024</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>NUMBER BASE CONVERTER</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Hello, welcome to our base conversion project for HackKU 2024!</h4>",
                unsafe_allow_html=True)

    # Break line
    st.markdown("***")

    # Inputs for conversion
    in_base = st.number_input("Select a base to convert from:", 2, 10, value=10)
    out_base = st.number_input("Select a base to convert to:", 2, 10, value=2)
    in_number = st.number_input("Enter a number to translate to:", max_value=1000000000, step=1, value=73)

    st.markdown("***")

    col1, col2 = st.columns(2)

    # If the base is the same, return the same number
    if in_base == out_base:
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Base {in_base}: {in_number}</h4>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Base {out_base}: {in_number}</h4>", unsafe_allow_html=True)

    else:
        # Get the output number through the base_converter
        out_number = base_converter(in_base, out_base, in_number)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Base {in_base}: {in_number}</h4>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Base {out_base}: {out_number}</h4>", unsafe_allow_html=True)

