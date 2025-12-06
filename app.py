import streamlit as st
import pandas as pd
import joblib
import os
import requests
from datetime import datetime
from config import MODEL_PATH

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="Walmart Satış Tahmin Sistemi",
    page_icon="🛒",
    layout="centered"
)

MODEL_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=1fZ0UAsVXTFWsuPYdSfUJmBFtpPdDhA-H"

# 2. Modeli Yükleme Fonksiyonu

@st.cache_resource
def load_model():

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    # Model indirme
    if not os.path.exists(MODEL_PATH):
        st.warning("Model dosyası bulunamadı.")

        try:
            r = requests.get(MODEL_DOWNLOAD_URL, stream=True)
            with open(MODEL_PATH, "wb") as f:
                f.write(r.content)
            st.success("Model başarıyla indirildi.")
        except Exception as e:
            st.error(f"İndirme hatası: {e}")
            return None

    # Modeli yükle
    return joblib.load(MODEL_PATH)

model = load_model()

# 3. Başlık ve Açıklama
st.title(" Walmart Haftalık Satış Tahmini")
st.markdown("""
Bu proje, makine öğrenmesi kullanarak Walmart mağazalarının haftalık satışlarını tahmin eder.
""")
st.markdown("---")

# 4. Kullanıcı Girdileri
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        store_id = st.number_input("Mağaza No (Store ID)", min_value=1, max_value=45, value=1)
        dept_id = st.number_input("Departman No (Dept ID)", min_value=1, max_value=99, value=1)
        store_type = st.selectbox("Mağaza Tipi (Type)", ["A", "B", "C"])
        store_size = st.number_input("Mağaza Boyutu (Size)", min_value=1000, max_value=250000, value=150000)

    with col2:
        date_input = st.date_input("Tarih", datetime(2012, 10, 26))
        temperature = st.slider("Sıcaklık (Temperature)", -10.0, 110.0, 60.0)
        fuel_price = st.number_input("Yakıt Fiyatı (Fuel Price)", 2.0, 6.0, 3.5)
        cpi = st.number_input("TÜFE (CPI)", 100.0, 250.0, 190.0)
        unemployment = st.number_input("İşsizlik Oranı (%)", 0.0, 15.0, 8.0)

    # İndirimler
    with st.expander("Promosyon / İndirim Bilgileri (Opsiyonel)"):
        md1 = st.number_input("MarkDown 1", 0.0, value=0.0)
        md2 = st.number_input("MarkDown 2", 0.0, value=0.0)
        md3 = st.number_input("MarkDown 3", 0.0, value=0.0)
        md4 = st.number_input("MarkDown 4", 0.0, value=0.0)
        md5 = st.number_input("MarkDown 5", 0.0, value=0.0)

    # Tahmin Butonu
    submit_btn = st.form_submit_button(" Satışı Tahmin Et")

# 5. Tahmin İşlemi
if submit_btn and model is not None:
    # A) Feature Engineering

    # Tarih parçalama
    selected_date = pd.to_datetime(date_input)
    week = selected_date.isocalendar().week
    month = selected_date.month
    year = selected_date.year


    # Tatil Tipi Belirleme
    def get_holiday_type_simple(date_val):
        d_str = str(date_val).split(' ')[0]
        # Örnek tatil tarihleri
        if d_str in ['2012-02-10', '2013-02-08']: return 1  # Super Bowl
        if d_str in ['2012-09-07', '2013-09-06']: return 2  # Labor Day
        if d_str in ['2012-11-23', '2013-11-29']: return 3  # Thanksgiving
        if d_str in ['2012-12-28', '2013-12-27']: return 4  # Christmas
        return 0


    holiday_type = get_holiday_type_simple(selected_date)

    # Type Encoding
    type_mapping = {"A": 3, "B": 2, "C": 1}
    type_encoded = type_mapping[store_type]

    # B) DataFrame Oluşturma
    input_data = pd.DataFrame({
        'Store': [store_id],
        'Dept': [dept_id],
        'Type_Encoded': [type_encoded],
        'Size': [store_size],
        'Week': [week],
        'Month': [month],
        'Year': [year],
        'Holiday_Type': [holiday_type],
        'Temperature': [temperature],
        'Fuel_Price': [fuel_price],
        'CPI': [cpi],
        'Unemployment': [unemployment],
        'MarkDown1': [md1],
        'MarkDown2': [md2],
        'MarkDown3': [md3],
        'MarkDown4': [md4],
        'MarkDown5': [md5]
    })

    # C) Tahmin
    try:
        prediction = model.predict(input_data)[0]

        # Sonucu Gösterme
        st.success(f" Tahmini Haftalık Satış: **${prediction:,.2f}**")

        st.info(" Not: Bu tahmin; mağaza boyutu, geçmiş satış trendleri ve mevsimsellik verilerine dayanmaktadır.")

    except Exception as e:
        st.error(f"Hata oluştu: {e}")