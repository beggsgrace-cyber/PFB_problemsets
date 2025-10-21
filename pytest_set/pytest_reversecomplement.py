#!/usr/bin/env python3


def rev_comp(seq):
    seq_up = seq.upper()
    makecomplement = seq_up.maketrans({'A':'T', 'T':'A', 'G':'C','C':'G'})
    complement = seq_up.translate(makecomplement)
    reverse_complement = complement[::-1]
    valid = {'A','G','T','C'}
    if not set(seq_up).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    return reverse_complement

def test_rev_comp_tgggccc():
    expected = 'GGGCCCA'
    observed = rev_comp('tgggccc')
    assert observed == expected, f'expected {expected} but got {observed}'

def test_rev_comp_TGGGCCC():
    expected = 'GGGCCCA'
    observed = rev_comp('TGGGCCC')
    assert observed == expected, f'expected {expected} but got {observed}'

def test_rev_comp_Tgggccc():
    expected = 'GGGCCCA'
    observed = rev_comp('Tgggccc')
    assert observed == expected, f'expected {expected} but got {observed}' 

def test_rev_comp_ATCGN():
    try:
        observed = rev_comp('ATCGN')
    except ValueError:
        return
    assert False, 'expected ValueError, but got {observed}'