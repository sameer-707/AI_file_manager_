import streamlit as st
@st.fragment
def update():
    with st.container(border=True):
        for i in st.session_state.chatlist:
            with st.chat_message(i[0]):
                st.write(i[1])
    