#Arthur Robin
#1/30/2023
#POO3
import random as r

# fonction pour générer des dés aléatoires pour un Npc


def random_statistiques():
    # liste des dés
    de1 = r.randint(1, 6)
    de2 = r.randint(1, 6)
    de3 = r.randint(1, 6)
    de4 = r.randint(1, 6)
    # liste des dés 1 a 4
    liste_des_des = [de1, de2, de3, de4]
    # tri de la liste
    liste_des_des.sort()
    # suppression du plus petit dé
    liste_des_des.pop(0)
    # somme des 3 dés restant
    calcul_statistique = sum(liste_des_des)
    # retourne la valeur de la statistique
    return calcul_statistique

# class pour définir les caractéristiques des Npc


class Npc:
    def __init__(self):
        # générent les caractéristiques des Npc
        self.force = random_statistiques()
        self.agilite = random_statistiques()
        self.constitution = random_statistiques()
        self.intelligence = random_statistiques()
        self.sagesse = random_statistiques()
        self.charisme = random_statistiques()
        self.armure = r.randint(1, 12)
        self.nom = str
        self.race = str
        self.espece = str
        self.nombre_de_vie = r.randint(1, 20)
        self.profession = str

    # affiche les caractéristiques des Npc
    def afficher_caracteristiques(self):
        print("Force: ", self.force)
        print("Agilité: ", self.agilite)
        print("Constitution: ", self.constitution)
        print("Intelligence: ", self.intelligence)
        print("Sagesse: ", self.sagesse)
        print("Charisme: ", self.charisme)
        print("Armure: ", self.armure)
        print("Nom: ", self.nom)
        print('Race: ', self.race)
        print('Espèce: ', self.espece)
        print('Nombre de vie: ', self.nombre_de_vie)
        print('Profession: ', self.profession)

# classe pour définir les caractéristiques de Kobold


class Kobold(Npc):
    def __init__(self):
        # hérite des caractéristiques de Npc
        super().__init__()

    # méthode pour effectuer une attaque
    def attaquer(self, cible):
        return

    # méthode pour subir des dégâts
    def subir_degats(self, nombre_de_degats):
        self.nombre_de_vie -= nombre_de_degats


# classe pour définir les caractéristiques de Hero
class Hero(Npc):
    def __init__(self):
        # hérite des caractéristiques de Npc
        super().__init__()

    def attaquer(self, cible):
        de_attaque = r.randint(1, 20)
        if de_attaque == 20:
            # si le dé d'attaque est égal à 20 alors on inflige des degat d'un lancer de de de 8
            cible.subir_degats(r.randint(1, 8))

        elif 1 < de_attaque < 20 and de_attaque > cible.armure:
            cible.subir_degats(r.randint(1, 6))
    # méthode pour subir des dégâts

    def subir_degats(self, nombre_de_degats):
        return
