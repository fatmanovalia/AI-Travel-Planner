import streamlit as st

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Travel Planner")

st.write("Selamat datang di aplikasi AI Travel Planner")

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

if st.button("Generate Travel Plan"):
    st.success("Input berhasil diterima!")

    st.write("### Data Perjalanan")
    st.write(f"📍 Kota: {kota}")
    st.write(f"💰 Budget: {budget}")
    st.write(f"📅 Durasi: {durasi} hari")
    st.write(f"🎯 Jenis Wisata: {jenis_wisata}")