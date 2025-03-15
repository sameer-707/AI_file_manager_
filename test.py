import streamlit as st
import files
import numpy as np
import os
if 'source_dir' not in st.session_state:
    st.session_state.source_dir=os.getcwd()
@st.dialog("file manager")
def update_filemanager():

    fs=files.list_folders(st.session_state.source_dir)
    for f in fs:
        if st.button(f,icon=":material/folder:"):
            print(st.session_state.source_dir)
            st.session_state.source_dir=os.path.join(st.session_state.source_dir,f)
            print(st.session_state.source_dir)
            update_filemanager()
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    
update_filemanager()
st.write("This is outside the container")