import streamlit as st

st.title("Saeidi's Chain Analysis")
st.subheader("Inventor: Samaneh Saeidi")

user_input = st.text_input("Enter your large number:", value="1245876325458968742668878")

if st.button("Start Chain Analysis"):
    try:
        n = int(user_input.replace(",", "").strip())
        current = n
        
        # مرحله اول: رسیدن به اولین عدد فرد
        if current % 2 == 0:
            st.write("### ⬇️ Step 1: Descending to the first Odd Number")
            while current % 2 == 0:
                current //= 2
            st.warning(f"First Odd Number in Chain: {current}")
        else:
            st.info(f"Started with an Odd Number: {current}")

        # مرحله دوم: تحلیل تئوری سمانه از عدد فرد تا مضرب 16
        st.write("---")
        st.write("### 🎯 Step 2: Finding Saeidi's 16-Station")
        
        steps = 0
        first_odd = current
        
        while current > 1:
            if current % 16 == 0:
                st.success(f"✅ Target 16 reached!")
                st.code(f"Station 16 Value: {current}")
                st.info(f"Steps from first odd number: {steps}")
                break
            
            steps += 1
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
                
    except Exception as e:
        st.error(f"Error: {e}")
