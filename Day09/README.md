This program processes DNA sequences in FASTA or GenBank format. It provides two types of analysis options described below :

Identifying the longest sub-sequence that occurs at least twice within the sequence. Additionally, it calculates the GC content, which is the percentage of guanine (G) and cytosine (C) nucleotides.

Requirement :

python analyze.py FILE --duplicate --blabla

*  FILE represents Path to the sequence file
*  " --duplicate " finds the longest repeat sequence (optional for the user)
*  " --gc_content " calculates the GC content (optional for the user)

Note - User can run one or both analyzis at the same time by using the flags described above.
Example:

python analyze.py my_sequence.fasta --duplicate This will print the longest repeat sequence and its length for the sequence in my_sequence.fasta.

Requirements:

This program requires the Biopython library. You can install it using pip:

pip install biopython
