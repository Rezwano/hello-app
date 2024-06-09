import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        return None

# ---- LOAD ASSETS ----
# Updated Lottie URL for a different animation (example URL)
lottie_clothing = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")

# Custom CSS for styling
st.markdown("""
    <style>
        .centered-header {
            text-align: center;
        }
        .centered-content {
            text-align: center;
            margin-bottom: 20px;
        }
        .btn-primary {
            background-color: #E74C3C;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 10%;
        }
        .btn-primary:hover {
            background-color: #D62C1A;
        }
        .form-input, .form-textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-top: 6px;
            margin-bottom: 16px;
            box-sizing: border-box;
        }
        .container {
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .column-content {
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #ccc;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        }
        .project-section {
            display: flex;
            flex-direction: row;
            align-items: center;
        }
        .project-text {
            margin-left: 10px; /* Adjusted margin */
        }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, welcome to my website 👋")
    st.title("Welcome To Igniti 🔥")
    st.write("I am so excited to be announcing our new project.")
    st.write("[Learn more >](https://www.youtube.com/watch?v=VqgUkExPvLY&t=328s)")

# ---- WHAT I DO ----
with st.container():
    st.write("___")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why You Should Choose Igniti")
        st.write("##")
        st.markdown(
            """
            <div class='column-content'>
            - Trendsetting Styles:
              Igniti is at the forefront of fashion, offering the latest trends and styles that are sure to make you stand out. Whether you're into streetwear, casual chic, or bold statements, Igniti has something for everyone.

            - **Quality and Comfort**:
              Our clothing is made from high-quality materials that ensure durability and comfort. Each piece is designed to not only look great but also feel amazing to wear, providing you with the best of both worlds.

            - **Affordable Luxury**:
              At Igniti, we believe that fashion should be accessible to everyone. Our collection offers a range of affordable options without compromising on style or quality, allowing you to look your best without breaking the bank.

            - **Unique Designs**:
              Igniti takes pride in offering unique and original designs. Our creative team is constantly innovating, ensuring that our collections are fresh, exclusive, and unlike anything else on the market.

            - **Eco-Friendly Practices**:
              We are committed to sustainability and eco-friendly practices. Igniti uses environmentally responsible methods in our production processes, helping to reduce our carbon footprint and protect the planet.

            - **Inclusive Sizing**:
              Fashion is for everyone, and Igniti celebrates diversity by offering a wide range of sizes. We aim to make everyone feel confident and stylish, regardless of body type.

            Choose Igniti and discover the perfect blend of style, comfort, and individuality. Let your fashion journey begin with us and set your wardrobe ablaze with Igniti!
            </div>
            """, unsafe_allow_html=True
        )
        st.write("<div class='centered-content'><a href='https://igniti.teemill.com' style='color: #E74C3C; font-weight: bold;'>Where to buy ></a></div>", unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_clothing, height=400, key="clothing_animation")

# Error handling message for Lottie animation
if lottie_clothing is None:
    st.error("Failed to load animation. Please check the URL.")

# ---- PROJECTS ----
with st.container():
    st.write("___")
    st.header("My Achievements")
    st.write("##")
    st.write("### Project Title")
    st.write("Description of the project, including key achievements, goals, and results.")
    project_section = st.container()
    with project_section:
        project_image, project_text = st.columns((1, 2))
        with project_image:
            st.image("images/igniti.png", caption="Project Image", width=690)
        with project_text:
            st.write(
                """
                This project showcases our dedication to quality and innovation. Here, we achieved significant milestones and set new standards in the industry. Our goals were met with outstanding success, and we continue to strive for excellence.
                """
            )
            st.markdown("[Learn more >](https://example.com)")

# ---- CONTACT ----
with st.container():
    st.write("___")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/R_Rezwan@hotmail.com.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required class="form-input">
        <input type="email" name="email" placeholder="Your email" required class="form-input">
        <textarea name="message" placeholder="Your message here" required class="form-textarea"></textarea>
        <button type="submit" class="btn-primary">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
