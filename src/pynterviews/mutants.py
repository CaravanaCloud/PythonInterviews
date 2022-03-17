def get_dna(dna, x, y):
    if x > len(dna)-1:
        return None
    line = dna[x]
    if y > len(line)-1:
        return None
    char_dna = line[y]
    return char_dna

def check(dna,
          x1, y1,
          x2, y2,
          x3, y3,
          x4, y4
          ):
    curr = get_dna(dna, x1, y1)
    print("curr: " + curr)
    result = (curr == get_dna(dna, x2, y2)) and (curr == get_dna(dna, x3, y3)) and (curr == get_dna(dna, x4, y4))
    if result:
        print("result found! "+str(x1)+" "+str(y1))
    return result

def match(dna, x, y):
    # limites do array!!
    right = check(dna,
                  x, y,
                  x, y+1,
                  x, y+2,
                  x, y+3)
    if right:
        return True
    down = check(dna,
                  x, y,
                  x+1, y,
                  x+2, y,
                  x+3, y)
    if down:
        return True
    dleft = check(dna,
                  x, y,
                  x-1, y+1,
                  x-2, y+2,
                  x-3, y+3)
    if dleft:
        return True
    dright = check(dna,
                  x, y,
                  x+1, y+1,
                  x+2, y+2,
                  x+3, y+3)
    if dright:
        return True

def mutants(dna):
    if not isinstance(dna, list):
        print("Not a list")
        return False
    # para cada linha
    for x in range(len(dna)):
        line = dna[x]
        # para letra cada linha
        for y in range(len(line)):
            # verifica se bate com o padrao
            is_match = match(dna, x, y)
            if is_match:
                return True
    return False

def cli(args=None):
    """Process command line arguments."""
    dna = ["CTGAGA",
           "CTGAGC",
           "TATTGT",
           "AGAGAG",
           "CCCCTA",
           "TCACTG"];
    print(mutants(dna));