import streamlit as st

# تنظیمات ظاهری صفحه
st.set_page_config(page_title="Saeidi's Predictor", page_icon="💥")

st.title("Saeidi's Collatz Predictor")
st.subheader("Inventor: Samaneh Saeidi")
st.write("Finding the exact moment a number hits a multiple of 16 and collapses.")

# ورودی متن برای پشتیبانی از اعداد بی‌نهایت بزرگ
user_input = st.text_input("Enter a large number:", value="13")

if st.button("Analyze Collapse"):
    if user_input:
        try:
            n = int(user_input)
            original_n = n
            path = []
            hit_16_multiple = False
            
            # حلقه اصلی برای پیدا کردن مسیر فروپاشی
            while n > 1:
                path.append(n)
                
                # بررسی قانون طلایی سمانه: مضرب ۱۶
                if n % 16 == 0:
                    hit_16_multiple = True
                    break
                
                # محاسبات کلاتز
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3 * n + 1
            
            if not hit_16_multiple:
                path.append(n)

            # نمایش نتیجه
            st.divider()
            if hit_16_multiple:
                st.error(f"🎯 **BOOM!** Hit a multiple of 16: **{path[-1]}**")
                st.success(f"The number **{original_n}** is now in a total collapse.")
            else:
                st.success(f"The number reached 1.")

            # نمایش نمودار سقوط
            st.line_chart(path)
            
            # نمایش گام‌به‌گام مسیر
            with st.expander("See full path steps"):
                st.write(" ➔ ".join(map(str, path)))
                
        except ValueError:
            st.error("Please enter a valid whole number without dots or letters.")
    else:
        st.warning("Please enter a number first.")
import streamlit as st

# تنظیمات ظاهری صفحه
st.set_page_config(page_title="Saeidi's Predictor", page_icon="💥")

st.title("Saeidi's Collatz Predictor")
st.subheader("Inventor: Samaneh Saeidi")
st.write("Finding the exact moment a number hits a multiple of 16 and collapses.")

# ورودی متن برای پشتیبانی از اعداد بی‌نهایت بزرگ
user_input = st.text_input("Enter a large number:", value="13")

if st.button("Analyze Collapse"):
    if user_input:
        try:
            n = int(user_input)
            original_n = n
            path = []
            hit_16_multiple = False
            
            # حلقه اصلی برای پیدا کردن مسیر فروپاشی
            while n > 1:
                path.append(n)
                
                # بررسی قانون طلایی سمانه: مضرب ۱۶
                if n % 16 == 0:
                    hit_16_multiple = True
                    break
                
                # محاسبات کلاتز
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3 * n + 1
            
            if not hit_16_multiple:
                path.append(n)

            # نمایش نتیجه
            st.divider()
            if hit_16_multiple:
                st.error(f"🎯 **BOOM!** Hit a multiple of 16: **{path[-1]}**")
                st.success(f"The number **{original_n}** is now in a total collapse.")
            else:
                st.success(f"The number reached 1.")

            # نمایش نمودار سقوط
            st.line_chart(path)
            
            # نمایش گام‌به‌گام مسیر
            with st.expander("See full path steps"):
                st.write(" ➔ ".join(map(str, path)))
                
        except ValueError:
            st.error("Please enter a valid whole number without dots or letters.")
    else:
        st.warning("Please enter a number first.")
