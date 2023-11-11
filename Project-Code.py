from designer import *
from dataclasses import dataclass
@dataclass
class Game_World:
    knight: image
    knight_speed: int
    score: int



knight = image("https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/840386/knight-clipart-md.png")
grow(knight, .1)
draw(knight)

def create_game_world()-> Game_World:
    """ Create the world """
    return Game_World(knight, 0, 0)

def move_knight()

#when("updating", create_knight)
