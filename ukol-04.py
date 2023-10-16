"""
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:

Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420". 

Nepovinný bonus 1
Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš například tak, že použiješ metodu .replace(). První parametr metody replace je znak, který chceš nahradit, a druhý parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".

Odkaz na dokumentaci metody replace: https://docs.python.org/3/library/stdtypes.html#str.replace 

Nepovinný bonus 2
Přidej svým funkcím typování, aby bylo jasné, jaký typy mají parametry tvých funkcí a jaká je návratová hodnota tvých funkcí.

K typování se dostaneme až v 5. lekci. Pokud chceš, můžeš úlohu řešit předem pomocí Čtení na doma """ 

import math

def over_platnost_cisla (tel_cislo: str) -> bool:
    """ fce pro ověření platnosti tel. čísla dle délky"""
    tel_cislo_upravene = tel_cislo.replace(" ","")
    # print (tel_cislo_upravene)
    delka_cisla = len(tel_cislo_upravene)
    if delka_cisla == 9: 
        delka_cisla = True
        return delka_cisla == True
    elif delka_cisla == 13:
        predvolba = tel_cislo[0:4]
        if predvolba == "+420":
            delka_cisla = True
        return delka_cisla
    else: 
        delka_cisla = False
        return delka_cisla 
    
tel_cislo = (input ("Zadej telefonní číslo pro zaslání sms (platné pro ČR): "))
vysledek = over_platnost_cisla (tel_cislo)

"""print (f"{vysledek} ") """

if vysledek == True:
    def cena_sms(text_zpravy: str) -> int:
        """ fce pro výpočet ceny sms, vstup text zpravy, výstup - cena na základe délky textu zpravy.  """
        cena_jedne_sms = 3
        delka_sms = len(text_zpravy)
        cena_sms = math.ceil(delka_sms/180)* cena_jedne_sms
        return cena_sms

    #vstupy od uživatele pro cena_sms
    text_zpravy = (input ("Zadej obsah sms: "))

    #výstup pro cena_sms
    print (f"Cena sms je {cena_sms(text_zpravy)}.")

else:
    print("Číslo není platné.")