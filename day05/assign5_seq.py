import sys
from collections import Counter


def seq_file(file_path):
    
    counts = Counter()
    total = 0
    
    # Read and count nucleotides
    with open(file_path, 'r') as f:
        for line in f:
            sequence = line.strip().upper()
            counts.update(sequence)
            total += len(sequence)

    # percentages
    results = {}
    for base in "ACGT":
        count = counts[base]
        percent = (count / total * 100) if total > 0 else 0
        results[base] = (count, percent)

    unknown_count = total - sum(counts[base] for base in "ACGT")
    unknown_percent = (unknown_count / total * 100) if total > 0 else 0
    results["Unknown"] = (unknown_count, unknown_percent)

    results["Total"] = total
    return results


def display_results(title, statistic):
    

    print(f"\n{title}")
    for base in "ACGT":
        count, percent = statistic[base]
        print(f"{base}: {count:8} {percent:6.1f}%")
    unknown_count, unknown_percent = statistic["Unknown"]
    print(f"Unknown: {unknown_count:8} {unknown_percent:6.1f}%")
    print(f"Total: {statistic['Total']:8}")


def combine_stats(all_stats):
    
    combined = Counter()
    total = 0

    for statistic in all_stats:
        for base in "ACGT":
            combined[base] += statistic[base][0]
        combined["Unknown"] += statistic["Unknown"][0]
        total += statistic["Total"]

    # Calculate percentages
    results = {}
    for base in "ACGT":
        count = combined[base]
        percent = (count / total * 100) if total > 0 else 0
        results[base] = (count, percent)

    unknown_count = combined["Unknown"]
    unknown_percent = (unknown_count / total * 100) if total > 0 else 0
    results["Unknown"] = (unknown_count, unknown_percent)
    results["Total"] = total
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python seq.py <file1> <file2> ...")
        sys.exit(1)

    file_paths = sys.argv[1:]
    all_stats = []

    for file_path in file_paths:
        statistic = seq_file(file_path)
        display_results(file_path, statistic)
        all_stats.append(statistic)

    # Display combined statistics
    combined_stats = combine_stats(all_stats)
    display_results("All", combined_stats)


if __name__ == "__main__":
    main()
