import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(page_title="Enhanced Streamlit App", layout="wide")

# Background image and styling CSS
st.markdown(
    """
    <style>
    /* Background Image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1521747116042-5a810fda9664");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f0f0f0; /* Light color for default text */
    }

    /* Navigation Bar */
    .navbar {
        display: flex;
        justify-content: center;
        background-color: rgba(0, 0, 0, 0.75);
        padding: 10px;
        border-radius: 8px;
    }
    .navbar a {
        color: #ffffff;
        padding: 12px 20px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin: 0 10px;
        font-size: 18px;
    }
    .navbar a:hover {
        background-color: #4CAF50;
        border-radius: 5px;
    }

    /* Header Styling */
    .header {
        text-align: center;
        color: #D8BFD8; /* Light purple */
        font-size: 36px;
        font-weight: bold;
        margin-top: 20px;
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.6);
    }
    .subheader {
        text-align: center;
        color: #D3D3D3; /* Light grey */
        font-size: 18px;
        margin-bottom: 20px;
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.6);
    }

    /* Section Titles */
    .section-title {
        color: #E0FFFF; /* Light cyan */
        font-size: 28px;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
        margin-top: 30px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation Bar
st.markdown(
    """
    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#dataframe">DataFrame</a>
        <a href="#charts">Charts</a>
        <a href="#contact">Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Header and Subheader
st.markdown("<div class='header'>Welcome to My Enhanced Streamlit App</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Explore the power of Streamlit with custom HTML, CSS, and data visualizations.</div>", unsafe_allow_html=True)

# Home Section
st.markdown("<div class='section-title'>Home</div>", unsafe_allow_html=True)
st.write("Welcome to the homepage of my Streamlit app! Here, we'll showcase different sections with custom styles.")

# DataFrame Section
st.markdown("<div class='section-title'>DataFrame</div>", unsafe_allow_html=True)
df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})
st.write("### Sample DataFrame:")
st.write(df)

# Charts Section
st.markdown("<div class='section-title'>Charts</div>", unsafe_allow_html=True)
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['A', 'B', 'C']
)
st.write("### Line Chart Visualization:")
st.line_chart(chart_data)

# Contact Section
st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
st.write("For more information, please reach out to us!")

# Footer
st.markdown(
    "<p style='text-align: center; color: #ccc; margin-top: 20px;'>Thank you for visiting my Streamlit app!</p>",
    unsafe_allow_html=True
)

