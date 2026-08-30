import streamlit as st
from PIL import Image
st.set_page_config(page_title="AI Outfit Analyzer")
st.title("AI Outfit Analyzer")
st.write("Upload an outfit image and get suggestions for creating your outfit.")
st.header("Upload your outfit idea")
uploaded_file = st.file_uploader(
    "Choose an outfit image",
    type=["jpg", "jpeg", "png"]
)
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded outfit", use_container_width=True)
    st.success("Image uploaded successfully.")
    st.header("Your preferences")
    budget = st.number_input(
        "Your budget (Rs.)",
        min_value=500,
        value=3000,
        step=500
    )
    occasion = st.selectbox(
        "What is the occasion?",
        ["Casual", "College", "Party", "Wedding", "Formal"]
    )
    measurements = st.text_input(
        "Enter your measurements",
        placeholder="Example: Bust 34, Waist 28, Hip 36"
    )
    if st.button("Analyze Outfit"):
        st.header("Suggestions")
        st.write("Occasion:", occasion)
        st.write("Budget: Rs.", budget)
        if measurements:
            st.write("Measurements:", measurements)
        st.write("Fabric suggestions will be added using AI.")
        st.write("Colour and style suggestions will be added using AI.")
        st.write("Suitable tailors and designers will be suggested in the next version.")
