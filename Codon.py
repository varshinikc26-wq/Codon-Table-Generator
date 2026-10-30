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
    "TGA": "Stop",
}


def create_rna_codon_table():
    rna_table = {}
    for codon, amino_acid in codon_table.items():
        rna_codon = codon.replace("T", "U")
        rna_table[rna_codon] = amino_acid
    return rna_table


rna_codon_table = create_rna_codon_table()


def display_codon_table(table, sequence_type):
    print("\n" + "=" * 70)
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
    valid_bases = "ATGC" if sequence_type == "DNA" else "AUGC"
    return all(base in valid_bases for base in sequence)


def divide_into_codons(sequence):
    codons = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i : i + 3]
        if len(codon) == 3:
            codons.append(codon)
        else:
            return codons, codon
    return codons, ""


def translate_codons(codons, table):
    return [table[codon] for codon in codons]


def identify_start_stop_codons(codons, sequence_type):
    if sequence_type == "DNA":
        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]
    else:
        start_codon = "AUG"
        stop_codons = ["UAA", "UAG", "UGA"]

    start_codons_found = [c for c in codons if c == start_codon]
    stop_codons_found = [c for c in codons if c in stop_codons]
    return start_codons_found, stop_codons_found


def display_translation_result(
    sequence, codons, amino_acids, incomplete, start_codons, stop_codons, sequence_type
):
    print("\n" + "=" * 70)
    print(f"{'TRANSLATION RESULT':^70}")
    print("=" * 70)
    print(f"{'Field':<20} | {'Value'}")
    print("-" * 70)
    print(f"{'Sequence type':<20} | {sequence_type}")
    print(f"{'Input sequence':<20} | {sequence}")
    print(f"{'Codons':<20} | {'-'.join(codons)}")
    print(f"{'Amino acids':<20} | {' - '.join(amino_acids)}")
    print(f"{'Start codon':<20} | {', '.join(start_codons) if start_codons else 'None'}")
    print(f"{'Stop codon':<20} | {', '.join(stop_codons) if stop_codons else 'None'}")

    if incomplete:
        print(f"{'Incomplete codon':<20} | {incomplete} (omitted from translation)")

    print("=" * 70)


def main():
    print("\n" + "=" * 70)
    print(f"{'CODON TABLE GENERATOR':^70}")
    print("=" * 70)
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
        print("\nERROR: Invalid choice. Please enter 1 for DNA or 2 for RNA.")
        return

    sequence = input(f"\nEnter your {sequence_type} sequence: ").strip().upper()

    if not sequence:
        print("\nERROR: Sequence cannot be empty.")
        return

    if not validate_sequence(sequence, sequence_type):
        allowed = "A, T, G and C" if sequence_type == "DNA" else "A, U, G and C"
        print(f"\nERROR: Invalid sequence. {sequence_type} can contain only {allowed}.")
        return

    display_codon_table(table, sequence_type)
    codons, incomplete = divide_into_codons(sequence)
    amino_acids = translate_codons(codons, table)
    start_codons, stop_codons = identify_start_stop_codons(codons, sequence_type)
    display_translation_result(
        sequence, codons, amino_acids, incomplete, start_codons, stop_codons, sequence_type
    )


if __name__ == "__main__":
    main()
