import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama

st.title("Gemma3:1b Chatbot")

# init chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    st.session_state.messages.append(SystemMessage("Jadilah seorang asisten programmer untuk saya. Namamu adalah Arvin AI"))
    
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
    
    llm = ChatOllama(
        model="gemma3:1b",
        temperature=0.3
    )
        
    response = llm.invoke(st.session_state.messages).content
    
    with st.chat_message("assistant"):
        st.markdown(response)
        
        st.session_state.messages.append(AIMessage(response))