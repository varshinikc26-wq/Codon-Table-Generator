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

Commits Explaination
Step 1: Create the Codon Table
A Python dictionary called `codon_table` is created to store all 64 DNA codons and their corresponding amino acids. It follows the standard genetic code.

Step 2: Create the RNA Codon Table
The function `create_rna_codon_table()` creates an RNA codon table from the DNA codon table. It replaces the nucleotide T with U in each codon.

Step 3: Display the Codon Table
The function `display_codon_table()` displays all codons, their corresponding amino acids, and their types. It marks the start codon, stop codons, and other codons.

Step 4: Validate the Sequence
The function `validate_sequence()` checks whether the entered sequence contains only valid nucleotides. DNA accepts A, T, G, and C, while RNA accepts A, U, G, and C.

Step 5: Divide the Sequence into Codons
The function `divide_into_codons()` divides the sequence into groups of three nucleotides. If one or two nucleotides remain at the end, they are identified as an incomplete codon.

Step 6: Translate the Codons
The function `translate_codons()` uses the codon table to convert each complete codon into its corresponding amino acid.

Step 7: Identify Start and Stop Codons
The function `identify_start_stop_codons()` identifies start codons and stop codons in the sequence. The standard start codon is ATG in DNA and AUG in RNA. The stop codons are TAA, TAG, and TGA in DNA, and UAA, UAG, and UGA in RNA.

Step 8: Display the Translation Results
The function `display_translation_result()` displays the input sequence, codons, amino acids, start codons, stop codons, and any incomplete codon.

Step 9: Run the Main Program
The `main()` function controls the program. It asks the user to select DNA or RNA, accepts the sequence, checks the input, displays the codon table, and calls the other functions to process the sequence.

Step 10: Start Program Execution
The statement `if __name__ == "__main__":` checks whether the Python file is being run directly. If it is, the `main()` function is called to start the program.
