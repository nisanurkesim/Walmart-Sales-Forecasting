import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import sys
import os

# Config dosyasını bulabilmek için ana dizini yola ekleme
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import TRAIN_DATA_PATH, STORES_DATA_PATH, FEATURES_DATA_PATH, MODEL_PATH


def get_holiday_type(row):

    if row['IsHoliday'] == 1:
        date_str = str(row['Date']).split(' ')[0]
        if date_str in ['2010-02-12', '2011-02-11', '2012-02-10', '2013-02-08']:
            return 1  # Super Bowl
        elif date_str in ['2010-09-10', '2011-09-09', '2012-09-07', '2013-09-06']:
            return 2  # Labor Day
        elif date_str in ['2010-11-26', '2011-11-25', '2012-11-23', '2013-11-29']:
            return 3  # Thanksgiving
        elif date_str in ['2010-12-31', '2011-12-30', '2012-12-28', '2013-12-27']:
            return 4  # Christmas
    return 0  # Tatil Değil


def train_model():
    # 1. Veriyi Oku
    train_df = pd.read_csv(TRAIN_DATA_PATH)
    stores_df = pd.read_csv(STORES_DATA_PATH)
    features_df = pd.read_csv(FEATURES_DATA_PATH)

    # 2. Merge İşlemleri
    dp_temp = pd.merge(train_df, stores_df, on='Store', how='left')

    if 'IsHoliday' in features_df.columns:
        features_clean = features_df.drop(columns=['IsHoliday'])
    else:
        features_clean = features_df

    final_dp = pd.merge(dp_temp, features_clean, on=['Store', 'Date'], how='left')

    # 3. Preprocessing & Feature Engineering
    # Tarih formatı
    final_dp['Date'] = pd.to_datetime(final_dp['Date'])

    # Eksik Markdown doldurma
    final_dp.fillna({
        'MarkDown1': 0, 'MarkDown2': 0, 'MarkDown3': 0, 'MarkDown4': 0, 'MarkDown5': 0
    }, inplace=True)

    # Tarih türetme
    final_dp['Year'] = final_dp['Date'].dt.year
    final_dp['Month'] = final_dp['Date'].dt.month
    final_dp['Week'] = final_dp['Date'].dt.isocalendar().week
    final_dp['Day'] = final_dp['Date'].dt.day

    final_dp['Holiday_Type'] = final_dp.apply(get_holiday_type, axis=1)

    # Type Encoding (A=3, B=2, C=1)
    type_mapping = {"A": 3, "B": 2, "C": 1}
    final_dp['Type_Encoded'] = final_dp['Type'].map(type_mapping)

    # 4. Model Hazırlığı
    features_cols = [
        'Store', 'Dept', 'Type_Encoded', 'Size',
        'Week', 'Month', 'Year', 'Holiday_Type',
        'Temperature', 'Fuel_Price', 'CPI', 'Unemployment',
        'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5'
    ]

    # Eksik verileri (NaN) temizleme
    final_dp = final_dp.dropna(subset=['Weekly_Sales'] + features_cols)

    X = final_dp[features_cols]
    y = final_dp['Weekly_Sales']

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Eğitim ( n_estimators=50, min_samples_split=5)

    rf_model = RandomForestRegressor(
        n_estimators=50,
        min_samples_split=5,
        max_depth=None,
        n_jobs=-1,
        random_state=42
    )

    rf_model.fit(X_train, y_train)

    # 6. Değerlendirme
    y_pred = rf_model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)

    print(f" RMSE: {rmse:.2f}")
    print(f" MAE:  {mae:.2f}")

    # 7. Kaydetme
    joblib.dump(rf_model, MODEL_PATH)
    print("İşlem tamam")


if __name__ == "__main__":
    train_model()