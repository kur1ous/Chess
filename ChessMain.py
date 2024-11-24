import pygame as p
import ChessEngine


width = height = 512 
dimension = 8
square_size = width // dimension
max_fps = 15
images = {}

#initalize images
def load_images():
    pieces = ['wR', 'wQ', 'wp', 'wN', 'wK', 'wB', 'wR', 'wR', 'wQ', 'bp', 'bN', 'bK', 'bB', 'bR', 'bQ']
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (square_size, square_size))
        
#input/output handler
def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False    
        draw_game_state(screen, gs)
        clock.tick(max_fps)
        p.display.flip()
        
#Graphics handler
def draw_game_state(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)
        

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("light green")]
    for row in range(dimension):
        for column in range(dimension):
            color = colors[((row+column) % 2)]
            p.draw.rect(screen, color, p.Rect(row*square_size, column*square_size, square_size, square_size))
    
def drawPieces(screen, board):
    for row in range(dimension):
        for collumn in range(dimension):
            piece = board[row][collumn]
            if piece != "--":
                screen.blit(images[piece], p.Rect(collumn*square_size, row*square_size, square_size, square_size))

if __name__ == "__main__":
    main()
    
        