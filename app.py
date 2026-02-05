import streamlit as st

# تنظیمات اصلی که باعث سنگینی سایت نمی‌شود
st.set_page_config(page_title="Saeidi's Predictor", page_icon="🎯")
st.title("Saeidi's Collapse Predictor")
st.subheader("Inventor: Samaneh Saeidi")

user_input = st.text_input("Enter a large number:", value="13")

if st.button("Analyze"):
    try:
        n = int(user_input)
        original_n = n
        path = []
        step_count = 0
        
        # منطق اصلی تئوری سمانه: حرکت تا رسیدن به مضرب ۱۶
        current = n
        while current > 1:
            path.append(current)
            if current % 16 == 0: # ایستگاه ۱۶
                break
            
            step_count += 1
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
        
        # نمایش خروجی دقیق و متنی (برای جلوگیری از OverflowError)
        st.divider()
        if path[-1] % 16 == 0:
            st.error(f"🎯 **Collapse Point Reached:** {path[-1]}")
            st.info(f"**Step Number:** {step_count}")
            st.success(f"The number {str(original_n)[:10]}... is in total collapse.")
            
        with st.expander("Show full path steps"):
            st.write(path)

    except ValueError:
        st.error("Please enter a valid number.")
