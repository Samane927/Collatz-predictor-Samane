import streamlit as st

st.set_page_config(page_title="Saeidi's Predictor", page_icon="🎯")
st.title("Saeidi's Collapse Predictor")
st.write("Inventor: Samaneh Saeidi")

user_input = st.text_input("Enter a large number:", value="13")

if st.button("Analyze"):
    try:
        n = int(user_input)
        original_n = n
        path = []
        
        # مرحله اول: پیدا کردن نقطه فروپاشی (مضرب ۱۶)
        while n > 1:
            path.append(n)
            if n % 16 == 0:
                break
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        
        # نمایش نتیجه اصلی
        st.divider()
        if path[-1] % 16 == 0:
            st.error(f"🎯 **Collapse Point Reached:** {path[-1]}")
            
            # --- کادر جدید برای ادامه مسیر (سقوط آزاد) ---
            st.subheader("📉 Post-Collapse Descent (The 16-Rule):")
            descent_path = []
            current = path[-1]
            # محاسبه ۴ مرحله سقوط حتمی (چون مضرب ۱۶ است، حداقل ۴ بار بر ۲ تقسیم می‌شود)
            for _ in range(4):
                current //= 2
                descent_path.append(current)
            
            st.info(f"Next 4 guaranteed steps: {' ➔ '.join(map(str, descent_path))}")
            st.write("Since it hit a multiple of 16, it is now diving towards 1.")
            # ------------------------------------------
            
            st.success(f"The number {str(original_n)[:10]}... is in total collapse.")
        
        with st.expander("Show full calculation steps"):
            st.write(path)

    except ValueError:
        st.error("Please enter a valid number.")
