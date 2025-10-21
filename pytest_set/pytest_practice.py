#!/usr/bin/env python3


def gc_content(seq):
    seq_up = seq.upper()
    valid = {'A','G','T','C','N'}
    if not set(seq_up).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    if len(seq_up) == 0:
        return 0
    return (seq_up.count('G') + seq_up.count('C')) / len(seq_up)

def test_gc_content_GCGC():
    expected = 1.0
    observed = gc_content('GCGC')
    assert observed == expected, f'expected {expected} but got {observed}'

def test_AT_content_ATAT():
    expected = 0
    observed = gc_content('ATAT')
    assert observed == expected, f'expected {expected} but got {observed}'

def test_gc_content_ATGC():
    expected = 0.5
    observed = gc_content('ATGC')
    assert observed == expected, f'expected {expected} but got {observed}'

def test_gc_content_empty():
    expected = 0
    observed = gc_content('')
    assert observed == expected, f'expected {expected} but got {observed}'

def test_gc_content_ATGXB():
    try:
        observed = gc_content('ATGXB')
    except ValueError:
        return
    assert False, 'expected ValueError, but got {observed}'

def test_gc_content_ATGNNNTAGC():
    expected = 0.3
    observed = gc_content('ATGNNNTAGC')
    assert observed == expected, f'expected {expected} but got {observed}'

def test_gc_content_gattacaa():
    expected = 0.25
    observed = gc_content('gattacaa')
    assert observed == expected, f'expected {expected} but got {observed}'