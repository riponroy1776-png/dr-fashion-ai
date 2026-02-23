import streamlit as st
import google.generativeai as genai
from PIL import Image

# আপনার API Key
genai.configure(api_key="AIzaSyAMeh3S8Gl9h5vv9e4NFOuutashyz0jJTg")

st.title("👕 DR Fashion Ads Funnel AI")
st.write("আপনার ড্রপ শোল্ডার টি-শার্টের ছবি দিন, আমি সেলস কপি লিখে দিচ্ছি।")

uploaded_file = st.file_uploader("টি-শার্টের ছবি দিন", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='প্রোডাক্টের ছবি', use_container_width=True)
    
    if st.button("অ্যাড কপি তৈরি করুন"):
        try:
            # সঠিক মডেল ভার্সন ব্যবহার করা হয়েছে
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = """
            এই টি-শার্টের ছবি দেখে ফেসবুকের জন্য একটি আকর্ষণীয় অ্যাড কপি লেখো। 
            ফিচার: ২২০ GSM প্রিমিয়াম ফেব্রিক, ডিটিএফ প্রিন্ট।
            দাম: ৩৯৯ টাকা। ডেলিভারি: সারা বাংলাদেশে ক্যাশ অন ডেলিভারি।
            অর্ডার: drfashion.shop অথবা হোয়াটসঅ্যাপে 01604831776।
            """
            response = model.generate_content([prompt, image])
            st.success("আপনার অ্যাড কন্টেন্ট তৈরি হয়ে গেছে:")
            st.write(response.text)
        except Exception as e:
            st.error(f"দুঃখিত, একটি সমস্যা হয়েছে: {e}")
