# image example
import streamlit as st
from PIL import Image

# Title
st.title("Bano Qabil 2.0")

# Load image
image = Image.open("example_image.jpg")

# Display image
st.image(image, caption='Example Image', use_column_width=True)
