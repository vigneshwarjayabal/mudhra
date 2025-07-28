import streamlit as st
import base64

# -------------- Set Background --------------
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

        div.stRadio > label > div > p {{
            font-size : 22px;
            color:#FAFAD2;
            font-weight: 700;
            text-align: center;
        }}

        div[role="radiogroup"] > label {{
            font-size: 20px !important;
            color: #00FFFF !important;
            font-weight: 600 !important;
            margin-right: 20px;
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
        font-weight: 600;
        }}

        div[role="radiogroup"] > label {{
        font-size: 18px !important;
        color: orange !important; /* Change to any color you like */
        font-weight: 600 !important;
        margin-right: 15px;
        }}

        .info-text {{
            text-align: center;
            font-size: 2rem;
            color: #f5f5dc;
            margin-bottom: 50px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------- Streamlit Page Config ----------
st.set_page_config(page_title="MudraGuide 🖐️", layout="wide")
set_bg()

# ---------- Language Switch ----------
if "language" not in st.session_state:
    st.session_state.language = "English"

language = st.radio("🗣️ Choose Language / மொழி தேர்ந்தெடுக்கவும்", ["English", "Tamil"], horizontal=True)
st.session_state.language = language

# ---------- TITLE & SLOGAN ----------
if st.session_state.language == "English":
    title_text = "🌟 MudraGuide 🖐️"
    slogan = "\"Your healing begins at your fingertips.\""
    guide_title = "🌿 Mudra Guide"
    guide_para1 = "Mudra Guide is committed to guiding individuals toward better health and well-being using authentic, traditional, and natural practices."
    guide_para2 = "Our app is designed to be your companion in exploring effective wellness methods rooted in the science of mudras—a time-honored technique used in yoga and Ayurveda."
else:
    title_text = "🌟 முத்திரை வழிகாட்டி 🖐️"
    slogan = "\"உங்கள் குணமாக்கல் உங்கள் விரல்களில் ஆரம்பமாகிறது.\""
    guide_title = "🌿 முத்திரை வழிகாட்டி"
    guide_para1 = "முத்திரை வழிகாட்டி பரம்பரையாக பரிமாறப்பட்ட இயற்கையான முறைகளைப் பயன்படுத்தி நலனையும் உடல்நலத்தையும் மேம்படுத்தும் நோக்குடன் உருவாக்கப்பட்டுள்ளது."
    guide_para2 = "இந்த செயலி யோகாவிலும் ஆயுர்வேதத்திலும் பரவலாக பயன்படுத்தப்படும் முத்திரைகள் என்ற பழம்பெரும் அறிவியலை அடிப்படையாகக் கொண்டு உங்கள் நலன் பயணத்திற்கு துணையாக இருக்கும்."

# ---------- RENDER TITLE & SLOGAN ----------
st.markdown(f"<div class='title-text'>{title_text}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='slogan-text'>{slogan}</div>", unsafe_allow_html=True)

# ---------- TOP SECTION ----------
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown(
        f"""
        <div class="content-box">
            <h3>{guide_title}</h3>
            <p>{guide_para1}</p>
            <p>{guide_para2}</p>
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

# ---------- SECOND ROW CONTENT BASED ON LANGUAGE ----------
if st.session_state.language == "English":
    mudra_title = "🤲 What Are Mudras?"
    mudra_para1 = "Mudras are hand gestures or placements used in yoga and Ayurveda to channel the body's energy flow, balance elements, and promote physical and mental health."
    mudra_para2 = "Each finger represents a specific element, and by touching them in certain combinations, you can influence your body's internal equilibrium."

    help_title = "🧘‍♀️ How Mudhra Solutions Can Help You"
    help_points = [
        "<strong>Personalized Mudra Recommendations:</strong> Get suggestions based on your symptoms or health goals.",
        "<strong>Science-Backed Guidance:</strong> Insights rooted in ancient yogic texts and modern research.",
        "<strong>Step-by-Step Instructions:</strong> Learn mudras easily with clear visuals and directions."
    ]
else:
    mudra_title = "🤲 முத்திரைகள் என்றால் என்ன?"
    mudra_para1 = "யோகாவிலும் ஆயுர்வேதத்திலும், முத்திரைகள் என்பது கையினால் செய்யப்படும் சைகைகள் ஆகும். இது உடலின் ஆற்றல் ஓட்டத்தை சீரமைத்து, உடல் மற்றும் மன நலனைக் கூட்ட பயன்படுகின்றன."
    mudra_para2 = "ஒவ்வொரு விரலும் ஒரு தனி தனி உறுப்பை/தத்துவத்தை குறிக்கின்றது; விரல்களை சரியான முறைப் படி பதுக்குவதால் உடலின் சமநிலையை சீராக்க முடியும்."

    help_title = "🧘‍♀️ முத்திரா ஹெல்த் தீர்வுகள் உங்களுக்கு எவ்வாறு உதவுகின்றன?"
    help_points = [
        "<strong>தனிப்பட்ட முத்திரை பரிந்துரைகள்:</strong> உங்கள் உடல் நிலை அல்லது நோயின்படி சிறந்த முத்திரைகளை அறிவுறுத்துகிறது.",
        "<strong>அறிவியல் ஆதாரங்கள்:</strong> பழமையான யோக நூல்கள் மற்றும் நவீன ஆராய்ச்சிகளை சார்ந்த தகவல்கள்.",
        "<strong>வழிமுறைகள் எளிதில்:</strong> படங்களும் எளிய விளக்கங்களும் கொண்டு முத்திரைகளை எளிதாக கற்றுக்கொள்ளுங்கள்."
    ]

# ---------- RENDER SECOND ROW ----------
st.markdown(" ")  # Spacer
col3, col4 = st.columns([1, 1], gap="large")

with col3:
    st.markdown(
        f"""
        <div class="content-box">
            <h4>{mudra_title}</h4>
            <p>{mudra_para1}</p>
            <p>{mudra_para2}</p>
        </div>
        """, unsafe_allow_html=True
    )

with col4:
    st.markdown(f"""
        <div class="content-box">
            <h4>{help_title}</h4>
            <ul>
                {''.join(f"<li>{point}</li>" for point in help_points)}
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ---------- HEALING OPTIONS SETUP ----------
if st.session_state.language == "English":
    healing_prompt = "Choose the type of healing you want to explore:"
    healing_labels = {":orange[Mental]": "mental", ":orange[Physical]": "physical"}
    healing_display = list(healing_labels.keys())
    start_btn = "🚀 Start Healing Now"
    redirect_msg = "Redirecting to Physical Healing Page..."
    coming_soon_msg = "<div class='info-text'>Mental Healing coming soon... 🧠✨</div>"
else:
    healing_prompt = "நீங்கள் ஆராய விரும்பும் குணமாக்கல் வகையைத் தேர்ந்தெடுக்கவும்:"
    healing_labels = {":orange[மனநலம்]": "mental", ":orange[உடல் நலம்]": "physical"}
    healing_display = list(healing_labels.keys())
    start_btn = "🚀 இப்போது குணமாக தொடங்குங்கள்"
    redirect_msg = "உடல் நல பக்கம் செல்லப்படுகிறது..."
    coming_soon_msg = "<div class='info-text'>மன நலம் விரைவில் வருகிறது... 🧠✨</div>"

# ---------- START HEALING BUTTON ----------
col_start, col_spacer, col_choice = st.columns([2, 2, 2])
with col_spacer:
    if st.button(start_btn, use_container_width=True):
        st.session_state.show_options = True

# ---------- SHOW RADIO + HANDLE SELECTION ----------
if st.session_state.get("show_options", False):
    with col_choice:
        selected_display = st.radio(healing_prompt, healing_display, horizontal=True)
        selected_value = healing_labels[selected_display]  # "mental" or "physical"

        if selected_value == "physical":
            st.success(redirect_msg)
            st.switch_page("pages/physical.py")  # page name only
        else:
            st.markdown(coming_soon_msg, unsafe_allow_html=True)
