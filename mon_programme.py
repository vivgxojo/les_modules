from mon_module import *
# bonjour
mon_inventaire : list[str] = ["Dégats", "Vitalité"]
total_inventaire : int = 5
total_copie : int = 0
total_autre_copie : int = 0

ajouter_potion(mon_inventaire, "Invisibilité")
total_inventaire = additionner_potions(total_inventaire, 1)

ma_copie = copier_inventaire(mon_inventaire)
total_copie = total_inventaire
mon_autre_copie = mon_inventaire # ça reste la même liste, pas une copie
total_autre_copie = total_inventaire # vrai copie de la variable

ajouter_potion(mon_inventaire, "Guérison")
total_inventaire = additionner_potions(total_inventaire, 1)

ajouter_potion(mon_inventaire, "Vitessssssssssssssse")
total_inventaire = additionner_potions(total_inventaire, 1)

print("Inventaire:", mon_inventaire, "Total:", total_inventaire)
print("Ma copie:", ma_copie, "Total:", total_copie)
print("Autre copie:", mon_autre_copie, "Total:", total_autre_copie)