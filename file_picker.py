import streamlit as st
import files
import numpy as np
import os

def up_dir(dir_string,devider): 
    # Find the last occurrence of '/' using rindex()
    last_slash_index = dir_string.rindex(devider)
    # Return the substring from the start up to (but not including) the last slash
    return dir_string[:last_slash_index]
@st.fragment
@st.dialog('select yo moma')
def folder_selector(root):
    st.title(st.session_state[root])
    if st.button('up a level', icon=":material/arrow_upward:"):
        st.session_state[root] = up_dir(st.session_state[root], "\\") 

    fs=files.list_folders(st.session_state[root])
    for f in fs:
        if st.button(f,icon=":material/folder:"):
            print(st.session_state[root])
            st.session_state[root]=os.path.join(st.session_state[root],f)
            print(st.session_state[root])
            #final_value=False
            st.session_state.x=False
            st.rerun(scope='fragment')

    if st.button('select'):
        selected_folder = st.session_state[root]
        st.session_state.x=True
        st.rerun(scope='app')
        
        #return selected_folder
        
    
if __name__ == '__main__':
    x=1
    if st.button('run'):
        x=folder_selector()
    print(st.session_state[root],x,'thiz iz X')
    # You can call any Streamlit command, including custom components:
    

