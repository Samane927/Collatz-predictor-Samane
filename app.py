import streamlit as st

st.title("Saeidi's Collatz Predictor")
st.write("Inventor: Samaneh Saeidi")

# ورودی به صورت متن برای جلوگیری از رند شدن اعداد بزرگ
user_input = st.text_input("Enter your number:", value="13")

if st.button("Predict"):
    try:
        # تبدیل متن به عدد صحیح
        val = int(user_input)
        result = (val % 16) * 577
        st.success(f"Capture Point: {result}")
        st.balloons()
    except:
        st.error("Please enter a valid number.")
