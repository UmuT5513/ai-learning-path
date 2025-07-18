# Amazon Price Tracker

Bu Python scripti, Amazon.com.tr'deki belirli bir ürünün fiyatını takip eder ve belirlenen eşik değerinin altına düştüğünde Telegram üzerinden bildirim gönderir.

## Özellikler

- Amazon.com.tr ürün fiyatlarını otomatik olarak takip eder
- Belirlenen eşik fiyatının altına düştüğünde Telegram bildirimi gönderir
- Zamanlanmış çalışma desteği (isteğe bağlı)
- Kolay yapılandırma ve kullanım

## Gereksinimler

```bash
pip install beautifulsoup4 requests schedule
```

## Kurulum

1. Repoyu klonlayın veya dosyaları indirin
2. Gerekli Python kütüphanelerini yükleyin:
   ```bash
   pip install beautifulsoup4 requests schedule
   ```

## Yapılandırma

### 1. Telegram Bot Kurulumu

1. Telegram'da [@BotFather](https://t.me/botfather) ile konuşun
2. `/newbot` komutu ile yeni bot oluşturun
3. Bot token'ınızı alın
4. Chat ID'nizi öğrenmek için [@userinfobot](https://t.me/userinfobot) ile konuşun

### 2. Script Yapılandırması

Aşağıdaki değişkenleri kendi bilgilerinizle güncelleyin:

```python
# Telegram Bot bilgileri
token = "BOT_TOKEN_BURAYA"
chat_id = "CHAT_ID_BURAYA"

# Takip edilecek ürün URL'si
URL = "AMAZON_URUN_URL_BURAYA"

# Eşik fiyat (TL)
th_price = 600
```

## Kullanım

### Tek Seferlik Çalıştırma

```bash
python amazon_price_tracker.py
```

### Zamanlanmış Çalıştırma

Script'in alt kısmındaki yorum satırlarını açarak belirli saatlerde otomatik çalışmasını sağlayabilirsiniz:

```python
schedule.every().day.at("15:40").do(main)
while True:
    schedule.run_pending()
    time.sleep(60)
```

## Script Yapısı

### Fonksiyonlar

- `scrape_product_infos(soup)`: Amazon sayfasından ürün bilgilerini çıkarır
- `send_telegram_message(token, chat_id, message)`: Telegram bildirimi gönderir
- `main()`: Ana fonksiyon - fiyat kontrolü ve bildirim gönderimi

### Çalışma Mantığı

1. Belirtilen Amazon URL'sinden ürün sayfasını çeker
2. BeautifulSoup ile HTML'i parse eder
3. Ürün fiyatını ve başlığını çıkarır
4. Fiyatı eşik değerle karşılaştırır
5. Eşik değerin altındaysa Telegram bildirimi gönderir

## Önemli Notlar

- Script Amazon.com.tr için optimize edilmiştir
- User-Agent header'ı ile bot tespitini engellemek için tarayıcı kimliği kullanır
- Fiyat formatı Türk Lirası (TL) için ayarlanmıştır
- Rate limiting'e dikkat edin - çok sık istek göndermeyin

## Hata Giderme

### Yaygın Sorunlar

1. **"centerCol bulunamadı!" hatası**: Amazon sayfa yapısı değişmiş olabilir
2. **Telegram mesajı gönderilmiyor**: Token ve Chat ID'yi kontrol edin
3. **Fiyat bulunamıyor**: Ürün sayfasının yapısı değişmiş olabilir

### Debugging

Hata ayıklama için print statement'ları ekleyebilirsiniz:

```python
print(f"Çekilen fiyat: {price}")
print(f"Eşik fiyat: {th_price}")
print(f"Ürün başlığı: {title}")
```

## Güvenlik

- Telegram bot token'ınızı güvenli tutun
- Script'i public repository'lerde paylaşırken hassas bilgileri kaldırın
- Environment variables kullanarak token'ları saklayın

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.