import streamlit as st
import base64
import streamlit.components.v1 as components

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

        .title-text {{
            text-align: center;
            font-size: 5rem;
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

        .custom-radio-wrapper {{
            text-align: left;
            margin-top: 20px;
        }}

        .custom-radio-title {{
            font-size: 40px;
            font-weight: bold;
            color: orange;
            margin-bottom: 10px;
            font-family : 'Segoe UI' ;
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

        .stRadio > label {{
        font-size: 40px;
        font-weight: 700;
        color: #FAFAD2;
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

def change_radio_option_size(option_text,new_size='40px'):
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




# ---------- Streamlit Page Config ----------
st.set_page_config(page_title="MudraGuide 🖐️", layout="wide")
set_bg()

# ---------- Language Switch ----------

if "language" not in st.session_state:
    st.session_state.language = "Tamil"

st.markdown("""
    <div class="custom-radio-wrapper">
        <div class="custom-radio-title">🗣️ Choose Language / மொழி தேர்ந்தெடுக்கவும்</div>
    </div>
""", unsafe_allow_html=True)

# Step 2: Bind the radio button directly to session state
st.radio(
    "",
    ["Tamil", "English"],
    horizontal=True,
    key="language"  # This binds directly to session_state["language"]
)

# ---------- TITLE & SLOGAN ----------
if st.session_state.language == "English":
    title_text = "🌟  ElderCare Finger Therapy  🖐️"
    slogan = "\"Natural Healing for Body and Mind.\""
else:
    title_text = "🌟 மூத்தவர்கள் விரல் சிகிச்சை 🖐️"
    slogan = "\"உடலும் மனதும் நலமடைய இயற்கை சிகிச்சை.\""
    
# ---------- RENDER TITLE & SLOGAN ----------
st.markdown(f"<div class='title-text'>{title_text}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='slogan-text'>{slogan}</div>", unsafe_allow_html=True)
# ---------- HEALING OPTIONS SETUP ----------
# ---------- Set Healing Options Based on Language ----------

if st.session_state.language == "English":
    healing_prompt = "🧘‍♂️ Choose the type of healing you want to explore:"
    healing_options = ["Mental", "Physical"]
    start_btn = "🚀 Start Healing Now"
    redirect_messages = {
        "Mental": "Redirecting to Mental Healing coming soon...",
        "Physical": "Redirecting to Physical Healing Page..."
    }
    redirect_pages = {
        "Mental": "pages/mental.py",
        "Physical": "pages/physical.py"
    }
else:
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


# ---------- START BUTTON ----------
col_start, col_spacer, col_choice = st.columns([2, 2, 2])
with col_spacer:
    if st.button(start_btn, use_container_width=True):
        st.session_state.show_options = True
        st.session_state.selected_display = None  # Reset selection

# ---------- HEALING OPTIONS ----------
if st.session_state.get("show_options", False):
    with col_choice:
        st.markdown(
            f"<p style='font-size:28px; color:orange; font-weight:bold; font-family:Segoe UI;'>{healing_prompt}</p>",
            unsafe_allow_html=True
        )

        selected_display = st.radio(
            label=" ",
            options=healing_options,
            index=None,
            key="selected_display",
            horizontal=True
        )

        if st.session_state.selected_display:
            selected_value = st.session_state.selected_display
            st.success(redirect_messages[selected_value])
            st.switch_page(redirect_pages[selected_value])



change_radio_option_size("English","40px")
change_radio_option_size("Tamil","40px")

change_radio_option_color("English",'orange')
change_radio_option_color("Tamil",' orange')

change_radio_option_font("English",'Segoe UI')
change_radio_option_font("Tamil",'Segoe UI')

change_radio_option_weight("English",'bold')
change_radio_option_weight("Tamil",'bold')


for option in healing_options:
    change_radio_option_size(option,'40px')
    change_radio_option_color(option,'orange')
    change_radio_option_font(option,'Segoe UI')
    change_radio_option_weight(option,'bold')

