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

value_dict = {'1': ('J', 'eV'), '2': ('eV', 'J'), '3': ('J', 'erg'),
              '4': ('erg', 'J'), '5': ('eV', 'erg'), '6': ('erg', 'eV')}

print('Hello, I am energy units converter :)')

while True:
    print('You can choose something from following list: ')
    for n, val in value_dict.items():
        print(f'{n}: {val[0]} -> {val[1]}')
    button = input('Press number to choose units you want: ')
    value = int(input('Enter a quantity: '))
    answer = convet_dict[button](value)
    print(f'\n{value} {value_dict[button][0]} = ' +
          f'{answer} {value_dict[button][1]}')
    print('\nDo you want to repeat? [Y/n]')
    if input().lower() in ['yes', 'y']:
        continue
    else:
        print('Bye :)')
        break
