import tkinter as tk
from tkinter import filedialog
import os
import streamlit as st
from easygui import diropenbox
import main


initial_dir = os.getcwd()


button=st.button("Run?")
if button:
    json_file="D:\zaved\pythonprojects\gemini\last_output.json"
    source_dir=os.path.join('D:\zaved\pythonprojects\gemini', 'ios_icons')
    with st.spinner("Gemini is working..."):
        if(main.dothething(source_dir, source_dir,json_file)):   
            st.write("done")
        
