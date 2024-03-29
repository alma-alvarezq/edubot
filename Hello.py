import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
import json
import requests

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append({'message': user_input, 'is_user': True})
    url ='https://6630-2806-2f0-4060-c5c1-dcb6-9a93-f6ed-4c79.ngrok-free.app/database'
    question = {'Question' : user_input}
    headers = {'ngrok-skip-browser-warning': 'true', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=question)
    print("JSON Response ", response)

    msg = json.loads(response.text)
    st.session_state.past.append({'message': msg['message'], 'is_user': False})
    st.session_state.user_input = ""


def on_btn_click():
    st.session_state.past.clear()

st.session_state.setdefault(
    'past',[]
)

st.session_state.setdefault(
    'generated', []
)

st.title("ChatBot")

chat_placeholder = st.empty()

index = 0
for item in st.session_state.past:
    if isinstance(item, dict):
        message(item['message'], is_user=item['is_user'], key=f"{index}_user")
        index = index + 1

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")

if st.button("Clear History"):
    on_btn_click()

