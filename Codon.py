codon_table = {

    # Phenylalanine
    "TTT": "Phenylalanine",
    "TTC": "Phenylalanine",

    # Leucine
    "TTA": "Leucine",
    "TTG": "Leucine",
    "CTT": "Leucine",
    "CTC": "Leucine",
    "CTA": "Leucine",
    "CTG": "Leucine",

    # Isoleucine
    "ATT": "Isoleucine",
    "ATC": "Isoleucine",
    "ATA": "Isoleucine",

    # Methionine
    "ATG": "Methionine",

    # Valine
    "GTT": "Valine",
    "GTC": "Valine",
    "GTA": "Valine",
    "GTG": "Valine",

    # Serine
    "TCT": "Serine",
    "TCC": "Serine",
    "TCA": "Serine",
    "TCG": "Serine",
    "AGT": "Serine",
    "AGC": "Serine",

    # Proline
    "CCT": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",

    # Threonine
    "ACT": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",

    # Alanine
    "GCT": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",

    # Tyrosine
    "TAT": "Tyrosine",
    "TAC": "Tyrosine",

    # Histidine
    "CAT": "Histidine",
    "CAC": "Histidine",

    # Glutamine
    "CAA": "Glutamine",
    "CAG": "Glutamine",

    # Asparagine
    "AAT": "Asparagine",
    "AAC": "Asparagine",

    # Lysine
    "AAA": "Lysine",
    "AAG": "Lysine",

    # Aspartic acid
    "GAT": "Aspartic acid",
    "GAC": "Aspartic acid",

    # Glutamic acid
    "GAA": "Glutamic acid",
    "GAG": "Glutamic acid",

    # Cysteine
    "TGT": "Cysteine",
    "TGC": "Cysteine",

    # Tryptophan
    "TGG": "Tryptophan",

    # Arginine
    "CGT": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",
    "AGA": "Arginine",
    "AGG": "Arginine",

    # Glycine
    "GGT": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine",

    # Stop codons
    "TAA": "Stop",
    "TAG": "Stop",
    "TGA": "Stop"
}
def create_rna_codon_table():
    """
    Creates an RNA codon table by replacing T with U
    in the DNA codon table.
    """

    rna_table = {}

    for codon, amino_acid in codon_table.items():
        rna_codon = codon.replace("T", "U")
        rna_table[rna_codon] = amino_acid

    return rna_table


rna_codon_table = create_rna_codon_table()

def display_codon_table(table, sequence_type):
    """
    Displays the complete codon table.
    """

    print("\n")
    print("=" * 70)
    print(f"              STANDARD {sequence_type} CODON TABLE")
    print("=" * 70)

    print(f"{'Codon':<12}{'Amino Acid':<25}{'Type':<15}")
    print("-" * 70)

    for codon, amino_acid in table.items():

        if codon in ["ATG", "AUG"]:
            codon_type = "Start"

        elif amino_acid == "Stop":
            codon_type = "Stop"

        else:
            codon_type = "Normal"

        print(f"{codon:<12}{amino_acid:<25}{codon_type:<15}")

    print("=" * 70)

def validate_sequence(sequence, sequence_type):
    """
    Validates whether the sequence contains only valid
    DNA or RNA nucleotides.
    """

    if sequence_type == "DNA":
        valid_bases = "ATGC"

    else:
        valid_bases = "AUGC"

    for base in sequence:

        if base not in valid_bases:
            return False

    return True

def divide_into_codons(sequence):
    """
    Divides the sequence into groups of three nucleotides.

    Returns:
        codons      -> complete groups of three
        incomplete  -> remaining nucleotides
    """

    codons = []

    for i in range(0, len(sequence), 3):

        codon = sequence[i:i + 3]

        if len(codon) == 3:
            codons.append(codon)

        else:
            return codons, codon

    return codons, ""

def translate_codons(codons, table):
    """
    Translates each codon into its corresponding amino acid.
    """

    amino_acids = []

    for codon in codons:

        amino_acid = table[codon]

        amino_acids.append(amino_acid)

    return amino_acids

def identify_start_stop_codons(codons, sequence_type):
    """
    Identifies start and stop codons.
    """

    if sequence_type == "DNA":

        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]

    else:

        start_codon = "AUG"
        stop_codons = ["UAA", "UAG", "UGA"]

    start_codons_found = []
    stop_codons_found = []

    for codon in codons:

        if codon == start_codon:
            start_codons_found.append(codon)

        if codon in stop_codons:
            stop_codons_found.append(codon)

    return start_codons_found, stop_codons_found

def display_translation_result(
    sequence,
    codons,
    amino_acids,
    incomplete,
    start_codons,
    stop_codons,
    sequence_type
):
    """
    Displays the final translation result.
    """

    print("\n")
    print("=" * 70)
    print("                 TRANSLATION RESULT")
    print("=" * 70)

    print(f"Sequence type : {sequence_type}")
    print(f"Input sequence: {sequence}")

    print("\nCodons:")
    print(" - ".join(codons))

    print("\nAmino acids:")
    print(" - ".join(amino_acids))

    print("\nStart codon(s):")

    if start_codons:
        print(" - ".join(start_codons))
    else:
        print("None")

    print("\nStop codon(s):")

    if stop_codons:
        print(" - ".join(stop_codons))
    else:
        print("None")

    if incomplete:

        print("\nIncomplete codon:")
        print(incomplete)

        print(
            "The incomplete codon was not translated "
            "because it contains fewer than three nucleotides."
        )

    else:

        print("\nIncomplete codon:")
        print("None")

    print("=" * 70)

def main():

    print("\n")
    print("=" * 70)
    print("                 CODON TABLE GENERATOR")
    print("=" * 70)

    print(
        "\nThis program translates DNA/RNA sequences using "
        "the standard genetic code."
    )

    # Select sequence type

    print("\nSelect sequence type:")
    print("1. DNA")
    print("2. RNA")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "1":

        sequence_type = "DNA"
        table = codon_table

    elif choice == "2":

        sequence_type = "RNA"
        table = rna_codon_table

    else:

        print("\nERROR: Invalid choice.")
        print("Please enter 1 for DNA or 2 for RNA.")

        return

    # Get sequence from user

    sequence = input(
        f"\nEnter your {sequence_type} sequence: "
    ).strip().upper()


    # Check empty input

    if not sequence:

        print("\nERROR: Sequence cannot be empty.")

        return

    # Validate sequence

    if not validate_sequence(sequence, sequence_type):

        print("\nERROR: Invalid sequence.")

        if sequence_type == "DNA":

            print(
                "DNA can contain only the nucleotides "
                "A, T, G and C."
            )

        else:

            print(
                "RNA can contain only the nucleotides "
                "A, U, G and C."
            )

        return

    # Check codon table

    if sequence_type == "DNA":

        print(
            f"\nNumber of codons in the standard table: "
            f"{len(codon_table)}"
        )

    else:

        print(
            f"\nNumber of codons in the standard RNA table: "
            f"{len(rna_codon_table)}"
        )

    # Display complete codon table

    display_codon_table(table, sequence_type)

    # Divide sequence into codons

    codons, incomplete = divide_into_codons(sequence)

    # Translate codons

    amino_acids = translate_codons(codons, table)

    # Identify start and stop codons

    start_codons, stop_codons = identify_start_stop_codons(
        codons,
        sequence_type
    )

    # Display final result

    display_translation_result(
        sequence,
        codons,
        amino_acids,
        incomplete,
        start_codons,
        stop_codons,
        sequence_type
    )

if __name__ == "__main__":
    main()
