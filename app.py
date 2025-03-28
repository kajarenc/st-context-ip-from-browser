import streamlit as st

st.title("IP address demo")

st.write(
    f"Your real IP address (based on https://checkip.amazonaws.com/) is: {st.context.ip_address}"
)

x = st.slider("Select a number", 0, 100, 50)
st.write(f"X squared is {x**2}")
