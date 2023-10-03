# https://docs.streamlit.io/library/api-reference/chat/st.chat_message
import streamlit as st
from leroLero import LeroLero

# Corpo da página
st.set_page_config('🐍💣 ChatVSF','☠')
st.title("☠🐍💣 ChatVSF")
st.caption("Chatbot Powered by Dirty Mount")

# monta área de chat
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Como Posso te Ajudar?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# recebe input do usuário
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # gera resposta aleatória do gerador de lero-lero
    msg = {"role": "assistant", "content": LeroLero()}
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg["content"])
