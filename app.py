import streamlit as st

# تنظیمات ظاهری صفحه
st.set_page_config(page_title="Collatz Predictor", page_icon="🔮")

st.title("Saeidi's Collatz Predictor")
st.subheader("Inventor: Samaneh Saeidi")

# حذف عبارت Modulo 16 برای حفظ راز الگوریتم
st.write("Enter a number to see its collapse point.")

number = st.number_input("Input Number:", min_value=1, value=77, step=1)

if st.button("Predict"):
    # محاسبات مخفی پشت صحنه
    collapse_point = (number % 16) * 577  # یا هر فرمولی که خودت داشتی
    # اینجا فقط نتیجه رو نشون میدیم بدون لو دادن روش محاسبه
    st.success(f"The number reaches Capture Point **{collapse_point}**")
    st.balloons() # یه افکت قشنگ برای وقتی که پیش‌بینی انجام میشه
