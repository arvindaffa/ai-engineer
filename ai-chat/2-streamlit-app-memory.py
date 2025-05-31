import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.title("Chatbot")

# init chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# display chat messages from history on app
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    
    if isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)
            
# Create input user message
prompt = st.chat_input("Ketik sesuatu...")

if prompt:
    # add prompt to screen
    with st.chat_message("user"):
        st.markdown(prompt)
        
        st.session_state.messages.append(HumanMessage(prompt))
        
    response = f"Kamu barusan bilang {prompt}"
    
    with st.chat_message("assistant"):
        st.markdown(response)
        
        st.session_state.messages.append(AIMessage(response))