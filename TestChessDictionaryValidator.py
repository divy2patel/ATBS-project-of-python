from ChessDictionaryValidator import isValidChessBoard

# --- Test 1: Valid starting position (partial) ---
board1 = {
    "e1": "wK", "e8": "bK",
    "a1": "wR", "h1": "wR",
    "a8": "bR", "h8": "bR",
    "d1": "wQ", "d8": "bQ",
}
print(isValidChessBoard(board1))  # Expect: True

# --- Test 2: Missing a king ---
board2 = {"e1": "wK", "a1": "wR"}
print(isValidChessBoard(board2))  # Expect: False (no black king)

# --- Test 3: Two kings same color ---
board3 = {"e1": "wK", "e2": "wK", "e8": "bK"}
print(isValidChessBoard(board3))  # Expect: False

# --- Test 4: Invalid coordinate ---
board4 = {"e1": "wK", "e8": "bK", "i9": "wQ"}
print(isValidChessBoard(board4))  # Expect: False (i9 isn't on the board)

# --- Test 5: Invalid piece code ---
board5 = {"e1": "wK", "e8": "bK", "e2": "wX"}
print(isValidChessBoard(board5))  # Expect: False ("X" isn't a real piece)

# --- Test 6: Too many pieces for one side ---
board6 = {"e1": "wK", "e8": "bK"}
# add 16 extra white pawns to push white over the 16-piece limit
for i, file in enumerate("abcdefgh"):
    board6[f"{file}2"] = "wP"
    board6[f"{file}3"] = "wP"  # this makes 16 pawns + king = 17 white pieces
print(isValidChessBoard(board6))  # Expect: False

# --- Test 7: Empty board ---
print(isValidChessBoard({}))  # Expect: False (no kings at all)

assert isValidChessBoard(board1) == True
assert isValidChessBoard(board2) == False
assert isValidChessBoard(board3) == False
assert isValidChessBoard(board4) == False
assert isValidChessBoard(board5) == False
assert isValidChessBoard(board6) == False
assert isValidChessBoard({}) == False
print("All tests passed.")