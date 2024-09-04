import random

carNumber = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
majAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''

carNumber = input('Combien de caractères souhaitez vous dans votre mot de passe ?')
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
    if


''' random.randint(a, b) : entier aléatoire entre a et b (inclus).
random.uniform(a, b) : flottant aléatoire entre a et b.
random.random() : flottant entre 0.0 et 1.0.
random.choice(seq) : élément aléatoire d'une séquence.
random.shuffle(seq) : mélange une séquence.
random.sample(seq, k) : tire un échantillon aléatoire de k éléments.
random.seed(x) : fixe la graine pour contrôler la reproductibilité.'''