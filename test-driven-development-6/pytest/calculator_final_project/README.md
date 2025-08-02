# 🧮 Calculator Projesi

Bu proje, temel matematiksel işlemleri ve rol tabanlı yetkilendirmeyi içeren bir Python modülüdür. Testler **pytest** ile yazılmıştır ve parametrizasyon, fixture, marker gibi pytest özelliklerini örnekler.

## 📁 Klasör Yapısı

```
calculator/
│
├── calculator.py         # ➕➖✖️➗ işlemler
├── user.py              # 👤 Kullanıcı sınıfı
├── validator.py         # ✅ Girdi ve rol kontrolü
├── pytest.ini           # 🏷️ Marker tanımları
├── tests/
│   ├── __init__.py
│   ├── confest.py       # 🧩 Fixture'lar
│   ├── test_calculator.py
│   ├── test_user.py
│   ├── test_validator.py
```

## ⚡ Kurulum

1. Python 3.10+ yüklü olmalı.
2. Gerekli paketleri yükleyin:
   ```
   pip install pytest
   ```

## Kullanım

Testleri çalıştırmak için:
```
pytest
```
veya belirli bir marker ile:
```
pytest -m bolme
```

## ✨ Özellikler

- **calculator.py**: Toplama, çıkarma, çarpma, bölme fonksiyonları ve hata yönetimi.
- **user.py**: Kullanıcı adı ve rolü tutan sınıf.
- **validator.py**: Girdi tipini ve rol bazlı işlem yetkisini kontrol eden fonksiyonlar.
- **tests/**: Her modül için ayrı test dosyaları ve ortak fixture.

## Marker Kullanımı

`pytest.ini` ile testleri gruplayabilirsiniz:
- `bolme`: Sadece bölme işlemi ile ilgili testler.

## Katkı

Yeni özellik eklemek veya hata bildirmek için pull request gönderebilirsiniz.

---
**Not:** Proje test odaklı geliştirilmiştir ve pytest'in temel özelliklerini öğrenmek için