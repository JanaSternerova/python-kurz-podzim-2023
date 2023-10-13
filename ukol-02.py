"""
Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:

Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.
"""

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input ("Zadej číslo součástky: ")
pocet = int (input ("Zadej počet: "))


if kod in sklad.keys():
    print(sklad[kod])
    if pocet <= sklad[kod]:
        print (f" Poptávku lze uspokojit v plné výši.")
        sklad[kod] = sklad[kod] - pocet
        print(sklad[kod])
    else:
        print (f" Lze prodat pouze Omezené množství.")
        sklad.pop(kod)
        print(sklad)
else:
    print ("Součástka není skladem.") 

"""
mnozstvi_mensi = sklad[kod] < pocet
mnozstvi_dostatecne = sklad[kod] >= pocet
je_skladem = kod in sklad.keys()

if (je_skladem and mnozstvi_dostatecne):
    print (f" Poptávku lze uspokojit v plné výši.")
    sklad[kod] = sklad[kod] - pocet
    print(sklad[kod])
elif (je_skladem and mnozstvi_mensi):
    print (f" Lze prodat pouze Omezené množství.")
    sklad.pop(kod)
    print(sklad)
else:
    print ("Součástka není skladem.") 
"""
