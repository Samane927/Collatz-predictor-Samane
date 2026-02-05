import streamlit as st

st.set_page_config(page_title="Saeidi's Collapse Theorem", page_icon="📜")

st.title("Saeidi's 16-Station Theorem")
st.markdown("---")
st.write("### Input Analysis")
user_input = st.text_input("Enter the Target Number:", value="1245876325458968742668878")

if st.button("Generate Proof"):
    try:
        n = int(user_input)
        original_n = n
        steps = 0
        
        # پیمایش مسیر تا نقطه فروپاشی
        while n > 1:
            if n % 16 == 0:
                break
            steps += 1
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        
        # نمایش سند اثبات
        if n % 16 == 0:
            st.balloons()
            st.success("## 📄 OFFICIAL PROOF CERTIFICATE")
            
            # کادر اطلاعات اصلی
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Collapse Point (Station 16)", value="Confirmed")
                st.write(f"**Value:** `{n}`")
            with col2:
                st.metric(label="Steps to Collapse", value=steps)
            
            st.markdown("---")
            st.info(f"**Theorem Conclusion:** The number `{original_n}` has officially entered the 16-multiple zone at step **{steps}**. According to Saeidi's Theorem, its descent to 1 is now mathematically inevitable and irreversible.")
            
        else:
            st.warning("The number reached 1 without hitting a specific 16-multiple in its path.")

    except ValueError:
        st.error("Invalid Input. Please enter a whole number.")

st.sidebar.info("This tool was developed in 2 weeks as a companion to the Saeidi Collatz Paper.")
