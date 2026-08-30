import streamlit as st
from PIL import Image
from transformers import pipeline
st.set_page_config(page_title="AI Outfit Analyzer")
st.title("AI Outfit Analyzer")
st.write("Upload an outfit image and get basic fashion suggestions.")
uploaded_file = st.file_uploader(
    "Upload an outfit image",
    type=["jpg", "jpeg", "png"]
)
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(
        image,
        caption="Uploaded outfit",
        use_container_width=True
    )
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
    if st.button("Analyze Outfit"):
        with st.spinner("Analyzing the outfit..."):
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
            results = classifier(image, candidate_labels=labels)
        st.subheader("AI Analysis")
        best_result = results[0]
        st.write(
            "The AI thinks this outfit is:",
            best_result["label"]
        )
        st.write(
            "Confidence:",
            round(best_result["score"] * 100, 2),
            "%"
        )
        st.subheader("Your Preferences")
        st.write("Budget: Rs.", budget)
        st.write("Occasion:", occasion)
st.subheader("Personalized Suggestions")
outfit_type = best_result["label"]
if outfit_type in ["saree", "traditional outfit", "kurti"]:
    fabrics = ["Cotton", "Silk", "Georgette"]
else:
    fabrics = ["Cotton", "Linen", "Rayon"]
if occasion == "Wedding":
    colours = ["Maroon", "Emerald Green", "Navy Blue"]
elif occasion == "Party":
    colours = ["Black", "Wine", "Royal Blue"]
elif occasion == "College":
    colours = ["Pastel Blue", "Lavender", "Beige"]
else:
    colours = ["White", "Beige", "Pastel Green"]
st.write("Outfit type:", outfit_type)
st.write("Suggested fabrics:")
for fabric in fabrics:
    st.write("-", fabric)
st.write("Suggested colours:")
for colour in colours:
    st.write("-", colour)
st.write("Budget considered: Rs.", budget)
st.subheader("Find a Tailor or Designer")
st.subheader("Find a Tailor or Designer")
st.write(
    "Discover skilled tailors and designers and explore their work."
)
creator_type = st.radio(
    "I am looking for:",
    ["Tailor", "Designer"]
)
if creator_type == "Tailor":
    tailors = [
        {
            "name": "Amina Tailoring",
            "speciality": "Custom dresses and traditional wear",
            "rating": 4.8,
            "location": "Kozhikode"
        },
        {
            "name": "Fathima Stitch Studio",
            "speciality": "Ladies wear and alterations",
            "rating": 4.6,
            "location": "Malappuram"
        },
        {
            "name": "Nila Home Tailors",
            "speciality": "Custom stitching from home",
            "rating": 4.7,
            "location": "Kozhikode"
        }
    ]
else:
    tailors = [
        {
            "name": "Ziya Designs",
            "speciality": "Custom outfit design",
            "rating": 4.9,
            "location": "Kozhikode"
        },
        {
            "name": "Noor Studio",
            "speciality": "Modern and traditional designs",
            "rating": 4.7,
            "location": "Malappuram"
        }
    ]
for creator in tailors:
    st.write("### " + creator["name"])
    st.write("Speciality:", creator["speciality"])
    st.write("Location:", creator["location"])
    st.write("Rating:", creator["rating"], "/ 5")
    if st.button(
        "View Profile",
        key=creator["name"]
    ):
        st.info(
            "Creator profile selected. "
            "Portfolio and communication features can be added here."
        )
    st.divider()
