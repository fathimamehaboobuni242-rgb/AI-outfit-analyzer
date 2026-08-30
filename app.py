import streamlit as st
from PIL import Image
st.set_page_config(page_title="AI Outfit Analyzer")
st.title("AI Outfit Analyzer")
st.write(
    "Upload an outfit idea and get suggestions for creating "
    "a similar outfit."
)
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
        st.header("Outfit Information")
        st.write("Occasion:", occasion)
        st.write("Budget: Rs.", budget)
        st.write("Height:", height, "cm")
        st.write("Bust:", bust, "inches")
        st.write("Waist:", waist, "inches")
        st.write("Hip:", hip, "inches")
        st.header("Suggested Fabrics")
        if occasion == "Wedding":
            fabrics = ["Silk", "Georgette", "Satin"]
        elif occasion == "Party":
            fabrics = ["Georgette", "Chiffon", "Satin"]
        elif occasion == "Formal":
            fabrics = ["Linen", "Cotton", "Crepe"]
        else:
            fabrics = ["Cotton", "Linen", "Rayon"]
        for fabric in fabrics:
            st.write("-", fabric)
        st.header("Colour Suggestions")
        if occasion == "Wedding":
            colours = ["Maroon", "Emerald Green", "Navy Blue"]
        elif occasion == "Party":
            colours = ["Black", "Wine", "Royal Blue"]
        else:
            colours = ["Beige", "Pastel Blue", "Lavender"]
        for colour in colours:
            st.write("-", colour)
        st.header("Tailor and Designer Matching")
        st.write(
            "The next stage will match your requirements with "
            "suitable tailors and designers based on their skills, "
            "ratings and location."
        )
else:
    st.info("Please upload an outfit image to continue.")
