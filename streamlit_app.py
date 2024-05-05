import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Streamlit başlık ve logo
st.set_page_config(page_title="Thera Bank", page_icon=":bank:", layout="wide")

# Üst bilgi: logo ve portföy yöneticisi
col1, col2, col3 = st.columns([1, 6, 2])
with col1:
    st.image("indir.jpeg", width=100)  # Logo yolu güncellenmeli
with col2:
    st.markdown("<h1 style='text-align: center; color: purple;'>Thera Bank</h1>", unsafe_allow_html=True)
with col3:
    st.markdown("#### Bireysel Portföy Yöneticisi: Gizem Kule")

# Modeli yüklemek
model = joblib.load('finalized_model.joblib')  # Ensure the path is correct

# Input kutucukları iki sütun halinde
left_column, right_column = st.columns(2)
with left_column:
    income = st.number_input('Gelir (Yıllık)', min_value=0, value=50000)
    experience = st.number_input('Tecrübe Yılı', min_value=0, value=5)
    education = st.selectbox('Eğitim Seviyesi', options=[1, 2, 3], format_func=lambda x: {1: 'Lisans', 2: 'Yüksek Lisans', 3: 'Doktora'}.get(x, 'Bilinmeyen'))
    age = st.number_input('Yaş', min_value=18, value=30)
    family = st.number_input('Aile Büyüklüğü', min_value=1, value=1)
    securities_account = st.selectbox('Menkul Kıymet Hesabı Var mı?', options=[0, 1])

with right_column:
    cc_avg = st.number_input('Aylık Kredi Kartı Harcaması', min_value=0.0, value=1000.0)
    mortgage = st.number_input('Mortgage Miktarı', min_value=0, value=0)
    cd_account = st.selectbox('CD Hesabı Var mı?', options=[0, 1])
    credit_card = st.selectbox('Kredi Kartı Var mı?', options=[0, 1])
    online = st.selectbox('Online Bankacılık Kullanımı', options=[0, 1])

# Tahmin butonu
if st.button("Tahmin Yap"):
    input_data = pd.DataFrame({
        'AGE': [age],
        'EXPERIENCE': [experience],
        'INCOME': [income],
        'FAMILY': [family],
        'CCAVG': [cc_avg],
        'EDUCATION': [education],
        'MORTGAGE': [mortgage],
        'SECURITIESACCOUNT': [securities_account],
        'CDACCOUNT': [cd_account],
        'ONLINE': [online],
        'CREDITCARD': [credit_card]
    }, index=[0])
    prediction = model.predict(input_data)
    result = 'Uygun' if prediction[0] == 1 else 'Uygun Değil'
    st.markdown(f"<p style='font-size: 24px; color: purple;'>{result}</p>", unsafe_allow_html=True)
