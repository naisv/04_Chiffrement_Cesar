"""
Groupe 10 - MGA802-01 ETE26
Projet A - Chiffrement de César
"""

#Fonctions de configuration -----------------------------------------------------------------------------------------
"""Cette fonction permet à l'utilisateur de dire s'il possède une clé et de l'entrer
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

