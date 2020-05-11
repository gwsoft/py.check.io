"""
Task URL: https://py.checkio.org/en/mission/pawn-brotherhood/

Almost everyone in the world knows about the ancient game Chess
and has at least a basic understanding of its rules. It has various
units with a wide range of movement patterns allowing for a huge number
of possible different game positions (for example Number of possible
chess games at the end of the n-th plies.) For this mission, we will
examine the movements and behavior of chess pawns.

Chess is a two-player strategy game played on a checkered game board
laid out in eight rows (called ranks and denoted with numbers 1 to 8)
and eight columns (called files and denoted with letters a to h)
of squares. Each square of the chessboard is identified by a unique
coordinate pair — a letter and a number (ex, "a1", "h8", "d6").
For this mission we only need to concern ourselves with pawns.
A pawn may capture an opponent's piece on a square diagonally
in front of it on an adjacent file, by moving to that square.
For white pawns the front squares are squares with greater row
number than the square they currently occupy.

A pawn is generally a weak unit, but we have 8 of them which
we can use to build a pawn defense wall. With this strategy,
one pawn defends the others. A pawn is safe if another pawn can
capture a unit on that square. We have several white pawns on the
chess board and only white pawns. You should design your code to
find how many pawns are safe.
"""

files = 'abcdefgh'
ranks = '12345678'

def safe_pawns(pawns: set) -> int:
    defenders = {}      # The dictionary consisting of all possible
                        # squares for every pawn, where a defending pawn can
                        # be placed.
    safe_pawns = set()  # The output set consisting of pawns having at least
                        # one defending pawn.

    for p in pawns:
        idx_file = files.index(p[0])
        idx_rank = ranks.index(p[1])
        # Each pawn can have two possible defenders
        # on its left-bottom diagonal and/or its right-bottom diagonal
        p_defenders = set()
        # The row (rank) == 0 is not protected, a pawn has not got defenders there (if it
        # only could be placed on this row).
        if idx_rank > 0 and idx_rank < 8:
            if idx_file > 0 and idx_file < 7:
                p_defenders.add(files[idx_file+1] + ranks[idx_rank-1])
                p_defenders.add(files[idx_file-1] + ranks[idx_rank-1])
            # pawn on the leftmost column
            elif idx_file == 0:
                p_defenders.add(files[idx_file+1] + ranks[idx_rank-1])
            # pawn on the rightmost column
            elif idx_file == 7:
                p_defenders.add(files[idx_file-1] + ranks[idx_rank-1])
            defenders[p] = p_defenders

    # For every pawn check if its defenders' squares are physically filled with another pawn.
    # If so, add the pawn to the output set.
    for k,v in defenders.items():
        for i in range(len(v)):
            if list(v)[i] in pawns:
                safe_pawns.add(k)

    return len(safe_pawns)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a1", "a8", "h1", "h8"}) == 0
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
