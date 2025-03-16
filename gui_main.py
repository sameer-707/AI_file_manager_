import tkinter as tk
from tkinter import filedialog
import os
import streamlit as st
from easygui import diropenbox
import main
import file_picker
# gui to get the source and destination directory
import streamlit as st
st.logo('icon3.png',size='large')
destination_dir="destination_dir"
source_dir="source_dir"
with st.sidebar:
    if st.button('Develop mode'):
        st.session_state[source_dir]=r"D:\zaved\pythonprojects\gemini\ios_icons"
        st.session_state[destination_dir]=r"D:\zaved\pythonprojects\gemini\ios_icons"
    def filepick(source_dir):
        
        
        file_picker.folder_selector(source_dir)
        

    if source_dir not in st.session_state:

            st.session_state[source_dir]=os.path.join(os.getcwd(),"ios_icons")
    with st.container(height=300):
        if st.button("Select source directory"):
            source_dir='source_dir'
            filepick(source_dir)
        st.write(st.session_state[source_dir])


        if destination_dir not in st.session_state:

                st.session_state[destination_dir]=os.path.join(os.getcwd(),"ios_icons")

        if st.button("Select destination directory"):
            destination_dir='destination_dir'
            filepick(destination_dir)
        st.write(st.session_state[destination_dir])
    json_file_path=r"D:\zaved\pythonprojects\gemini\last_output.json"
    if st.button('Undo?'):
        main.revert(json_file_path, st.session_state.source_dir, st.session_state.destination_dir)

prompt=st.chat_input('how you want to organize your files?')
if prompt:
    chat=st.chat_message("user")
    #chat.write(prompt)
    st.write(prompt)
   # with st.spinner("Gemini is working..."):
    #    if(main.dothething(st.session_state.source_dir , st.session_state.destination_dir,json_file_path,custom_prompt)):   
     #       st.write("done")



