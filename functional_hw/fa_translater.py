from Bio import SeqIO


def fasta_translator(path, codon_table='Standard'):
    fasta = SeqIO.parse(path, 'fasta')
    yield from map(lambda x: x.seq.translate(codon_table), fasta)


if __name__ == '__main__':
    print(*list(fasta_translator('example.fa')))
