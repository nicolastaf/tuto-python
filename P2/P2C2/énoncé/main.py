# Ecrivez votre code ici !
#races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
#for chien in races_de_chien:
  #  print(chien)

nombres = input("Saisissez une liste de nombres séparés par des virgules: ")
liste = nombres.split(",")
print("Liste des nombres:", liste)
liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)
# Calculer la somme des nombres
somme = 0
for nombre in liste_entiers:
    somme += nombre
print("Somme des nombres:", somme)
moyenne = somme / len(liste_entiers)
print("Moyenne des nombres:", moyenne)
# Trouver combien de nombres de la liste sont supérieurs à la moyenne
nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne:", nombre_au_dessus_moyenne)
# Equivalent à:
nombres_pairs = 0
for nombre in liste_entiers:
    if nombre % 2 == 0:
        #nombres_pairs = nombres_pairs + 1
        nombres_pairs += 1
print("Nombre de nombres pairs:", nombres_pairs)


