#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run pawn-brotherhood

# 
# END_DESC

def safe_pawns(pawns: set) -> int:
    safe = {}

    for pawn in pawns:
        safe[pawn] = 0
        for safe_pawn in pawns:
            pos_1 = f'{chr(ord(pawn[0])+1)}{int(pawn[1])-1}'
            pos_2 = f'{chr(ord(pawn[0])-1)}{int(pawn[1])-1}'
            if safe_pawn == pos_1 or safe_pawn == pos_2:
                safe[pawn] += 1

    return sum([1 for v in safe.values() if v > 0])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
