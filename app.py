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
    st.image(
        image,
        caption="Uploaded outfit",
        use_container_width=True
    )
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
    st.subheader("Your measurements")
    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=220,
        value=160
    )
    bust = st.number_input(
        "Bust (inches)",
        min_value=20,
        max_value=60,
        value=34
    )
    waist = st.number_input(
        "Waist (inches)",
        min_value=20,
        max_value=60,
        value=28
    )
    hip = st.number_input(
        "Hip (inches)",
        min_value=20,
        max_value=60,
        value=36
    )
    if st.button("Analyze Outfit"):
        st.header("Suggestions")
        st.write("Occasion:", occasion)
        st.write("Budget: Rs.", budget)
        st.write("Height:", height, "cm")
        st.write("Bust:", bust, "inches")
        st.write("Waist:", waist, "inches")
        st.write("Hip:", hip, "inches")
        st.write("Fabric suggestions will be added using AI.")
        st.write("Colour and style suggestions will be added using AI.")
        st.write("Suitable tailors and designers will be suggested next.")
else:
    st.info("Please upload an outfit image to continue.")
