import streamlit as st
import google.generativeai as genai
from PIL import Image

# Tetapan API Key dari Secrets
try:
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("Ralat: API_KEY tidak dijumpai dalam Streamlit Secrets!")

st.set_page_config(page_title="Gold AI Analyzer", layout="centered")
st.title("📈 Gold AI Analyzer (Mobile)")
st.write("Analisis XAU/USD Pantas")

# Upload Gambar
uploaded_file = st.file_uploader("Upload screenshot chart...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Chart anda sedang diproses...', use_container_width=True)
    
    if st.button("Dapatkan Entry Sekarang"):
        with st.spinner('AI sedang mengira setup...'):
            try:
                # Gunakan format nama model penuh untuk elakkan ralat NotFound
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = """
                Bertindak sebagai pakar trader XAU/USD. Lihat screenshot chart ini dan berikan:
                - Entry (Buy/Sell)
                - SL (Stop Loss)
                - TP (Take Profit)
                - Volume Pasaran (Besar/Kecil)
                - Tahap Keyakinan (%)
                - Analisis Ringkas (Sebab Entry)
                Gunakan format yang kemas dalam Bahasa Melayu.
                """
                
                response = model.generate_content([prompt, image])
                st.subheader("Hasil Analisis:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Berlaku masalah: {str(e)}")

st.divider()
st.caption("Aplikasi peribadi Kopi Fry. Dagangan berisiko tinggi.")
