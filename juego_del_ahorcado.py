import random
import os

LABEL_HEAD = """ 
   ============================================  
   ||          EL JUEGO DEL AHORCADO         ||
   ============================================ 
   """ 

HANGMAN_IMAGES = ['''

\t   +-----+
\t   |     |
\t         |
\t         | 
\t         |
\t         |
\t ===========''', '''

\t   +-----+
\t   |     |
\t   O     |
\t         |
\t         |
\t         |
\t ===========''', '''

\t   +-----+
\t   |     |
\t   O     |
\t   |     |
\t         |
\t         |
\t ===========''', '''

\t   +-----+
\t   |     |
\t   O     |
\t  /|     |
\t         |
\t         |
\t ===========''', '''

\t   +-----+
\t   |     |
\t   O     |
\t  /|\    |
\t         |
\t         |
\t ===========''', '''

\t   +-----+
\t   |     |
\t   O     |
\t  /|\    |
\t  /      |
\t         |
\t ===========''', '''

\t   +-----+
\t   |     |
\t   O     |
\t  /|\    |
\t  / \    |
\t         |
\t ===========''']

def cleanScreen(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def getSecretWord():
    words = []
    with open('./archivos/data.txt','r',encoding='utf8') as f:
        for line in f:
            line = line.upper()
            line = line.rstrip()
            line = normalize(line)
            words.append(line)

    posicion = random.randint(0, len(words) - 1)
    secret_word = words[posicion]
    return secret_word


def normalize(s): # It removes the accents of a string
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s    

def printHeader(word_game, count_wrong):       
    print(LABEL_HEAD)
    print(HANGMAN_IMAGES[count_wrong]) 
    print('\nAdivina la palabra oculta\n')
    word = ''
    for letter in word_game:
        word += letter + ' ' 

    print(word)


 
def run():
    loser = False
    winner = False
    secret_word = getSecretWord()    
    word_game = ['_' for i in range(0, len(secret_word))]
    count_wrong = 0
    max_wrong = len(HANGMAN_IMAGES) - 1

    while loser == False and winner == False:        
        printHeader(word_game, count_wrong)
        letter = input('\nIngresa una letra y presiona enter: ')
        letter = letter.upper()

        if letter in secret_word:
            pos = 0
            ini = 0
            fin = len(secret_word)
            while pos >= 0:                
                pos = secret_word.find(letter, ini, fin)
                if pos >= 0:
                    word_game[pos] = letter

                ini = pos + 1

        else:
            count_wrong += 1

        if count_wrong >= max_wrong:
            loser = True
            
        if secret_word == str("").join(word_game):
            winner = True 
        
        cleanScreen()


    printHeader(word_game, count_wrong)

    if winner:
        print('\nGANASTE!!!')
    else:
        print('\nPERDISTE!!!')        
        print(f'\nLa palabra oculta era {secret_word}')

    input('\nPresione tecla enter para salir: ')    


if __name__ == '__main__':
    run()