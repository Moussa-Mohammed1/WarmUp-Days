def afficher_menu():
    print("Gestionnaire des contacts:\n")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Supprimer un contact")
    print("4. Quitter \n")


def ajouter_contact(contacts):
    nom = input("Nom: ")
    telephone = input("Telephone: ")
    email = input("Email: ")

    contact = {
        "nom": nom,
        "telephone": telephone,
        "email": email
    }
    contacts.append(contact)
    sauvegarder_contacts(contacts)
    print(f"{nom} a ete ajoute avec succes!")


def afficher_contacts(contacts):
    if len(contacts) == 0:
        print("Aucun contact enregistre.")
        return

    print("\n===== LISTE DES CONTACTS =====")

    for index, contact in enumerate(contacts, start=1):
        print(f"\n{index}. Nom : {contact['nom']}")
        print(f"   Telephone : {contact['telephone']}")
        print(f"   Email : {contact['email']}")


def sauvegarder_contacts(contacts):
    with open("contacts.txt", "w") as f:
        for contact in contacts:
            ligne = (
                contact["nom"]
                + "|"
                + contact["telephone"]
                + "|"
                + contact["email"]
                + "\n"
            )
            f.write(ligne)


def charger_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne == "":
                    continue
                informations = ligne.split("|")
                contact = {
                    "nom": informations[0],
                    "telephone": informations[1],
                    "email": informations[2]
                }
                contacts.append(contact)
    except FileNotFoundError:
        print("Aucun fichier trouve, un nouveau fichier sera cree")
    return contacts


def supprimer_contact(contacts):
    if len(contacts) == 0:
        print("Aucun contact a supprimer.")
        return
    afficher_contacts(contacts)
    try:
        numero = int(
            input("\nEntrer le numero du contact a supprimer: ")
        )
        index = numero - 1
        if index >= 0 and index < len(contacts):
            supprime = contacts.pop(index)
            sauvegarder_contacts(contacts)
            print(
                f"Contact {supprime['nom']} a ete supprime avec succes."
            )
        else:
            print("Numero invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


contacts = charger_contacts()

while True:
    afficher_menu()

    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_contact(contacts)

    elif choix == "2":
        afficher_contacts(contacts)

    elif choix == "3":
        supprimer_contact(contacts)

    elif choix == "4":
        print("Merci d'avoir utilise le gestionnaire de contacts.")
        break

    else:
        print("Choix invalide. Veuillez reessayer.")
