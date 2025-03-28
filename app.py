import streamlit as st

st.title("IP address demo")

st.write(
    f"Your real IP address (based on https://checkip.amazonaws.com/) is: {st.context.ip_address}"
)

x = st.slider("Slider for interactivity", 0, 100, 50)
st.write(f"X squared is {x**2}")

st.write(
    "WHEEL FILE LINK: https://core-previews.s3-us-west-2.amazonaws.com/pr-10927/streamlit-1.44.0-py3-none-any.whl"
)
