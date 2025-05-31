import streamlit as st

# Create input user message
prompt = st.chat_input("Ketik sesuatu...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        st.markdown(f"Kamu barusan bilang {prompt}")