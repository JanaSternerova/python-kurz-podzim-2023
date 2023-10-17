"""Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

Soubor si ulož a načti do slovníku.

Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.json"""

import json

with open("body.json", mode='r', encoding='utf-8') as bodyFile:
    data = json.load(bodyFile)

print (data)

prospech = {}

for jmeno,body in data.items():
    if body >= 60:
        prospech.update({jmeno:"pass"})
    else:
        prospech.update({jmeno:"fail"})

print (prospech)

with open("prospech.json", mode="w", encoding="utf-8") as output_file:
    json.dump(prospech, output_file, ensure_ascii=False)

