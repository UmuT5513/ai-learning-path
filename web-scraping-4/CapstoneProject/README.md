# Books to Scrape - Web Scraping Project

Bu proje, [Books to Scrape](https://books.toscrape.com/) web sitesinden "Food and Drink" ve "Travel" kategorilerindeki kitap bilgilerini otomatik olarak çeken bir web scraping uygulamasıdır.

## 📋 Proje Özeti

Proje, Selenium WebDriver ve BeautifulSoup kullanarak kitap bilgilerini çeker ve CSV formatında saklar. Uygulama, sayfalama (pagination) desteği ile tüm kategorilerdeki kitapları otomatik olarak tarar.

## 🚀 Özellikler

- **Kategori Bazlı Tarama**: Food and Drink ve Travel kategorilerini otomatik olarak tarar
- **Sayfalama Desteği**: Her kategorinin tüm sayfalarını otomatik olarak gezinir
- **Detaylı Bilgi Çekme**: Her kitap için ayrıntılı bilgileri toplar
- **Hata Yönetimi**: Eksik veriler için güvenli hata yönetimi
- **CSV Çıktısı**: Toplanan verileri CSV formatında kaydeder

## 📊 Toplanan Veriler

Her kitap için aşağıdaki bilgiler toplanır:

- **Kitap Adı** (Name)
- **Fiyat** (Price)
- **Açıklama** (Description)
- **Vergi** (Tax)
- **Vergisiz Fiyat** (Price with Tax)
- **Stok Durumu** (Availability)
- **Yorum Sayısı** (Number of Reviews)
- **UPC Kodu** (UPC)

## 🛠️ Teknolojiler

- **Python 3.x**
- **Selenium WebDriver** - Web tarayıcı otomasyonu
- **BeautifulSoup** - HTML parsing
- **lxml** - XML/HTML processing
- **pandas** - Veri manipülasyonu ve CSV çıktısı
- **Chrome WebDriver** - Tarayıcı kontrolü

## 📦 Kurulum

### Gereksinimler

```bash
pip install selenium beautifulsoup4 lxml pandas
```

### Chrome WebDriver

1. Chrome tarayıcınızın sürümünü kontrol edin
2. [ChromeDriver](https://chromedriver.chromium.org/) sayfasından uygun sürümü indirin
3. ChromeDriver'ı PATH'e ekleyin veya proje dizinine yerleştirin

## 🎯 Kullanım

```bash
python scraper.py
```

### Kod Çalıştırma Adımları

1. Uygulama Chrome tarayıcısını açar
2. Books to Scrape sitesine gider
3. "Food and Drink" ve "Travel" kategorilerini bulur
4. Her kategoriyi sırayla işler:
   - Kategoriye tıklar
   - Sayfadaki tüm kitapları bulur
   - Her kitabın detay sayfasına gider
   - Bilgileri çeker ve listede saklar
   - Sonraki sayfaya geçer (varsa)
5. Tüm veriler CSV dosyasına kaydedilir

## 📁 Çıktı Dosyaları

- `outputs/miuul_capstone.csv` - Birincil çıktı dosyası
- `C:/Users/Umut/Desktop/ai-learning-path/web-scraping-4/outputs/miuul_webscraping_capstone.csv` - Yedek çıktı dosyası

## ⚙️ Konfigürasyon

### Chrome Seçenekleri

```python
options = webdriver.ChromeOptions()
options.add_argument("--start-minimized")  # Küçük ekran modunda başlat
# options.add_argument("--headless")        # Görünmez mod (isteğe bağlı)
```

### Bekleme Süreleri

- Sayfa yükleme: 3 saniye
- Kategori geçişi: 2 saniye
- Kitap detayı: 2 saniye
- Geri dönüş: 2 saniye

## 🔧 Hata Yönetimi

- **StaleElementReferenceException**: WebDriverWait ile çözülür
- **Eksik Veri**: Boş string ile doldurulur
- **Liste Uzunluk Uyumsuzluğu**: Otomatik düzeltme
- **CSV Kaydetme Hatası**: Alternatif dosya yolu

## 📈 Performans

- Çalışma süresini ölçer ve gösterir
- Sayfa geçişlerini loglar
- İşlem tamamlandığında bildirim verir

## 🚨 Dikkat Edilmesi Gerekenler

1. **Robot.txt**: Web sitesinin robot.txt kurallarına uyulmalı
2. **Rate Limiting**: Çok hızlı istek göndermekten kaçının
3. **Etik Scraping**: Sitenin kaynaklarını aşırı yüklemeyin
4. **Yasal Sorumluluk**: Kullanım şartlarını kontrol edin

## 🐛 Bilinen Sorunlar

- Bazı kitaplarda eksik bilgiler olabilir
- Ağ bağlantı sorunları scraping'i kesebilir
- Chrome güncellemeleri WebDriver uyumsuzluğuna neden olabilir

## 🔄 Gelecek Geliştirmeler

- [ ] Daha fazla kategori desteği
- [ ] Paralel işleme
- [ ] Veritabanı entegrasyonu
- [ ] API endpoint'i
- [ ] Daha gelişmiş hata yönetimi

## 📄 Lisans

Bu proje eğitim amaçlı olarak geliştirilmiştir.

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'i push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

## 📞 İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.

---

**Not**: Bu proje sadece eğitim amaçlıdır. Web scraping yaparken her zaman sitenin kullanım şartlarına ve etik kurallara uyunuz.