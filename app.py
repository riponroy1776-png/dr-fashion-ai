import streamlit as st
import google.generativeai as genai
from PIL import Image

# আপনার Gemini API Key এখানে বসানো হয়েছে
genai.configure(api_key="AIzaSyAMeh3S8Gl9h5vv9e4NFOuutashyz0jJTg")

# অ্যাপের ইন্টারফেস সেটআপ
st.set_page_config(page_title="DR Fashion AI", page_icon="👕")
st.title("👕 DR Fashion Ads Funnel AI")
st.write("টি-শার্টের ছবি আপলোড করুন এবং আকর্ষণীয় ফেসবুক অ্যাড কপি তৈরি করুন।")

# ছবি আপলোড করার অপশন
uploaded_file = st.file_uploader("আপনার টি-শার্টের ছবি বাছুন...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='প্রোডাক্টের ছবি', use_container_width=True)
    
    if st.button("অ্যাড কপি তৈরি করুন"):
        with st.spinner('এআই কাজ করছে...'):
            try:
                # মডেল কল করা
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # আপনার ব্যবসার জন্য কাস্টমাইজড প্রম্পট
                prompt = """
                এই ছবিটি বিশ্লেষণ করে ফেসবুকের জন্য একটি হাই-কনভার্সন অ্যাড কপি লেখো। 
                উল্লেখ করো: এটি DR Fashion-এর ২২০ GSM প্রিমিয়াম কটন ফেব্রিক এবং হাই-কোয়ালিটি ডিটিএফ প্রিন্ট। 
                অফার প্রাইস: মাত্র ৩৯৯ টাকা। 
                ডেলিভারি: সারা বাংলাদেশে ক্যাশ অন ডেলিভারি। 
                কল টু অ্যাকশন: সরাসরি হোয়াটসঅ্যাপে (01604831776) অর্ডার করুন অথবা drfashion.shop ভিজিট করুন।
                লেখাটি ইমোজি দিয়ে সাজিয়ে লিখবে।
                """
                
                response = model.generate_content([prompt, image])
                st.success("আপনার অ্যাড কপি তৈরি হয়ে গেছে:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"দুঃখিত, একটি সমস্যা হয়েছে: {e}")
