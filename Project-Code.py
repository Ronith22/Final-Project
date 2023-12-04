from designer import *
from dataclasses import dataclass
from random import randint
RUNNER_SPEED = 10



@dataclass
class World:
    runner: DesignerObject
    runner_speed: int
    obstacles: list[DesignerObject]
    score: int
    counter: DesignerObject
    collision: bool

background_image("https://images.freeimages.com/clg/istock/previews/8322/83224399-skyscraper-icon.jpg")

def create_world() -> World:
    """ Create the game world """
    return World(create_runner(), RUNNER_SPEED, [], 0, text("black", "Score:", 30, 200, 50), False)


def create_runner() -> DesignerObject:
    """ Create the runner/ Carlo the Gorilla """
    runner = emoji("Gorilla")
    runner.y = 550
    runner.flip_x = True
    return runner

def create_obstacle() -> DesignerObject:
    """ Create the Barrel"""
    obstacle = rectangle("red", 60, 20)
    obstacle.x = randint(0, get_width())
    obstacle.y = 10
    return obstacle


def head_left(world: World):
    """ Make Carlo start moving left """
    world.runner_speed = -(RUNNER_SPEED)
    world.runner.flip_x = False


def head_right(world: World):
    """ Make Carlo start moving right """
    world.runner_speed = RUNNER_SPEED
    world.runner.flip_x = True


def boundary_check_runner(world: World):
    """ Handles if the player tries to run Carlo off screen """
    if world.runner.x > get_width():
        head_left(world)
    elif world.runner.x < 0:
        head_right(world)


def flip_runner(world: World, key: str):
    """ Changes the direction Carlo is moving"""
    if key == "left":
        head_left(world)
    elif key == "right":
        head_right(world)


def move_runner(world: World):
    """ Moves Carlo horizontally"""
    world.runner.x += world.runner_speed



def make_obstacles_fall(world: World):
    """ Makes the barrels fall down at varying speeds ranging from 2-13 """
    for obstacle in world.obstacles:
        obstacle.y += randint(2, 13)


def destroy_obstacles_on_landing(world: World):
    """ Destroys any obstacles that have fallen past the screen, also updates score by +1 for
    each obstacle to do so."""
    kept = []
    new_score = 0
    for obstacle in world.obstacles:
        if obstacle.y < 570:
            kept.append(obstacle)
        else:
            destroy(obstacle)
            new_score += 1
        world.obstacles = kept
        world.score += new_score
        print("Updated Score:", world.score)



def make_obstacles(world: World):
    """ Checks to see how many obstacle objects exist on the screen and then generates more."""
    not_too_many_obstacles = len(world.obstacles) < 10
    random_chance = randint(20, 100) == 50
    if not_too_many_obstacles and random_chance:
        world.obstacles.append(create_obstacle())


def collide_runner_obstacle(world: World):
    """Checks every update to see if the runner and the obstacle have collided, returns a message in
    form of a boolean."""
    for obstacle in world.obstacles:
        if colliding(obstacle, world.runner):
            world.collision = True

def update_score(world: World):
    """Updates the score"""
    world.counter.text = "Score: " + str(world.score)


def flash_game_over(world: World):
    """Show the game over message"""
    if world.collision:
        world.counter.text = "GAME OVER!, Score: " + str(world.score)
        pause()

when('starting', create_world)
when("updating", move_runner)
when("updating", make_obstacles)
when('updating', collide_runner_obstacle)
when("updating", destroy_obstacles_on_landing)
when("updating", make_obstacles_fall)
when("updating", boundary_check_runner)
when("typing", flip_runner)
when("updating", update_score)
when("updating", flash_game_over)
start()