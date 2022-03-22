LEVEL = 0
BOARDS = [
    [
        'bbbb bbbb',
        'b       b',
        'b bbpbb b',
        'b b   b b',
        'b       b',
        'b b   b b',
        'b bb bb b',
        'b       b',
        'bbbbbbbbb',
    ],
]

CANVASSIZE = 450
BLOCKSIZE = int((CANVASSIZE/len(BOARDS[LEVEL]))*0.9)
PLAYERSIZE = int(BLOCKSIZE*0.8)

blocks = []
coins = []
ghosts = []
player = None