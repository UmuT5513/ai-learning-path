# 📝 Todo System

Basit ve kullanımı kolay bir Python komut satırı todo uygulaması! Görevlerinizi kolayca ekleyebilir, silebilir ve yönetebilirsiniz.

## ✨ Özellikler

- 📋 Görev ekleme
- 🗑️ Görev silme  
- ✅ Görev tamamlama
- 📊 Görev listeleme
- 📝 Detaylı loglama
- 🎯 Benzersiz ID sistemi

## 🚀 Kurulum

1. Projeyi bilgisayarınıza klonlayın:
```bash
git clone <repository-url>
cd todo-system
```

2. Python 3.7+ sürümünün yüklü olduğundan emin olun:
```bash
python --version
```

## 📖 Kullanım

### Yeni Görev Ekleme 📝
```bash
python main.py add -t "Alışveriş listesi hazırla"
python main.py add -t "Doktor randevusu al"
```

### Görevleri Listeleme 📋
```bash
python main.py list
```

Çıktı örneği:
```
2 görev listelendi!
Görev ID: 0
Görev Açıklaması: Alışveriş listesi hazırla
Tamamlanma Durumu: ✗
------------------------------
Görev ID: 1
Görev Açıklaması: Doktor randevusu al
Tamamlanma Durumu: ✓
------------------------------
```

### Görev Tamamlama ✅
```bash
python main.py done -i 0
```

### Görev Silme 🗑️
```bash
python main.py remove -i 0
```

### Yardım Alma ❓
```bash
python main.py --help
python main.py add --help
python main.py remove --help
```

## 📁 Proje Yapısı

```
todo-system/
│
├── main.py          # Ana uygulama ve komut satırı arayüzü
├── program.py       # TodoItem ve TodoManager sınıfları
├── file.log         # Otomatik oluşturulan log dosyası
└── README.md        # Bu dosya
```

## 🔧 Teknik Detaylar

### TodoItem Sınıfı
- `text`: Görev açıklaması
- `_done`: Tamamlanma durumu (varsayılan: False)
- `id`: Benzersiz görev kimliği (otomatik atanır)

### TodoManager Sınıfı
Görev yönetimi için ana sınıf:
- `add(task_text)`: Yeni görev ekler
- `remove(task_id)`: Görev siler
- `mark_done(task_id)`: Görevi tamamlanmış olarak işaretler
- `get_todo_item(task_id)`: ID'ye göre görev bulur
- `list()`: Tüm görevleri listeler

## 📊 Loglama

Uygulama tüm işlemleri `file.log` dosyasına kaydeder:
- ℹ️ Bilgi mesajları (görev ekleme, silme, vb.)
- ⚠️ Uyarı mesajları
- ❌ Hata mesajları

Log formatı:
```
2024-12-26 14:30 - INFO - Görev başarıyla eklendi! ID: 0
2024-12-26 14:31 - INFO - 1 görev listelendi!
```

## 🎨 Durum Göstergeleri

- ✅ `✓` - Tamamlanmış görev
- ❌ `✗` - Henüz tamamlanmamış görev

## 🐛 Hata Yönetimi

Uygulama aşağıdaki durumları kontrol eder:
- Boş görev açıklaması
- Var olmayan görev ID'si
- Geçersiz komutlar

## 📋 Komut Örnekleri

```bash
# Birden fazla görev ekleme
python main.py add -t "Kahvaltı hazırla"
python main.py add -t "Egzersiz yap"
python main.py add -t "Kitap oku"

# Durumu kontrol etme
python main.py list

# Görevleri tamamlama
python main.py done -i 0
python main.py done -i 1

# Tamamlanan görevleri silme
python main.py remove -i 0
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🚀 Gelecek Özellikler

- [ ] 📅 Görev tarihleri
- [ ] 🏷️ Görev kategorileri
- [ ] 🔍 Görev arama
- [ ] 📤 Görev dışa aktarma
- [ ] 🎨 Renkli çıktı
- [ ] 💾 Kalıcı veri saklama

---

