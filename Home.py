import streamlit as st
import base64
import os

def set_bg():
    with open("bg_image3.png", 'rb') as f:
        bg_data = f.read()
    encoded = base64.b64encode(bg_data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: top;
            background-attachment: fixed;
            font-family: 'Segoe UI', 'Arial', 'sans-serif';
            min-height: 100vh;
        }}

        .title-text {{
            text-align: center;
            font-size: 6rem;
            font-weight: bold;
            color: #FAFAD2;
            margin-top: 50px;
        }}

        .slogan-text {{
            text-align: center;
            font-size: 2rem;
            color: #f5f5dc;
            margin-bottom: 50px;
        }}

        .content-box {{
            background: rgba(255, 255, 255, 0.15);
            border-radius: 16px;
            padding: 1.8rem;
            color: #ffffff;
            backdrop-filter: blur(12px);
            height: auto;
            width: 100%;
            box-sizing: border-box;
        }}

        .content-box h3, .content-box h4 {{
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: #ffffdd;
        }}

        .content-box p {{
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 0.8rem;
            color: #f0f0f0;
        }}

        .content-box ul {{
            font-size: 1.05rem;
            line-height: 1.6;
            padding-left: 1.2rem;
            margin: 0;
        }}

        .content-box li {{
            margin-bottom: 0.5rem;
        }}

        .video-box {{
            height: 360px;
            width: 100%;
            border-radius: 12px;
            overflow: hidden;
        }}

        video {{
            width: 90%;
            height: 90%;
            object-fit: cover;
            border-radius: 12px;
        }}

        /* Hide Sidebar */
        [data-testid="stSidebar"] {{
            display: none;
        }}

        button {{
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(6px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            color: white;
            font-weight: 500;
            padding: 10px 16px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            
        }}

        button:hover {{
            background-color: rgba(255, 255, 255, 0.2);
            border-color: rgba(255, 255, 255, 0.6);
            transform: scale(1.03);
        }}

        div.stRadio > label > div > p{{
        font-size : 20px;
        color:#FAFAD2;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set page config and background
st.set_page_config(page_title="MudraGuide 🖐️", layout="wide")
set_bg()

# Title and tagline
st.markdown("<div class='title-text'>🌟 MudraGuide 🖐️</div>", unsafe_allow_html=True)
st.markdown("<div class='slogan-text'>\"Your healing begins at your fingertips.\"</div>", unsafe_allow_html=True)

# ---------- Top Section ----------
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown(
        """
        <div class="content-box">
            <h3>🌿 Mudra Guide</h3>
            <p>Mudra Guide is committed to guiding individuals toward better health and well-being using authentic, traditional, and natural practices.</p>
            <p>Our app is designed to be your companion in exploring effective wellness methods rooted in the science of mudras—a time-honored technique used in yoga and Ayurveda.</p>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    video_path = "v1.mp4"
    video_bytes = open(video_path, "rb").read()
    video_base64 = base64.b64encode(video_bytes).decode("utf-8")
    st.markdown(f"""
        <div class="video-box">
            <video autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    """, unsafe_allow_html=True)

# ---------- Second Row ----------
st.markdown(" ")
col3, col4 = st.columns([1, 1], gap="large")
with col3:
    st.markdown(
        """
        <div class="content-box">
            <h4>🤲 What Are Mudras?</h4>
            <p>Mudras are hand gestures or placements used in yoga and Ayurveda to channel the body's energy flow, balance elements, and promote physical and mental health.</p>
            <p>Each finger represents a specific element, and by touching them in certain combinations, you can influence your body's internal equilibrium.</p>
        </div>
        """, unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="content-box">
            <h4>🧘‍♀️ How Mudhra Solutions Can Help You</h4>
            <ul>
                <li><strong>Personalized Mudra Recommendations:</strong> Get suggestions based on your symptoms or health goals.</li>
                <li><strong>Science-Backed Guidance:</strong> Insights rooted in ancient yogic texts and modern research.</li>
                <li><strong>Step-by-Step Instructions:</strong> Learn mudras easily with clear visuals and directions.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

# ---------- Final CTA ----------
st.markdown(
    """
    <div class="content-box" style="margin-top: 2rem; text-align: center;">
        <h3>✨ Start Your Journey</h3>
        <p>Begin by selecting your health concern and explore personalized mudra routines!</p>
        <p>Discover the harmony of body and mind with guidance from <strong>Mudhra Health Solutions</strong>.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(" ")
st.markdown(" ")

# ---------- Start Healing Button ----------
col_start, col_spacer, col_choice = st.columns([2, 2, 2])
with col_spacer:
    if st.button("🚀 Start Healing Now", use_container_width=True):
        st.session_state.show_options = True

if st.session_state.get("show_options", False):
    with col_choice:
        healing_type = st.radio(
            "Choose the type of healing you want to explore:",
            ["Mental", "Physical"],
            horizontal=True
        )

        if healing_type == "Physical":
            st.success("Redirecting to Physical Healing Page...")
            st.switch_page("pages/physical.py")  # Ensure physical.py is inside the 'pages/' folder
        elif healing_type == "Mental":
            st.info("Mental Healing coming soon... 🧠✨")
