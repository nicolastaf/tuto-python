# Ecrivez votre code ici

salaire_annuel = float(
    input("Saisissez votre salaire annuel : "))
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):  
    return salaire_hebdomadaire / heures_travaillees 

heures_travaillees = float(
    input("Entrez le nombre d'heures travaillées par semaine : "))

salaire_mensuel = salaire_mensuel(float(salaire_annuel))
salaire_hebdomadaire = salaire_hebdomadaire(salaire_mensuel)
salaire_horaire = salaire_horaire(salaire_hebdomadaire, heures_travaillees)

print("Salaire horaire : ", salaire_horaire)