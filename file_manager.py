import streamlit as st
import files
import numpy as np
import os

def up_dir(dir_string,devider): 
    # Find the last occurrence of '/' using rindex()
    last_slash_index = dir_string.rindex(devider)
    # Return the substring from the start up to (but not including) the last slash
    return dir_string[:last_slash_index]

@st.dialog('select yo moma')
def fragment():

    if 'source_dir' not in st.session_state:
        st.session_state.source_dir=os.getcwd()

    if st.button('up a level', icon=":material/arrow_upward:"):
        st.session_state.source_dir = up_dir(st.session_state.source_dir, "\\") 

    fs=files.list_folders(st.session_state.source_dir)
    for f in fs:
        if st.button(f,icon=":material/folder:"):
            print(st.session_state.source_dir)
            st.session_state.source_dir=os.path.join(st.session_state.source_dir,f)
            print(st.session_state.source_dir)
            st.rerun()
    if st.button('select'):
        st.write(st.session_state.source_dir+" selected")
if st.button('fragment'):
    fragment()

    # You can call any Streamlit command, including custom components:
    

