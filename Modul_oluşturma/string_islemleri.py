def sesli_harf_sayaci(metin):
    
    if not isinstance(metin,str):
        raise TypeError("sesli_harf_sayaci fonksiyonunda sadece string kullanmalısın.")
    sesli_harf = 0
    for harfler in metin.lower():
        if harfler in "aeıioöuü":
            sesli_harf += 1
    return sesli_harf
def kelime_sayisi_hesaplama(metin):
    if not isinstance(metin,str):
        raise TypeError("kelime_sayisi fonksiyonunda sadece string kullanılmalıdır.")
    return len(metin.split())
def ters_cevir(metin):
    if not isinstance(metin,str):
          raise TypeError("ters_cevir fonksiyonunda sadece string kullanılmalıdır.")
    return metin[::-1]
if __name__=="__main__":
    print(sesli_harf_sayaci("kerim"))