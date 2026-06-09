import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key dari .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
st.write("API Key ditemukan:", api_key is not None)
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# Konfigurasi halaman
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Travel Planner")

st.write("Rencanakan perjalanan wisata dengan bantuan AI")

# Input
kota = st.text_input("📍 Kota Tujuan")

budget = st.selectbox(
    "💰 Budget",
    [
        "< Rp1.000.000",
        "Rp1.000.000 - Rp3.000.000",
        "Rp3.000.000 - Rp5.000.000",
        "> Rp5.000.000"
    ]
)

durasi = st.number_input(
    "📅 Durasi Perjalanan (Hari)",
    min_value=1,
    max_value=14,
    value=3
)

jenis_wisata = st.selectbox(
    "🎯 Jenis Wisata",
    [
        "Alam",
        "Kuliner",
        "Sejarah",
        "Belanja",
        "Hiburan"
    ]
)

transportasi = st.selectbox(
    "🚗 Transportasi Utama",
    ["Mobil", "Kereta", "Pesawat", "Bus"]
)

bulan = st.selectbox(
    "🌤️ Bulan Perjalanan",
    [
        "Januari","Februari","Maret",
        "April","Mei","Juni",
        "Juli","Agustus","September",
        "Oktober","November","Desember"
    ]
)

mode_perjalanan = st.selectbox(
    "👨‍👩‍👧‍👦 Tipe Perjalanan",
    [
        "Solo",
        "Pasangan",
        "Keluarga",
        "Teman"
    ]
)

# Tombol Generate
if st.button("✨ Generate Travel Plan"):

    prompt = f"""
    Buatkan travel planner yang detail.

    Kota tujuan: {kota}
    Budget: {budget}
    Durasi: {durasi} hari
    Jenis wisata: {jenis_wisata}
    Transportasi: {transportasi}
    Bulan perjalanan: {bulan}
    Tipe perjalanan: {mode_perjalanan}

    Berikan:
    1. Ringkasan perjalanan
    2. Itinerary harian
    3. Tempat wisata rekomendasi
    4. Kuliner yang wajib dicoba
    5. Rekomendasi transportasi lokal
    6. Rekomendasi penginapan
    7. Hidden gem
    8. Estimasi biaya
    9. Checklist barang bawaan
    10. Tips perjalanan
    """

try:
    with st.spinner("Membuat itinerary..."):
        response = model.generate_content(prompt)

    st.success("Travel Plan Berhasil Dibuat!")

    st.subheader("📋 Detail Perjalanan")

    st.markdown(f"""
    - 📍 **Kota Tujuan:** {kota}
    - 💰 **Budget:** {budget}
    - 📅 **Durasi:** {durasi} Hari
    - 🎯 **Jenis Wisata:** {jenis_wisata}
    - 👨‍👩‍👧‍👦 **Tipe Perjalanan:** {mode_perjalanan}
    """)

    st.markdown(response.text)

    st.download_button(
        label="📥 Download Itinerary",
        data=response.text,
        file_name="travel_plan.txt",
        mime="text/plain"
    )

except Exception as e:
    st.error(
        "Server AI sedang sibuk atau kuota sementara tercapai. Silakan tunggu beberapa saat lalu coba lagi."
    )