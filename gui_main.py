import tkinter as tk
from tkinter import filedialog
import os
import streamlit as st
from easygui import diropenbox
import main
import file_picker
import chat_gui
# gui to get the source and destination directory
import streamlit as st
#variable defining

source_dir="source_dir"
if "chatlist" not in st.session_state:
     st.session_state.chatlist=[]


def dothings(json_file_path,prompt,mode):
    with st.spinner("Gemini is working..."):
        response=main.dothething(st.session_state.source_dir , st.session_state.destination_dir,json_file_path,prompt,mode)   
        return response
st.logo('icon3.png',size='large')




toggle_label = (
    "File Manager"
    if st.session_state.get("my_toggle", False)
    else "Gemini Chat"
)
toggle_value = st.session_state.get("my_toggle", False)

is_toggle = st.toggle(toggle_label, value=toggle_value, key="my_toggle")

            
destination_dir="destination_dir"

dev_mode=st.toggle('developer mode')



for message in st.session_state.chatlist:
    with st.chat_message(message[0]):
        st.markdown(message[1])




with st.sidebar:
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
    st.session_state.chatlist.append(('human',prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    #chat_gui.update()
    if not dev_mode:
        print('not dev mode')
        if is_toggle:
            print('file manager mode')
            mode='file manager'
            response=dothings(json_file_path,prompt,mode)
        else:
            mode='chat'
            response=dothings(json_file_path,prompt,mode)
    else:
         response='this is a test message'
    with st.chat_message("assistant"):
         st.markdown(response)
    st.session_state.chatlist.append(('ai',response))
    #print(st.session_state.chatlist,'this is chatlist')
    #chat_gui.update()
    
    #chat.write(prompt)
    
    
    
    



