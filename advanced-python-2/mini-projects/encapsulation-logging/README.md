# 🏦 Banka Hesap Yönetim Sistemi

Basit bir Python tabanlı banka hesap yönetim sistemi. Bu proje, nesne yönelimli programlama (OOP) prensiplerini kullanarak temel bankacılık işlemlerini simüle eder.

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Sınıf Yapısı](#-sınıf-yapısı)
- [Hata Yönetimi](#-hata-yönetimi)
- [Logging Sistemi](#-logging-sistemi)
- [Örnek Kullanım](#-örnek-kullanım)

## ✨ Özellikler

- 👤 **Müşteri Yönetimi**: Kişi bilgileri ve hesap bilgilerini saklama
- 💳 **Banka Hesabı Yönetimi**: Hesap oluşturma ve bakiye takibi
- 💰 **Para İşlemleri**: Para yatırma ve çekme işlemleri
- 🛡️ **Hata Yönetimi**: Özel exception sınıfları ile güvenli işlemler
- 📝 **Logging**: Tüm işlemlerin kayıt altına alınması
- 🔒 **Encapsulation**: Private değişkenler ve property'ler kullanımı

## 🚀 Kurulum

1. Python 3.x yüklü olduğundan emin olun
2. Projeyi klonlayın veya dosyaları indirin
3. Herhangi bir ek kütüphane kurulumu gerekmez (standart Python kütüphaneleri kullanılmıştır)

## 💻 Kullanım

```python
# Banka hesabı oluşturma
account1 = BankAccount(152000, 10011001)
account2 = BankAccount(50100, 10011002)

# Müşteri oluşturma
person = Person("Ahmet", "05551234567", "Mühendis", accounts=[account1, account2])

# Yönetim sistemi oluşturma
management = Management(person, account1)

# Para yatırma
management.deposit(1000)

# Para çekme
management.withdraw(500)
```

## 🏗️ Sınıf Yapısı

### 🏦 `BankAccount` Sınıfı
- Banka hesap bilgilerini yönetir
- **Özellikler:**
  - `balance`: Hesap bakiyesi
  - `account_number`: Hesap numarası
  - `account_list`: Tüm hesapların listesi

### 👤 `Person` Sınıfı
- Müşteri bilgilerini saklar
- **Özellikler:**
  - `name`: Müşteri adı
  - `phone`: Telefon numarası (11 haneli validasyon)
  - `job`: Meslek
  - `accounts`: Sahip olunan hesaplar listesi

### 🎯 `Management` Sınıfı
- Bankacılık işlemlerini yönetir
- **İşlemler:**
  - Para yatırma (`deposit`)
  - Para çekme (`withdraw`)
  - Hesap seçimi (`select_account`)
  - Müşteri kaydetme (`save_customers`)

## ⚠️ Hata Yönetimi

### `AmountError` Exception
- Negatif para miktarları için özel hata sınıfı
- Otomatik hata mesajı oluşturma

### `PhoneLenError` Exception
- Telefon numarası uzunluk kontrolü için
- 11 haneli telefon numarası zorunluluğu

## 📊 Logging Sistemi

Sistem tüm işlemleri `bank.log` dosyasında takip eder:

```
2024-01-15 14:30 - INFO - deposit işlemi başarılı.
2024-01-15 14:31 - WARNING - withdraw, Girilen para değeri eksi bir değer olamaz!
```

### Log Özellikleri:
- 📅 Tarih/saat damgası
- 📈 Log seviyesi (INFO, WARNING)
- 📝 İşlem detayları
- 🔄 Dosyaya ekleme modu

## 🎯 Örnek Kullanım

```python
# Hesap oluşturma
account1 = BankAccount(152000, 10011001)
account2 = BankAccount(50100, 10011002)

# Müşteri bilgileri
person = Person("Umut", "05551234567", "Çiftçi", accounts=[account1, account2])

# Hesapları listele
person.list_accounts()

# Yönetim sistemi
management = Management(person, account1)

# Geçerli işlem
management.deposit(1000)  # ✅ Başarılı

# Geçersiz işlem
management.withdraw(-100)  # ❌ AmountError fırlatır
```

## 🔧 Decorator Kullanımı

`@amount_validation` decorator'u tüm para işlemlerinde:
- 🛡️ Hata yakalama
- 📝 Logging
- ✅ İşlem doğrulama

## 📝 Notlar

- Telefon numaraları 11 haneli olmalıdır
- Para miktarları pozitif olmalıdır
- Tüm işlemler log dosyasında kayıt altına alınır
- Private değişkenler `__` ile korunur

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!