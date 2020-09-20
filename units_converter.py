#eqweqweqwewqe

def j_to_ev(x):
    return x * 6.24151 * 10 ** 18


def ev_to_j(x):
    return x / 6.24151 / 10 ** 18


def j_to_erg(x):
    return x * 10 ** 7


def erg_to_j(x):
    return x / 10 ** 7


def ev_to_erg(x):
    return x * 1.602 * 10 ** (-12)


def erg_to_ev(x):
    return x / 1.602 / 10 ** (-12)



convet_dict = {'1': j_to_ev, '2': ev_to_j, '3': j_to_erg,
               '4': erg_to_j, '5': ev_to_erg, '6': erg_to_ev}

value_dict = {'1': ('Дж', 'эВ'), '2': ('эВ', 'Дж'), '3': ('Дж', 'эрг'),
              '4': ('эрг', 'Дж'), '5': ('эВ', 'эрг'), '6': ('эрг', 'эВ')}

print('Здравствуйте, Вас приветствует конвертер величин энергии')
while True:
    button = input('Для выбора введите соответствующую цифру:')
    value = int(input('Введите количество:'))
    answer = convet_dict[button](value)
    print(f'\n{value} {value_dict[button][0]} =' +
          f'{answer} {value_dict[button][1]}')
    print('\nХотите повторить? [Y/n]')
    if input().lower() in ['yes', 'y']:
        continue
    else:
        print('Пока')
        break
