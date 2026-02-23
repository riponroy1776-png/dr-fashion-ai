import streamlit as st
import google.generativeai as genai
from PIL import Image

# আপনার API Key
genai.configure(api_key="AIzaSyAMeh3S8Gl9h5vv9e4NFOuutashyz0jJTg")

st.title("👕 DR Fashion Ads Funnel AI")
uploaded_file = st.file_uploader("টি-শার্টের ছবি দিন", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)
    if st.button("অ্যাড কপি তৈরি করুন"):
        try:
            # এখানে নাম পরিবর্তন করে 'gemini-1.5-flash-latest' দেওয়া হয়েছে
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            prompt = "এই টি-শার্টের ছবির জন্য ৩৯৯ টাকা দাম এবং ২২০ GSM ফেব্রিক উল্লেখ করে একটি আকর্ষণীয় ফেসবুক অ্যাড কপি লেখো।"
            response = model.generate_content([prompt, image])
            st.write(response.text)
        except Exception as e:
            st.error(f"দুঃখিত, সমস্যাটি হলো: {e}")
