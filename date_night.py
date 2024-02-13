
import random
import time

class DateNight:
    """
    Welcome to the game night program specially made for Ambre and Antoine!!!

    There are multiple categories to choose from, type a number between 1 and 5 to get started!
    """

    def __init__(self):
        self.__possibilities_dict = {
        "En extérieur": ["Pique-nique dans le parc", "Observation des étoiles", "Randonnée", "Coucher de soleil à la plage"],
        "En intérieur": ["Cuisiner ensemble", "Soirée cinéma avec popcorn maison", "Soirée jeux de société", "Pique-nique intérieur"],
        "Aventureux": ["Escape room", "Course de karting", "Balade en montgolfière", "Escalade"],
        "Culturel": ["Visiter un musée", "Assister à une performance live", "Visite d'une galerie d'art", "Essayer une nouvelle cuisine"],
        "Relaxant": ["Soirée spa à la maison", "Dîner aux chandelles", "Yoga ensemble", "Rendez-vous en librairie"]
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

        chosen = categories[int(input(">>> ")) - 1]

        return chosen

