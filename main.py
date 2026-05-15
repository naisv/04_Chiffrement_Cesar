"""
Groupe 10 - MGA802-01 ETE26
Projet A - Chiffrement de César
"""
import unicodedata

#Fonctions de configuration -----------------------------------------------------------------------------------------
"""Cette fonction permet à l'utilisateur de dire s'il possède une clé et de la saisir
Elle accepte les majuscules et espaces lors de la réponse "oui" mais pas la ponctuation
Elle n'accepte que les entiers pour la valeur de la clé, sinon reboucle
Elle retourne la valeur de la clé modulo 26 (pour avoir des entiers entre 0 et 26) ou None si pas de clé
"""
def entrer_cle():
    possede_cle = input("Connaissez-vous la clé pour encrypter/décrypter votre texte? oui ou non").lower().strip()
    cle=None
    if possede_cle == "oui":
        cle_valide=False
        while not cle_valide:
            try:
                saisie=int(input("Veuillez entrer la clé:"))
                cle=saisie % 26
                cle_valide=True
            except ValueError:
                print("Erreur: vous devez entrer un entier valide")
    return cle

#Fonction qui retourne True si l'utilisateur souhaite encrypter son texte, False s'il souhaite le décrypter
def encrypter_ou_decrypter():
    saisie_valide=False
    while not saisie_valide:
        saisie=str(input("Souhaitez-vous encrypter ou décrypter ce texte ?")).lower().strip()
        if saisie in ["encrypter", "decrypter", "décrypter"]:
            saisie_valide=True
            cryptage=saisie.startswith('e')
        else:
            print("Erreur: Veuillez répondre 'encrypter' ou 'decrypter'")
    return cryptage

#Fonction qui supprime les accents de la chaîne de caractères fournie en paramètre et la retourne sans accent
def supprimer_accents(texte):
    forme_nfd = unicodedata.normalize('NFD', texte)
    texte_propre = "".join(c for c in forme_nfd if unicodedata.category(c) != 'Mn')
    return texte_propre

""" Cette fonction récupère le texte venant d'un fichier ou d'un texte saisi dans la console 
Il faut saisir le nom du fichier avec ".txt" à la fin et que le fichier soit dans le dossier du programme
Le programme boucle tant que le fichier est introuvable.
Sinon l'utilisateur peut taper son texte dans la console.
La fonction enregistre ce texte dans une chaîne de caractères
La fonction retourne la chaîne de caractères sans accent, avec la ponctuation et la casse initiale"""
def recuperer_texte():
    saisie_valide=False
    rep = str(input("Voulez-vous utiliser un fichier texte ? oui ou non")).lower().strip()
    while not saisie_valide:
        if rep == "oui":
            nom_fichier = input("Insérez le nom du fichier.txt :")
            try:
                with open(nom_fichier, 'r', encoding='utf-8') as f:
                    fichier = f.read()
                    saisie_valide=True
            except FileNotFoundError:
                print("Fichier introuvable. Veuillez réessayer")

        else:
            saisie_valide=True
            fichier = str(input("Saisissez votre texte:"))

    fichier_propre=supprimer_accents(fichier)

    return fichier_propre

