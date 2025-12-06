import joblib
import sys
import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from config import MODEL_PATH


def load_model():

    # 1. Dosya var mı kontrol et
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"HATA: Model dosyası bulunamadı! Lütfen 'models' klasörünü kontrol et.")

    # 2. Modeli yükle
    print("Model yükleniyor...")
    try:
        model = joblib.load(MODEL_PATH)
        print(" BAŞARILI: Model hatasız yüklendi!")
        return model
    except Exception as e:
        print(f" Model yüklenirken hata oluştu: {e}")
        # Numpy sürüm hatası
        raise e


# Bu dosya doğrudan çalıştırıldığında (Test için) burası çalışır
if __name__ == "__main__":
    model = load_model()

    # Modelin tipini görme
    print(f"Model Tipi: {type(model)}")