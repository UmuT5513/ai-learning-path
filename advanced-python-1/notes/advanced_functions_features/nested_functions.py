def faktoriyel(sayi):

    if not isinstance(sayi, int):
        raise TypeError("Sayı bir tamsayı olmalıdır.")
    
    if not sayi>= 0:
        raise ValueError("Sayı negatif olmamalıdır.")

    def inner_faktöriyel(sayi):
        if sayi <= 1:
            return 1
        return sayi* inner_faktöriyel(sayi - 1)
    
    return inner_faktöriyel(sayi)

sonuc = faktoriyel(5)

try:
    sonuc = faktoriyel(-5)
    print(sonuc)
except Exception as e:
    print(f"Hata: {e}")

