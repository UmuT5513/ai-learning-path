# 🗝️ LoginSystem

Basit ama geliştirilebilir bir **Kullanıcı Kayıt & Giriş** uygulaması.  
Hem **etkileşimli menü** (stdin) hem de **komut satırı arayüzü (CLI)** üzerinden çalışır ve tüm kritik olayları `logging` modülüyle dosyaya kaydeder.

> **Log dosyası:** `login_system.log` (UTF-8, ekleme modu, ayrıntılı tarih-saat damgaları)

---

## İçindekiler
1. [Özellikler](#özellikler)
2. [Gereksinimler](#gereksinimler)
3. [Kurulum](#kurulum)
4. [Kullanım](#kullanım)
   - [Etkileşimli Menü](#1-etkileşimli-menü)
   - [Komut Satırı (CLI)](#2-komut-satırı-cli)
5. [Günlük (Log) Çıktıları](#günlük-log-çıktıları)
6. [Katkı Sağlama](#katkı-sağlama)
7. [Lisans](#lisans)

---

## Özellikler

- 📝 **Kayıt** – Yeni kullanıcı adı + parola ekler.  
  - Kullanıcı zaten varsa `WARNING`
  - Parola < 6 karakterse `ERROR`
- 🔐 **Giriş** – Kullanıcı adı + parolayı doğrular.  
  - Her hatalı denemede `WARNING`
  - 3 ardışık hatada `ERROR`
- 🧰 **CLI Desteği** – `argparse` ile hızlı otomasyon veya test imkânı
- 📂 **Kalıcı Loglama** – INFO/WARNING/ERROR seviyeleri ayrı ayrı kaydedilir
- 🇹🇷 **Tamamen Türkçe** uyarı / mesajlar

---

## Gereksinimler

- Python **3.8+**  
- Ek bağımlılık **yok** (yalnızca standart kütüphaneler: `logging`, `argparse`)

---

## Kurulum

```bash
# Projeyi klonlayın
git clone https://github.com/kullanici/LoginSystem.git
cd LoginSystem

# (Opsiyonel) Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

## Kullanım

### 1. Etkileşimli Menü (Terminal)

Ana sistemi etkileşimli menü ile çalıştırmak için:

```bash
python LoginSystem.py
```

**Menü Seçenekleri:**
- `1` - Yeni kullanıcı kaydı
- `0` - Mevcut kullanıcı girişi
- `q` - Sistemden çıkış

**Örnek Kullanım:**
```
> Kayıt olmak için 1, Giriş yapmak için 0 a basın: 1
> Kullanıcı adı: john_doe
> Parola: mypassword123
```

### 2. Komut Satırı (CLI)

Komut satırı arayüzü ile hızlı işlemler yapabilirsiniz:

#### Kullanıcı Kaydı
```bash
python cli.py register --username kullanici_adi --password parola123
```

#### Kullanıcı Girişi
```bash
python cli.py login --username kullanici_adi --password parola123
```

#### Yardım
```bash
python cli.py --help
python cli.py register --help
python cli.py login --help
```

---

## Günlük (Log) Çıktıları

Sistem, tüm işlemleri `login_system.log` dosyasına kaydeder:

- **INFO**: Başarılı kayıt ve giriş işlemleri
- **WARNING**: Zaten kayıtlı kullanıcı, yanlış parola, kayıtlı olmayan kullanıcı
- **ERROR**: Zayıf parola, 3 kez yanlış giriş denemesi

**Log Format:**
```
2024-01-15 14:30 - INFO - Kayıt başarılı
2024-01-15 14:31 - WARNING - password='123': Zayıf parola. Parola 6 haneden kısa olamaz.
```

---

## Güvenlik Özellikleri

- Parola minimum 6 karakter olmalı
- Yanlış parola denemeleri loglanır
- Mevcut kullanıcı kontrolü
- Güvenli hata mesajları

---

## Dosya Yapısı

```
login-system/
├── LoginSystem.py      # Ana sistem dosyası
├── cli.py             # Komut satırı arayüzü
├── login_system.log   # Log dosyası (otomatik oluşturulur)
└── README.md          # Bu dosya
```

---

## Katkı Sağlama

1. Bu projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik ekle'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

---

## Lisans

Bu proje MIT Lisansı altında dağıtılmaktadır. Detaylar için `LICENSE` dosyasına bakınız.