def value_int():
    value = input('Introduzca un número entero: ')

    try:
        value = int(value)

    except Exception:
        print('¡Error!')

        while not isinstance(value, int):

            try:
                value = int(input('Introduzca un número entero: '))

            except Exception:
                print('Error!')

            else:
                return value

    else:
        return value


def vallue_flo():
    value = input('Introduzca un número decimal: ')

    try:
        value = float(value)

    except Exception:
        print('¡Error!')

        while not isinstance(value, float):

            try:
                value = float(input('Introduzca un número decimal: '))

            except Exception:
                print('Error!')

            else:
                return value

    else:
        return value


def value_bol():
    value_true = ['True', '1']
    value_false = ['False', '0']
    values = value_true + value_false
    value = input('Introduzca una expresión booleana (True / 1 / False / 0): ')

    while value not in values:
        print('¡Error!')
        value = input('Introduzca una expresión booleana: ')

    if value in values:

        if value in value_true:
            return True

        else:
            return False


def value_dec():
    value_yes = ['SI', 'Si', 'si', 'SÍ', 'Sí', 'sí']
    value_no = ['NO', 'No', 'no']
    values = value_yes + value_no
    value = input('Introduzca una decision (Sí / No): ')

    while value not in values:
        print('¡Error!')
        value = input('Introduzca una decision (Sí / No): ')

    if value in values:

        if value in value_yes:
            return True

        else:
            return False
