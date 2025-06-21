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

# Çalıştırmaya hazırsınız!


