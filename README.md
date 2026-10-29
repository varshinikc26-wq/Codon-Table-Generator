Codon Table Generator
Introduction
The Codon Table Generator is a Python-based bioinformatics program that translates DNA and RNA sequences into their corresponding amino acids using the standard genetic code.
It identifies start and stop codons, checks sequence validity, and handles incomplete codons.

How It Works
1. The program displays a menu to select DNA or RNA.
2. The user enters a nucleotide sequence.
3. The program checks whether the sequence contains valid nucleotides.
4. It displays the standard codon table containing all 64 codons and their corresponding amino acids.
5. The sequence is divided into groups of three nucleotides called codons.
6. Each complete codon is translated into its corresponding amino acid.
7. The program identifies start and stop codons.
8. If one or two nucleotides remain at the end, they are displayed as an incomplete codon and are not translated.
9. Finally, the program displays the codons, amino acids, start codons, stop codons, and any incomplete codon.

How to Run
1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the command:

   `python codon.py`

4. Select DNA or RNA and enter the sequence when prompted.

Example
Input DNA sequence: `ATGGCTTTTTAA`

Output:
- Codons: ATG - GCT - TTT - TAA
- Amino acids: Methionine - Alanine - Phenylalanine - Stop
- Start codon: ATG
- Stop codon: TAA
- Incomplete codon: None
