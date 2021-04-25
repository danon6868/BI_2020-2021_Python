class Sequence:
    # Here it means biological sequence
    # e. g. DNA, RNA, protein
    def __init__(self, seq):
        if isinstance(seq, str):
            self.seq = seq.upper()
        else:
            raise TypeError('Sequence must be made from $str$ object')

    def __iter__(self):
        for elem in self.seq:
            yield elem

    def __hash__(self):
        return hash(self.seq)

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, slic_e):
        return self.seq[slic_e]

    def __str__(self):
        return self.seq

    def __add__(self, other):
        return Sequence(self.seq + other.seq)

    def __repr__(self):
        return f'{type(self).__name__}({self.seq})'

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if type(other) == type(self) and other.seq == self.seq:
            return True
            
    def gc_content(self):
        n_g = self.seq.count('G')
        n_c = self.seq.count('C')
        return (n_g + n_c) / len(self.seq)

    def complement(self):
        if type(self) == Sequence:
            raise NotImplementedError('Sequence object cannot be complemented')
        return type(self)(self.seq.translate(str.maketrans(self.comp_table)))

    def reverse_complement(self):
        if type(self) == Sequence:
            raise NotImplementedError('Sequence object cannot be complemented')
        return type(self)(self.complement()[::-1])


class DNA(Sequence):
    comp_table = {'A': 'T',
                  'T': 'A',
                  'G': 'C',
                  'C': 'G'}

    alph = {'A', 'T', 'G', 'C'}

    def __init__(self, seq):
        if set(seq.upper()) <= self.alph:
            super().__init__(seq)
        else:
            raise TypeError("Invalid alphabet for DNA")

    def transcribe(self):
        return RNA(self.seq.replace("T", "U")).reverse_complement()


class RNA(Sequence):
    comp_table = {'A': 'U',
                  'U': 'A',
                  'G': 'C',
                  'C': 'G'}

    alph = {'A', 'U', 'G', 'C'}

    def __init__(self, seq):
        if set(seq.upper()) <= self.alph:
            super().__init__(seq)
        else:
            raise TypeError('Invalid alphabet for RNA')


if __name__ == '__main__':
    seq_1 = DNA('ATGGC')
    seq_2 = RNA('GCCAU')
    seq_1.transcribe() == seq_2
