#!/usr/bin/env python3
import sys
import argparse
from collections import Counter
import math

def parse_args():
    parser = argparse.ArgumentParser(
        description="Count kmers from reads in a FASTQ file and compute Shannon entropy."
    )
    parser.add_argument("fastq_file", help="Input FASTQ file (.fastq or .fq)")
    parser.add_argument("k", type=int, help="K-mer size")
    parser.add_argument(
        "-n", "--top", type=int, default=None,
        help="Limit output to top N most abundant kmers"
    )
    return parser.parse_args()


def read_fastq_sequences(fastq_file):
    """Generator that yields sequence lines from a FASTQ file."""
    with open(fastq_file, "r") as fh:
        line_number = 0
        for line in fh:
            line_number += 1
            if line_number % 4 == 2:  # Sequence line
                yield line.strip()


def count_kmers(fastq_file, k):
    """Count kmers of size k from FASTQ sequences."""
    kmer_counts = Counter()
    for seq in read_fastq_sequences(fastq_file):
        if len(seq) < k:
            continue
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i + k]
            kmer_counts[kmer] += 1
    return kmer_counts


def shannon_entropy(seq):
    """Compute Shannon entropy (base 2) for a kmer sequence."""
    length = len(seq)
    if length == 0:
        return 0.0
    freqs = Counter(seq)
    entropy = 0.0
    for base, count in freqs.items():
        p = count / length
        entropy -= p * math.log2(p)
    return entropy


def main():
    args = parse_args()

    kmer_counts = count_kmers(args.fastq_file, args.k)

    # Sort by count (descending), then alphabetically
    sorted_kmers = sorted(kmer_counts.items(), key=lambda x: (-x[1], x[0]))

    # Apply top N limit if specified
    if args.top:
        sorted_kmers = sorted_kmers[:args.top]

    # Print header
    print("kmer\tcount\tshannon_entropy")

    # Output results
    for kmer, count in sorted_kmers:
        entropy = shannon_entropy(kmer)
        print(f"{kmer}\t{count}\t{entropy:.4f}")


if __name__ == "__main__":
    main()
