"""
Author: Zain Nomani
Date: 27/3/2025
Description: Qur'an web app integrated with AI to better understand meanings

Test by running "streamlit run main.py" in terminal to test
"""
import streamlit as st
from Surah import Surah
x: int = st.slider("Select a Chapter", min_value = 1, max_value = 114, value = 1)


st.title(f"Chapter {x}")
surah: dict = Surah().getSurah(x)



for index, item in enumerate(surah):
    st.divider()
    col1, col2 = st.columns([5, 2])
    with col2:
        if st.button(f"Query verse {index + 1}", key = index):
            st.write("Button clicked")
    
    with col1:
        arabic = item["Arabic"]
        st.title(arabic)
        st.write(item["English"])