# manual_text_tools.py

from typing import Dict, List

def slicing_examples(text: str) -> None:
    """
    Karakter ve dilimleme örnekleri.
    """
    print("Orijinal:", text)
    print("İlk karakter:", text[0])
    print("Son karakter:", text[-1])
    print("0-7 dilimi:", text[0:7])
    print("Her 2. karakter:", text[::2])
    print("Baştan 5:", text[:5])
    print("Sondan 5:", text[-5:])
    print()

def split_join_examples(sentence: str, csv: str) -> None:
    """
    split & join örnekleri.
    """
    words = sentence.split()
    fruits = csv.split(",")
    rejoined = " ".join(words)

    print("Cümle:", sentence)
    print("Split words:", words)
    print("CSV:", csv)
    print("Split fruits:", fruits)
    print("Rejoined:", rejoined)
    print()

def find_count_examples(text: str, sub: str) -> None:
    """
    find() ve count() örnekleri.
    """
    idx = text.find(sub)
    cnt = text.count(sub)
    print(f"Metin: {text}")
    print(f"Alt metin '{sub}' ilk bulunduğu indeks:", idx)
    print(f"Alt metin '{sub}' toplam sayısı:", cnt)
    print()

def replace_strip_examples(raw: str) -> None:
    """
    replace(), strip() ve birden fazla karakter silme örnekleri.
    """
    trimmed = raw.strip()
    no_exclaims = trimmed.replace("!", "")
    clean = trimmed
    for ch in "!,.;:":
        clean = clean.replace(ch, "")

    print(f"Orijinal: '{raw}'")
    print(f"strip(): '{trimmed}'")
    print(f"replace('!',''): '{no_exclaims}'")
    print(f"Loop ile noktalama silme: '{clean}'")
    print()

def count_words_manual(text: str) -> int:
    """
    Basit kelime sayısı (noktalama temizle + split).
    """
    for ch in ",.!?;:":
        text = text.replace(ch, "")
    text = text.lower()
    tokens = text.split()
    tokens = [t for t in tokens if t]
    return len(tokens)

def char_freq_manual(text: str) -> Dict[str, int]:
    """
    Karakter sıklığı (boşluk hariç).
    """
    freq: Dict[str,int] = {}
    for ch in text:
        if not ch.isspace():
            freq[ch] = freq.get(ch, 0) + 1
    return freq

if __name__ == "__main__":
    sample_text = "Merhaba, dünya! Python 3.10 ile metin işleme."
    slicing_examples(sample_text)

    sentence = "bu bir örnek cümledir"
    csv = "elma,armut,çilek"
    split_join_examples(sentence, csv)

    find_count_examples("bugün bugün değil mi bugün?", "bugün")

    raw = "   merhaba dünya!!!   "
    replace_strip_examples(raw)

    manual_count = count_words_manual("Merhaba, dünya! Nasılsın?")
    print("Manual kelime sayısı:", manual_count)

    freq = char_freq_manual("aabbc a!")
    print("Manual karakter frekansı:", freq)
