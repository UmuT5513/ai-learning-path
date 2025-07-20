# Web Scraping Projects Collection 🕷️

Bu repository 1.5 haftalık web scraping öğrenme sürecimde geliştirdiğim çeşitli projeleri içeriyor. BeautifulSoup, Selenium, ve Requests kütüphanelerini kullanarak farklı web sitelerinden veri çekme deneyimleri kazandım.

## 📁 Proje Yapısı

### 🔧 Ana Projeler

#### 1. **Google Search Analyzer** 🔍 (`first5search.py`)
Google arama sonuçlarını otomatik olarak analiz eden Selenium tabanlı scraper.

**Özellikler:**
- Chrome WebDriver ile tam otomatik arama
- İlk 5 arama sonucunu detaylı analiz
- Başlık ve kaynak website bilgilerini çıkarma
- XPath ile dinamik element seçimi
- Sonuçları dictionary formatında saklama

**Teknik Detaylar:**
- `--start-maximized` ile tarayıcı optimizasyonu
- 20 saniye bekleme süresi ile sayfa yükleme garantisi
- `kb0PBd A9Y9g jGGQ5e` class'ına sahip blokları hedefleme
- Nested element yapısında h3 ve span elementlerini bulma

#### 2. **Amazon Price Tracker** 💰 (`main.py`)
Amazon ürünlerinin fiyat değişimlerini takip eden ve Telegram bildirimi gönderen otomatik sistem.

**Özellikler:**
- Gerçek zamanlı fiyat takibi
- Telegram Bot API entegrasyonu
- Threshold bazlı uyarı sistemi (600 TL altı)
- Schedule kütüphanesi ile zamanlanmış kontroller
- User-Agent header ile bot tespitini önleme

**Teknik Detaylar:**
- BeautifulSoup ile Amazon DOM parsing
- `centerCol > apex_desktop` yapısında fiyat çıkarma
- `a-price-whole` ve `a-price-fraction` class'larını birleştirme
- String manipülasyonu ile TL dönüşümü
- Datetime formatında bildirim zamanı

#### 3. **Cookie Clicker Bot** 🍪 (`main.py - CookieClicker`)
Cookie Clicker oyununu otomatik oynayan akıllı bot sistemi.

**Özellikler:**
- 5 dakikalık kesintisiz oyun oturumu
- Akıllı satın alma algoritması
- Her 5 saniyede strateji güncellemesi
- En pahalı alınabilir ürünü tercih etme
- Undetected ChromeDriver ile tespit önleme

**Teknik Detaylar:**
- `orteil.dashnet.org/cookieclicker/` hedef site
- Dil seçimi otomasyonu (EN)
- Gerçek zamanlı cookie sayısı parsing
- 5 ürün için fiyat karşılaştırması
- `enabled` class kontrolü ile satın alma doğrulama
- Timeout ve interval yönetimi

#### 4. **Billboard to Spotify Playlist Creator** 🎵 (`Billboard_to_Spotify.py`)
Billboard Hot 100 listesini otomatik Spotify playlist'ine dönüştüren kapsamlı sistem.

**Özellikler:**
- Kullanıcı tanımlı tarih aralığı (YYYY-MM-DD)
- Billboard Hot 100 chart scraping
- Spotify API ile otomatik kimlik doğrulama
- Şarkı arama ve eşleştirme algoritması
- Public playlist oluşturma ve paylaşım

**Teknik Detaylar:**
- `c-title a-no-trucate a-font-primary-bold-s` CSS selector kullanımı
- Spotipy OAuth2 flow implementation
- `user-library-read` ve `playlist-modify-public` scope'ları
- Track ID extraction ve playlist population
- Error handling ile robust şarkı eşleştirme

#### 5. **Python Events Scraper** 🐍 (`upcoming-events-python.py`)
Python.org'un resmi etkinlik takviminden gelecek etkinlikleri çeken otomatik scraper.

**Özellikler:**
- Python.org homepage'den gerçek zamanlı etkinlik bilgileri
- Tarih ve etkinlik adı structured data extraction
- Nested dictionary formatında veri organizasyonu
- Chrome WebDriver ile dinamik içerik handling

**Teknik Detaylar:**
- `shrubbery` class'ına sahip table element targeting
- `<li>` elementleri içindeki `<time>` ve `<a>` tag'lerini parse etme
- Enumeration ile index-based data structure
- Dictionary nesting: `{index: {'time': date, 'name': event}}`

### 🔧 Yardımcı Projeler

#### **Animal Table Parser** (`animal.py`)
- HTML tablosundan hayvan bilgilerini çekerek metin dosyasına kaydetme
- BeautifulSoup kullanarak tablo verilerini parse etme

#### **Quote Scraper** (`author.py`)
- quotes.toscrape.com sitesinden alıntıları çekme
- Parsel kütüphanesi ile XPath kullanımı

#### **Book Price Filter** (`book.py` & `book_pandas.py`)
- books.toscrape.com'dan kitap bilgilerini çekme
- Fiyat filtreleme ve CSV export

#### **IMDB Top Movies** (`IMDB.py`)
- IMDB listesinden film bilgilerini çekme
- Yönetmen bilgilerini detay sayfalarından toplama

#### **Comprehensive Book Analysis** (`Analysis.py`)
- Çoklu kategori ve sayfa gezinme
- Detaylı kitap metadata extraction

#### **Movie Ranking** (`movie.py`)
- Empire Magazine'in en iyi filmler listesi
- Web Archive'den historical data çekme

## 🛠️ Kullanılan Teknolojiler

- **BeautifulSoup4**: HTML parsing
- **Selenium**: Dinamik web sayfaları ve otomasyon
- **Requests**: HTTP istekleri
- **Pandas**: Veri analizi ve CSV işlemleri
- **Parsel**: XPath ile veri çekme
- **Spotipy**: Spotify API entegrasyonu
- **Schedule**: Zamanlanmış görevler
- **Undetected ChromeDriver**: Bot tespitini önleme

## 📊 Çıktı Dosyaları

- `animal.txt`: Hayvan bilgileri
- `books.csv`: Kitap verileri
- `IMDB_top_10.csv`: Film verileri
- `miuul_capstone.csv`: Detaylı kitap analizi
- `100_movies.txt`: Film sıralaması

## 🎯 Öğrenilen Konular

- Static ve dynamic web scraping farkları
- XPath ve CSS selector kullanımı
- API entegrasyonları (Spotify, Telegram)
- Veri temizleme ve düzenleme
- Hata yönetimi ve exception handling
- Web driver optimizasyonu
- Sayfa geçişleri ve pagination
- Bot tespit önleme teknikleri

## 🚀 Çalıştırma

Her proje bağımsız olarak çalıştırılabilir. Gerekli kütüphaneler:

```bash
pip install beautifulsoup4 selenium requests pandas parsel spotipy schedule undetected-chromedriver lxml
```

**Not**: Spotify ve Telegram projeler için API anahtarlarınızı eklemeyi unutmayın! 🔑

---

*Bu projeler web scraping öğrenme sürecimin bir parçasıdır. Her proje farklı zorluklar ve teknikler içermektedir.*