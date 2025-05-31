# 🤖 Chatbot Gemma 3:1b via LangChain + Ollama + Streamlit

## Deskripsi
Proyek ini menampilkan integrasi model AI lokal dari Ollama (gemma3:1b) ke dalam bentuk web interaktif menggunakan Streamlit dan LangChain. Chatbot ini mampu menerima input pengguna dan merespons secara natural.

## Penjelasan file
- `1-streamlit-app.py`
  - Versi sederhana yang hanya menampilkan input dan output tanpa memori.

- `2-streamlit-app-memory.py`
  - Versi dengan chat history (memory) menggunakan st.session_state.

- `chatbot.py`
  - Versi final: integrasi dengan model gemma3:1b dari Ollama menggunakan langchain_ollama dan support memory.

## Langkah Instalasi dan Cara Menjalankan Chatbot
1. Clone repository
2. Buat virtual environment (opsional)
3. Install dependencies: `pip install -r requirements.txt`
4. Install [Ollama](https://ollama.com/)
5. Jalankan di terminal: `ollama run gemma3:1b`
6. Jalankan aplikasi dengan command: `streamlit run chatbot.py`

## Fitur
1. Chat UI berbasis Streamlit
2. Support memory/chat history
3. Terintegrasi dengan LLM lokal via Langchain
4. Role System: Bot berperan sebagai asisten programmer bernama Arvin AI

