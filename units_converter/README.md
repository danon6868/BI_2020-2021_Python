# Units converter

Here it is a program which was made to perform energy units conversion.

## Description

Converter supports ***energy*** units, for example J, eV and erg. You can interact with script via CLI with simple syntax.

### Interaction with program

The first you need to choose one of the following option:

```bash
Hello, I am energy units converter :)
You can choose something from following list:
1: J -> eV
2: eV -> J
3: J -> erg
4: erg -> J
5: eV -> erg
6: erg -> eV
```

You just need to type number in your CL. Then you need to enter a quantity of corresponding unit. Also convater will ask you if you want to repeat after convartion.

### Examples

```bash
1: J -> eV
2: eV -> J
3: J -> erg
4: erg -> J
5: eV -> erg
6: erg -> eV
>>> Press number to choose units you want: 4
>>> Enter a quantity: 20

20 erg = 2e-06 J
```

```bash
1: J -> eV
2: eV -> J
3: J -> erg
4: erg -> J
5: eV -> erg
6: erg -> eV
>>> Press number to choose units you want: 3
>>> Enter a quantity: 2

2 J = 20000000 erg
```

## Usage

### Download source code

```bash
git clone https://github.com/danon6868/BI_2020-2021_Python.git
cd BI_2020-2021_Python/units_converter
```

### Launch script

```
python units_converter.py
```

