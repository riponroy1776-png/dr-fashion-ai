import streamlit as st
import google.generativeai as genai
from PIL import Image

# আপনার API Key
genai.configure(api_key="AIzaSyAMeh3S8Gl9h5vv9e4NFOuutashyz0jJTg")

st.set_page_config(page_title="DR Fashion AI", page_icon="👕")
st.title("👕 DR Fashion Ads Funnel AI")
st.write("টি-শার্টের ছবি আপলোড করুন এবং আকর্ষণীয় অ্যাড কপি তৈরি করুন।")

uploaded_file = st.file_uploader("ছবি বাছুন...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='আপলোড করা প্রোডাক্ট', use_container_width=True)
    
    if st.button("অ্যাড কপি তৈরি করুন"):
        with st.spinner('এআই ভাবছে...'):
            try:
                # মডেলের সঠিক নাম ব্যবহার করা হয়েছে
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                prompt = """
                এই ছবিটি বিশ্লেষণ করে ফেসবুকের জন্য একটি হাই-কনভার্সন অ্যাড কপি লেখো। 
                উল্লেখ করো: এটি DR Fashion-এর ২২০ GSM প্রিমিয়াম ফেব্রিক এবং ডিটিএফ প্রিন্ট। 
                অফার প্রাইস: মাত্র ৩৯৯ টাকা। 
                ডেলিভারি: সারা বাংলাদেশে ক্যাশ অন ডেলিভারি। 
                কল টু অ্যাকশন: সরাসরি হোয়াটসঅ্যাপে (01604831776) অর্ডার করতে বলো অথবা drfashion.shop ভিজিট করতে বলো।
                """
                
                response = model.generate_content([prompt, image])
                st.success("আপনার অ্যাড কন্টেন্ট তৈরি হয়ে গেছে:")
                st.write(response.text)
            except Exception as e:
                st.error(f"দুঃখিত, একটি সমস্যা হয়েছে: {e}")
