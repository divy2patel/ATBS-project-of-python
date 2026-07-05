def isValidChessBoard(borad):
    whiteking=0
    blackking=0
    blackpiece=0
    whitepiece=0

    for place,piece in borad.items():
        if piece[0]=='w':
            whitepiece+=1
        elif piece[0]=='b':
            blackpiece+=1
        
        if piece =='wK':
            whiteking+=1
        elif piece =='bK':
            blackking+=1

        if piece[1] not in ('K','B','Q','N','P','R'):
            return False
        
        if place[0] not in 'abcdefgh' or place[1] not in '12345678':
            return False
        
    if whiteking!=1 or blackking!=1:
        return False
    
    if whitepiece > 16 or blackpiece > 16:
        return False
    
    return True
