from random import randrange, choice

# Words for game
words = ('Arroz', 'Amarillo', 'Carros')

# Selected word for game
selected_word = choice(words)

# Word hint
print(f'INICIO DEL JUEGO \nPalabra de {len(selected_word)} letras')

#Grafic for attempts
grafic_attempts = [
        '  |--------|  ',
        '(x x)      |  ',
        ' /|\       |  '
        '  |        |  ',
        ' / \       |  ',
        '         __|__'
    ]

# Inicialized failed attempts
failed_attempts = 0

# Used words
used_words = []

# List correct words
list_word = []

# Create spaces in list
for n in range(len(selected_word)):
    list_word.append(' _ ')

# Function -> show game process
def show_result(message):
    print(message)
    print(f'Intentos restantes {5 - failed_attempts}')
    print('\n'.join(grafic_attempts[0:failed_attempts]))
    print('\n')
    print(list_word)

# Init Game
while failed_attempts < 5:
    # Word
    word_input = input('Ingresa una letra por favor \n')

    if  word_input in used_words:
        failed_attempts += 1
        show_result('Letra ya fue usada\n')
    elif not word_input in selected_word:
        failed_attempts += 1
        show_result('Letra no coincide\n')
    else:
        used_words.append(word_input)
        position = 0
        for n in selected_word:
            if n.lower() == word_input.lower() :
                list_word[position] = word_input
            position += 1

        show_result('Letra correcta\n')

        if  not ' _ ' in list_word:
            show_result('Muy bien ganaste')
            break
    if failed_attempts >= 5:
        print('Perdiste')

print('FIN DEL JUEGO')
