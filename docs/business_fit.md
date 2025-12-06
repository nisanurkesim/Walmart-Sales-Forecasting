# 7. Final Modelin İş Gereksinimleri ile Uyumu

**İş Problemi:** Stok fazlası maliyetleri ve yok satma (stock-out) riskini azaltmak.

**Final Model Hata Payı (RMSE):** ~3,722 dolar

**Başarı Kriteri:** Lineer Regresyon ile kurulan Baseline modelin (RMSE: 21,820 ) hata payı, Random Forest ile %80'in üzerinde düşürülerek 3,722  seviyesine indirilmiştir.

**Stok Optimizasyonu:** Modelin haftalık hata payını 3,722 dolar seviyesine düşürmesi, mağaza yönetiminin stokları çok daha dar bir marjla yönetebilmesini sağlar. Bu, özellikle envanterin en kritik olduğu bayram ve özel günlerde (Thanksgiving, Christmas) stok fazlası veya stok eksikliği riskini minimize ederek doğrudan maliyet tasarrufuna yol açar.

**Karar Verme:** Modelin Feature Importance analizi, mağaza boyutu ve departman bilgisinin kritik faktörler olduğunu göstererek, yöneticilerin hangi mağazalara daha fazla kaynak ayırması gerektiği konusunda somut kararlar almasını sağlar.