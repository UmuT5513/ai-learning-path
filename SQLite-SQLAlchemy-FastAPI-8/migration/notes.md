Alembic, SQL alchemy bünyesinde bulunan bir *migration tool* dur.

# 1. Migration Nedir?

Migration (göç/dönüşüm), yazılım geliştirmede veritabanı şemasının versiyon kontrolü demektir.
**Sen kodunu değiştiriyorsun → modellerine yeni bir sütun ekliyorsun → veritabanı şemasının da bu değişikliği izlemesi gerekiyor.** İşte bu noktada migration devreye giriyor.

Örnek:

**Başlangıç: users tablosu var (id, username).**

Yeni istek: email kolonu eklenecek.
Migration dosyası: `ALTER TABLE users ADD COLUMN email VARCHAR(255);` gibi SQL komutlarını içerir.

# 2. Alembic’in Mantığı

**Alembic, migrationları versiyonlanmış Python dosyaları olarak tutar.
Genelde proje kök dizininde alembic/ klasörü olur.**

İçinde:

*versions/* → migration script’lerinin tutulduğu yer

*env.py* → migration ortamı ayarları

*alembic.ini* → Alembic konfig dosyası

**Alembic migrationları şu şekilde çalışır:**

Sen bir değişiklik yaparsın (ör. SQLAlchemy models.py içinde).

`alembic revision --autogenerate -m "add email to users"` komutunu çalıştırırsın.

Bu, yeni bir migration dosyası oluşturur.

`alembic upgrade head` komutunu çalıştırırsın.

Bu, migration dosyasındaki SQL komutlarını sırasıyla SQLite’a uygular.

# ÖZET
## Migration = Veritabanı şema versiyonlaması

## Alembic = SQLAlchemy için migration aracı

## revision ile dosya oluştur, upgrade ile uygula, downgrade ile geri al

### downgrade sqlite da pek temiz çalışmaz:

**SQLite bazı DDL işlemlerini desteklemez.**
Örneğin:

`ALTER TABLE DROP COLUMN` yok (yani sütun silemezsin).

`ALTER TABLE MODIFY COLUMN` yok (kolon tipini değiştiremezsin).

Bu yüzden Alembic bazen downgrade işlemlerinde zorlanır. Çözüm genelde şu:

**Yeni tabloyu oluştur, eski tablodan veriyi kopyala, eski tabloyu sil, yenisini yeniden adlandır.**

Yani migration script’i, PostgreSQL gibi full-featured DB’lerde çok temizken, SQLite’ta biraz “hacky” olabilir.

## SQLite kısıtlı, ama basit projelerde gayet iş görür


# En çok kullanılan komutlar:

### Alembic konfigürasyonu başlat
`alembic init alembic`

### Yeni migration oluştur (autogenerate = modelleri tarar)
`alembic revision --autogenerate -m "create users table"`

### Migration uygula (son versiyona kadar)
`alembic upgrade head`

### Migration geri al (bir önceki sürüme dön)
`alembic downgrade -1`

### Mevcut versiyonu kontrol et
`alembic current`

### Tüm migration geçmişini gör
`alembic history`
