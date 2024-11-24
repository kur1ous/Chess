class GameState():
    def __init__(self):
        #8x8 2d list
        #first char represents colour, 2nd represents piece
        # "--" empty space
        self.board = [
            ["bR", "bN", "bB", "bK", "bQ", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]
        ]
        
        self.whiteToMove = True
        self.moveLog = []