# Öğrenci Yönetim Sistemi

Bu proje, öğrencilerin kayıtlarını yönetmek, kurs eklemek, öğrencilere kurs atamak ve notları takip etmek için geliştirilmiş bir komut satırı uygulamasıdır.

## Özellikler

- **Öğrenci Yönetimi**: Öğrenci ekleme ve listeleme
- **Kurs Yönetimi**: Online ve Laboratuvar kursları ekleme
- **Kurs Atama**: Öğrencilere kurs atama
- **Not Yönetimi**: Öğrencilere not ekleme ve görüntüleme
- **Esnek Not Hesaplama**: Kurs türüne göre ağırlıklı not hesaplama

## Dosya Yapısı

```
├── cli.py          # Komut satırı arayüzü
├── program.py      # Ana sınıf tanımları
└── README.md       # Bu dosya
```

## Kurulum

1. Projeyi klonlayın veya dosyaları indirin
2. Python 3.6+ kurulu olduğundan emin olun
3. Terminal/komut istemcisini açın ve proje dizinine gidin

## Kullanım

### Öğrenci Ekleme
```bash
python cli.py add-student --name "Ahmet" --id 1001
```

### Kurs Ekleme

**Online Kurs:**
```bash
python cli.py add-course --type "Online" --name_katilim_note "Matematik-0.3-0.7"
```

**Laboratuvar Kursu:**
```bash
python cli.py add-course --type "Lab" --name_katilim_note "Fizik-0.4-0.6"
```

Format: `KursAdı-KatılımAğırlığı-NotAğırlığı`

### Kurs Atama
```bash
python cli.py assign-course --id 1001 --courses "Matematik"
```

### Not Ekleme
```bash
python cli.py add-grade --id 1001 --course "Matematik" --katilim 85 --note 90
```

### Listeleme İşlemleri

**Öğrencileri Listele:**
```bash
python cli.py list-students
```

**Kursları Listele:**
```bash
python cli.py list-courses
```

**Öğrenci Notlarını Listele:**
```bash
python cli.py list-grades --id 1001
```

## Sınıf Yapısı

### Student Sınıfı
- Öğrenci bilgilerini yönetir
- Kurs ve not ekleme işlemlerini gerçekleştirir
- Iterator protokolünü destekler
- Decorator ile not doğrulama yapar

### Course Sınıfı (Abstract Base Class)
- Tüm kurs türleri için temel sınıf
- Abstract metotlar: `hesapla_not()`, `create_course()`

### OnlineCourse Sınıfı
- Online kurslar için özel sınıf
- Katılım ve sınav notlarını ağırlıklı hesaplar

### LabCourse Sınıfı
- Laboratuvar kursları için özel sınıf
- Katılım ve lab notlarını ağırlıklı hesaplar

## Not Hesaplama Sistemi

Her kurs türü için not hesaplama farklıdır:

- **Online Kurs**: `(Katılım × Katılım_Ağırlığı) + (Sınav × Sınav_Ağırlığı)`
- **Lab Kurs**: `(Katılım × Katılım_Ağırlığı) + (Lab × Lab_Ağırlığı)`

## Validasyon Kuralları

- Öğrenci ID'leri benzersiz olmalıdır
- Notlar 0-100 arasında olmalıdır
- Ağırlıklar toplamı genellikle 1.0 olmalıdır
- Kurs adları string olmalıdır

## Örnekleri

### Tam Örnek Kullanım

```bash
# 1. Öğrenci ekle
python cli.py add-student --name "Ayşe" --id 1002

# 2. Online kurs ekle
python cli.py add-course --type "Online" --name_katilim_note "Algoritma-0.2-0.8"

# 3. Lab kursu ekle
python cli.py add-course --type "Lab" --name_katilim_note "Kimya-0.5-0.5"

# 4. Kursu öğrenciye ata
python cli.py assign-course --id 1002 --courses "Algoritma"

# 5. Not ekle
python cli.py add-grade --id 1002 --course "Algoritma" --katilim 75 --note 88

# 6. Notları görüntüle
python cli.py list-grades --id 1002
```

## Hata Yönetimi

- Geçersiz notlar için `ValueError` ve `TypeError` fırlatılır
- Komut satırı hataları için kullanıcı dostu mesajlar gösterilir
- Eksik parametreler için otomatik yardım mesajları

## Geliştirici Notları

- Sınıflar arasında kompozisyon ilişkisi kullanılır
- Generator fonksiyonları ile memory-efficient iteration
- Decorator pattern ile input validation
- Class methods ile factory pattern implementasyonu

## Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

## Katkıda Bulunma
**Bazı fonksiyonlar şuan çalışmıyor olabilir. Sorunu beraber çözmeyi deneyebiliriz.**
1. Projeyi fork edin
2. Yeni özellik branch'i oluşturun
3. Değişikliklerinizi commit edin
4. Pull request gönderin



