import streamlit as st
import base64
import streamlit.components.v1 as components

# -------------- Set Background --------------
def set_bg():
    with open("bg_image6.png", 'rb') as f:
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
            font-size: 5rem;
            font-weight: bold;
            color: #FFD700;
            margin-top: 50px;
        }}

        .slogan-text {{
            text-align: center;
            font-size: 2rem;
            color: #FFD700;
            margin-bottom: 50px;
        }}

        .custom-radio-wrapper {{
            text-align: left;
            margin-top: 20px;
        }}

        .custom-radio-title {{
            font-size: 40px;
            font-weight: bold;
            color: #FAFAD2;
            margin-bottom: 10px;
            font-family : 'Segoe UI' ;
        }}

        /* Hide Sidebar */
        [data-testid="stSidebar"] {{
            display: none;
        }}

        /* Big, glossy buttons for CTAs */
        div.stButton > button {{
            background-color: rgba(255, 255, 255, 0.10);
            color: #ffffff;
            border: 2px solid rgba(255, 255, 255, 0.35);
            border-radius: 16px;
            padding: 14px 20px;
            font-size: 24px;
            font-weight: 800;
            backdrop-filter: blur(8px);
            box-shadow: 0 10px 24px rgba(0,0,0,0.25);
            transition: all .18s ease-in-out;
        }}
        div.stButton > button:hover {{
            transform: translateY(-2px) scale(1.02);
            background-color: rgba(255, 255, 255, 0.18);
            border-color: rgba(255, 255, 255, 0.6);
            box-shadow: 0 16px 36px rgba(0,0,0,.35);
        }}

        /* Language radio label styling (title) */
        .stRadio > label {{
            font-size: 40px;
            font-weight: 700;
            color: #FAFAD2;
        }}

        .info-text {{
            text-align: center;
            font-size: 2rem;
            color: #FFD700;
            margin-bottom: 50px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------- Helpers to style radio options (used for Language only) ----------
def change_radio_option_size(option_text, new_size='60px'):
    js = f"""
            <script>
            const elems = window.parent.document.querySelectorAll('*');
            elems.forEach(el => {{
            if (el.innerText === '{option_text}') {{
            el.style.fontSize = '{new_size}';
            }}
            }}) ;
            </script>
            """
    components.html(js, height=0, width=0)

def change_radio_option_color(option_text, new_color='#2E8B57'):
    js = f"""
            <script>
            const elems = window.parent.document.querySelectorAll('*');
            elems.forEach(el => {{
            if (el.innerText === '{option_text}') {{
            el.style.color = '{new_color}';
            }}
            }}) ;
            </script>
            """
    components.html(js, height=0, width=0)

def change_radio_option_font(option_text, new_font_family="'Noto Sans', sans-serif"):
    js = f"""
            <script>
            const elems = window.parent.document.querySelectorAll('*');
            elems.forEach(el => {{
            if (el.innerText === '{option_text}') {{
            el.style.fontFamily = '{new_font_family}';
            }}
            }}) ;
            </script>
            """
    components.html(js, height=0, width=0)

def change_radio_option_weight(option_text, new_font_weight='bold'):
    js = f"""
            <script>
            const elems = window.parent.document.querySelectorAll('*');
            elems.forEach(el => {{
            if (el.innerText === '{option_text}') {{
            el.style.fontWeight = '{new_font_weight}';
            }}
            }}) ;
            </script>
            """
    components.html(js, height=0, width=0)


# ---------- Streamlit Page Config ----------
st.set_page_config(page_title="MudraGuide 🖐️", layout="wide")
set_bg()

# ---------- Language Switch ----------
if "language" not in st.session_state:
    st.session_state.language = "Tamil"

st.markdown("""
    <div class="custom-radio-wrapper">
        <div class="custom-radio-title">🗣️ Choose Language / மொழி தேர்ந்தெடுக்கவும் / भाषा चुनें </div>
    </div>
""", unsafe_allow_html=True)

# Language radio
st.radio(
    "",
    ["Tamil", "English", "Hindi"],
    horizontal=True,
    key="language"
)

# ---------- TITLE & SLOGAN ----------
if st.session_state.language == "English":
    title_text = "🌟 Ancient Siddhar's Natural Aligned Mudra  🖐️"
    slogan = "\"Natural Healing for Body and Mind.\""
elif st.session_state.language == "Tamil":
    title_text = "🌟 Ancient Siddhar's Natural Aligned Mudra 🖐️"
    slogan = "\"உடலும் மனதும் நலமடைய இயற்கை சிகிச்சை.\""
else:
    title_text = "🌟 प्राचीन सिद्ध की प्राकृतिक संरेखित मुद्रा 🖐️"
    slogan = "\"शरीर और मन के लिए प्राकृतिक उपचार.\""

# ---------- RENDER TITLE & SLOGAN ----------
st.markdown(f"<div class='title-text'>{title_text}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='slogan-text'>{slogan}</div>", unsafe_allow_html=True)

# ---------- Set Healing Options Based on Language ----------
if st.session_state.language == "English":
    healing_prompt = "🧘‍♂️ Choose the type of healing you want to explore:"
    healing_options = ["Mental", "Physical"]
    start_btn = "🚀 Start Healing Now"
    redirect_messages = {
        "Mental": "Redirecting to Mental Healing Page...",
        "Physical": "Redirecting to Physical Healing Page..."
    }
    redirect_pages = {
        "Mental": "pages/mental.py",
        "Physical": "pages/physical.py"
    }
elif st.session_state.language == "Tamil":
    healing_prompt = "🧘‍♀️ நீங்கள் ஆராய விரும்பும் குணமாக்கல் வகையைத் தேர்ந்தெடுக்கவும்:"
    healing_options = ["மனநலம்", "உடல் நலம்"]
    start_btn = "🚀 இப்போது குணமாக தொடங்குங்கள்"
    redirect_messages = {
        "மனநலம்": "மன நலம் பக்கம் செல்லப்படுகிறது...",
        "உடல் நலம்": "உடல் நல பக்கம் செல்லப்படுகிறது..."
    }
    redirect_pages = {
        "மனநலம்": "pages/mental.py",
        "உடல் நலம்": "pages/physical.py"
    }
else:
    healing_prompt = "🧘‍♀️ आप जिस प्रकार की उपचार पद्धति का अन्वेषण करना चाहते हैं, उसे चुनें:"
    healing_options = ["मानसिक", "भौतिक"]
    start_btn = "🚀 अभी उपचार शुरू करें"
    redirect_messages = {
        "मानसिक": "मानसिक उपचार पृष्ठ पर पुनर्निर्देशित किया जा रहा है...",
        "भौतिक": "शारीरिक उपचार पृष्ठ पर पुनर्निर्देशित किया जा रहा है..."
    }
    redirect_pages = {
        "मानसिक": "pages/mental.py",
        "भौतिक": "pages/physical.py"
    }

# Emoji for the healing options in all languages
emoji_map = {
    "Mental": "🧠", "Physical": "💪",
    "மனநலம்": "🧠", "உடல் நலம்": "💪",
    "मानसिक": "🧠", "भौतिक": "💪"
}

# ---------- START BUTTON ----------
col_start, col_spacer, col_choice = st.columns([2, 2, 2])
with col_spacer:
    if st.button(start_btn, use_container_width=True, type="primary"):
        st.session_state.show_options = True
        st.session_state.selected_display = None  # Reset selection (not used now, but kept for safety)

# ---------- HEALING OPTIONS (Option 1: Two big pill buttons) ----------
if st.session_state.get("show_options", False):
    with col_choice:
        st.markdown(
            f"<p style='font-size:28px; color:#FAFAD2; font-weight:bold; font-family:Segoe UI;'>{healing_prompt}</p>",
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2, gap="large")
        # Button for first option
        if c1.button(f"{emoji_map.get(healing_options[0], '')} {healing_options[0]}",
                     use_container_width=True):
            selected_value = healing_options[0]
            st.success(redirect_messages[selected_value])
            st.switch_page(redirect_pages[selected_value])

        # Button for second option
        if c2.button(f"{emoji_map.get(healing_options[1], '')} {healing_options[1]}",
                     use_container_width=True):
            selected_value = healing_options[1]
            st.success(redirect_messages[selected_value])
            st.switch_page(redirect_pages[selected_value])

# ---------- Style the Language radio options (only) ----------
change_radio_option_size("English", "50px")
change_radio_option_size("Tamil", "50px")
change_radio_option_size("Hindi", "50px")

change_radio_option_color("English", '#FAFAD2')
change_radio_option_color("Tamil", '#FAFAD2')
change_radio_option_color("Hindi", '#FAFAD2')

change_radio_option_font("English", "'Segoe UI', sans-serif")
change_radio_option_font("Tamil", "'Segoe UI', sans-serif")
change_radio_option_font("Hindi", "'Segoe UI', sans-serif")

change_radio_option_weight("English", 'bold')
change_radio_option_weight("Tamil", 'bold')
change_radio_option_weight("Hindi", 'bold')
