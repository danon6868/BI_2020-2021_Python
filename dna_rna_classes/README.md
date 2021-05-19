# OOP homework

Here I created classes whitch represent biological sequences: *DNA* and *RNA*.

## Description

*RNA* and *DNA* classes are inherited from the *Sequence* class which mostly satisfies *str* interface. *Sequence* class also has *complement*, *reverse_complement*, and *gc_content* methods, but only its descendants can use it. Also, *DNA* objects have *transcribe* method that returns the corresponding *RNA* object.

### Examples

```python
>>> from rna_dna_classes import DNA, RNA

>>> RNA("AAAUUUGGGCCC").reverse_complement()
RNA(GGGCCCAAAUUU)

>>> DNA("AAATTTGGGCCC").transcribe()
RNA(GGGCCCAAAUUU)

>>> DNA("GGGCCCAAATTT").gc_content()
0.5

>>> (RNA("AAAUUU") + RNA("GGGCCC"))[1:-1]
RNA(AAUUUGGGCC)
```

## Usage

### Download source code

```bash
git clone https://github.com/danon6868/BI_2020-2021_Python.git
cd BI_2020-2021_Python/dna_rna_classes
```
