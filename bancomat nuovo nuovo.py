saldo = 1000

def mostra_menu():
    print("Benvenuto nella tua banca")
    print("1 prelievo")
    print("2 deposito")
    print("3 controllo saldo")
    print("4 esci")    

def prelievo(saldo, importo):
    if importo > saldo:
        print("non ce li hai questi soldi")
    elif importo <= 0:
        print("importo non valido")
    else:
        saldo -= importo
        print(f"sei sempre più povera. ti è rimasto solo {saldo: }")
    return saldo

def deposito (saldo, importo):
    if importo <= 0:
        print("importo non valido")
    else:
        saldo += importo
        print(f"sei sempre più ricca. ora hai {saldo: }")
    return saldo

def mostra_saldo (saldo):
    print(f"hai {saldo} euro nel conto. poveraccia")

while True:
    mostra_menu()
    scelta = input("scegli un'opzione")

    try:
        if scelta == "1":
            importo = float(input("quanto vuoi prelevare?"))
            saldo = prelievo(saldo, importo)
        elif scelta == "2":
                importo = float(input("quanto vuoi depositare?"))
                saldo = deposito (saldo, importo)
        elif scelta == "3":
            saldo(saldo)
        elif scelta == "4":
            print("grazie per avere usato banco di sardegna")
    except ValueError:
        print ("inserisci numero euro, cretina")
