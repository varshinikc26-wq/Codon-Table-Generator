# Codon Table Generator
## Author: Varshini K C
### Check my repository:
https://github.com/varshinikc26-wq/Codon-Table-Generator

# Introduction:

The Codon Table Generator is a Python-based bioinformatics program that translates DNA and RNA sequences into their corresponding amino acids using the standard genetic code.
It identifies start and stop codons, checks sequence validity, and handles incomplete codons.

# How It Works
1. The program displays a menu to select DNA or RNA.
2. The user enters a nucleotide sequence.
3. The program checks whether the sequence contains valid nucleotides.
4. It displays the standard codon table containing all 64 codons and their corresponding amino acids.
5. The sequence is divided into groups of three nucleotides called codons.
6. Each complete codon is translated into its corresponding amino acid.
7. The program identifies start and stop codons.
8. If one or two nucleotides remain at the end, they are displayed as an incomplete codon and are not translated.
9. Finally, the program displays the codons, amino acids, start codons, stop codons, and any incomplete codon.

# How to Run
1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the command:
   `python Codon.py`
4. Select DNA or RNA and enter the sequence when prompted.

Example
Input DNA sequence: `ATGGCTTTTTAA`

Output:
- Codons: ATG - GCT - TTT - TAA
- Amino acids: Methionine - Alanine - Phenylalanine - Stop
- Start codon: ATG
- Stop codon: TAA
- Incomplete codon: None


# Requirement 1:
Create a dictionary containing all 64 codons and their corresponding amino acids
## How It Is Fulfilled:
  Created codon_table containing all 64 triplets. Every triplet maps directly to the standard amino acid full name (e.g., "TTT": "Phenylalanine", "ATG": "Methionine") or "Stop" for termination codons ("TAA", "TAG", "TGA").

# Requirement 2:
Accept a DNA sequence from the user
## How It Is Fulfilled:
  Implemented using Python's input() function within the main() execution routine. Inputs are automatically cleaned and normalized using .strip().upper() to avoid formatting or case-sensitivity errors.

# Requirement 3:
Validate the input to ensure that it contains only valid DNA nucleotides (A, T, G, and C)
## How It Is Fulfilled:
  The validate_sequence(sequence, sequence_type) function sets the allowed alphabet ("ATGC" for DNA or "AUGC" for RNA) and uses all(base in valid_bases for base in sequence) to iterate across the sequence. If an invalid base or empty input is detected, the program prints an error message and stops execution gracefully.

# Requirement 4:
Divide the sequence into codons in groups of three nucleotides
## How It Is Fulfilled:
  The divide_into_codons(sequence) function loops using a step of 3 (range(0, len(sequence), 3)), slices the string into triplets (sequence[i:i + 3]), and gathers complete 3-nucleotide sequences into a list named codons.

# Requirement 5:
Translate each codon into its corresponding amino acid using the codon table
## How It Is Fulfilled:
  The translate_codons(codons, table) function takes each grouped codon, performs an O(1) dictionary lookup (table[codon]), and returns a list of matching amino acid strings.

# Requirement 6:
Identify start codons and stop codons
## How It Is Fulfilled:
  The identify_start_stop_codons(codons, sequence_type) function scans for ATG (DNA) or AUG (RNA) for start codons, and TAA, TAG, TGA (DNA) or UAA, UAG, UGA (RNA) for stop codons.

# Requirement 7:
Handle incomplete codons at the end of the sequence
## How It Is Fulfilled:
  divide_into_codons() checks len(codon) == 3. If a slice has a length of 1 or 2, it is assigned to incomplete, returned separately, omitted from translation, and flagged in the final report.

# Requirement 8:
Display the codon table and the translated amino acid sequence in table format
## How It Is Fulfilled:
  display_codon_table() renders all 64 codons, their amino acid targets, and their functional types (Start, Stop, or Normal). display_translation_result() presents the output in an aligned tabular structure matching the expected format (e.g., "ATG-GCT-TTT-TAA").

# Requirement 9: Comparison
### 1. Data Structure
Online GitHub Repositories (Biopython(https://biopython.org/docs/latest/)): They use complex object classes that split data into separate dictionaries for regular amino acids, start codons, and stop codons.
#### My Project:
use one simple flat dictionary (codon_table) that stores all 64 codons in a single place.
#### Why:
Our design requires no external libraries and makes the code clean and direct.
### 2. Stop Codons
Online GitHub Repositories: They leave stop codons out of the main translation dictionary, so searching for a stop codon throws a KeyError unless handled separately.
#### My Project:
includes stop codons directly in the dictionary with the value "Stop" (e.g., "TAA": "Stop").
#### Why:
This lets the program translate the whole sequence in one smooth pass without needing error-handling code.
### 3. Lookup Speed
Online GitHub Repositories: They run at \mathcal{O}(1) lookup speed using Python hash tables.
#### My Project:
also run at \mathcal{O}(1) lookup speed using standard dictionary hashing.
#### Why:
Both implementations achieve the fastest possible lookup performance.
### 4. RNA Translation
Online GitHub Repositories: They use separate static files or special transcription modules to convert DNA to RNA.
#### My Project:
automatically build the RNA table by swapping "T" with "U" from our DNA dictionary using create_rna_codon_table().
#### Why:
It eliminates code duplication and prevents human typing mistakes across 64 extra entries.
### 5. Input Validation
Online GitHub Repositories: They accept messy sequencing reads with ambiguous letters like N, R, or Y.
#### My Project:
strictly accept only standard bases (A, T, G, C for DNA; A, U, G, C for RNA).
#### Why:
It prevents ambiguity and immediately catches typos entered by the user.
### 6. Output Format
Online GitHub Repositories: They usually output short single-letter codes like M - A - F - *.
#### My Project:
We output full amino acid names like Methionine - Alanine - Phenylalanine - Stop.
#### Why:
It directly fulfills the exact table and formatting requirements of the assignment.

## Comparison with Other GitHub Codon Table Projects

To check my codon table, I compared it with codon table implementations
available online:

1. **DNASequenceTranslator** (github.com/mansikath/DNASequenceTranslator)
2. **Biopython standard genetic code** (Bio.Data.CodonTable, "Standard" table)

**Result of comparison:** My codon table contains all 64 codons and follows the
standard genetic code. The amino acid assigned to each codon matches the standard
The main difference is that my program is built for learning: it displays the
full codon table, marks start and stop codons, and reports incomplete codons
clearly. Biopython is a library meant for large-scale work, while my project
is a standalone program for step-by-step translation.
​
# Requirement 10:
Pull / push this given project on your GitHub
## How It Is Fulfilled:
  Hosted in a public GitHub repository at: https://github.com/varshinikc26-wq/Codon-Table-Generator

# Additional Challenge: RNA Sequence Translation
- Mandate: Extend program functionality to support direct RNA inputs by replacing Thymine (T) with Uracil (U).
## How It Is Fulfilled:
  create_rna_codon_table() programmatically derives an RNA dictionary from the base DNA table using .replace("T", "U"). An interactive prompt in main() allows the user to choose between DNA and RNA modes.


# Commits Explaination

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
