
import random
import time

class DateNight:
    """
    Welcome to the game night program specially made for Ambre and Antoine!!!

    There are multiple categories to choose from, type a number between 1 and 5 to get started!
    """

    def __init__(self):
        # all date ideas --- CHANGE HERE
        self.__possibilities_dict = {
            "En extérieur": [
                "Pique-nique dans le parc",
                "Observation des étoiles",
                "Randonnée",
                "Coucher de soleil à la plage",
                "Cyclisme dans la nature",
                "Session de photographie en plein air",
                "Kayak sur un lac",
                "Journée de pêche",
                "Picnic au bord d'une rivière",
                "Parcours d'accrobranche"
            ],
            "En intérieur": [
                "Cuisiner ensemble",
                "Soirée cinéma avec popcorn maison",
                "Soirée jeux de société",
                "Pique-nique intérieur",
                "Atelier de cuisine",
                "Séance de peinture ou d'artisanat",
                "Soirée dégustation de vin et fromage",
                "Visite virtuelle de musées en ligne",
                "Cours de danse à domicile",
                "Journée de détente avec des massages à la maison"
            ],
            "Aventureux": [
                "Escape room",
                "Course de karting",
                "Balade en montgolfière",
                "Escalade",
                "Saut à l'élastique",
                "Ski nautique",
                "Plongée sous-marine",
                "Excursion en VTT",
                "Parachutisme en tandem",
                "Randonnée en quad"
            ],
            "Culturel": [
                "Visiter un musée",
                "Assister à une performance live",
                "Visite d'une galerie d'art",
                "Essayer une nouvelle cuisine",
                "Participer à une soirée culturelle",
                "Cours de poterie ou de sculpture",
                "Explorer des quartiers historiques",
                "Assister à un spectacle de théâtre",
                "Participer à une leçon de danse culturelle",
                "Visiter des sites archéologiques"
            ],
            "Relaxant": [
                "Soirée spa à la maison",
                "Dîner aux chandelles",
                "Yoga ensemble",
                "Rendez-vous en librairie",
                "Promenade tranquille au clair de lune",
                "Journée de méditation",
                "Lecture commune d'un livre",
                "Séance de cinéma en plein air",
                "Journée de plage relaxante",
                "Cueillette de fruits dans un verger"
            ]
        }

    def run(self):
        print(f"\n{'-'*100}\nBienvenue dans ce programme qui vous choisiera quelle activitée vous allez pouvoir faire ce soir!\
                \nIl y a le choix parmis ces options\
                \n(utilisez les nombres 1 à 5 sur le clavier puis taper sur entré)\n")

        # print all options and prompt the user to choose one
        categorie_choice = self.ask_categorie()

        # random activity from the categorie the user has chosen
        random_activity = self.get_random_categorie(categorie_choice)

        print(f"\nVous avez choisi {categorie_choice}\
                \n\nVotre activité seras (roulement de tambour) : ", end="")

        # wait a little for the suspens
        time.sleep(3)

        print(random_activity)
        print(f"{'-'*100}")


    def get_random_categorie(self, categorie):
        # gets a random activity from a categorie

        activities = self.__possibilities_dict[categorie]
        random_activity = random.choice(activities)

        return random_activity


    def ask_categorie(self):
        # displays all the categories and asks the user to choose one of them

        categories = list(self.__possibilities_dict.keys())

        for i in range(len(categories)):
            print(f"{i+1} -- {categories[i]}")

        try:
            chosen = categories[int(input(">>> ")) - 1]
        except:
            print("\nVeuillez s'il vous plaît choisir un nombre!!\n")
            return self.ask_categorie()

        return chosen

