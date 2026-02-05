import streamlit as st

st.title("Saeidi's Predictor")
st.write("Inventor: Samaneh Saeidi")

# گرفتن عدد به صورت متن برای جلوگیری از خطای اولیه
user_input = st.text_input("Enter your large number:", value="13")

if st.button("Find Collapse Point"):
    try:
        # تبدیل مستقیم به عدد بزرگ
        n = int(user_input)
        step_count = 0
        current = n
        found = False
        
        # حلقه محاسباتی فوق سریع و سبک
        while current > 1:
            if current % 16 == 0:
                st.success("🎯 Target Found!")
                st.write("**Collapse Value:**")
                # استفاده از st.text برای اینکه عدد غول‌آسا باعث Overflow نشود
                st.text(str(current))
                st.info(f"**At Step:** {step_count}")
                found = True
                break
            
            step_count += 1
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
        
        if not found:
            st.write("Reached 1 without hitting a 16-multiple.")
            
    except Exception as e:
        st.error("Error: Please enter only digits without spaces.")
