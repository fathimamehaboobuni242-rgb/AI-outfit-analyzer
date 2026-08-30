import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="AI Outfit Analyzer",
    page_icon="AI-OUTFIT ANALYZER"
)
st.title("AI Outfit Analyzer ")
st.write("Upload an outfit image and explore personalized fashion suggestions.")
st.subheader("Upload your outfit")
uploaded_file = st.file_uploader(
    "Choose an outfit image",
    type=["jpg", "jpeg", "png"]
)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded outfit", use_container_width=True)
    st.success("Image uploaded successfully!")
    st.subheader("Your preferences")
    budget = st.number_input(
        "Your budget (Rs)",
        min_value=500,
        max_value=100000,
        value=3000,
        step=500
    )
    occasion = st.selectbox(
        "Occasion",
        ["Casual", "College", "Party", "Wedding", "Formal"]
    )
    if st.button("Analyze Outfit"):
        st.info("AI outfit analysis will be added in the next version.")
        st.write("**Budget:** Rs", budget)
        st.write("**Occasion:**", occasion)
