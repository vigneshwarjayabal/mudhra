import streamlit as st
import pandas as pd
import re


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

def main():
    st.title("MudraGuide: Discover Your Healing Finger by Organ")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


    if st.button("clear chat"):
        st.session_state.chat_history = []
        st.rerun()
    df = load_data()
    eng_dict, tamil_dict = build_mudra_dict(df)

    user_input = st.chat_input("Type your organ name in English or Tamil...")

    if user_input:
        # Match organ from input
        organ_en = extract_organs(user_input, eng_dict.keys(), is_tamil=False)
        organ_ta = extract_organs(user_input, tamil_dict.keys(), is_tamil=True)

        # Save user input
        st.session_state.chat_history.append(("user", user_input))

        # Response logic
        if organ_en:
            response = f"The mudra finger for **{organ_en.title()}** is Left Hand **{eng_dict[organ_en]}**."
        elif organ_ta:
            response = f"**{organ_ta}** உடற்கூறிற்கு உரிய முத்திரை விரல் இடது கை **{tamil_dict[organ_ta]}** ஆகும்."
        else:
            response = "🙏 Sorry, I don't have mudra information for that organ."

        # Save bot response
        st.session_state.chat_history.append(("assistant", response))

    # Display full chat history
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)

    
if __name__ == "__main__":
    main()