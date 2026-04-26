stgrs = []

while True:
    print("\n--- MENU ---")
    print("1. Ajouter")
    print("2. Afficher")
    print("3. Rechercher")
    print("4. Modifier")
    print("5. Supprimer")
    print("6. Quitter")

    choix = input("Choisissez une option: ").strip()

    #Ajouter
    if choix == "1":
        stgr = input("Enter stagiaire: ").strip().lower()

        if stgr == "":
            print("Invalid input")
        elif stgr in stgrs:
            print("Stagiaire already exists")
        else:
            stgrs.append(stgr)
            print("Stagiaire added")

    #Afficher
    elif choix == "2":
        if len(stgrs) == 0:
            print("No stagiaires available")
        else:
            print("List of stagiaires:")
            for i in range(len(stgrs)):
                print(i, "-", stgrs[i])

    #Rechercher
    elif choix == "3":
        stgr = input("Enter stagiaire to search: ").strip().lower()

        if len(stgrs) == 0:
            print("No stagiaires available")
        elif stgr in stgrs:
            print("Stagiaire found")
        else:
            print("Stagiaire not found")

    #  Modifier
    elif choix == "4":
        old = input("Enter old stagiaire: ").strip().lower()
        new = input("Enter new stagiaire: ").strip().lower()

        found = False

        for i in range(len(stgrs)):
            if stgrs[i] == old:
                stgrs[i] = new
                found = True
                break

        if found:
            print("Stagiaire modified")
        else:
            print("Stagiaire not found")

    #Supprimer
    elif choix == "5":
        stgr = input("Enter stagiaire to delete: ").strip().lower()

        i = 0
        found = False

        while i < len(stgrs):
            if stgrs[i] == stgr:
                del stgrs[i]
                found = True
                break
            else:
                i += 1

        if found:
            print("Stagiaire deleted")
        else:
            print("Stagiaire not found")

    #Quitter
    elif choix == "6":
        print("Goodbye....")
        break

    else:
        print("Invalid choice")