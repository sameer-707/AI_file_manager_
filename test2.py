import streamlit as st

def page2():
    st.title("Second page")

    toggle_label = (
        "The toggle is ON"
        if st.session_state.get("my_toggle", False)
        else "The toggle is OFF"
    )
    toggle_value = st.session_state.get("my_toggle", False)

    is_toggle = st.toggle(toggle_label, value=toggle_value, key="my_toggle")
    st.info(f"The toogle is {is_toggle}")

pg = st.navigation([
    st.Page("gui_main.py", title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
    #st.Page('test3.py', title='third page',icon="🤖")
])


pg.run()