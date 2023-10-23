""" Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci. 

Vytvoř seznam průměrných teplot pro každý den.
Vytvoř seznam ranních teplot.
Vytvoř seznam nočních teplot.
Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu. """

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

"""
avg_temp = []
temp_morn = []
temp_night = []
temp_aft = []

for den in teploty:
    temp_morn.append(den[0])
    temp_night.append(den[-1])
    temp_aft_1 = []
    temp_aft_1.append(den[1])
    temp_aft_1.append(den[3])
    temp_aft.append(temp_aft_1)
    avg_temp.append(round(sum(den)/len(den),2))

"""

temp_morn = [den[0] for den in teploty]
temp_night =[den[-1] for den in teploty]

def get_temp_aft (teplota_poledne, teplota_vecer):
    temp_aft_1 = []
    temp_aft_1.append(teplota_poledne)
    temp_aft_1.append(teplota_vecer)
    return temp_aft_1

temp_aft = [get_temp_aft(den[1],den[3]) for den in teploty]

avg_temp = [(round(sum(den)/len(den),2)) for den in teploty]


print(temp_morn)
print(temp_night)
print(temp_aft)
print(avg_temp) 