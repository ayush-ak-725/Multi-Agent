import streamlit as st
import requests

st.title("Multi-Agent Research")

topic = st.text_input("Enter topic")

if st.button("Run"):
    res = requests.post(
        "http://127.0.0.1:8000/run",
        params={"topic": topic}
    )

    data = res.json()

    st.write("### Report")
    st.write(data["report"])

    st.write("### Critique")
    st.write(data["feedback"])