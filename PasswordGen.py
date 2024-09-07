import random

carNumber = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
majAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''
listeCharSpeciaux = '!@#$%^&*()-_=+[]|;:,.<>?/~`'

while True:
    try:
        carNumber = int(input('Combien de caractères souhaitez vous dans votre mot de passe ?'))
        break #Sortie de la boucle si l'entrée est valide
    except ValueError:
        print('Erreur : Veuillez entrer un nombre entier') #entrée non valide

for i in range (carNumber):
    newChar = ''
    carType = random.randint(1,3) #Choix du type de char, 1=lettre, 2=chiffre, 3=characteres speciaux
    
    #lettres
    if carType == 1 :
        minOrMaj = random.randint(1,2) #Lettre minuscule ou majuscule, 1=min, 2=maj
        if minOrMaj == 1 :
            password += random.choice(alphabet)
        if minOrMaj == 2 :
            password += random.choice(majAlphabet)
    
    #chiffre
    if carType == 2 :
        chiffreAlea = random.randint(1, 10)  # Génère un nombre aléatoire entre 1 et 10
        password += str(chiffreAlea)

    #characteres speciaux
    if carType == 3 :
        charSpeciaux = random.choice(listeCharSpeciaux)
        password += charSpeciaux

print(password)