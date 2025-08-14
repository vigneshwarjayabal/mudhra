import streamlit as st
import pandas as pd
import re
import os
import base64
import streamlit.components.v1 as components
import time

st.set_page_config(
    page_title="Mudhra Healing App",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def load_data():
    return pd.read_excel("mudhramn.xlsx")

def build_mudra_dict(df):
    eng_dict = dict(zip(df['mentel'].str.lower().str.strip(), df['mudhra_en'].str.strip()))
    tamil_dict = dict(zip(df['mentel_tm'].str.strip(), df['mudhra_tm'].str.strip()))
    hindi_dict = dict(zip(df['mentel_hn'].str.strip(), df['mudhra_hn'].str.strip()))
    return eng_dict, tamil_dict, hindi_dict

def extract_organs(user_input, organ_list, language="english"):
    for organ in organ_list:
        if language.lower() == "tamil" or language.lower() == "hindi":
            if organ.strip() in user_input.strip():
                return organ
        else:  # English
            pattern = r"\b" + re.escape(organ.strip().lower()) + r"\b"
            if re.search(pattern, user_input.lower()):
                return organ
    return None

def get_image_path(finger_name):
    finger_map = {
        # Tamil mapping
        "பெருவிரல்": "thumb finger",
        "ஆள்காட்டி விரல்": "index finger",
        "நடு விரல்": "middle finger",
        "மோதிர விரல்": "ring finger",
        "சுண்டு விரல்": "little finger",

        # Hindi mapping
        "अंगूठा उंगली": "thumb finger",
        "तर्जनी": "index finger",
        "बीच की ऊँगली": "middle finger",
        "रिंग फिंगर": "ring finger",
        "छोटी उंगली": "little finger"
    }

    mapped = finger_map.get(finger_name.strip(), finger_name.lower())
    filename = f"{mapped}.jpg"
    path = os.path.join("right", filename)
    return path if os.path.exists(path) else None

def display_therapy_script_sections(pre_mudra=True):
    lang = st.session_state.language
    video1_url = "https://drive.google.com/file/d/19TS07fdAesG5KIKBRDn3tLUXfh6BAbNx/preview"
    video2_url = "https://drive.google.com/file/d/1OoU34EdDtIfekMSuCr-uhicmwi_yu2Xj/preview"

    st.markdown("""<div class='content-box'>""", unsafe_allow_html=True)

    if pre_mudra:
        if lang == "Tamil":
            st.markdown("""
            <h2 style='color:#90EE90; text-align:center;'>🌿 மூத்தவர்கள் நலம் மேம்பாட்டு நிகழ்வு 🌿</h2>
            <p style='font-size:18px; color:#FAFAD2; text-align:center;'>
                நம்முடைய தொடு விரல் சிகிச்சை முறையை கீழ்கண்ட வகையில் தொகுப்பாக பயனாளர்களுக்கு சமர்ப்பிக்க உள்ளோம்<br><br>
                <strong>மொத்த நேரம் – 35 முதல் 40 நிமிடங்கள்</strong>
            </p>
            <hr style='border:1px solid #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 1. விரல் பயிற்சி – 5 நிமிடம்</h4>
            """, unsafe_allow_html=True)

            st.markdown(f"""
<a href="{video1_url}" target="_blank" style="
    display:inline-block; padding:10px 15px;
    background-color:#FFD700; color:black;
    border-radius:8px; text-decoration:none;
    font-weight:bold;">
▶ விரல் பயிற்சிகள் வீடியோவைப் பாருங்கள்
</a>
""", unsafe_allow_html=True)

            st.markdown("""
            <ul style='color:#FAFAD2; font-size:17px;'>
                <li>1. விரல் மூடி திரத்தல்</li>
                <li>2. வணங்கி விரித்தல்</li>
                <li>3. உள்ளங்கை மேல் நோக்கி, கீழ் நோக்கி, பக்க வாட்டில்</li>
                <li>4. விரல் இடுக்கு கலை உரசுதல்</li>
                <li>5. கைகளை மெதுவாக தட்டுதல்</li>
            </ul>
            <p style='color:#ADFF2F;'>🎯 நரம்பு இயக்கம், மூட்டு நெகிழ்வு, சுறுசுறுப்பு</p>
            <hr style='border:1px dashed #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 2. முக (அஷ்ட கோணல்) பயிற்சி – 5 நிமிடம்</h4>
            <p style='color:#FAFAD2;'>(சத்தமின்றி வாயை திறந்து முக தசைகளை இயக்குதல்)</p>
            <p style='font-size:20px; color:#FAFAD2; text-align:center;'>
            🔠 உயிரெழுத்துகள்: <br>
            அ – ஆ – இ – ஈ – உ – ஊ – எ – ஏ – ஐ – ஒ – ஓ – ஔ
            </p>
            <p style='color:#ADFF2F;'>🎯 முக தசை இயக்கம், முக இருக்கம் குறையும் பக்கவாதம் தடுப்பு</p>
            <hr style='border:1px dashed #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 3. மிருக சத்த பயிற்சி – 5 நிமிடம்</h4>
            <p style='color:#FAFAD2;'>(ஒவ்வொரு சத்தமும் 5 முறை, 30 விநாடி)</p>
            """, unsafe_allow_html=True)

            st.markdown(f"""
<a href="{video2_url}" target="_blank" style="
    display:inline-block; padding:10px 15px;
    background-color:#FFD700; color:black;
    border-radius:8px; text-decoration:none;
    font-weight:bold;">
▶ மிருக சத்த பயிற்சி வீடியோவைப் பாருங்கள்
</a>
""", unsafe_allow_html=True)

            st.markdown("""
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

        elif lang == "English":
            st.markdown("""
            <h2 style='color:#90EE90; text-align:center;'>🌿 Elder Wellness Program 🌿</h2>
            <p style='font-size:18px; color:#FAFAD2; text-align:center;'>
                Our Finger Touch Therapy is presented as follows:<br><br>
                <strong>Total Duration – 35 to 40 Minutes</strong>
            </p>
            <hr style='border:1px solid #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 1. Finger Exercises – 5 Minutes</h4>
            """, unsafe_allow_html=True)

            st.markdown(f"""
<a href="{video1_url}" target="_blank" style="
    display:inline-block; padding:10px 15px;
    background-color:#FFD700; color:black;
    border-radius:8px; text-decoration:none;
    font-weight:bold;">
▶ Watch Finger Exercises Video
</a>
""", unsafe_allow_html=True)
            st.markdown("""
            <ul style='color:#FAFAD2; font-size:17px;'>
                <li>1. Fist clenching and releasing</li>
                <li>2. Stretching fingers forward and backward</li>
                <li>3. Palm facing up, down, and sideways</li>
                <li>4. Finger interlocking and rubbing</li>
                <li>5. Gentle hand tapping</li>
            </ul>
            <p style='color:#ADFF2F;'>🎯 Improves nerve function, joint flexibility, and agility</p>
            <hr style='border:1px dashed #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 2. Facial (Eight Angles) Exercise – 5 Minutes</h4>
            <p style='color:#FAFAD2;'>(Move facial muscles silently by opening the mouth)</p>
            <p style='font-size:20px; color:#FAFAD2; text-align:center;'>
            🔠 Vowels: <br>
            A – AA – I – EE – U – OO – E – AE – AI – O – OA – AU
            </p>
            <p style='color:#ADFF2F;'>🎯 Strengthens facial muscles, reduces sagging, prevents paralysis</p>
            <hr style='border:1px dashed #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 3. Animal Sound Exercise – 5 Minutes</h4>
            <p style='color:#FAFAD2;'>(Repeat each sound 5 times, 30 seconds each)</p>
            """, unsafe_allow_html=True)

            st.markdown(f"""
<a href="{video2_url}" target="_blank" style="
    display:inline-block; padding:10px 15px;
    background-color:#FFD700; color:black;
    border-radius:8px; text-decoration:none;
    font-weight:bold;">
▶ Watch Animal Sound Video
</a>
""", unsafe_allow_html=True)
            st.markdown("""
            <ul style='color:#FAFAD2; font-size:17px;'>
                <li>🦚 Peacock – "Av-Av"</li>
                <li>🐦 Cuckoo – "Coo...Hoo..."</li>
                <li>🐦 Crow – "Caw...Caw..."</li>
                <li>🐶 Dog – "Bow...Bow..."</li>
                <li>🐱 Cat – "Meow..."</li>
                <li>🐍 Snake – "Sss...Sss..."</li>
                <li>🐅 Tiger – "Rrr..."</li>
                <li>🐸 Frog – "Kk...Kk...Kk..."</li>
            </ul>
            <p style='color:#ADFF2F;'>🎯 Improves breathing, vocal practice, and confidence</p>
            """, unsafe_allow_html=True)

        elif lang == "Hindi":
            st.markdown("""
            <h2 style='color:#90EE90; text-align:center;'>🌿 वरिष्ठ नागरिक स्वास्थ्य कार्यक्रम 🌿</h2>
            <p style='font-size:18px; color:#FAFAD2; text-align:center;'>
                हमारी उंगली स्पर्श चिकित्सा इस प्रकार प्रस्तुत की जाती है:<br><br>
                <strong>कुल समय – 35 से 40 मिनट</strong>
            </p>
            <hr style='border:1px solid #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 1. उंगली व्यायाम – 5 मिनट</h4>
            """, unsafe_allow_html=True)

            st.markdown(f"""
<a href="{video1_url}" target="_blank" style="
    display:inline-block; padding:10px 15px;
    background-color:#FFD700; color:black;
    border-radius:8px; text-decoration:none;
    font-weight:bold;">
▶ उंगली व्यायाम वीडियो देखें
</a>
""", unsafe_allow_html=True)

            st.markdown("""
            <ul style='color:#FAFAD2; font-size:17px;'>
                <li>1. मुट्ठी बांधना और खोलना</li>
                <li>2. आगे और पीछे उंगलियों को खींचना</li>
                <li>3. हथेली ऊपर, नीचे और बगल की ओर करना</li>
                <li>4. उंगलियों को इंटरलॉक कर रगड़ना</li>
                <li>5. धीरे से हाथ थपथपाना</li>
            </ul>
            <p style='color:#ADFF2F;'>🎯 नसों का कार्य सुधार, जोड़ों की लचीलापन, फुर्ती</p>
            <hr style='border:1px dashed #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 2. चेहरे का (आठ कोण) व्यायाम – 5 मिनट</h4>
            <p style='color:#FAFAD2;'>(मुंह खोलकर चुपचाप चेहरे की मांसपेशियों को हिलाना)</p>
            <p style='font-size:20px; color:#FAFAD2; text-align:center;'>
            🔠 स्वर: <br>
            अ – आ – इ – ई – उ – ऊ – ए – ऐ – ओ – औ
            </p>
            <p style='color:#ADFF2F;'>🎯 चेहरे की मांसपेशियां मजबूत, झुर्रियां कम, लकवा रोकथाम</p>
            <hr style='border:1px dashed #FAFAD2;'>

            <h4 style='color:#FFD700;'>🟢 3. जानवरों की आवाज का व्यायाम – 5 मिनट</h4>
            <p style='color:#FAFAD2;'>(प्रत्येक ध्वनि 5 बार, 30 सेकंड)</p>
            """, unsafe_allow_html=True)

            st.markdown(f"""
<a href="{video2_url}" target="_blank" style="
    display:inline-block; padding:10px 15px;
    background-color:#FFD700; color:black;
    border-radius:8px; text-decoration:none;
    font-weight:bold;">
▶ पशु ध्वनि वीडियो देखें
</a>
""", unsafe_allow_html=True)

            st.markdown("""
            <ul style='color:#FAFAD2; font-size:17px;'>
                <li>🦚 मोर – "अव-अव"</li>
                <li>🐦 कोयल – "कू...हू..."</li>
                <li>🐦 कौआ – "का...का..."</li>
                <li>🐶 कुत्ता – "भौं...भौं..."</li>
                <li>🐱 बिल्ली – "म्याऊ..."</li>
                <li>🐍 सांप – "स्स...स्स..."</li>
                <li>🐅 बाघ – "र्र्र..."</li>
                <li>🐸 मेंढक – "क्...क्...क्..."</li>
            </ul>
            <p style='color:#ADFF2F;'>🎯 श्वसन सुधार, आवाज का अभ्यास, आत्मविश्वास</p>
            """, unsafe_allow_html=True)

    else:
        # Post-mudra section (unchanged)
        if lang == "Tamil":
            st.markdown("""
            <hr style='border:1px dashed #FAFAD2;'>
            <h4 style='color:#FFD700;'>🟢 5. இசை சிகிச்சை – 5 நிமிடம்</h4>
            <p style='color:#FAFAD2; font-size:17px;'>
            இயற்கையான இசைகள் / ஆதார இசைகள்<br><br>
            (கண் மூடிக் கேட்க வேண்டும்)
            </p>
            <p style='color:#ADFF2F;'>🎯 மன நிம்மதி, மன அழுத்தம் குறைப்பு</p>
            """, unsafe_allow_html=True)

        elif lang == "English":
            st.markdown("""
            <hr style='border:1px dashed #FAFAD2;'>
            <h4 style='color:#FFD700;'>🟢 5. Music Therapy – 5 Minutes</h4>
            <p style='color:#FAFAD2; font-size:17px;'>
            Natural sounds / background instrumental music<br><br>
            (Listen with eyes closed)
            </p>
            <p style='color:#ADFF2F;'>🎯 Promotes relaxation, reduces stress</p>
            """, unsafe_allow_html=True)

        elif lang == "Hindi":
            st.markdown("""
            <hr style='border:1px dashed #FAFAD2;'>
            <h4 style='color:#FFD700;'>🟢 5. संगीत चिकित्सा – 5 मिनट</h4>
            <p style='color:#FAFAD2; font-size:17px;'>
            प्राकृतिक ध्वनियां / पृष्ठभूमि वाद्य संगीत<br><br>
            (आंखें बंद करके सुनें)
            </p>
            <p style='color:#ADFF2F;'>🎯 मानसिक शांति, तनाव में कमी</p>
            """, unsafe_allow_html=True)

        

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
    eng_dict, tamil_dict,hindi_dict = build_mudra_dict(df)
    english_organs = list(eng_dict.keys())
    tamil_organs = list(tamil_dict.keys())
    hindi_organs = list(hindi_dict.keys())

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
            ["Tamil", "English" ,"Hindi"], 
            horizontal=True, key="language_radio")
    
    is_tamil = st.session_state.language == "Tamil"
    is_hindi = st.session_state.language == "Hindi"

    # 🌟 Welcome Heading and Slogan (moved after language toggle)
    if is_tamil:
        st.markdown("# 🌿 மூத்தோர் விரல் தொடுதல் சிகிச்சை 🖐️")
        st.markdown("### இயற்கை முறை, பரம்பரை அறிவு மூலம் ஆரோக்கியத்தை மேம்படுத்துங்கள்.")
    elif is_hindi:
         st.markdown("# 🌿   वृद्धजन देखभाल उंगली स्पर्श उपचार 🖐️")
         st.markdown("### ✨अंग-आधारित सिद्ध ज्ञान के माध्यम से अपनी उपचारात्मक मुद्रा उंगली खोजें")
        
    else:
        st.markdown("# 🌿  Elderly Care Finger Touch Therapy 🖐️")
        st.markdown("### ✨ Discover your healing **mudra finger** through organ-based Siddha wisdom")

    organs = tamil_organs if is_tamil else hindi_organs if is_hindi else english_organs
    box1, box2, box3, box4 = organs[:6], organs[6:12], organs[12:17], organs[17:]

    def render_organ_box(organs_list):
     with st.container():
        cols = st.columns(3)
        for idx, organ in enumerate(organs_list):
            with cols[idx % 3]:
                if st.button(
                    organ.title() if not (is_tamil or is_hindi) else organ, 
                    key=organ
                ):
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
    display_therapy_script_sections(pre_mudra=True)  # 🧘 Show Section 1–3

    if user_input:
        organ_en = extract_organs(user_input, eng_dict.keys())
        organ_ta = extract_organs(user_input, tamil_dict.keys())
        organ_hn = extract_organs(user_input, hindi_dict.keys())

        st.session_state.chat_history.append(("user", user_input))

        if organ_en:
            finger = eng_dict[organ_en]
            response = f"""
                <h4 style='color:#FFD700;'>🟢 4. Finger Touch Therapy – 15 Minutes</h4><br>
                <span style='color:#FAFAD2; font-size:20px;'>
                The mudra finger for <b>{organ_en.title()}</b> is <b>Right Hand {finger}</b>.
                </span>
            """
            image_path = get_image_path(finger.strip())

        elif organ_ta:
            finger = tamil_dict[organ_ta]
            response = f"""
                <h4 style='color:#FFD700;'>🟢 4. தொடு விரல் சிகிச்சை – 15 நிமிடம்</h4><br>
                <span style='color:#FAFAD2; font-size:20px;'>
                <b>{organ_ta}</b> உடற்கூறிற்கு உரிய முத்திரை விரல் <b>வலது கை {finger}</b> ஆகும்.
                </span>
            """
            image_path = get_image_path(finger.strip())

        elif organ_hn:
            finger = tamil_dict[organ_hn]
            response = f"""
                <h4 style='color:#FFD700;'>🟢 4. उंगली स्पर्श चिकित्सा – 15 मिनट</h4><br>
                <span style='color:#FAFAD2; font-size:20px;'>
                के लिए मुद्रा उंगली <b>{organ_hn.title()}</b> है <b> दांया हाथ {finger}
                </span>
            """
            image_path = get_image_path(finger.strip())


        else:
            response = "🙏 Sorry, I don't have mudra information for that organ."
        

        st.session_state.scroll_to_result = time.time()
        st.session_state.chat_history = []
        st.session_state.chat_history.append(("assistant", response))
        if image_path:
            st.session_state.chat_history.append(("image", image_path))

    elif st.session_state.selected_organ:
        organ = st.session_state.selected_organ

        if is_tamil and organ in tamil_dict:
            finger = tamil_dict[organ]
            response = f"""
                <h4 style='color:#FFD700;'>🟢 4. தொடு விரல் சிகிச்சை – 15 நிமிடம்</h4><br>
                <span style='color:#FAFAD2; font-size:20px;'>
                <b>{organ}</b> உடற்கூறிற்கு உரிய முத்திரை விரல் <b>வலது கை {finger}</b> ஆகும்.
                </span>
            """
            image_path = get_image_path(finger)
        elif not is_tamil and is_hindi:
            finger = hindi_dict[organ]
            response = f"<h4 style='color:#FFD700;'>🟢 4. उंगली स्पर्श चिकित्सा – 15 मिनट </h4><br><span style='color:#FAFAD2; font-size:20px;'>के लिए मुद्रा उंगली <b>{organ.title()}</b> है <b> दांया हाथ {finger}</span>"
            image_path = get_image_path(finger.strip())


        elif not is_tamil and organ in eng_dict:
            finger = eng_dict[organ]
            response = f"""
                <h4 style='color:#FFD700;'>🟢 4. Finger Touch Therapy – 15 Minutes</h4><br>
                <span style='color:#FAFAD2; font-size:20px;'>
                The mudra finger for <b>{organ.title()}</b> is <b>Right Hand {finger}</b>.
                </span>
            """
            image_path = get_image_path(finger)

        else:
            response = "🙏 Sorry, I don't have mudra information for that organ."

        if not st.session_state.chat_history or st.session_state.chat_history[-1][1] != response:
            st.session_state.scroll_to_result = time.time()
            st.session_state.chat_history = []
            st.session_state.chat_history.append(("assistant", response))
            if image_path:
                st.session_state.chat_history.append(("image", image_path))

        st.session_state.selected_organ = None

    # 🧘 Show Section 5 (Post-mudra therapy script)
    display_therapy_script_sections(pre_mudra=False)



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
                    .replace("अंग","<span style='color:#90EE90; font-weight:700;'>अंग</span>")
                   .replace("मुद्रा उंगली", "<span style='color:#90EE90; font-weight:700;'>मुद्रा उंगली</span>")
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
            st.markdown(f"<div style='color:white; font-size: 18px;'>{msg} </div>", unsafe_allow_html=True)
            
    ts = st.session_state.get("scroll_to_result", None)
    if ts:
     marker_id = f"bottom-marker-{int(ts * 1000)}"
    else:
     marker_id = "bottom-marker-static"

# Render the marker into the page
    st.markdown(f"<div id='{marker_id}'></div>", unsafe_allow_html=True)

# If a timestamp trigger exists, inject JS that polls until the marker is present then scrolls
    if ts:
     scroll_js = f"""
    <script>
    (function() {{
      const id = "{marker_id}";
      let attempts = 0;
      const maxAttempts = 30;   // 30 * 50ms = 1500ms max
      const interval = setInterval(function() {{
        attempts++;
        const marker = window.parent.document.getElementById(id);
        if (marker) {{
          marker.scrollIntoView({{ behavior: "smooth", block: "start" }});
          clearInterval(interval);
        }} else if (attempts >= maxAttempts) {{
          clearInterval(interval);
        }}
      }}, 50);
    }})();
    </script>
    """
     components.html(scroll_js, height=0)
    # reset flag so future clicks create a new timestamp
     st.session_state.scroll_to_result = None

    change_radio_option_size("English","30px")
    change_radio_option_size("Tamil","30px")
    change_radio_option_size("Hindi","30px")
    change_radio_option_color("English",'orange')
    change_radio_option_color("Tamil",' orange')
    change_radio_option_color("Hindi","orange")

    change_radio_option_font("English",'Segoe UI')
    change_radio_option_font("Tamil",'Segoe UI')
    change_radio_option_font("Hindi","Segoe UI")

    change_radio_option_weight("English",'bold')
    change_radio_option_weight("Tamil",'bold')
    change_radio_option_weight("Hindi",'bold')
    




if __name__ == "__main__":
    main()
