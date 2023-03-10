import streamlit as st
from PIL import Image
from streamlit.source_util import get_pages
from Pages import About

st.set_page_config(
    page_title="JK Lakshmi Cement",
    page_icon="👋",
)

# Define the logo and text
logo = "pic.png"

# Create a two-column layout
col1, col2 = st.columns([1, 2.4])

# Display the logo in the first column
with col1:
    st.image(logo, use_column_width=True)

# Display the text in the second column
with col2:
    st.title("Face Detection and Recognition JK Lakshmi Cement")
