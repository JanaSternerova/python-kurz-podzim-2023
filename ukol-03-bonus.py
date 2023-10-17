import json

with open("body.json", mode='r', encoding='utf-8') as bodyFile:
    znamka = json.load(bodyFile)

print (znamka)

with open("bonusy.json", mode='r', encoding='utf-8') as bodyFile:
    bonus_body = json.load(bodyFile)

print (bonus_body)

for jmeno, body in znamka.items():
    # Součet bodů z písemky a bonusových bodů
    soucet_body = body + bonus_body.get(jmeno, 0)
    znamka.update({jmeno:soucet_body})

print (znamka)

for jmeno,soucet_body in znamka.items():

    # Přiřazení známky
    if soucet_body >= 90:
        znamka.update({jmeno:"1"})
    elif soucet_body >= 70:
        znamka.update({jmeno:"2"})
    elif soucet_body >= 50:
        znamka.update({jmeno:"3"})
    elif soucet_body >= 30:
        znamka.update({jmeno:"4"})
    else:
        znamka.update({jmeno:"5"})

print (znamka)

with open("znamky.json", mode="w", encoding="utf-8") as output_file:
    json.dump(znamka, output_file, ensure_ascii=False) 
