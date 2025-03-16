import file_picker
import streamlit as st
import os
st.text('hi')
if 'source_dir' not in st.session_state:
    st.session_state.source_dir=os.getcwd()


if st.button('run the selector'):
    file_picker.folder_selector()
print(st.session_state.source_dir,'printed from here')
    #st.rerun(scope='app')
