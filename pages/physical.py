import streamlit as st
import pandas as pd
import re
import os
import base64

st.set_page_config(
    page_title="Mudhra Healing App",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def load_data():
    return pd.read_excel("mudhra.xlsx")

def build_mudra_dict(df):
    eng_dict = dict(zip(df['organs'].str.lower().str.strip(), df['finger'].str.strip()))
    tamil_dict = dict(zip(df['organs_t'].str.strip(), df['finger_t'].str.strip()))
    return eng_dict, tamil_dict

def extract_organs(user_input, organ_list, is_tamil=False):
    for organ in organ_list:
        if is_tamil:
            if organ.strip() in user_input.strip():
                return organ
        else:
            pattern = r"\b" + re.escape(organ.strip().lower()) + r"\b"
            if re.search(pattern, user_input.lower()):
                return organ
    return None

def get_image_path(finger_name):
    finger_map = {
        "கட்டைவிரல்": "thumb finger",
        "ஆள்காட்டி விரல்": "index finger",
        "நடுத்துவிரல்": "middle finger",
        "மோதிர விரல்": "ring finger",
        "சுட்டுவிரல்": "little finger",
    }

    mapped = finger_map.get(finger_name.strip(), finger_name.lower())
    filename = f"{mapped}.jpg"
    path = os.path.join("image", filename)
    return path if os.path.exists(path) else None

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

        .stMarkdown h1 {{
            font-size: 2.5rem;
            font-weight: bold;
            color: #FAFAD2;
            text-align: center;
        }}

        .stMarkdown h3 {{
            font-size: 1.3rem;
            font-weight: 500;
            text-align: center;
            color:#FAFAD2;
            margin-bottom: 1.5rem;
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

        div.stRadio label {{
        font-size: 30px;
        color: #FAFAD2;
        margin-bottom: 5px;
    }}

    /* Style the radio options */
    div.stRadio > div {{
        display: flex;
        justify-content: flex-end;
        gap: 20px;
    }}

    .content-box {{
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 25px;
            backdrop-filter: blur(8px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
            color: #fff;
        }}

        .content-box h3 {{
            color: #FFD700;
            text-align: center;
            font-size: 1.4rem;
        }}

        .content-box p {{
            font-size: 0.95rem;
            line-height: 1.4rem;
        }}

        .stButton>button {{
            width: 100%;
            background-color: rgba(255, 255, 255, 0.15);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 12px;
            padding: 10px;
            font-weight: 500;
            transition: 0.3s ease-in-out;
        }}

        .stButton>button:hover {{
            background-color: rgba(255, 255, 255, 0.25);
            transform: scale(1.02);
        }}
       

        </style>
        """,
        unsafe_allow_html=True
    )


def main():

    set_bg()

    df = load_data()
    eng_dict, tamil_dict = build_mudra_dict(df)
    english_organs = list(eng_dict.keys())
    tamil_organs = list(tamil_dict.keys())

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "language" not in st.session_state:
        st.session_state.language = "English"
    if "selected_organ" not in st.session_state:
        st.session_state.selected_organ = None

    col_left, col_spacer, col_right = st.columns([2, 4, 2])

    with col_left:
        if st.button("🧹 Clear Chat"):
            st.session_state.chat_history = []
            st.session_state.selected_organ = None
            st.session_state.language = "English"
            st.rerun()

    with col_right:
        st.session_state.language = st.radio(
            "Choice Your Language", 
            ["English", "Tamil"], 
            horizontal=True, key="language_radio")

    is_tamil = st.session_state.language == "Tamil"

    # 🌟 Welcome Heading and Slogan (moved after language toggle)
    if is_tamil:
        st.markdown("# 🧘🏻 சித்தர் முத்திரை வழிகாட்டி")
        st.markdown("### இயற்கை முறை, பரம்பரை அறிவு மூலம் ஆரோக்கியத்தை மேம்படுத்துங்கள்.")
    else:
        st.markdown("# 🌿 MudraGuide 🖐️")
        st.markdown("### ✨ Discover your healing **mudra finger** through organ-based Siddha wisdom")

    organs = tamil_organs if is_tamil else english_organs
    box1, box2, box3, box4 = organs[:6], organs[6:12], organs[12:17], organs[17:]

    def render_organ_box(title, organs_list):
        with st.container():
            st.markdown(f"""<div class='content-box'><h3>{title}</h3>""", unsafe_allow_html=True)
            cols = st.columns(3)
            for idx, organ in enumerate(organs_list):
                with cols[idx % 3]:
                    if st.button(organ.title() if not is_tamil else organ, key=organ):
                        st.session_state.selected_organ = organ
            st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        render_organ_box("🔠 Organ Group 1" if not is_tamil else "🔠 உடற்கூறு தொகுதி 1", box1)
        render_organ_box("🔠 Organ Group 2" if not is_tamil else "🔠 உடற்கூறு தொகுதி 2", box2)
    with col2:
        render_organ_box("🔠 Organ Group 3" if not is_tamil else "🔠 உடற்கூறு தொகுதி 3", box3)
        render_organ_box("🔠 Organ Group 4" if not is_tamil else "🔠 உடற்கூறு தொகுதி 4", box4)

    user_input = st.chat_input("Type your organ name in English or Tamil...")

    if user_input or st.session_state.selected_organ:
        image_path = None

        if user_input:
            organ_en = extract_organs(user_input, eng_dict.keys(), is_tamil=False)
            organ_ta = extract_organs(user_input, tamil_dict.keys(), is_tamil=True)

            st.session_state.chat_history.append(("user", user_input))

            if organ_en:
                finger = eng_dict[organ_en]
                response = f"The mudra finger for **{organ_en.title()}** is Left Hand **{finger}**."
                image_path = get_image_path(finger.strip())
            elif organ_ta:
                finger = tamil_dict[organ_ta]
                response = f"**{organ_ta}** உடற்கூறிற்கு உரிய முத்திரை விரல் இடது கை **{finger}** ஆகும்."
                image_path = get_image_path(finger.strip())
            else:
                response = "🙏 Sorry, I don't have mudra information for that organ."

            st.session_state.chat_history.append(("assistant", response))
            if image_path:
                st.session_state.chat_history.append(("image", image_path))

        elif st.session_state.selected_organ:
            organ = st.session_state.selected_organ

            if is_tamil and organ in tamil_dict:
                finger = tamil_dict[organ]
                response = f"**{organ}** உடற்கூறிற்கு உரிய முத்திரை விரல் இடது கை **{finger}** ஆகும்."
                image_path = get_image_path(finger)
            elif not is_tamil and organ in eng_dict:
                finger = eng_dict[organ]
                response = f"The mudra finger for **{organ.title()}** is Left Hand **{finger}**."
                image_path = get_image_path(finger)
            else:
                response = "🙏 Sorry, I don't have mudra information for that organ."

            if not st.session_state.chat_history or st.session_state.chat_history[-1][1] != response:
                st.session_state.chat_history.append(("assistant", response))
                if image_path:
                    st.session_state.chat_history.append(("image", image_path))

            st.session_state.selected_organ = None

    for role, msg in st.session_state.chat_history:
        with st.chat_message(role if role in ["user", "assistant"] else "assistant"):
            if role == "image":
                st.image(msg, caption="Mudra Finger", use_container_width=True)
            else:
                st.markdown(msg)

if __name__ == "__main__":
    main()
