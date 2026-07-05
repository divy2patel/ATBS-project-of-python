def isValidChessBoard(board):
    numBlackKings = 0
    numWhiteKings = 0
    numWhitePieces = 0
    numBlackPieces = 0

    for square, piece in board.items():
        # Count pieces
        if piece[0] == 'w':
            numWhitePieces += 1
        elif piece[0] == 'b':
            numBlackPieces += 1

        # Count kings
        if piece == 'wK':
            numWhiteKings += 1
        elif piece == 'bK':
            numBlackKings += 1

        # Check piece type is valid
        if piece[1] not in ('K', 'Q', 'R', 'B', 'N', 'P'):
            return False

        # Check square is a valid coordinate
        if square[0] not in 'abcdefgh' or square[1] not in '12345678':
            return False

    # Each side needs exactly one king
    if numWhiteKings != 1 or numBlackKings != 1:
        return False

    # Max 16 pieces per side
    if numWhitePieces > 16 or numBlackPieces > 16:
        return False

    return True