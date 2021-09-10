countries = {
    'mexico': 122,
    'argentina': 50,
    'colombia': 55,
    'chile': 20,
    'peru': 33
}

def main():
    while True:
        country = str(input('Nombre del país: ')).lower()
        try:
            print('La poblacion de {} es: {} millones.'.format(country, countries[country]))
        except KeyError:
            print('[Hey, no tenemos el dato de la poblacion de {}]'.format(country))
            print('Deseas agregar {} a la lista?'.format(country))
            choice = str(input('Yes [y] or No [n]: '))
            if choice == 'y':
                poblation = int(input('Digite el numero de habitantes de dicho país: '))
                add_country(country, poblation)
            elif choice == 'n':
                break


def add_country(country, poblation):
    countries[country] = poblation


if __name__ == '__main__':
    main()

