# mini-compiler-python
Septian Handita Surya - 231011400174
## Deskripsi
Implementasi sederhana Mini Compiler dengan fitur:
- Lexical Analysis
- Parsing (EBNF)
- Abstract Syntax Tree (AST)
- Three Address Code (TAC)
- Operator Pangkat (^)

## Cara Menjalankan
```bash
python main.py


## Fitur
- Lexical Analysis
- Parser (Recursive Descent)
- Abstract Syntax Tree (AST)
- Three Address Code (TAC)
- Operator Pangkat (^) dengan precedence tertinggi

## Operator Precedence
1. ^
2. * /
3. + -

## Contoh
Input:
a ^ 2 + b * c

Output:
t1 = a ^ 2
t2 = b * c
t3 = t1 + t2

Catatan: Implementasi operator ^ pada versi ini bersifat left-associative. Dalam teori compiler, operator ini seharusnya right-associative, namun tidak mempengaruhi tujuan utama.


