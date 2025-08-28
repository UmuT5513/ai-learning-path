# Proje Kurulum Rehberi

## 1. Repository'yi Klonlayın

Yerel proje klasörünü oluşturup repository'yi klonlayın. Virtual environment (venv) oluşturmayı unutmayın.

```bash
# Fork'unuzu klonlayın
git clone <your-fork-url>
cd note-system

# Virtual environment oluşturun
python -m venv venv

# Virtual environment'ı aktif edin
# Linux/Mac için:
source venv/bin/activate
# Windows için:
venv\Scripts\activate

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Environment değişkenlerini ayarlayın
cp .env.example .env
# .env dosyasını kendi ayarlarınızla düzenleyin
```

## 2. Kütüphaneleri Yükleyin

Requirements.txt dosyasındaki kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

## 3. Uygulamaları Çalıştırın

İki ayrı terminal penceresi açarak şu komutları çalıştırın:

### Terminal 1 - Ana Uygulama
```bash
python main.py
```

### Terminal 2 - GUI Uygulaması
```bash
python -m streamlit run app/gui_app.py
```

> **Not:** Her iki terminal de virtual environment'ın aktif olduğu durumda çalıştırılmalıdır.