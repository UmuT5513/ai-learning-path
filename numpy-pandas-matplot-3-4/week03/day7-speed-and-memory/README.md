# 📊 CSV Okuma Yöntemleri: Hız ve Bellek Karşılaştırması

Bu mini projede yaklaşık 50 MB büyüklüğünde bir CSV dosyasını üç farklı yöntemle okuyarak **süre** ve **RAM kullanımı** açısından karşılaştırdım.

---

## 🎯 Amaç

- Pandas ile büyük dosyaları okurken performans farklarını görmek
- Aşağıdaki yöntemleri karşılaştırmak:
  1. `pd.read_csv()` (standart yöntem)
  2. `pd.read_csv()` + `chunksize` (parça parça okuma)
  3. `pd.read_csv()` + `engine='pyarrow'` (hızlı C tabanlı okuma)

---

## ⚙️ Kurulum

```bash
pip install pandas pyarrow psutil matplotlib seaborn



| Yöntem    | Süre (s) | RAM Kullanımı (MB) | Satır Sayısı |
| --------- | -------- | ------------------ | ------------ |
| Standard  | 0.549     | 62.863              | 2,000,000    |
| Chunksize | 0.569     | 59.980               | 2,000,000    |
| PyArrow   | 0.115     | 251.895               | 2,000,000    |


ℹ️ Gerçek değerler bilgisayar sistemine göre değişebilir.