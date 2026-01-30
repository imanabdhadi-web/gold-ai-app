import streamlit as st
import google.generativeai as genai
from PIL import Image

# Ambil API Key dari Secrets Streamlit secara automatik
API_KEY = st.secrets["API_KEY"]
genai.configure(api_key=API_KEY)

st.title("📈 Gold AI Analyzer (Mobile)")

uploaded_file = st.file_uploader("Upload screenshot chart...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Analisis Chart...', use_container_width=True)
    
    if st.button("Dapatkan Entry"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = "Analisis gambar chart XAU/USD ini. Berikan: 1. Entry (Buy/Sell), 2. SL, 3. TP, 4. Volume (Besar/Kecil), 5. Tahap Keyakinan. Gunakan format yang kemas."
        response = model.generate_content([prompt, image])
        st.write(response.text)
      
