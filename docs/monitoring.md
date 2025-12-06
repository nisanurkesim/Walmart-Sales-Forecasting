# Modelin Canlı İzlenmesi (Monitoring)

Model canlı ortama alındıktan sonra (Streamlit Cloud), performansını koruması ve güncelliğini yitirmemesi için sürekli izlenmelidir.

**İzlenmesi Gereken Metrikler:**

 **Model Performansı** / **Canlı RMSE, MAE** :
  Gerçekleşen satışlar ile tahminler arasındaki hata payının zaman içindeki değişimini izlemek.
 
**Veri Kalitesi (Data Quality)** / **Outliers** : Yeni gelen veride (Temperature, Fuel Price vb.) beklenmedik şekilde eksik veri veya aşırı aykırı değerler olup olmadığını kontrol etmek. 

 **Model Kayması (Drift)** / **Feature Importance** : Zamanla modelin en önemli gördüğü özelliklerin (Örn: CPI veya Unemployment) ağırlığının değişip değişmediğini kontrol etmek.
