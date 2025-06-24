# User Manager Project

Bu proje, Python'un dataclasses modülünü kullanarak oluşturulmuş basit bir kullanıcı yönetim sistemidir. Kullanıcı oluşturma, ekleme ve alma işlemlerini destekler.

## Özellikler

* Ad, yaş, e-posta ve aktif durum ile kullanıcı oluşturma
* Otomatik benzersiz kullanıcı ID üretimi
* ID ile kullanıcı alma
* Kullanıcıları listeleme

## Gereksinimler

* Python 3.8+
* dataclasses modülü (Python 3.7+ ile birlikte gelir)

## Kullanım

1. Deposunu klonlayın veya indirin
2. `python main.py` komutunu çalıştırarak kullanıcı yöneticisini başlatın
3. Aşağıdaki komutları kullanarak kullanıcı yöneticisi ile etkileşime geçin:
	* [add](cci:1://file:///c:/Users/Umut/Desktop/ai-learning-path/advanced-python-2/mini-projects/data-classes/user-manager/main.py:9:4-10:31): Yeni bir kullanıcı ekleyin
	* `list`: Tüm kullanıcıları listleyin
	* `get <id>`: ID ile bir kullanıcı alın

## Kod Yapısı

Proje, iki ana dosyadan oluşur:

* `data_class.py`: [User](cci:2://file:///c:/Users/Umut/Desktop/ai-learning-path/advanced-python-2/mini-projects/data-classes/user-manager/data_class.py:4:0-22:98) dataclass'ını ve özniteliklerini tanımlar
* `main.py`: [UserClass](cci:2://file:///c:/Users/Umut/Desktop/ai-learning-path/advanced-python-2/mini-projects/data-classes/user-manager/main.py:5:0-13:68)'ı ve kullanıcıları yönetmek için metodlarını tanımlar

## Yazar

* Umut Ağrıman
