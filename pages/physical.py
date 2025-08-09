import streamlit as st
import pandas as pd
import re
import os
import base64
import streamlit.components.v1 as components

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
        "பெருவிரல்": "thumb finger",
        "ஆள்காட்டி விரல்": "index finger",
        "நடு விரல்": "middle finger",
        "மோதிர விரல்": "ring finger",
        "சுண்டு விரல்": "little finger",
    }

    mapped = finger_map.get(finger_name.strip(), finger_name.lower())
    filename = f"{mapped}.jpg"
    path = os.path.join("image", filename)
    return path if os.path.exists(path) else None
# ------------------ Therapy Script Display Helper ------------------ #
def display_therapy_script_sections(pre_mudra=True):
    st.markdown("""<div class='content-box'>""", unsafe_allow_html=True)
    
    if pre_mudra:
        st.markdown("""
        <h2 style='color:#90EE90; text-align:center;'>🌿 மூத்தவர்கள் நலம் மேம்பாட்டு நிகழ்வு 🌿</h2>
        <p style='font-size:18px; color:#FAFAD2; text-align:center;'>
            நம்முடைய தொடு விரல் சிகிச்சை முறையை கீழ்கண்ட வகையில் தொகுப்பாக பயனாளர்களுக்கு சமர்ப்பிக்க உள்ளோம்<br><br>
            <strong>மொத்த நேரம் – 35 முதல் 40 நிமிடங்கள்</strong>
        </p>
        <hr style='border:1px solid #FAFAD2;'>

        <h4 style='color:#FFD700;'>🟢 1. விரல் பயிற்சி – 5 நிமிடம்</h4>
        <ul style='color:#FAFAD2; font-size:17px;'>
            <li>1. விரல் மூடி திரத்தல்</li>
            <li>2. கைகளை மெதுவாக தட்டுதல்</li>
        </ul>
        <p style='color:#ADFF2F;'>🎯 நரம்பு இயக்கம், மூட்டு நெகிழ்வு, சுறுசுறுப்பு</p>
        <hr style='border:1px dashed #FAFAD2;'>


        <h4 style='color:#FFD700;'>🟢 2. முக (அஷ்ட கோணல்) பயிற்சி – 5 நிமிடம்</h4>
        <p style='color:#FAFAD2;'> (சத்தமின்றி வாயை திறந்து முக தசைகளை இயக்குதல்)</p>
        <p style='font-size:20px; color:#FAFAD2; text-align:center;'>
        🔠 உயிரெழுத்துகள்: <br>
        அ – ஆ – இ – ஈ – உ – ஊ – எ – ஏ – ஐ – ஒ – ஓ – ஔ
        </p>
        <p style='color:#ADFF2F;'>🎯 முக தசை இயக்கம், முக இருக்கம் குறையும் பக்கவாதம் தடுப்பு</p>
        <hr style='border:1px dashed #FAFAD2;'>


        <h4 style='color:#FFD700;'>🟢 3. மிருக சத்த பயிற்சி – 5 நிமிடம்</h4>
        <p style='color:#FAFAD2;'> (ஒவ்வொரு சத்தமும் 5 முறை, 30 விநாடி)</p>
        <ul style='color:#FAFAD2; font-size:17px;'>
            <li>🦚 மயில் – "அவ்-அவ்"</li>
            <li>🐦 குயில் – "கூ...ஹூ..."</li>
            <li>🐦 காக்கா – "கா...கா..."</li>
            <li>🐶 நாய் – "பௌ...பௌ..."</li>
            <li>🐱 பூனை – "ம்யாஉ்..."</li>
            <li>🐍 பாம்பு – "சீ...சீ..."</li>
            <li>🐅 புலி – "ர்ர்ர்..."</li>
            <li>🐸 தவளை – "க்...க்...க்..."</li>
        </ul>
        <p style='color:#ADFF2F;'>🎯 சுவாசம், குரல் பயிற்சி, மன உறுதி</p>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <hr style='border:1px dashed #FAFAD2;'>
        <h4 style='color:#FFD700;'>🟢 5. இசை சிகிச்சை – 5 நிமிடம்</h4>
        <p style='color:#FAFAD2; font-size:17px;'>
        இயற்கையான இசைகள் / ஆதார இசைகள்<br><br>
        (கண் மூடிக் கேட்க வேண்டும்)
        </p>
        <p style='color:#ADFF2F;'>🎯 மன நிம்மதி, மன அழுத்தம் குறைப்பு</p>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


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
    div.stRadio > label > div > p {{
            font-size : 22px;
            color:#FAFAD2;
            font-weight: 700;
            text-align: center;
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

def change_radio_option_size(option_text,new_size='20px'):
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

def change_radio_option_color(option_text,new_color='#2E8B57'):
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

def change_radio_option_font(option_text,new_font_family="'Noto Sans', sans-serif"):
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

def change_radio_option_weight(option_text,new_font_weight='bold'):
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


def main():

    set_bg()

    df = load_data()
    eng_dict, tamil_dict = build_mudra_dict(df)
    english_organs = list(eng_dict.keys())
    tamil_organs = list(tamil_dict.keys())

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "language" not in st.session_state:
        st.session_state.language = "Tamil"
    if "selected_organ" not in st.session_state:
        st.session_state.selected_organ = None

    col_left, col_spacer, col_right = st.columns([2, 4, 2])

    with col_left:
        if st.button("🧹 Clear Chat"):
            st.session_state.chat_history = []
            st.session_state.selected_organ = None
            st.session_state.language = "Tamil"
            st.rerun()

    with col_right:
        st.markdown(
            f"<p style='font-size:30px; color:orange; font-weight:bold; font-family:Segoe UI;'>Choice Your Language</p>",
            unsafe_allow_html=True
        )
        st.session_state.language = st.radio(
            "", 
            ["Tamil", "English"], 
            horizontal=True, key="language_radio")
    

    is_tamil = st.session_state.language == "Tamil"

    # 🌟 Welcome Heading and Slogan (moved after language toggle)
    if is_tamil:
        st.markdown("# 🌿 மூத்தோர் விரல் தொடுதல் சிகிச்சை 🖐️")
        st.markdown("### ✨ எந்த உடல் உறுப்பில் பிரச்சனை")
    else:
        st.markdown("# 🌿  Elderly Care Finger Touch Therapy 🖐️")
        st.markdown("### ✨ Which body part has a problem")

    organs = tamil_organs if is_tamil else english_organs
    box1, box2, box3, box4 = organs[:6], organs[6:12], organs[12:17], organs[17:]

    def render_organ_box(organs_list):
        with st.container():
            cols = st.columns(3)
            for idx, organ in enumerate(organs_list):
                with cols[idx % 3]:
                    if st.button(organ.title() if not is_tamil else organ, key=organ):
                        st.session_state.selected_organ = organ
            st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        render_organ_box(box1)
        render_organ_box(box2)
    with col2:
        render_organ_box(box3)
        render_organ_box(box4)

    user_input = st.chat_input("Type your organ name in English or Tamil...")

    if user_input or st.session_state.selected_organ:

     image_path = None
    display_therapy_script_sections(pre_mudra=True)  # 🧘 Show 1–3 first

    if user_input:
        organ_en = extract_organs(user_input, eng_dict.keys(), is_tamil=False)
        organ_ta = extract_organs(user_input, tamil_dict.keys(), is_tamil=True)

        st.session_state.chat_history.append(("user", user_input))

        if organ_en:
            finger = eng_dict[organ_en]
            response = f"<h4 style='color:#FFD700;'>🟢 4. தொடு விரல் சிகிச்சை – 15 நிமிடம்</h4><br><span style='color:#FAFAD2; font-size:20px;'>The mudra finger for <b>{organ_en.title()}</b> is <b>Left Hand {finger}</b>.</span>"
            image_path = get_image_path(finger.strip())
        elif organ_ta:
            finger = tamil_dict[organ_ta]
            response = f"<h4 style='color:#FFD700;'>🟢 4. தொடு விரல் சிகிச்சை – 15 நிமிடம்</h4><br><span style='color:#FAFAD2; font-size:20px;'><b>{organ_ta}</b> உடற்கூறிற்கு உரிய முத்திரை விரல் <b>இடது கை {finger}</b> ஆகும்.</span>"
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
            response = f"<h4 style='color:#FFD700;'>🟢 4. தொடு விரல் சிகிச்சை – 15 நிமிடம்</h4><br><span style='color:#FAFAD2; font-size:20px;'><b>{organ}</b> உடற்கூறிற்கு உரிய முத்திரை விரல் <b>இடது கை {finger}</b> ஆகும்.</span>"
            image_path = get_image_path(finger)
        elif not is_tamil and organ in eng_dict:
            finger = eng_dict[organ]
            response = f"<h4 style='color:#FFD700;'>🟢 4. தொடு விரல் சிகிச்சை – 15 நிமிடம்</h4><br><span style='color:#FAFAD2; font-size:20px;'>The mudra finger for <b>{organ.title()}</b> is <b>Left Hand {finger}</b>.</span>"
            image_path = get_image_path(finger)
        else:
            response = "🙏 Sorry, I don't have mudra information for that organ."

        if not st.session_state.chat_history or st.session_state.chat_history[-1][1] != response:
            st.session_state.chat_history.append(("assistant", response))
            if image_path:
                st.session_state.chat_history.append(("image", image_path))

        st.session_state.selected_organ = None

    display_therapy_script_sections(pre_mudra=False)  # 🎵 Show music therapy (Section 5)


    for role, msg in st.session_state.chat_history:
     with st.chat_message(role if role in ["user", "assistant"] else "assistant"):

        if role == "image":
            st.image(msg, caption="Mudra Finger", use_container_width=True)

        elif role == "assistant":
            # Highlight organ and mudhra finger (Tamil + English) with clean style
            styled_msg = (
                msg.replace("Organ", "<span style='color:#90EE90; font-weight:700;'>Organ</span>")
                   .replace("Mudhra Finger", "<span style='color:#90EE90; font-weight:700;'>Mudhra Finger</span>")
                   .replace("உடற்கூறு", "<span style='color:#90EE90; font-weight:700;'>உடற்கூறு</span>")
                   .replace("முத்திரை விரல்", "<span style='color:#90EE90; font-weight:700;'>முத்திரை விரல்</span>")
            )

            st.markdown(
                f"""
                <div style='
                    font-size: 22px;
                    font-family: "Noto Sans Tamil", "Poppins", "Trebuchet MS", sans-serif;
                    font-weight: 600;
                    color: #FAFAD2;
                    line-height: 1.6;
                    background: transparent;
                    padding: 0;'>
                    {styled_msg}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.markdown(f"<div style='color:white; font-size: 18px;'>{msg}</div>", unsafe_allow_html=True)
            
    st.markdown("<div id='bottom-marker'></div>", unsafe_allow_html=True)

    scroll_script = """
<script>
const marker = window.parent.document.getElementById("bottom-marker");
if(marker){ marker.scrollIntoView({ behavior: "smooth", block: "start" }); }
</script>
"""
    components.html(scroll_script, height=0)

    change_radio_option_size("English","30px")
    change_radio_option_size("Tamil","30px")
    change_radio_option_color("English",'orange')
    change_radio_option_color("Tamil",' orange')

    change_radio_option_font("English",'Segoe UI')
    change_radio_option_font("Tamil",'Segoe UI')

    change_radio_option_weight("English",'bold')
    change_radio_option_weight("Tamil",'bold')

    




if __name__ == "__main__":
    main()




