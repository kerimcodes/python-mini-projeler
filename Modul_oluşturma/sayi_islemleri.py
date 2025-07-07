def faktöriyel(n):
    if not isinstance(n,int):
       raise TypeError("Lütfen tam sayı girişi yapınız.")
    if n<0:
        return None
    i =1
    for sayi in range(1,n+1):
        i*=sayi
    return i
def asal_mi(n):
    if not isinstance(n,int):
        raise TypeError("Lütfen tam sayı girişi yapınız.")
    if n<2:
        return f"{n} sayısı 2 den küçük olduğu için asal değildir."
    for sayi in range(2,int((n**0.5)+1)):
        if n %sayi ==0:
            return f"{n} sayisi asal değildir."
    return f"{n} sayisi asaldır."

if __name__=="__main__":
    print(asal_mi(5))
    print(asal_mi(0))
    print(faktöriyel("a"))
    