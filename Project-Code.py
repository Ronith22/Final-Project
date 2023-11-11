from designer import *
from dataclasses import dataclass
KNIGHT_SPEED = 5
@dataclass
class Game_World:
    knight: image
    knight_speed: int
    score: int


#Knight Object, supposed to be the playable character
Knight = image("https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/840386/knight-clipart-md.png")
grow(Knight, .1)
draw(Knight)

def create_game_world()-> Game_World:
    """ Create the world """
    return Game_World(Knight, 0, 0)

def move_knight(game_world: Game_World):
    pass
def create_knight():
    knight = Knight
    return knight

def head_left(game_world: Game_World):
    """ Make the knight start moving left """
    game_world.knight_speed = -(KNIGHT_SPEED)

def head_right(game_world: Game_World):
    """ Make the knight start moving left """
    game_world.knight_speed = KNIGHT_SPEED
def flip_knight(game_world: Game_World, key: str):
    """ Change the direction that the knight is moving """
    if key == "left":
        head_left(world)
    elif key == "right":
        head_right(world)

when("updating", create_knight)
when('starting', create_game_world)

start()