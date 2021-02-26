def sequence_generator(length, prefix=''):
    if prefix:
        yield prefix
    for base in 'ATGC':
        if length == 0:
            break
        yield from sequence_generator(length - 1,
                                      prefix + base)


if __name__ == '__main__':
    l = int(input('Please enter the sequence length: '))
    print(*sequence_generator(l))
