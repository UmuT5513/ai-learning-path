# Task Management API

FastAPI ile geliştirilmiş basit ve etkili bir görev yönetimi REST API'si.

## 🚀 Özellikler

- ✅ **CRUD İşlemleri**: Task oluşturma, okuma, güncelleme ve silme
- 📊 **Status Yönetimi**: Pending, In Progress, Completed, Cancelled durumları
- 🎯 **Öncelik Seviyeleri**: Low (1) - Critical (5) arası öncelik sistemi
- ⚡ **Hızlı Aksiyonlar**: Task'ları tek tıkla tamamlama, başlatma, iptal etme
- 🔍 **Type Safety**: Pydantic ile güçlü veri validasyonu
- 📚 **Auto Documentation**: Swagger UI ile otomatik API dokümantasyonu
- 🎨 **Clean Code**: Enum'lar ve type hinting ile temiz kod yapısı

## 🛠️ Teknolojiler

- **FastAPI**: Modern, hızlı web framework
- **Pydantic**: Veri validasyonu ve serialization
- **Python 3.9+**: Type hints ve modern Python özellikleri
- **Uvicorn**: ASGI server

## 📁 Proje Yapısı

```
├── main.py          # API endpoint'leri ve iş mantığı
├── schemas.py       # Pydantic modelleri ve validasyonlar
└── README.md        # Proje dokümantasyonu
```

## 🔧 Kurulum

### 1. Gereksinimler

```bash
pip install fastapi uvicorn pydantic
```

### 2. Projeyi Çalıştırma

```bash
python main.py
```

veya

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 3. API Dokümantasyonu

Tarayıcınızda aşağıdaki URL'leri ziyaret edin:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📖 API Kullanımı

### Task Oluşturma

```http
POST /tasks
Content-Type: application/json

{
    "title": "Yeni Görev",
    "description": "Görev açıklaması",
    "status": "pending",
    "priority": 3
}
```

**Response:**
```json
{
    "id": 0,
    "title": "Yeni Görev",
    "description": "Görev açıklaması",
    "status": "pending",
    "priority": 3,
    "created_at": "2024-12-10T10:30:00.123456",
    "updated_at": null
}
```

### Task Listeleme

```http
GET /tasks
```

### Tek Task Getirme

```http
GET /tasks/{task_id}
```

### Task Güncelleme

```http
PUT /tasks/{task_id}
Content-Type: application/json

{
    "title": "Güncellenmiş Başlık",
    "status": "in_progress"
}
```

### Task Silme

```http
DELETE /tasks/{task_id}
```

## ⚡ Hızlı Aksiyonlar

### Task'ı Tamamla
```http
PATCH /tasks/{task_id}/complete
```

### Task'ı Başlat
```http
PATCH /tasks/{task_id}/start
```

### Task'ı İptal Et
```http
PATCH /tasks/{task_id}/cancel
```

## 🎯 Status ve Priority Değerleri

### Task Status
- `pending` - Beklemede
- `in_progress` - Devam Ediyor
- `completed` - Tamamlandı
- `cancelled` - İptal Edildi

### Priority Levels
- `1` - Low (Düşük)
- `2` - Medium (Orta) - *Default*
- `3` - High (Yüksek)
- `4` - Urgent (Acil)
- `5` - Critical (Kritik)

## 📝 Örnek Kullanım Senaryoları

### 1. Basit Task Oluşturma
```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Market alışverişi",
    "description": "Süt, ekmek, peynir al"
  }'
```

### 2. Yüksek Öncelikli Task
```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Sunum hazırla",
    "description": "Pazartesi toplantısı için",
    "priority": 4
  }'
```

### 3. Task'ı Başlatma
```bash
curl -X PATCH "http://127.0.0.1:8000/tasks/0/start"
```

### 4. Partial Update
```bash
curl -X PUT "http://127.0.0.1:8000/tasks/0" \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

## ⚠️ Kısıtlamalar

- **Veri Kalıcılığı**: Veriler memory'de tutulur, uygulama yeniden başlatıldığında kaybolur
- **Authentication**: Güvenlik katmanı bulunmaz
- **Rate Limiting**: API rate limiti yok
- **Pagination**: Tüm task'lar tek seferde döndürülür

## 🔮 Gelecek Geliştirmeler

- [ ] **Database Integration** (SQLite/PostgreSQL)
- [ ] **User Authentication** (JWT)
- [ ] **Filtering & Search** (status, priority, text bazlı)
- [ ] **Pagination** (skip/limit parametreleri)
- [ ] **Bulk Operations** (toplu ekleme/silme)
- [ ] **File Upload** (task'lara dosya ekleme)
- [ ] **Due Dates** (bitiş tarihi özelliği)
- [ ] **Categories/Tags** (kategori sistemi)

## 🐛 Hata Bildirimi

Bir hata bulduysanız veya öneriniz varsa, lütfen GitHub issues bölümünden bildirin.

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

---

**Not**: Bu API geliştirme ve öğrenme amaçlı olup, production ortamında kullanmadan önce güvenlik ve performans iyileştirmeleri yapılmalıdır.