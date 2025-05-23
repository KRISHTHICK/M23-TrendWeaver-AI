import streamlit as st
from PIL import Image
import random
import json
from fpdf import FPDF
import matplotlib.pyplot as plt

# Set up the Streamlit page configuration
st.set_page_config(page_title="TrendWeaver AI", layout="wide")
st.title("\U0001F457 TrendWeaver AI – Fabric Pattern Classifier & Outfit Composer")

# Load pattern suggestions from JSON file
pattern_ideas = {
    "floral": ["Flowy skirt", "Lace top", "Strappy sandals"],
    "striped": ["Navy blazer", "White pants", "Loafers"],
    "solid": ["Denim jacket", "Graphic tee", "Sneakers"],
    "polka dots": ["A-line dress", "Cardigan", "Ballet flats"],
    "checked": ["Plaid shirt", "Denim jeans", "Boots"]
}

pattern_types = list(pattern_ideas.keys())

# Simulate pattern prediction (replace with actual ML model if available)
def predict_pattern(image):
    return random.choice(pattern_types)

# Generate PDF Lookbook
def generate_lookbook(pattern, suggestions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Lookbook for {pattern} Patterns", ln=True)
    pdf.ln()
    for item in suggestions:
        pdf.cell(200, 10, f"- {item}", ln=True)
    path = "lookbook.pdf"
    pdf.output(path)
    return path

# Descriptions for patterns
descriptions = {
    "floral": "Often used in spring and summer, floral patterns bring freshness and femininity.",
    "striped": "A versatile design used in both casual and formal wear for a clean look.",
    "solid": "Timeless and universal. Perfect for pairing with bold accessories or prints.",
    "polka dots": "Playful and retro. A pattern often seen in vintage styles.",
    "checked": "Common in winter fashion and associated with flannel or tartan designs."
}

# Upload multiple images
uploaded_images = st.file_uploader("Upload up to 3 outfit/fabric images", type=["jpg", "png"], accept_multiple_files=True)

# Initialize pattern counter in session
if 'pattern_count' not in st.session_state:
    st.session_state.pattern_count = {}

if uploaded_images:
    for img_file in uploaded_images:
        img = Image.open(img_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=True)

        predicted = predict_pattern(img)
        st.success(f"\U0001F985 Detected Pattern: **{predicted.upper()}**")

        st.session_state.pattern_count[predicted] = st.session_state.pattern_count.get(predicted, 0) + 1

        st.info(f"\U0001F4A1 About `{predicted}`: {descriptions.get(predicted, 'No info')}")

        st.subheader("\U0001F45A Suggested Outfit Items")
        outfit = pattern_ideas[predicted]
        st.write(", ".join(outfit))

        path = generate_lookbook(predicted, outfit)
        with open(path, "rb") as f:
            st.download_button("\U0001F4E5 Download Lookbook PDF", f, file_name="lookbook.pdf")

# Display bar chart of pattern frequency
if st.session_state.pattern_count:
    st.subheader("\U0001F4CA Most Common Patterns (this session)")
    fig, ax = plt.subplots()
    ax.bar(st.session_state.pattern_count.keys(), st.session_state.pattern_count.values(), color='salmon')
    ax.set_ylabel("Detected Count")
    st.pyplot(fig)
