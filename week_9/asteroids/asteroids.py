"""
Author: Lewis Lockhart
Assignment: Asteroids
"""

import arcade
import math
import random
import os.path
from abc import abstractmethod

# if os.path.isfile("images/bg.jpg"):
#     print("File exists")
# else:
#     print("File not found")

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 15
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.05
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

ALPHA = 255


class Point:
    """ Point class for moving objects. """
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


class Velocity:
    """ Holds velocity variables. """
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0


class FlyingObj:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.radius = SHIP_RADIUS
        self.angle = 0
        self.speed = 0
        self.direction = 1
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed

    def advance(self):
        """ Moves the objects forward. """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def is_alive(self):
        return self.alive

    @abstractmethod
    def draw(self):
        pass

    def wrap(self, screen_width, screen_height):
        if self.center.x > screen_width:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = screen_width
        elif self.center.y > screen_height:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = screen_height


class Ship(FlyingObj):
    # set the ship attributes and methods based off the flying object
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.turn = SHIP_TURN_AMOUNT
        self.img = "images/ship.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, ALPHA)

    def speed_control(self, thrust):
        if thrust == "pos":
            self.velocity.dx += math.cos(math.radians(self.angle + 90)) * SHIP_THRUST_AMOUNT
            self.velocity.dy += math.sin(math.radians(self.angle + 90)) * SHIP_THRUST_AMOUNT
        elif thrust == "neg":
            self.velocity.dx -= math.cos(math.radians(self.angle + 90)) * SHIP_THRUST_AMOUNT
            self.velocity.dy -= math.sin(math.radians(self.angle + 90)) * SHIP_THRUST_AMOUNT

        # Speed limit for x
        vx = self.velocity.dx
        if vx > 5:
            self.velocity.dx = 5
        elif vx < -5:
            self.velocity.dx = -5
        # Speed limit for x
        vy = self.velocity.dy
        if vy > 5:
            self.velocity.dy = 5
        elif vy < -5:
            self.velocity.dy = -5


class Bullet(FlyingObj):
    def __init__(self):
        super().__init__()
        self.velocity.dx = BULLET_SPEED
        self.velocity.dy = BULLET_SPEED
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.angle = 90
        self.img = "images/laserBlue01.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, ALPHA)

    def fire(self, angle, ship):
        self.velocity.dx = (math.cos(math.radians(angle - 270)) * BULLET_SPEED) + (ship.velocity.dx / 2)
        self.velocity.dy = (math.sin(math.radians(angle - 270)) * BULLET_SPEED) + (ship.velocity.dy / 2)
        return self.velocity.dx, self.velocity.dy

    def align_with_ship(self, ship):
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.angle += ship.angle
        self.velocity.dx = (ship.velocity.dx + self.fire(ship.angle, ship)[0])
        self.velocity.dy = (ship.velocity.dy + self.fire(ship.angle, ship)[1])


class Asteroid(FlyingObj):
    def __init__(self):
        super().__init__()
        self.spin_speed = 0
        self.img = "images/meteorGreyBig4.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, ALPHA)

    def advance(self):
        self.angle += self.spin_speed
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy


class LargeRock(Asteroid):
    def __init__(self):
        super().__init__()
        self.center.x = random.randint(1, 100)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 150)
        self.speed = BIG_ROCK_SPEED
        self.radius = BIG_ROCK_RADIUS
        self.spin_speed = BIG_ROCK_SPIN
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed


class MediumRock(Asteroid):
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(-(BIG_ROCK_SPEED + 2), (BIG_ROCK_SPEED + 2))
        self.velocity.dy = random.uniform(-(BIG_ROCK_SPEED + 2), (BIG_ROCK_SPEED + 2))
        self.radius = MEDIUM_ROCK_RADIUS
        self.spin_speed = MEDIUM_ROCK_SPIN
        self.img = "images/meteorGrey_med2.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height


class SmallRock(Asteroid):
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(-(BIG_ROCK_SPEED + 5), (BIG_ROCK_SPEED + 5))
        self.velocity.dy = random.uniform(-(BIG_ROCK_SPEED + 5), (BIG_ROCK_SPEED + 5))
        self.radius = SMALL_ROCK_RADIUS
        self.spin_speed = SMALL_ROCK_SPIN
        self.img = "images/meteorGrey_small1.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        # if no background image is set
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.ship = Ship()
        self.held_keys = set()
        self.bullets = list()
        self.asteroids = list()
        for i in range(5):
            asteroid = LargeRock()
            self.asteroids.append(asteroid)

        self.background_image = "images/bg.jpg"
        self.bg_texture = arcade.load_texture(self.background_image)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # background image
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.bg_texture, 0, 255)

        for b in self.bullets:
            if b.alive:
                b.draw()

        for asteroid in self.asteroids:
            asteroid.draw()

        if self.ship.alive:
            self.ship.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        if self.ship.alive:
            self.ship.advance()
            self.ship.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

        for b in self.bullets:
            if b.alive:
                b.advance()
                b.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
                b.life -= 1
                if b.life <= 0:
                    b.alive = False

        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """

        if arcade.key.LEFT in self.held_keys:
            self.ship.angle += self.ship.turn

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle -= self.ship.turn

        if arcade.key.UP in self.held_keys:
            self.ship.speed_control("pos")

        if arcade.key.DOWN in self.held_keys:
            self.ship.speed_control("neg")

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet = Bullet()
                bullet.align_with_ship(self.ship)
                self.bullets.append(bullet)

            if key == arcade.key.LEFT:
                self.held_keys.add(arcade.key.LEFT)

            if key == arcade.key.RIGHT:
                self.held_keys.add(arcade.key.RIGHT)

            if key == arcade.key.UP:
                self.held_keys.add(arcade.key.UP)

            if key == arcade.key.DOWN:
                self.held_keys.add(arcade.key.DOWN)

        # If ship died, pressing ENTER makes ship regenerate.
        if key == arcade.key.ENTER:
            self.held_keys.add(arcade.key.ENTER)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
