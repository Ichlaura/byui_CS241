"""
Author: Lewis Lockhart
Assignment: Asteroids
"""

""" SPACE changed out for LSHIFT """

import arcade
import math
import random
import os.path
from abc import abstractmethod, ABC

# if os.path.isfile("images/bg.jpg"):
#     print("File exists")
# else:
#     print("File not found")

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 15
BULLET_LIFE = 30

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


class Score:
    def __init__(self):
        self.score = 0

    def update_score(self, value):
        self.score += value

    def display(self):
        score_text = "Score: {}".format(self.score)
        start_x = 20
        start_y = SCREEN_HEIGHT - 30
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=16, color=arcade.color.WHITE)


def game_over():
    text = "GAME OVER"
    start_x = SCREEN_HEIGHT / 2
    start_y = SCREEN_HEIGHT / 2
    arcade.draw_rectangle_outline(center_x=start_x + 100, center_y=start_y, width=120, height=40, color=arcade.color.WHITE, border_width=2)
    arcade.draw_text(text, start_x=start_x + 50, start_y=start_y - 10, font_size=16, color=arcade.color.WHITE)


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
    """ Base class for any flying object. """
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

    @abstractmethod
    def draw(self):
        """ To be implemented by child classes. """
        pass

    def wrap(self, screen_width, screen_height):
        """ Allows any flying object to wrap from one side of the screen to the other. """
        if self.center.x > screen_width:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = screen_width
        elif self.center.y > screen_height:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = screen_height


class Alien(FlyingObj):
    def __init__(self):
        super().__init__()
        self.center.x = random.randint(1, 100)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 150)
        self.speed = 2
        self.radius = 20
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        self.img = "images/alien.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width / 8
        self.height = self.texture.height / 8
        self.change_direction = 0
        self.point_value = 10

    def advance(self):
        self.change_direction += 1
        if self.change_direction >= 40:
            self.direction = random.randint(1, 200)
            self.speed = random.randint(0, 5)
            self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
            self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy
            self.change_direction = 0
        else:
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy

    def draw(self):
        """ Draw alien. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, ALPHA)


class Ship(FlyingObj):
    # set the ship attributes and methods based off the flying object
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.turn = SHIP_TURN_AMOUNT
        self.img = "images/ship.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width / 2
        self.height = self.texture.height / 2

    def draw(self):
        """ Draw ship. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, ALPHA)

    def speed_control(self, thrust):
        """ Adjusts velocity dx/dy used for thrust. """
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
    """ Bullet class - fired in the direction the ship is pointing. """
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
        """ Draws bullet. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, ALPHA)

    def fire(self, angle, ship):
        """ Controls the speed of the bullet. """
        self.velocity.dx = (math.cos(math.radians(angle - 270)) * BULLET_SPEED) + (ship.velocity.dx / 2)
        self.velocity.dy = (math.sin(math.radians(angle - 270)) * BULLET_SPEED) + (ship.velocity.dy / 2)
        return self.velocity.dx, self.velocity.dy

    def align_with_ship(self, ship):
        """ Orients he bullet in the direction the ship is facing. """
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.angle += ship.angle
        self.velocity.dx = (ship.velocity.dx + self.fire(ship.angle, ship)[0])
        self.velocity.dy = (ship.velocity.dy + self.fire(ship.angle, ship)[1])


class Asteroid(FlyingObj):
    """ Base class for asteroids. """
    def __init__(self):
        super().__init__()
        self.spin_speed = 0
        self.img = "images/meteorGreyBig4.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height

    def draw(self):
        """ Draws asteroids. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, ALPHA)

    def advance(self):
        """ Advances and spins asteroids. """
        self.angle += self.spin_speed
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    @abstractmethod
    def split(self, asteroid_list):
        pass

    def hit(self, asteroid_list):
        self.split(asteroid_list)


class LargeRock(Asteroid):
    """ Sets variables for large asteroids. """
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
        self.point_value = 1

    def split(self, asteroid_list):
        chunks = [MediumRock(), MediumRock(), SmallRock()]
        for c in chunks:
            c.center.x = self.center.x
            c.center.y = self.center.y
            asteroid_list.append(c)
        self.alive = False


class MediumRock(Asteroid):
    """ Sets variables for medium asteroids. """
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(-(BIG_ROCK_SPEED + 0.5), (BIG_ROCK_SPEED + 0.5))
        self.velocity.dy = random.uniform(-(BIG_ROCK_SPEED + 0.5), (BIG_ROCK_SPEED + 0.5))
        self.radius = MEDIUM_ROCK_RADIUS
        self.spin_speed = MEDIUM_ROCK_SPIN
        self.img = "images/meteorGrey_med2.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width * 1.5
        self.height = self.texture.height * 1.5
        self.point_value = 2

    def split(self, asteroid_list):
        chunks = [SmallRock(), SmallRock()]
        for c in chunks:
            c.center.x = self.center.x
            c.center.y = self.center.y
            asteroid_list.append(c)
        self.alive = False


class SmallRock(Asteroid):
    """ Sets variables for small asteroids. """
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(-(BIG_ROCK_SPEED + 1), (BIG_ROCK_SPEED + 1))
        self.velocity.dy = random.uniform(-(BIG_ROCK_SPEED + 1), (BIG_ROCK_SPEED + 1))
        self.radius = SMALL_ROCK_RADIUS
        self.spin_speed = SMALL_ROCK_SPIN
        self.img = "images/meteorGrey_small1.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.point_value = 3

    def split(self, asteroid_list):
        self.alive = False


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

        # creates ship
        self.ship = Ship()

        # holds keyboard keys
        self.held_keys = set()

        # holds fired bullets until they die
        self.bullets = list()

        # holds asteroids until destroyed
        self.asteroids = list()

        # holds aliens
        self.alien = list()
        self.increment = 800
        self.alien_spawn_increment = self.increment

        for i in range(3):
            asteroid = LargeRock()
            self.asteroids.append(asteroid)

        # sets background image as background texture
        self.background_image = "images/bg.jpg"
        self.bg_texture = arcade.load_texture(self.background_image)

        self.score = Score()

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

        # draws bullets if they are alive
        for b in self.bullets:
            if b.alive:
                b.draw()

        # draws asteroids if they are alive
        for a in self.asteroids:
            if a.alive:
                a.draw()

        # draws the alien if alive
        for al in self.alien:
            if al.alive:
                al.draw()

        # draws ship if it is alive
        if self.ship.alive:
            self.ship.draw()
        else:
            game_over()

        # draw score
        self.score.display()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collisions()

        # countdown / alien generation
        self.alien_spawn_increment -= 1
        # if the count is too low - reset it
        if self.alien_spawn_increment < -180:
            self.alien_spawn_increment = self.increment
        # if there is no alien, and the count is below 0, make a new alien
        if self.alien_spawn_increment <= 0 and len(self.alien) == 0:
            spawn = Alien()
            self.alien.append(spawn)
            self.alien_spawn_increment = self.increment

        # update alien if there is one
        for al in self.alien:
            if al.alive:
                al.advance()
                al.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

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

        for a in self.asteroids:
            if a.alive:
                a.advance()
                a.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

        # generates more asteroids if total number is less than 5
        if len(self.asteroids) < 3:
            add_asteroid = LargeRock()
            self.asteroids.append(add_asteroid)

    def check_collisions(self):

        # ship collision
        for a in self.asteroids:
            if self.ship.alive and a.alive:
                if abs(self.ship.center.x - a.center.x) < (a.radius + 20) and \
                        abs(self.ship.center.y - a.center.y) < (a.radius + 20):
                    self.ship.alive = False

        # asteroid / bullet collision
        for b in self.bullets:
            for a in self.asteroids:
                if b.alive and a.alive:
                    if abs(b.center.x - a.center.x) < (a.radius * 3.5) and \
                            abs(b.center.y - a.center.y) < (a.radius * 3.5):
                        b.alive = False
                        a.hit(self.asteroids)
                        self.score.update_score(a.point_value)

        # alien / bullet collision
        for b in self.bullets:
            for al in self.alien:
                if b.alive and al.alive:
                    if abs(b.center.x - al.center.x) < al.radius and \
                            abs(b.center.y - al.center.y) < al.radius:
                        b.alive = False
                        al.alive = False
                        self.score.update_score(al.point_value)

        self.bring_out_your_dead()

    def bring_out_your_dead(self):
        # comments made by the bullets and asteroids in honor if Monty Python
        comments = ["I'm not dead.", "I'm not dead.", "I'm not dead.", "I'm getting better.", "I don't want to go on the cart."]

        # clean up dead asteroids
        for a in self.asteroids:
            if not a.alive:
                self.asteroids.remove(a)
                print(f"Removed Asteroid: {random.choice(comments)}")

        # clean up dead bullets
        for b in self.bullets:
            if not b.alive:
                self.bullets.remove(b)
                print(f"Removed Bullet: {random.choice(comments)}")

        # clean up dead alien
        for al in self.alien:
            if not al.alive:
                self.alien.remove(al)
                print(f"Removed Alien: {random.choice(comments)}")

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

            if key == arcade.key.LEFT:
                self.held_keys.add(arcade.key.LEFT)

            if key == arcade.key.RIGHT:
                self.held_keys.add(arcade.key.RIGHT)

            if key == arcade.key.UP:
                self.held_keys.add(arcade.key.UP)

            if key == arcade.key.DOWN:
                self.held_keys.add(arcade.key.DOWN)

            if key == arcade.key.LSHIFT:
                bullet = Bullet()
                print("bullet created")
                bullet.align_with_ship(self.ship)
                self.bullets.append(bullet)

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
