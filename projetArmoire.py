habitschaud = ["T-shirt manches courtes", "Polo", "Jean", "Jogging",
               "Shirt", "Caleçon", "Chausettes", "Chaussures"]  # Liste des habits chauds
habitsfroid = ["Manteau", "Pull", "T-shirt manches longues", "Jean",
               "Jogging", "Caleçon", "Chausettes", "Chaussures"]  # Liste des habits froids
habitsacc = ["bonnet(s)", "écharpe(s)", "casquette(s)", "chapeau(x)", "lunette(s) de soleil",
             "cravate(s)", "noeud(s) papillon", "montre(s)", "ceinture(s)"]  # Liste des accessoires


météo = input("Quel temps fait-il ? (chaud/froid) ")  # On demande quel temps il fait

if météo in ["Chaud", "chaud", "CHAUD"]:  # Si il fait chaud :
    jour = input("Sommes-nous en week-end ou en semaine ? (semaine/week-end) \n")
    # On demande si on est un jour de la semaine ou le week-end
    if jour in ["Week-end", "week-end", "WEEK-END"]:  # Si on est en week-end
        print(f"Il fait chaud et vous êtes en week-end , voici ce que vous avez de disponible comme habits pour les journées chaudes dans l'armoire : ")
        # On imprime ce message
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:  # Boucle de la liste des habits chauds
            print(f"{habitschaud[i]} ")  # Imprimer les habits chauds
        acc = input("Voulez-vous prendre un accessoire ? (o/n) ")  # On demande si la personne veut des accessoires
        if acc in ["n", "Non", "non", "NON"]:  # Si la personne ne veut pas d'accessoire :
            print(f"Vous êtes prêt pour votre journée !")  # On imprime que la personne est prête pour la journée
            exit(0)  # On stoppe le programme ici vu que tout est bon
        elif acc in ["o", "Oui", "oui", "OUI"]:  # Si la personne veut un accessoire :
            for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:  # Boucle de la liste des accessoires
                choix = input(f"Voulez vous prendre cet accessoire : {habitsacc[i]} (o/n) ? ")
                # On demande 1 par 1 quel accessoire veut la personne
                if choix in ["o", "Oui", "oui", "OUI"]:  # Si elle veut l'accessoire en question ( par exemple le bonnet) :
                    print(f"Vous avez pris votre/vos {habitsacc[i]}.")
                    # On imprime le message suivant avec l'accessoire en question
                elif choix in ["n", "Non", "non", "NON"]:  # Si elle ne veut pas l'accessoire en question :
                    print(f"Vous n'avez pas pris votre/vos {habitsacc[i]}.")
                    # On imprime le message suivant avec l'accessoire en question
            exit(0)  # On stoppe le programme ici vu que tout est bon
    elif jour in ["Semaine", "semaine", "SEMAINE"]:  # Si c'est un jour de la semaine :
        print(f"Il fait chaud , voici ce que vous avez de disponible comme habits pour les journées chaudes dans l'armoire : ")
        # On imprime ce message
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:  # Boucle de la liste des habits chauds
            print(f"{habitschaud[i]} ")  # Imprimer les habits chauds
        acc = input("Voulez-vous prendre un accessoire ? (o/n) ")  # On demande si la personne veut des accessoires
        if acc in ["n", "Non", "non", "NON"]:  # Si la personne ne veut pas d'accessoire :
            print(f"Vous êtes prêt pour votre journée !")  # On imprime que la personne est prête pour la journée
            exit(0)  # On stoppe le programme ici vu que tout est bon
        elif acc in ["o", "Oui", "oui", "OUI"]:  # Si la personne veut un accessoire :
            for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:  # Boucle de la liste des accessoires
                choix = input(f"Voulez vous prendre cet accessoire : {habitsacc[i]} ? ")
                # On demande 1 par 1 quel accessoire veut la personne
                if choix in ["o", "Oui", "oui", "OUI"]:  # Si elle veut l'accessoire en question ( par exemple le bonnet) :
                    print(f"Vous avez pris votre/vos {habitsacc[i]}.")
                    # On imprime le message suivant avec l'accessoire en question
                elif choix in ["n", "Non", "non", "NON"]:  # Si la personne ne veut pas d'accessoire :
                    print(f"Vous n'avez pas pris votre/vos {habitsacc[i]}.")
                    # On imprime le message suivant avec l'accessoire en question
            exit(0)  # On stoppe le programme ici vu que tout est bon
elif météo in ["Froid", "froid", "FROID"]:  # Si il fait froid :
    jour = input("Sommes-nous en week-end ou en semaine ? (semaine/week-end) \n")
    # La suite est exactement pareil qu'au dessus , sauf que ce sera la liste des habits froids qui seront affichés
    if jour in ["Week-end", "week-end", "WEEK-END"]:
        print(f"Il fait froid et vous êtes en week-end , voici ce que vous avez de disponible comme habits pour les journées froides dans l'armoire : ")
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            print(f"{habitsfroid[i]} ")
        acc = input("Voulez-vous prendre un accessoire ? (o/n) ")
        if acc in ["n", "Non", "non", "NON"]:
            print(f"Vous êtes prêt pour votre journée !")
            exit(0)
        elif acc in ["o", "Oui", "oui", "OUI"]:
            for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                choix = input(f"Voulez vous prendre cet accessoire : {habitsacc[i]} (o/n) ? ")
                if choix in ["o", "Oui", "oui", "OUI"]:
                    print(f"Vous avez pris votre/vos {habitsacc[i]}.")
                elif choix in ["n", "Non", "non", "NON"]:
                    print(f"Vous n'avez pas pris votre/vos {habitsacc[i]}.")
            exit(0)
    elif jour in ["Semaine", "semaine", "SEMAINE"]:
        print(f"Il fait froid, voici ce que vous avez de disponible comme habits pour les journées froides dans l'armoire : ")
        for i in [0, 1, 2, 3, 4, 5, 6, 7]:
            print(f"{habitsfroid[i]} ")
        acc = input("Voulez-vous prendre un accessoire ? (o/n) ")
        if acc in ["n", "Non", "non", "NON"]:
            print(f"Vous êtes prêt pour votre journée !")
            exit(0)
        elif acc in ["o", "Oui", "oui", "OUI"]:
            for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                choix = input(f"Voulez vous prendre cet accessoire : {habitsacc[i]} (o/n) ? ")
                if choix in ["o", "Oui", "oui", "OUI"]:
                    print(f"Vous avez pris votre/vos {habitsacc[i]}.")
                elif choix in ["n", "Non", "non", "NON"]:
                    print(f"Vous n'avez pas pris votre/vos {habitsacc[i]}.")
            exit(0)
else:
    print(f"Veuillez indiquer la météo (chaud/froid) ")
    exit(0)
