text = "Merhaba, dünya!"

# Tek bir karaktere erişmek
first_char = text[0]         # 'M'
last_char  = text[-1]        # '!'

# Dilimleme: [başlangıç:son:adım]
sub = text[0:7]              # 'Merhaba'
every_second = text[::2]     # 'Mrhb dn!'

# Metnin başından sondan kırpma
head_5 = text[:5]            # 'Merha'
tail_5 = text[-5:]           # 'a!'



sentence = "bu bir örnek cümledir"

# Boşluklardan böl (tokenize temel hali)
words = sentence.split()     # ['bu','bir','örnek','cümledir']

# Virgülle böl
csv = "elma,armut,çilek"
fruits = csv.split(",")      # ['elma','armut','çilek']

# Listeyi yeniden birleştir
rejoined = " ".join(words)   # 'bu bir örnek cümledir'




text = "bugün bugün değil mi bugün?"

# Belirli bir alt metni bul (ilk geçiş)
idx = text.find("bugün")     # 0, eğer yoksa -1

# Tüm metinde kaç kez var?
cnt = text.count("bugün")    # 3





raw = "   merhaba dünya!!!   "

# Baş ve sondaki boşlukları al
trimmed = raw.strip()        # 'merhaba dünya!!!'

# Noktalama işaretlerini silmek için
no_exclaims = trimmed.replace("!", "")  
# 'merhaba dünya'

# Birden fazla karakter silmek istersek:
clean = trimmed
for ch in "!,.":
    clean = clean.replace(ch, "")
# 'merhaba dünya'






text = "Merhaba, dünya! 123"
filtered = []
for ch in text:
    if ch.isalpha() or ch.isspace():
        filtered.append(ch)
cleaned = "".join(filtered)   # 'Merhaba dünya'

cleaned = "".join([ch for ch in text if ch.isalpha() or ch.isspace()])





s = "PyThOn"

s_lower = s.lower()           # 'python'
s_upper = s.upper()           # 'PYTHON'
s_title = s.title()           # 'Python'
s_cap   = s.capitalize()       # 'Python'






def count_words_manual(text: str) -> int:
    # Noktalama işaretlerini kaldır (basit)
    for ch in ",.!?;:":
        text = text.replace(ch, "")
    # Küçük harfe çevir
    text = text.lower()
    # Split
    tokens = text.split()
    # Empty string’leri filtrele
    tokens = [t for t in tokens if t]
    return len(tokens)

print(count_words_manual("Merhaba, dünya! Nasılsın?"))  # 4





from typing import Dict, List
def char_freq_manual(text: str) -> Dict[str,int]:
    freq: Dict[str,int] = {}
    for ch in text:
        if not ch.isspace():    # boşlukları saymak istemezsen
            freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_freq_manual("aabbc a!"))  
# {'a':3, 'b':2, 'c':1, '!':1}


