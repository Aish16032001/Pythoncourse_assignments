import pytest
import os
from unittest.mock import patch
from assign5_seq import seq_file,main


def test_aseq():
    
    file_name = 'a_seq.txt'
    result = seq_file(file_name)
    counts = {key: value[0] if isinstance(value, tuple) else value for key, value     in result.items()}
    expected = {'A': 2, 'C': 5, 'G': 6, 'T': 7, 'Unknown': 7, 'Total' : 27}
    assert counts == expected

def test_bseq():
    
    file_name = 'b_seq.txt'
    result = seq_file(file_name)
    counts = {key: value[0] if isinstance(value, tuple) else value for key, value     in result.items()}
    expected = {'A': 1, 'C': 2, 'G': 3, 'T': 4, 'Unknown': 0, 'Total' : 10}
    assert counts == expected





