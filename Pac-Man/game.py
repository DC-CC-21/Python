import constants as const
from player import Player
from block import Block

class Game:
    def __init__(self) -> None:
        pass

    def createLevel(self):
        for i in range(len(const.BOARDS[const.LEVEL])):
            for j in range(len(const.BOARDS[const.LEVEL][i])):
                id = const.BOARDS[const.LEVEL][i][j]
                if(id == 'p'):
                    const.player = (Player({
                        'x': j*const.BLOCKSIZE,
                        'y': i*const.BLOCKSIZE,
                        'w': const.PLAYERSIZE,
                        'h': const.PLAYERSIZE,
                    }))
                elif(id == 'b'):
                    const.blocks.append(Block({
                        'x': j*const.BLOCKSIZE,
                        'y': i*const.BLOCKSIZE,
                        'w': const.BLOCKSIZE,
                        'h': const.BLOCKSIZE,
                    }))
    def display(self):
        for i in range(len(const.blocks)):
            const.blocks[i].display()
        const.player.display()