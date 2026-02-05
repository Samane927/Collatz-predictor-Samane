import streamlit as st

st.set_page_config(page_title="Saeidi's Predictor", page_icon="🎯")
st.title("Saeidi's Collapse Predictor")
st.subheader("Inventor: Samaneh Saeidi")

user_input = st.text_input("Enter a large number:", value="1245876325458968742668878")

if st.button("Analyze"):
    try:
        # پاکسازی ورودی
        clean_n = user_input.replace(",", "").replace(" ", "")
        n = int(clean_n)
        original_n = str(n)
        step_count = 0
        current = n
        
        # پیدا کردن نقطه فروپاشی (مضرب 16)
        while current > 1:
            if current % 16 == 0:
                break
            step_count += 1
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
        
        st.divider()
        
        if current % 16 == 0:
            st.error(f"### Collapse Point Reached:")
            st.code(str(current))
            st.info(f"**Step Number:** {step_count}")
            
            st.markdown("### 📉 Post-Collapse Descent (The 16-Rule):")
            st.write("Next 4 guaranteed steps:")
            
            # محاسبه 4 قدم قطعی بعد از مضرب 16
            next_step = current
            for i in range(4):
                next_step //= 2
                st.write(f"**{i+1}:** {next_step}")
                
            st.warning("Since it hit a multiple of 16, it is now diving towards 1.")
            st.success(f"The number {original_n[:10]}... is in total collapse.")
        else:
            st.write("Reached 1 without hitting a 16-multiple.")

    except Exception as e:
        st.error(f"Error: {e}")
