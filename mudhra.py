import streamlit as st
import pandas as pd
import re
import os


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
    filename = f"{finger_name.lower()}.jpg"
    path = os.path.join("image", filename)
    return path if os.path.exists(path) else None

def main():
    st.title("MudraGuide: Discover Your Healing Finger by Organ")

    st.markdown("""
    <style>
        /* Set overall background to white */
        .main, .block-container, .stApp {
            background-color: white !important;
            color: black !important;
        }

        /* Chat message text */
        .stChatMessage, .stChatMessage p {
            color: black !important;
            background-color: white !important;
        }

        /* Markdown inside chat */
        .stMarkdown p {
            color: black !important;
        }

        /* Optional: Button styling */
        button {
            background-color: #f0f0f0;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)


    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    df = load_data()
    eng_dict, tamil_dict = build_mudra_dict(df)

    user_input = st.chat_input("Type your organ name in English or Tamil...")

    if user_input:
        organ_en = extract_organs(user_input, eng_dict.keys(), is_tamil=False)
        organ_ta = extract_organs(user_input, tamil_dict.keys(), is_tamil=True)

        st.session_state.chat_history.append(("user", user_input))

        image_path = None

        if organ_en:
            finger = eng_dict[organ_en]
            response = f"The mudra finger for **{organ_en.title()}** is Left Hand **{finger}**."
            image_path = get_image_path(finger)
        elif organ_ta:
            finger = tamil_dict[organ_ta]
            response = f"**{organ_ta}** உடற்கூறிற்கு உரிய முத்திரை விரல் இடது கை **{finger}** ஆகும்."
            image_path = get_image_path(finger)
        else:
            response = "🙏 Sorry, I don't have mudra information for that organ."

        st.session_state.chat_history.append(("assistant", response))
        if image_path:
            st.session_state.chat_history.append(("image", image_path))

    for role, msg in st.session_state.chat_history:
        with st.chat_message(role if role in ["user", "assistant"] else "assistant"):
            if role == "image":
                st.image(msg, caption="Mudra Finger", use_container_width=True)
            else:
                st.markdown(msg)

if __name__ == "__main__":
    main()
