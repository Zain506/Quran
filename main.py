"""
Author: Zain Nomani
Date: 27/3/2025
Description: Qur'an web app integrated with AI to better understand meanings

Test by running "streamlit run main.py" in terminal to test
"""
import streamlit as st
from Surah import Surah
x: int = 2
st.title(f"Chapter {x}")
surah: dict = Surah().getSurah(x)
for index, item in enumerate(surah):
    st.title(str(index) + " " + item["Arabic"])
    st.write(item["English"])