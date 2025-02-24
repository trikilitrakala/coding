#ristorante magico
print ("Benvenuta al ristorante magico!")
# chiediamo i dati dell'utente
nome = input("come ti chiami?")
num_piatti = int(input("Quanti piatti hai ordinato?"))
costo_medio = int(input("quanto costa mediamente un piatto?"))
servizio = input ("il servizio è stato buono? (si/no)").strip().lower()

#calcoliamo il totale del conto
#totale = num_piatti * costo_medio

#print (f"il conto totale è di {totale} $")

#determiniamo la mancia
#if servizio == "si":
#    mancia = totale * 0.15
#    print("grazie per il tuo feedback positivo")
#else:   
    mancia = totale * 0.05
    print ("ci dispiace che il servizio non sia stato all'altezza")
       
#calcoliamo il totale da pagare
#totale_finale = totale + mancia

#stampiamo riepilogo
#print ("riepilogo del tuo conto")
#print (f"nome cliente {nome}")
#print (f"totale cibo: {totale} $")
#print (f"mancia aggiunta {mancia} $")
#print (f"totale da pagare:{totale_finale} $")
#print ("grazie per aver scelto il ristorante magico")


#bancomat
saldo = 500
prelievo = float (input("quanto vuoi prelevare?"))
if prelievo > saldo:
    print ("saldo insufficiente")
else:
    saldo -= prelievo
    print (f"nuovo saldo: {saldo} $")la
