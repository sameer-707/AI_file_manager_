import tkinter as tk
from tkinter import filedialog
import os
import streamlit as st
from easygui import diropenbox
import main
import file_picker


initial_dir = os.getcwd()

if "SOurce_dir" not in st.session_state:

# gui to get the source and destination directory
    st.session_state.SOurce_dir=os.path.join('D:\zaved\pythonprojects\gemini', 'ios_icons')
st.session_state.SOurce_dir=st.text_input("Enter the path of the source directory",value=st.session_state.SOurce_dir)
if st.button("Select source directory"):
    if file_picker.folder_selector():
        st.session_state.SOurce_dir=file_picker.folder_selector()
        st.rerun(scope='app')
if os.path.exists(st.session_state.SOurce_dir):
    path1_validated=True
    st.write("Passing")
else:
    path1_validated=False
    st.write("Invalid path")
if "destination_dir" not in st.session_state:
    st.session_state.destination_dir=os.path.join('D:\zaved\pythonprojects\gemini', 'ios_icons')
st.session_state.destination_dir=st.text_input("Enter the destination folder",value=st.session_state.destination_dir)
if os.path.exists(st.session_state.destination_dir):
    path2_validated=True
    st.write("Passing")
else:
    path2_validated=False
    st.write("Invalid path")
button=st.button("Run?")
# button pressed
if button:
    if path1_validated and path2_validated:
        json_file="D:\zaved\pythonprojects\gemini\last_output.json"
        
        with st.spinner("Gemini is working..."):
            if(main.dothething(st.session_state.SOurce_dir , st.session_state.destination_dir,json_file)):   
                st.write("done")
    else:
        st.write("Bad choice")
        
