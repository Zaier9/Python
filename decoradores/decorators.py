import time
import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'coronavirus',
    'argentina',
    'alcohol',
    'cuarentena',
    'aburrido',
    'computadora',
    'barbijo',
    'delivery',
    'instagram',
    'facebook',
    'hamburguesa',
    'escueladenada'
]

def timer(run):
    def wrapper():
        t1 = time.time()
        run()
        t2 = time.time()

        tt = t2 - t1
        print('El juego duró {} segundos'.format(tt))
    return wrapper


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('__*__*__*__*__*__')


@timer
def run():
    command = str(input('''
    Cómo quieres jugar?
    [s]olo
    [m]ultiplayer
    '''))

    if command == 's':
        word = random_word()
    elif command == 'm':
        word = str(input('Escoge una palabra: '))
    else:
        print('No reconozco el comando')
    hidden_word = ['__'] * len(word)
    tries = 0


    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('PERDISTE! La palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes == []
        try:
            hidden_word.index('__')
        except ValueError:
            print('')
            print('FELICIDADES! Has ganado el juego')
            break


if __name__ == '__main__':
    print('B I E N V E N I D O S  A L  A H O R C A D O')

    run()
