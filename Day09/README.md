This program processes DNA sequences in FASTA or GenBank format. It provides two types of analysis options described below :

Identifying the longest sub-sequence that occurs at least twice within the sequence. Additionally, it calculates the GC content, which is the percentage of guanine (G) and cytosine (C) nucleotides.

Requirement :

python analyze.py FILE --duplicate --gc_content

*  FILE represents Path to the sequence file
*  " --duplicate " finds the longest repeat sequence (optional for the user)
*  " --gc_content " calculates the GC content (optional for the user)

Note - User can run one or both analyzis at the same time by using the flags described above.


Syntax to run the code -

python analyze.py sequence.fasta --duplicate  ( This will print the longest repeating sequence and its length size in sequence.fasta )

python analyze.py gc_content.fasta --gc_content ( This will caclulated the GC content and print the value in gc_content.fasta )

Requirements:

This program requires the Biopython library. You can install it using pip:

pip install biopython
