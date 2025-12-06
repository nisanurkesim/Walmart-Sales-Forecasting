# 4. Validasyon Şeması Seçimi (Train/Test Split)

**Seçilen Yöntem:** Basit Train-Test Split (%80 Eğitim, %20 Test)

**Neden Seçildi?**
Walmart satış tahmini bir zaman serisi problemi olmasına rağmen proje başlangıç aşamasında modelleme ve hızlı iterasyon kolaylığı için basit Train-Test Split yöntemi kullanılmıştır. Bu yöntemin seçiminde;

1.  **Hız ve Basitlik:** Time Series Cross Validation yöntemlerinin kurulum ve yorumlama zorluğundan kaçınılması hedeflenmiştir.
2.  **Veri Kapsamı:** Veri setinin tarih bazlı çok büyük bir zaman aralığına sahip olmamasından dolayı geriye dönük test (hold-out) kullanılmıştır.

Modelin final doğruluğu, ayrılan %20'lik test seti üzerindeki RMSE metrikleri ile ölçülmüştür.