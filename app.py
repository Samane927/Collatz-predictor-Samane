import streamlit as st

def get_drop_point(n):
    current = n
    steps = 0
    while current != 1:
        if current % 16 == 0:
            return current, steps
        current = (current * 3 + 1) if current % 2 != 0 else (current // 2)
        steps += 1
    return 1, steps

st.set_page_config(page_title="Collatz Predictor", page_icon="🔢")
st.title("Saeidi's Collatz Predictor")
st.markdown("### Inventor: **Samaneh Saeidi**")
st.write("Enter a number to see its collapse point (Modulo 16).")

num = st.number_input("Input Number:", min_value=1, value=27, step=1)

if st.button("Predict"):
    point, step = get_drop_point(num)
    st.success(f"The number reaches Capture Point **{point}** at Step **{step}**")
    st.balloons()
