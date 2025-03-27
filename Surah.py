"""
Author: Zain Nomani
Date: 27/3/2025
Description: Handle the Surah, parsing, etc
"""
import requests

class Surah:

    def __init__(self):
        pass

    def getSurah(self, x: int) -> dict:
        """Get Surah Arabic and English as dictionary"""
        if x < 1 or x > 114:
            return {
                "status": 400
            }
        df = []
        try:
            url = f"http://api.alquran.cloud/v1/surah/{x}/quran-uthmani"
            response = requests.get(url)
            translation = requests.get(f"http://api.alquran.cloud/v1/surah/{x}/en.asad")
            response.raise_for_status()
            translation.raise_for_status()
        except:
            return [{
                "Arabic": "API Error",
                "English": "Please try again later"
            }]
        ordered = response.json()
        trans = translation.json()
        data = ordered["data"]["ayahs"]
        tran = trans["data"]["ayahs"]
        if len(data) != len(tran):
            print("Error!")
        else:
            n = len(data)
            for i in range(n):
                df.append({
                    "Arabic": data[i]["text"],
                    "English": tran[i]["text"]
                })
        return df