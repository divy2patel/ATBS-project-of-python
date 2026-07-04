def isValidChessBoard(board):
    """
    Validates a chess board represented as a dict of {coordinate: piece}.
    e.g. {"e1": "wK", "e8": "bK", "a2": "wP", ...}
    """
    valid_files = set("abcdefgh")
    valid_ranks = set("12345678")
    valid_piece_types = {"K", "Q", "R", "B", "N", "P"}

    white_count = 0
    black_count = 0
    white_kings = 0
    black_kings = 0

    for square, piece in board.items():
        # --- Validate coordinate ---
        if not isinstance(square, str) or len(square) != 2:
            return False
        file, rank = square[0], square[1]
        if file not in valid_files or rank not in valid_ranks:
            return False

        # --- Validate piece format ---
        if not isinstance(piece, str) or len(piece) != 2:
            return False
        color, ptype = piece[0], piece[1]
        if color not in ("w", "b") or ptype not in valid_piece_types:
            return False

        # --- Count pieces ---
        if color == "w":
            white_count += 1
            if ptype == "K":
                white_kings += 1
        else:
            black_count += 1
            if ptype == "K":
                black_kings += 1

    if white_kings != 1 or black_kings != 1:
        return False
    if white_count > 16 or black_count > 16:
        return False

    return True