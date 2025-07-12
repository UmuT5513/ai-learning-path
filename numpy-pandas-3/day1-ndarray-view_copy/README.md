# NumPy Views ve Memory Sharing

Bu proje, NumPy'da view ve copy kavramlarını, memory sharing mekanizmalarını ve farklı array manipülasyon yöntemlerinin davranışlarını incelemektedir.

## 📋 İçerik

### 1. Temel Kavramlar
- **View**: Aynı bellek bloğunu paylaşan farklı Python nesneleri
- **Copy**: Tamamen yeni bellek alanında oluşturulan kopya
- **Base**: Bir view'ın türetildiği orijinal array referansı
- **Memory Sharing**: İki array'in aynı bellek bloğunu paylaşıp paylaşmadığı

### 2. İncelenen Yöntemler

#### 2.1 reshape() Yöntemi
```python
arr = np.arange(16).reshape((4,4))
flat1 = arr.reshape(-1)
```
- Aynı veriyi paylaşan yeni bir view oluşturur
- `np.shares_memory()` ile kontrol edilebilir
- Bellek bloğu paylaşılır ama Python nesneleri farklıdır

#### 2.2 ravel() Yöntemi
```python
flat2 = arr.ravel()
```
- `reshape()` gibi view oluşturur
- Aynı memory sharing davranışını gösterir

#### 2.3 flatten() Yöntemi
```python
flat3 = arr.flatten()
```
- **Dikkat**: Bu yöntem copy döndürür, view değil!
- `flat3.base` None döner
- `np.shares_memory(arr, flat3)` False döner

#### 2.4 view() Yöntemi
```python
view1 = base0.view()
```
- Explicit view oluşturma
- Shape değişiklikleri yapılabilir
- Orijinal base'i korur

### 3. Base Referans Zinciri

```python
base0 = np.arange(16)           # Gerçek "owner"
arr = base0.reshape((4,4))      # arr.base is base0 → True
flat1 = arr.reshape(-1)         # flat1.base is base0 → True
view1 = base0.view()            # view1.base is base0 → True
```

**Önemli**: View'lar her zaman en dipteki orijinal veri sahibini (`base0`) referans gösterir, ara view'ları değil.

### 4. Memory Sharing Testleri

#### 4.1 View Davranışı (Değişiklikler Yansır)
- `reshape()`: ✅ Değişiklikler orijinal array'e yansır
- `ravel()`: ✅ Değişiklikler orijinal array'e yansır  
- `view()`: ✅ Değişiklikler orijinal array'e yansır
- Çoklu `reshape()` zincirleri: ✅ Değişiklikler yansır

#### 4.2 Copy Davranışı (Değişiklikler Yansımaz)
- `flatten()`: ❌ Değişiklikler orijinal array'e yansımaz

### 5. Pratik Örnekler

```python
# View oluşturma - değişiklikler yansır
base0 = np.arange(16)
arr = base0.reshape((4,4))
flat1 = arr.reshape(-1)
flat1[0] = 100  # arr[0,0] da 100 olur

# Copy oluşturma - değişiklikler yansımaz  
flat3 = arr.flatten()
flat3[0] = 200  # arr değişmez
```

## 🔍 Kontrol Yöntemleri

### 1. Base Kontrolü
```python
print(array.base is original_array)  # True/False
```

### 2. Memory Sharing Kontrolü
```python
print(np.shares_memory(array1, array2))  # True/False
```

### 3. Identity Kontrolü
```python
print(array1 is array2)  # True/False (aynı Python nesnesi mi?)
```

## ⚠️ Önemli Notlar

1. **View vs Copy**: `flatten()` dışındaki shape manipülasyon yöntemleri genellikle view döndürür
2. **Base Chain**: View'lar her zaman en dipteki orijinal array'i referans gösterir
3. **Memory Efficiency**: View'lar memory efficient'tir çünkü veri kopyalanmaz
4. **Unintended Modifications**: View'larda yapılan değişiklikler orijinal array'i etkileyebilir

## 🧪 Test Edilenler

- ✅ `reshape()` ile view oluşturma
- ✅ `ravel()` ile view oluşturma  
- ✅ `flatten()` ile copy oluşturma
- ✅ `view()` ile explicit view oluşturma
- ✅ Çoklu reshape zincirleri
- ✅ Memory sharing kontrolleri
- ✅ Base referans kontrolleri
- ✅ Değişikliklerin yansıma testleri

## 📚 Referanslar

Bu analiz, NumPy'da memory management ve view/copy mekanizmalarının derinlemesine anlaşılması için hazırlanmıştır. Özellikle büyük veri setleriyle çalışırken memory efficiency açısından kritik öneme sahiptir.