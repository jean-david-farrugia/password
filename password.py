"""Il doit contenir au moins huit caractères.
➔ Il doit contenir au moins une lettre majuscule.
➔ Il doit contenir au moins une lettre minuscule.
➔ Il doit contenir au moins un chiffre.
➔ Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *). """

#Demande d'un mot de passe à l'utilisateur
mot_de_passe = input("Entrer votre mot de passe :\n")


#Fonction qui vérifie le mot de passe selon les caractères 
def verif_mdp(password):     

    if len(password)<8 or len(password)>40:
        print("Le mot de passe doit faire entre 8 et 40 caractères !")
            
    minuscule = False
    majuscule = False    
    chiffre = False
    special = False           

    for i in range(len(password)):

        if password[i]>="a" and password[i]<="z":
            minuscule=True

        if password[i]>="A" and password[i]<="Z":
            majuscule=True

        if password[i]>="0" and password[i]<="9":
            chiffre=True

        if password[i]=="!" or password[i]=="@" or password[i]=="#" or \
        password[i]=="$" or password[i]=="%" or password[i]=="^" or \
        password[i]=="&" or password[i]=="*":
            special=True

    if minuscule == False:
        print("Le mot de passe doit comporter au moins une lettre minuscule !")        

    if majuscule == False:
        print("Le mot de passe doit comporter au moins une lettre majuscule !")     

    if chiffre == False:
        print("Le mot de passe doit comporter au moins un chiffre !") 

    if special == False:
        print("Le mot de passe doit comporter au moins un caractère spécial !")                  

    if (minuscule,majuscule,chiffre,special):
        print("Mot de passe enregistré")


verif_mdp(mot_de_passe)

