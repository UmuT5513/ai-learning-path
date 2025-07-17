# 🎵 Billboard to Spotify Playlist Creator

Bu proje, Billboard Hot 100 listelerinden şarkıları çekerek otomatik olarak Spotify oynatma listesi oluşturan bir Python uygulamasıdır! 🚀

## ✨ Özellikler

- 📊 Billboard Hot 100 listelerinden şarkı isimlerini çeker
- 🎧 Spotify API kullanarak otomatik oynatma listesi oluşturur
- 📅 Belirli bir tarihteki hit şarkıları için playlist oluşturur
- 💻 Kullanıcı dostu komut satırı arayüzü

## 📋 Gereksinimler

### 🐍 Python Kütüphaneleri

```bash
pip install requests beautifulsoup4 spotipy
```

### 🔑 Spotify API Kimlik Bilgileri

1. [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)'a gidin 🌐
2. Yeni bir uygulama oluşturun ➕
3. Client ID ve Client Secret bilgilerini alın 🔐
4. Redirect URI'yi `https://www.billboard.com/charts/hot-100/` olarak ayarlayın 🔗

## 🚀 Kurulum

1. Projeyi klonlayın veya indirin 📥
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. `CLIENT_ID` ve `CLIENT_SECRET` değerlerini kendi Spotify API kimlik bilgilerinizle değiştirin ✏️

## 🎯 Kullanım

1. Programı çalıştırın:
   ```bash
   python main.py
   ```

2. İstenen tarih formatında (YYYY-MM-DD) bir tarih girin. Örnek:
   ```
   2023-12-25
   ```

3. İlk çalıştırmada Spotify hesabınıza giriş yapmanız istenecektir 🔐

4. Program otomatik olarak:
   - ⬇️ Belirtilen tarihteki Billboard Hot 100 listesini çeker
   - ➕ Spotify'da "Billboard Top 100 [tarih]" adlı bir playlist oluşturur
   - 🎵 Bulduğu şarkıları bu playlist'e ekler

## 🏗️ Kod Yapısı

### ⚙️ Fonksiyonlar

- `get_songs(header, url)`: 📰 Billboard sitesinden şarkı listesini çeker
- `spotify(client_id, client_secret)`: 🔐 Spotify API kimlik doğrulaması yapar
- `add_playlist(sp, playlist_id, songs)`: ➕ Şarkıları Spotify playlist'ine ekler
- `main()`: 🎯 Ana program akışını yönetir

### 🛠️ Kullanılan Teknolojiler

- **requests**: 🌐 Web scraping için HTTP istekleri
- **BeautifulSoup**: 📝 HTML parsing ve veri çıkarma
- **spotipy**: 🎧 Spotify API ile etkileşim
- **Spotify Web API**: 📝 Playlist oluşturma ve şarkı ekleme

## ⚠️ Önemli Notlar

- ⚡ Program, şarkı isimlerini Billboard sitesinden çıkardığı için tam eşleşme garantisi yoktur
- 🔍 Bazı şarkılar Spotify'da bulunamayabilir veya farklı versiyonları eklenebilir
- 📈 Spotify API rate limit'lerine tabidir
- 🌐 İnternet bağlantısı gereklidir

## 🔧 Hata Ayıklama

Eğer şarkılar eklenemiyorsa:
1. 🔑 Spotify API kimlik bilgilerinizi kontrol edin
2. 🌐 İnternet bağlantınızı kontrol edin
3. 📅 Belirtilen tarihte Billboard Hot 100 listesinin mevcut olduğundan emin olun

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. Spotify API kullanım şartlarına ve Billboard'un robots.txt dosyasına uygun şekilde kullanın. 📚

## 🤝 Katkıda Bulunma

Projeyi geliştirmek için:
1. 🍴 Fork edin
2. 🌿 Yeni özellik dalı oluşturun
3. 💾 Değişikliklerinizi commit edin
4. 🔄 Pull request gönderin

---

**⚠️ Not**: Bu proje sadece eğitim amaçlıdır. Ticari kullanım öncesinde ilgili platformların kullanım şartlarını inceleyiniz. 📖