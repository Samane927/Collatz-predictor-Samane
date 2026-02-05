import streamlit as st

st.title("Saeidi's Predictor")
st.subheader("Inventor: Samaneh Saeidi")

user_input = st.text_input("Enter number:", value="13")

if st.button("Find Collapse Point"):
    try:
        n = int(user_input)
        original_n = n
        step_count = 0
        collapse_point = None
        
        # محاسبه برای پیدا کردن اولین مضرب 16
        current = n
        while current > 1:
            if current % 16 == 0:
                collapse_point = current
                break
            
            step_count += 1
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
        
        # اگر عدد از اول مضرب 16 باشد یا در مسیر به آن برسد
        if current % 16 == 0:
            collapse_point = current

        st.divider()
        
        # نمایش دقیق دو موردی که خواستی
        if collapse_point:
            st.success(f"Collapse Value: {collapse_point}")
            st.info(f"At Step: {step_count}")
        else:
            st.write("Reached 1 without hitting a specific 16-multiple.")
            
    except ValueError:
        st.error("Please enter a valid number.")
