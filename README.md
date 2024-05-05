Thera Bank Kredi Ön Onay Tahminleyici 🏦📈

Bu depo, Thera Bank müşterileri için ön onaylı kredi tekliflerini tahmin etmek amacıyla hazırlanmış bir makine öğrenmesi projesinin Python kodlarını ve gerekli dokümanları içermektedir. 🚀 Proje, çeşitli Python kütüphaneleri ve otomatik makine öğrenmesi süreçlerini yönetmek için TPOT kütüphanesini kullanmaktadır.

Proje Genel Bakış 📊
Bu projenin amacı, Thera Bank'ın bir müşterisine kredi ön onayı verilip verilmeyeceğini tahmin edebilecek bir model oluşturmaktır. Model, TPOT otomatik makine öğrenmesi kütüphanesi kullanılarak geliştirilmiştir ve çeşitli veri ön işleme, model seçimi ve parametre ayarlama süreçlerini içerir.

Dosyalar 📁
Depoda bulunan başlıca dosyalar:

analysis.py: Veri analizi ve ön işleme işlemlerinin yapıldığı Python scripti.
best_pipeline.py: TPOT tarafından seçilen en iyi makine öğrenmesi pipeline'ını içeren Python scripti.
finalized_model.joblib: Eğitilmiş modelin kaydedildiği dosya.
model3.py: Alternatif model yapılandırmalarını içeren Python scripti.
performance.py: Model performans değerlendirme scripti.
streamlit_app.py: Modelin sonuçlarını görselleştirmek için Streamlit uygulaması.
requirements.txt: Projede kullanılan Python kütüphanelerini içeren gereksinimler dosyası.
Kurulum 💻
Projeyi lokalde çalıştırmak için gereken adımlar:

Bu repository'i klonlayın:
git clone (https://github.com/KuleGizem/thera_bank)

Gerekli Python kütüphanelerini kurun:
pip install -r requirements.txt

Streamlit uygulamasını başlatın:
streamlit run streamlit_app.py
