"""ukol-06: Evidence aut
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	Peugeot 403 Cabrio	47534
1P3 4747	Škoda Octavia	41253
Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

registrační značka automobilu registracni_znacka,
značka a typ vozidla typ_vozidla,
počet najetých kilometrů najete_km,
informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy volné.""" 

class Auta:  
    def __init__(self, registracni_znacka:str, typ_vozidla:str, najete_km:int, dostupne:bool): 
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if self.dostupne: #== True:
            self.dostupne = False
            return f"Potvrzuji zapůjčení vozidla."
        else:
            return f"Vozidlo není k dispozici"

    def vrat_auto(self,stav_tachometru,pocet_dni):
        self.dostupne = True
        self.najete_km = stav_tachometru
        cena = pocet_dni * 300
        if (pocet_dni < 7):
            cena = pocet_dni * 400
        return f"Cena půjčení je {cena}."

        
    def get_info(self):
        if self.dostupne == True:
            return f" Auto s SPZ {self.registracni_znacka} značky {self.typ_vozidla}, má najeto{self.najete_km}je ve stavu dostupné."
        else:
            return f" Auto s SPZ {self.registracni_znacka} značky {self.typ_vozidla}, má najeto{self.najete_km}je ve stavu nedostupné."

    #def __str__(self):
        return f" Auto s SPZ {self.registracni_znacka} značky {self.typ_vozidla}, má najeto{self.najete_km}je ve stavu {self.dostupne}."
       
peugeot = Auta(registracni_znacka= "4A2 3020", typ_vozidla="Peugeot 403 Cabrio", najete_km=47534, dostupne=True)

skoda_octavia = Auta(registracni_znacka= "1P3 4747", typ_vozidla="Škoda Octavia", najete_km=41253, dostupne=True)


pozadavek = input("Jakou značku vozidla Peugeot nebo Škoda?:")

auto = skoda_octavia
if pozadavek == "Peugeot":
    auto = peugeot
print(auto.get_info())
print(auto.pujc_auto())
#print(auto.get_info())
#print(auto.pujc_auto())

vraceni_km = input ("Kolik km má auto při vrácení?: ")
vraceni_pocetdni= int(input ("Kolik dní bylo auto půjčeno?: "))

print(auto.vrat_auto(vraceni_km,vraceni_pocetdni))

print(auto.get_info())


"""
if pozadavek == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
else:
    print(skoda_octavia.get_info())
    print(skoda_octavia.pujc_auto())

print(peugeot.get_info())
print(skoda_octavia.get_info())
"""

"""
Vytvoř objekty, které reprezentují oba automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát."""

"""
Nepovinný bonus
Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return."""
