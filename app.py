import streamlit as st

# تنظیمات صفحه
st.set_page_config(page_title="Collatz Predictor", page_icon="🔮")

st.title("Saeidi's Collatz Predictor")
st.subheader("Inventor: Samaneh Saeidi")

st.write("Enter a number to see its collapse point.")

# استفاده از text_input برای پشتیبانی از عددهای خیلی بزرگ بدون خطا
number_str = st.text_input("Input Number:", value="13")

if st.button("Predict"):
    if number_str:
        try:
            # تبدیل متن به عدد صحیح (Integer) برای دقت بی‌نهایت
            number = int(number_str)
            
            # محاسبه نقطه شکست بر اساس منطق سمانه
            collapse_point = (number % 16) * 577
            
            st.success(f"The number reaches Capture Point **{collapse_point}**")
            st.balloons()
            
        except ValueError:
            st.error("Please enter a valid whole number (no letters or dots).")
    else:
        st.warning("Please enter a number first.")
