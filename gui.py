import tkinter as tk
from tkinter import filedialog
import os
import streamlit as st
from easygui import diropenbox
import main


initial_dir = os.getcwd()


# gui to get the source and destination directory
source_dir=os.path.join('D:\zaved\pythonprojects\gemini', 'ios_icons')
source_dir=st.text_input("Enter the path of the source directory",value=source_dir)
if os.path.exists(source_dir):
    path1_validated=True
    st.write("Passing")
else:
    path1_validated=False
    st.write("Invalid path")
destination_dir=st.text_input("Enter the path of the destination directory",value=source_dir)
if os.path.exists(destination_dir):
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
            if(main.dothething(source_dir, source_dir,json_file)):   
                st.write("done")
    else:
        st.write("Bad choice")
        
