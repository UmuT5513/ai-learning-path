import re, string
def analyze(text: str)-> dict[str,int] | list[str]:
    # noktalamaları kaldır
    """
    Analyzes the given text, removing punctuation and trimming whitespace,
    and returns various statistics about the text.

    Args:
        text (str): The input string to analyze.

    Returns:
        tuple: A tuple containing:
            - dict[str, int]: A dictionary representing the frequency of each character,
              excluding punctuation and spaces.
            - dict[str, int]: A dictionary representing the frequency of each word,
              case-insensitively.
            - int: The total number of words in the text.
    """

    cleaned = text
    for punc in ",.!?;:“”()": 
        cleaned = cleaned.replace(punc, "")

    # baştaki ve sondaki boşlukları silinir
    cleaned.strip() 

    # kelime sayısı: words
    splitted = cleaned.split(" ")
    words: int = len(splitted) #list

    # toplam char frekansı (noktalama ve boşluklar hariç)
    freq: dict[str,int] = {}
    for ch in text:
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    

    # en çok geçen kelime
    word_freq: dict[str,int] = {}
    for word in splitted:
        word = word.lower()
        word_freq[word] = freq.get(word, 0) + 1
    

    return words, freq, word_freq
    

with open("text.txt", "r", encoding='utf-8') as file:
    raw = file.read()

words, char_freq, word_freq = analyze(raw)

print(words)
print(char_freq)
print(word_freq)
