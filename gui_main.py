import tkinter as tk
from tkinter import filedialog
import os
import streamlit as st
from easygui import diropenbox
import main
import file_picker
# gui to get the source and destination directory

initial_dir = os.getcwd()
def filepick(source_dir):
    
    
    file_picker.folder_selector(source_dir)
    
source_dir="source_dir"
if source_dir not in st.session_state:

        st.session_state[source_dir]=os.path.join('D:\zaved\pythonprojects\gemini', 'ios_icons')

if st.button("Select source directory"):
    source_dir='source_dir'
    filepick(source_dir)
st.write(st.session_state[source_dir])

destination_dir="destination_dir"
if destination_dir not in st.session_state:

        st.session_state[destination_dir]=os.path.join('D:\zaved\pythonprojects\gemini', 'ios_icons')

if st.button("Select destination directory"):
    destination_dir='destination_dir'
    filepick(destination_dir)
st.write(st.session_state[destination_dir])


button=st.button("Run?")
# button pressed
if button:

    json_file="D:\zaved\pythonprojects\gemini\last_output.json"
    
    with st.spinner("Gemini is working..."):
        if(main.dothething(st.session_state.source_dir , st.session_state.destination_dir,json_file)):   
            st.write("done")
else:
    st.write("Bad choice")
    
