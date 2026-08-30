import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(page_title="AI Outfit Analyzer")

st.title("AI Outfit Analyzer")

st.write(
    "Upload an outfit image and get suggestions for creating "
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

        st.header("AI Outfit Analysis")

        with st.spinner("AI is analyzing your outfit..."):

            classifier = pipeline(
                "zero-shot-image-classification",
                model="openai/clip-vit-base-patch32"
            )

            labels = [
                "dress",
                "kurti",
                "shirt",
                "skirt",
                "saree",
                "traditional outfit",
                "western outfit",
                "casual outfit",
                "formal outfit"
            ]

            results = classifier(
                image,
                candidate_labels=labels
            )

        best_result = results[0]

        st.write("Detected outfit:", best_result["label"])

        confidence = best_result["score"] * 100

        st.write(
            "AI confidence:",
            round(confidence, 2),
            "%"
        )

        st.subheader("Suggested Fabrics")

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

        st.subheader("Colour Suggestions")

        if occasion == "Wedding":
            colours = ["Maroon", "Emerald Green", "Navy Blue"]
        elif occasion == "Party":
            colours = ["Black", "Wine", "Royal Blue"]
        else:
            colours = ["Beige", "Pastel Blue", "Lavender"]

        for colour in colours:
            st.write("-", colour)

        st.subheader("Your Measurements")

        st.write("Height:", height, "cm")
        st.write("Bust:", bust, "inches")
        st.write("Waist:", waist, "inches")
        st.write("Hip:", hip, "inches")

    st.divider()

    st.header("Find a Tailor or Designer")

    creator_type = st.radio(
        "I am looking for:",
        ["Tailors", "Designers"]
    )

    if creator_type == "Tailors":

        creators = [
            {
                "name": "Amina Tailoring",
                "speciality": "Custom dresses and traditional wear",
                "location": "Kozhikode",
                "rating": 4.8
            },
            {
                "name": "Nila Home Tailors",
                "speciality": "Custom stitching and alterations",
                "location": "Malappuram",
                "rating": 4.7
            }
        ]

    else:

        creators = [
            {
                "name": "Ziya Designs",
                "speciality": "Custom outfit design",
                "location": "Kozhikode",
                "rating": 4.9
            },
            {
                "name": "Noor Studio",
                "speciality": "Modern and traditional designs",
                "location": "Malappuram",
                "rating": 4.7
            }
        ]

    for creator in creators:

        st.subheader(creator["name"])

        st.write("Speciality:", creator["speciality"])
        st.write("Location:", creator["location"])
        st.write("Rating:", creator["rating"], "/ 5")

        if st.button(
            "View Profile",
            key=creator["name"]
        ):
            st.write("Creator profile")
            st.write("Name:", creator["name"])
            st.write("Speciality:", creator["speciality"])
            st.write("Location:", creator["location"])
            st.write("Rating:", creator["rating"], "/ 5")

        st.divider()

else:

    st.info("Please upload an outfit image to continue.")
