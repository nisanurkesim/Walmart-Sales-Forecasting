
#  Walmart Store Sales Forecasting (Uçtan Uca ML Projesi)

Bu proje, Walmart mağazalarının geçmiş satış verilerini, makroekonomik göstergeleri (TÜFE, İşsizlik, Yakıt Fiyatları) ve mağaza özelliklerini kullanarak haftalık satış tahminleri yapan uçtan uca bir Makine Öğrenmesi projesidir.

##  Proje Amacı
Perakende sektöründe doğru stok yönetimi ve finansal planlama için satış tahminleri kritiktir. Bu proje ile:
- Mağaza, departman ve tarih bazlı satış tahminleri yapılması,
- Özel günlerin (Super Bowl, Şükran Günü, Noel vb.) satışlara etkisinin analiz edilmesi,
- Stok maliyetlerinin optimize edilmesine katkı sağlanması hedeflenmiştir.

## Veri Seti
Kaggle Walmart Recruiting verisi kullanılmıştır.
- **Kaynak:** [Kaggle Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting/data)
- **Gerekli Dosyalar:** `train.csv`, `stores.csv`, `features.csv`, `test.csv`
- **Tarih Aralığı:** 2010 - 2012
- **Veri Boyutu:** 421,570 satır (Train seti)
- **Özellikler:** Mağaza Tipi, Boyutu, Sıcaklık, Yakıt Fiyatı, TÜFE (CPI), İşsizlik Oranı, Tatil Bilgisi ve İndirimler (MarkDowns).

##  Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda (Local) çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Gerekli Kütüphanelerin Yüklenmesi
Terminali açın ve proje bağımlılıklarını yükleyin:
```bash
pip install -r requirements.txt
````

### 2\. Modelin Eğitilmesi 

Proje içerisinde eğitilmiş model (`models/` klasöründe) mevcuttur. Ancak modeli veriyi kullanarak sıfırdan eğitmek isterseniz:

```bash
python src/train.py
```


### 3\. Arayüzün (App) Başlatılması

Satış tahmin uygulamasını tarayıcıda açmak için:

```bash
streamlit run app.py
```

## 📂 Proje Yapısı

```text
Walmart_Project/
├── data/            # Train, test, stores ve features csv dosyaları
├── models/          # Eğitilmiş model dosyası (.pkl)
├── notebooks/       # EDA, Feature Engineering ve Model denemeleri (.ipynb)
├── src/             # Kaynak kodlar (Modüler yapı)
│   ├── train.py     # Model eğitim pipeline'ı (Preprocessing + Training)
│   ├── inference.py # Tahminleme modülü (Model yükleme ve test)
├── app.py           # Streamlit Web Arayüzü (Deployment)
├── config.py        # Dosya yolları ve proje ayarları
├── requirements.txt # Kütüphane gereksinimleri
└── README.md        # Proje dokümantasyonu
```

##  Model Performansı

Model olarak **Random Forest Regressor** kullanılmış ve `RandomizedSearchCV` ile hiperparametre optimizasyonu yapılmıştır.

  - **Kullanılan Model:** Random Forest Regressor
  - **RMSE (Hata Payı):** \~3,722 $
  - **MAE (Mutlak Hata):** \~2,400 $
  - **Başarı:** Baseline modele (Linear Regression) göre hata payı %80'in üzerinde düşürülmüştür.

### Önemli Değişkenler (Feature Importance)

Modelin satış tahmininde en çok dikkat ettiği faktörler:

1.  **Dept (Departman):** Hangi ürün grubunun satıldığı.
2.  **Size (Mağaza Boyutu):** Mağazanın kapasitesi.
3.  **Week (Hafta):** Mevsimsellik etkisi (Yılbaşı, Bayram vb.).

##  Kullanılan Teknolojiler

  - **Python 3.10+**
  - **Pandas & NumPy:** Veri Manipülasyonu ve Temizleme
  - **Scikit-learn:** Makine Öğrenmesi Modelleri
  - **Streamlit:** Web Arayüzü Geliştirme
  - **Joblib:** Model Kaydetme/Yükleme
  - **PyCharm:** Geliştirme Ortamı (IDE)

##  İletişim

  - **Geliştirici:** Nisanur Kesim
  - **Linkedin:** www.linkedin.com/in/nisanur-kesim-756734313


