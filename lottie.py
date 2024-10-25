# Import necessary packages
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

# Define a function to load the Lottie JSON from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the Lottie animation JSON data
lottie_hello = load_lottieurl("https://lottie.host/5046f9ab-7e6e-48c2-bcc8-90d4f0bafb6f/FR6O1VwLt0.json")

# Display the animation if successfully loaded
if lottie_hello:
    st_lottie(lottie_hello, height=200, width=200, key="hello_animation")
else:
    st.write("Failed to load animation")






# lokaliai
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
