# Functional programming homework

These tasks are is aimed on making and using simple generators.

## Description

#### DNA sequence generator (sequence_generator.py)

*sequence_generator(n)* is a generator that yields all possible DNA sequences of length *n*.

**Example:**

```python
>>> list(generate_dna(2))
['A', 'AA', 'AT', 'AG', 'AC', 'T', 'TA', 'TT', 'TG', 'TC', 'G', 'GA', 'GT', 'GG', 'GC', 'C', 'CA', 'CT', 'CG', 'CC']
```

#### Fasta file translater  (fa_translater.py)

*fasta_translator(path, codon_table="Standard")* is a generator that reads fasta record from nucleotide fasta file and yields corresponding amino-acid **Seq object**.

**Example:**

```python
>>> print(*list(translated_fasta_reader("example.fna")))
MPTASLHRSIESTIFL HISLLLHTGLSIYHPN RPHSLIAIYLCTCQYV
```

## Usage

### Download source code and install dependencies

```bash
git clone https://github.com/danon6868/BI_2020-2021_Python.git
cd BI_2020-2021_Python/functional_hw
pip install -r requirements.txt
```

### Launch scripts

```bash
python sequence_generator.py
```

```bash
python fa_translater.py
```
