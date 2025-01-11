import argparse
import re

def read_file(file_path):
    """ content of the DNA sequence file"""
    with open(file_path, 'r') as file:
        return file.read().strip()

def find_longest_sequence(dna_sequence):
    valid_bases = re.findall(r'[ATCG]+', dna_sequence)  # continuous valid subsequences of A, T, C, G
    if valid_bases:
        longest = max(valid_bases, key=len)  
        return longest
    return ""

def calculate_gc_content(dna_sequence):
    """GC content of the DNA sequence."""
    valid_sequence = dna_sequence.upper()  
    g_count = valid_sequence.count('G')
    c_count = valid_sequence.count('C')
    total_bases = len(valid_sequence)
    return ((g_count + c_count) / total_bases) * 100 if total_bases > 0 else 0

def run_analysis(file_path, find_longest, calculate_gc):
    dna_sequence = read_file(file_path)
    
    if find_longest:
        longest_seq = find_longest_sequence(dna_sequence)
        if longest_seq:
            print(f"The longest continuous valid sequence is: {longest_seq}")
        else:
            print("No valid sequence found.")
    
    if calculate_gc:
        gc_content = calculate_gc_content(dna_sequence)
        print(f"GC content: {gc_content:.2f}%")

def main():
    parser = argparse.ArgumentParser(description="DNA sequence analysis tool")
    parser.add_argument('file_path', type=str, help='Path to the file with DNA sequence')
    parser.add_argument('--longest', action='store_true', help='Find the longest continuous valid sequence')
    parser.add_argument('--gc', action='store_true', help='Calculate the GC content')
    
    args = parser.parse_args()
    
    if not args.longest and not args.gc:
        print("You must select at least one analysis: --longest or --gc.")
        return
    
    run_analysis(args.file_path, args.longest, args.gc)

if __name__ == '__main__':
    main()