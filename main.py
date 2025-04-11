"""
Author: Zain Nomani
Date: 27/3/2025
Description: Qur'an web app integrated with AI to better understand meanings

Test by running "streamlit run main.py" in terminal to test
"""
import streamlit as st
from Surah import Surah
import json
with open("surahList.json", "r") as file:
    surahs = json.load(file)
    surah_list = surahs["surah_list"]
tab_names = [
    "Qur'an",
    "Vocabulary Bank"
]
chapter = st.sidebar.radio(
        label = "Chapters",
        options = surah_list
        )

tabs = st.tabs(tab_names)

with tabs[0]: # Qur'an Tab
    x = int(chapter.split()[0])
    st.title(chapter)
    if x != 9: # Remove Bismillah from Surah Tawbah
        st.divider()
        st.image("bismillah-5786134_1280.png")
    surah: dict = Surah().getSurah(x)
    for index, item in enumerate(surah):
        # Surah Fatihah has slightly different format - includes Bismillah in 1st verse
        if x != 1:
            index += 1
        if x == 1 and index == 0:
            continue
        st.divider()
        # Set 2 columns: 1 for index and 1 for Arabic verse as a title
        col, col1 = st.columns([1, 5])
        with col:
            st.title(index)
        with col1:
            arabic = item["Arabic"]
            if "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ" in arabic:
                arabic = arabic.replace("بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ", "").strip()
            st.title(arabic)
            # Create expandable block with text being supplied translation
            text = item["English"]
            more = st.expander(f"{text}")
            # Text to display below verse
            more.write("Info will be presented in the form {root: {derivation: meaning,...},...}")
