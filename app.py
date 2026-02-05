# به جای خط قبلی، این را بنویس:
number_str = st.text_input("Input Number:", value="77")

if st.button("Predict"):
    try:
        # تبدیل متن به عدد صحیح بزرگ بدون محدودیت رقم
        number = int(number_str) 
        
        collapse_point = (number % 16) * 577
        st.success(f"The number reaches Capture Point **{collapse_point}**")
        st.balloons()
    except ValueError:
        st.error("لطفاً فقط عدد وارد کنید!")
