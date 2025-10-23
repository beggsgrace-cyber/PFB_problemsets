#!/usr/bin/env python3
import argparse
import math
from collections import Counter, defaultdict

def parse_args():
    parser = argparse.ArgumentParser(
        description="Simplified Trinity-Inchworm like assembler with entropy threshold."
    )
    parser.add_argument("fastq_file", help="Input FASTQ file")
    parser.add_argument("k", type=int, help="K-mer size")
    parser.add_argument(
        "--min_entropy", type=float, default=1.5,
        help="Minimum Shannon entropy required for seed kmers (default: 1.5)"
    )
    parser.add_argument(
        "--top", type=int, default=None,
        help="Optional: limit to top N kmers for assembly (for speed)"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="assembled_contigs.fasta",
        help="Output FASTA file name (default: assembled_contigs.fasta)"
    )
    return parser.parse_args()


def read_fastq_sequences(fastq_file):
    with open(fastq_file, "r") as fh:
        for i, line in enumerate(fh):
            if i % 4 == 1:  # sequence line
                yield line.strip()


def count_kmers(fastq_file, k):
    kmer_counts = Counter()
    for seq in read_fastq_sequences(fastq_file):
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            kmer_counts[kmer] += 1
    return kmer_counts


def shannon_entropy(seq):
    freqs = Counter(seq)
    length = len(seq)
    entropy = 0.0
    for base, count in freqs.items():
        p = count / length
        entropy -= p * math.log2(p)
    return entropy


def build_index(kmer_counts, k):
    """Build prefix/suffix index for quick extension."""
    prefix_index = defaultdict(list)
    suffix_index = defaultdict(list)
    for kmer, count in kmer_counts.items():
        prefix = kmer[:-1]
        suffix = kmer[1:]
        prefix_index[prefix].append((kmer, count))
        suffix_index[suffix].append((kmer, count))
    return prefix_index, suffix_index


def greedy_extend(seed, kmer_counts, prefix_index, suffix_index, k):
    """Greedy extension left and right from the seed."""
    contig = seed
    used = set([seed])

    # Extend right
    while True:
        suffix = contig[-(k-1):]
        if suffix not in prefix_index:
            break
        candidates = [(kmer, c) for kmer, c in prefix_index[suffix] if kmer not in used]
        if not candidates:
            break
        next_kmer, count = max(candidates, key=lambda x: x[1])
        contig += next_kmer[-1]
        used.add(next_kmer)

    # Extend left
    while True:
        prefix = contig[:k-1]
        if prefix not in suffix_index:
            break
        candidates = [(kmer, c) for kmer, c in suffix_index[prefix] if kmer not in used]
        if not candidates:
            break
        next_kmer, count = max(candidates, key=lambda x: x[1])
        contig = next_kmer[0] + contig
        used.add(next_kmer)

    return contig, used


def main():
    args = parse_args()
    k = args.k

    print(f"Counting {k}-mers...")
    kmer_counts = count_kmers(args.fastq_file, k)

    # Optionally restrict to top kmers for speed
    if args.top:
        kmer_counts = Counter(dict(kmer_counts.most_common(args.top)))

    print("Building prefix/suffix indices...")
    prefix_index, suffix_index = build_index(kmer_counts, k)

    print("Computing entropy for kmers...")
    kmer_entropy = {kmer: shannon_entropy(kmer) for kmer in kmer_counts}

    assembled = []
    used_kmers = set()

    print("Starting greedy contig assembly...")
    for seed, count in sorted(kmer_counts.items(), key=lambda x: -x[1]):
        if seed in used_kmers:
            continue
        if kmer_entropy[seed] < args.min_entropy:
            continue

        contig, used = greedy_extend(seed, kmer_counts, prefix_index, suffix_index, k)
        assembled.append(contig)
        used_kmers.update(used)

    # Write assembled contigs to FASTA file
    print(f"Writing {len(assembled)} contigs to {args.output}...")
    with open(args.output, "w") as out_fh:
        for i, contig in enumerate(assembled, 1):
            out_fh.write(f">contig_{i}\n{contig}\n")

    print("Assembly complete.")


if __name__ == "__main__":
    main()
