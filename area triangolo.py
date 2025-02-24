def area_triangolo (base, altezza): 
    return (base*altezza) / 2

try:
    base = float(input("base del triangolo: "))
    altezza = float(input("altezza del triangolo: "))
    area = area_triangolo (base, altezza)
    print(f"l'area del triangolo è {area}")
except ValueError:
    print("errore! devi inserire un numero")