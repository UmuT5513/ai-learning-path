# Test Türleri ve Python Test Runner'ları
müthiş video = [python tdd with unittest](https://www.youtube.com/watch?v=6tNS--WetLI)

## Araba Farı Testi Örneği

Bir arabanın farlarının çalışıp çalışmadığını test etmek için aşağıdaki adımlar izlenir:

1. **Akşam olmasını bekle**  
   _Test Step_

2. **Dışarı çık**  
   _Test Step_

3. **Işıkları aç ve arkadaşına yanıp yanmadığını sor**  
   _Test Assertion_

---

## Test Türleri

### Integration Testing

> Birden fazla bileşenin birbiriyle çalışıp çalışmadığını test etmeye "integration testing" denir.

### Unit Test

Varsayalım ışıklar yanmıyor. Sorun nerede?  
- Ampuller patlak mı?
- Akım geliyor mu?
- Batarya çalışıyor mu?

Her küçük parçayı ayrı ayrı test eden testlere **"unit test"** denir.

---

## Test Runner'lar

Bir aracın sadece farı değil, diğer tüm bileşenleri de kontrol edilecekse ve her bileşene sebep olan birden fazla durum olabileceğinden çok sayıda test gerekir.  
Bu kadar çok testi yönetmek için "Python test runner"lar kullanılır.

**En popüler 3 test runner:**
- `unittest`
- `nose` veya `nose2`
- `pytest`

---

### Unittest

> Python'un standart kütüphanesinde yer alan, en temel test runner'dır.


if __name__ == "__main__":
    unittest.main()

eğer test_*.py dosyasında bu varsa python -m unittest test_* 'a gerek yok. direkt python test*.py yeterlidir.
