import os

class Piece:
    
    def __init__(self, name, color, value, texture=None, texture_rec=None): # texture here are just images
        self.name = name
        self.color = color
        value_sign = 1 if color == "white" else -1 
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rec = texture_rec
        
    def set_texture(self, size=80):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images", f"imgs-{size}px")
        
        self.texture = os.path.join(IMAGES_DIR, f"{self.color}_{self.name}.png")
        
    def add_move(self, move): 
        self.moves.append(move)
        
    def clear_moves(self):
        self.moves = [] 

class Pawn(Piece):
    
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)
        
class Knight(Piece):
    
    def __init__(self, color):
        super().__init__('knight', color, 3.0)
        
class Bishop(Piece):
    
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)
        
class Rook(Piece):
    
    def __init__(self, color):
        super().__init__('rook', color, 5.0)
        
class Queen(Piece):
    
    def __init__(self, color):
        super().__init__('queen', color, 9.0)
        
class King(Piece):
    
    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 10000.0)
        
        
        
        