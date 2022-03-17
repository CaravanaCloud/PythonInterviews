from pynterviews.mutants import mutants


def test_positive():
    dna = ["CTGAGA",
           "CTGAGC",
           "TATTGT",
           "AGAGAG",
           "CCCCTA",
           "TCACTG"]
    result = mutants(dna)
    assert result

def test_negative():
    dna = ["CTGAGA",
           "CTGAGC",
           "TATTGT",
           "AGAGAG",
           "CCCATA",
           "TCACTG"]
    result = mutants(dna)
    assert not result

def test_empty():
    dna = []
    result = mutants(dna)
    assert not result

def test_none():
    dna = None
    result = mutants(dna)
    assert not result

def test_large():
    dna = ["CTGAGADSFFGAGACTGAGACTGAGACTGAGACTGAGAGAGAC",
           "CTGAGCTGAGACTGAGACTGAGACTGAGACTGAGACTGAGACT",
           "CTGAGACTGAGACTGAGCTGAGACTGAGACTGAGCTGAGACTG",
           "AGACTGAGACTGAGACTGCTGAGACTGAGACTCTGAGACTGAG",
           "CTGAGACTGAGCCCCTGAGACTGAGACTGCTGAGACTGAGACD",
           "TCACTGCTGAGACTGAGACTGAGCTGAGACTGAGACTGACTGA",
           "CTGAGACTGAGACTGAGACTGAGACTGAGACTGAGACTGAGAC",
           "ETGAGCTGAGACTGAGACTGAGACTGAGACTGAGACTGAGACT",
           "CTGAGACTGAGACTGAGCTGAGACTGAGACTGAGCTGAGACTG",
           "AGACTGAGACTGAGACTGCTGAGACTGAGACTCTGAGACTGAG",
           "CTGAGACTGAGACTGCTGAGACTGAGACTGCTGAGACTGAGAC",
           "TCACTGCTGAGACTGAGACTGAGCTGAGACTGAGACTGACTGA"]
    result = mutants(dna)
    #TODO: assert not result
