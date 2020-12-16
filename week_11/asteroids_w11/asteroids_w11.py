"""
Author: Lewis Lockhart
Assignment: Asteroids

Extras Added:
1. Game Over Screen when ship is destroyed
2. Score Counter
3. 'Bring out your dead" Monty Python dialog in console when
    dead bullets, alien ship, or asteroids are removed
4. Player Ship speed control (limits)
5. Background image
6. Arcade bug work around: Due to a bug with arcade, holding
    UP + LEFT will prevent the SPACE from firing a bullet. Added
    another key to resolve this. LSHIFT will allow the bullets
    to fire with any arrow key combination. (Issue discovered
    by Chris Fowler - we worked together to isolate and resolve).
7. Alien Bullet class added
    1. Different image
    3. Shorter range
    4. Directs at player location
    5. Bullets have collisions with player ship and asteroids
        - no points added if alien bullet breaks asteroid
8. Added Alien ship (hostile)
    1. Random flight pattern
    2. Spawns within 980 frames
    3. Only one alien can be alive at a time
    4. Fires at player every 980 frames when count = 100
9. New Asteroids generated if total on screen is less than 4
10. Game sounds
    - asteroid break
    - bullet - player ship
    - bullet - alien
    - alien alarm
    - alien destroyed
    - player destroyed
"""

import arcade
import math
import random
import os.path
from abc import abstractmethod


# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 15
BULLET_LIFE = 30
ALIEN_BULLET_SPEED = 15
ALIEN_BULLET_LIFE = 15

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
VOLUME = 0.1


class Score:
    """ Score class tracks, updates and displays score. """
    def __init__(self):
        self.score = 0

    # add to current score
    def update_score(self, value):
        self.score += value

    def display(self):
        score_text = f"Score: {self.score}"
        start_x = 20
        start_y = SCREEN_HEIGHT - 30
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=16, color=arcade.color.WHITE)


class GameSound:
    """ Sound controls for game elements. """
    def __init__(self, sound_file, pan):
        self.sound = arcade.Sound(sound_file)
        self.pan = pan
        self.volume = VOLUME

    def play(self):
        """ Play """
        self.sound.play(pan=self.pan, volume=self.volume)


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

    @abstractmethod
    def __str__(self):
        pass

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
        self.direction = random.randint(1, 360)
        self.speed = 2
        self.radius = 20
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        self.img = "images/alien.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width / 8
        self.height = self.texture.height / 8
        self.change_direction = 0
        self.point_value = 25
        self.alarm = GameSound(":resources:sounds/jump3.wav", pan=-1.0)
        self.alarm_count = 60

    def __str__(self):
        return "Alien"

    def advance(self):
        """ Recalculates speed and direction every 40 frames. """
        self.change_direction += 1
        if self.change_direction >= 40:
            self.direction = random.randint(1, 360)
            self.speed = random.randint(0, 6)
            self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
            self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy
            self.change_direction = 0
        else:
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy

        # plays alien alarm sound at intervals
        self.alarm_count -= 1
        if self.alive and self.alarm_count <= 0:
            self.alarm.play()
            self.alarm_count = 60

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

    def __str__(self):
        return "Player Ship"

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
        self.fire_bullet = GameSound(":resources:sounds/laser1.ogg", pan=-1.0)

    def __str__(self):
        return "Player Bullet"

    def fire(self, angle, ship):
        """ Controls the speed of the bullet. """
        self.velocity.dx = (math.cos(math.radians(angle - 270)) * BULLET_SPEED) + (ship.velocity.dx / 2)
        self.velocity.dy = (math.sin(math.radians(angle - 270)) * BULLET_SPEED) + (ship.velocity.dy / 2)
        self.fire_bullet.play()
        return self.velocity.dx, self.velocity.dy

    def align_with_ship(self, ship):
        """ Orients the bullet in the direction the ship is facing. """
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.angle += ship.angle
        self.velocity.dx = (ship.velocity.dx + self.fire(ship.angle, ship)[0])
        self.velocity.dy = (ship.velocity.dy + self.fire(ship.angle, ship)[1])

    def draw(self):
        """ Draws bullet. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, ALPHA)


class AlienBullet(Bullet):
    """ Bullet class - fired in the direction the ship is pointing. """
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.velocity.dx = ALIEN_BULLET_SPEED
        self.velocity.dy = ALIEN_BULLET_SPEED
        self.life = ALIEN_BULLET_LIFE
        self.img = "images/alien_fireball.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width / 20
        self.height = self.texture.height / 20
        self.fire_alien_bullet = GameSound(":resources:sounds/laser3.wav", pan=-1.0)

    def __str__(self):
        return "Alien Bullet"

    def fire(self, angle, ship):
        """ Controls the speed of the bullet. """
        self.velocity.dx = (math.cos(angle) * BULLET_SPEED)
        self.velocity.dy = (math.sin(angle) * BULLET_SPEED)
        self.fire_alien_bullet.play()
        return self.velocity.dx, self.velocity.dy

    def fire_at_player_ship(self, ship, alien):
        """ Directs he bullet in the direction of the players ship. """
        self.center.x = alien.center.x
        self.center.y = alien.center.y
        player_x = ship.center.x
        player_y = ship.center.y
        x_diff = player_x - self.center.x
        y_diff = player_y - self.center.y

        # Calculation the angle in radians between the start points
        self.angle = math.atan2(y_diff, x_diff)

        self.velocity.dx = (ship.velocity.dx + self.fire(self.angle, ship)[0])
        self.velocity.dy = (ship.velocity.dy + self.fire(self.angle, ship)[1])


class Asteroid(FlyingObj):
    """ Base class for asteroids. """
    def __init__(self):
        super().__init__()
        self.spin_speed = 0
        self.img = "images/meteorGreyBig4.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.t_break = GameSound(":resources:sounds/explosion2.wav", pan=-1.0)

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
        """ If hit, split and play sound. """
        self.split(asteroid_list)
        self.t_break.play()


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

    def __str__(self):
        return "Large Asteroid"

    def split(self, asteroid_list):
        """ Splits when hit. """
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

    def __str__(self):
        return "Medium Asteroid"

    def split(self, asteroid_list):
        """ Splits when hit. """
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

    def __str__(self):
        return "Small Asteroid"

    def split(self, asteroid_list):
        """ No splits. """
        self.alive = False


def game_over(is_over):
    """ Displays Game Over message when player is killed. """
    if is_over:
        text = "GAME OVER"
        start_x = SCREEN_HEIGHT / 2
        start_y = SCREEN_HEIGHT / 2
        arcade.draw_rectangle_outline(center_x=start_x + 100, center_y=start_y, width=120, height=40, color=arcade.color.WHITE, border_width=2)
        arcade.draw_text(text, start_x=start_x + 50, start_y=start_y - 10, font_size=16, color=arcade.color.WHITE)


def bring_out_your_dead(passed_list):
    """ Clears the dead elements out. """

    # comments made by the bullets and asteroids in honor if Monty Python
    comments = ["I'm not dead.", "I'm not dead.", "I'm not dead.", "I'm getting better.", "I don't want to go on the cart."]

    for i in passed_list:
        """ Loops through the list and removes any alive = false items. """
        if not i.alive:
            passed_list.remove(i)
            print(f"Removed {i}: {random.choice(comments)}")


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
        # ship death sound
        self.dead_player = GameSound(":resources:sounds/gameover4.wav", pan=-1.0)

        # holds keyboard keys
        self.held_keys = set()

        # holds fired bullets until they die
        self.bullets = list()
        self.alien_bullet = list()

        # holds asteroids until destroyed
        self.asteroids = list()

        # holds aliens
        self.alien = list()
        # alien spawn reset number
        self.increment = 800
        self.alien_spawn_increment = self.increment
        # alien death sound
        self.dead_alien = GameSound(":resources:sounds/upgrade2.wav", pan=-1.0)

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
        for ab in self.alien_bullet:
            if ab.alive:
                ab.draw()

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
            # calls game_over - clears if Enter is pressed
            game_over(True)

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
            # create alien
            spawn = Alien()
            self.alien.append(spawn)
            self.alien_spawn_increment = self.increment

        # update alien if there is one
        for al in self.alien:
            if al.alive:
                al.advance()
                al.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

                # causes alien to fire at the player
                if self.alien_spawn_increment == 100 and self.ship.alive:
                    bullet = AlienBullet()
                    bullet.fire_at_player_ship(self.ship, al)
                    self.alien_bullet.append(bullet)

        if self.ship.alive:
            # ship can move if alive
            self.ship.advance()
            self.ship.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

        for b in self.bullets:
            # moves and counts down life of bullets
            if b.alive:
                b.advance()
                b.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
                b.life -= 1
                if b.life <= 0:
                    b.alive = False

        for ab in self.alien_bullet:
            # moves and counts down life of bullets
            if ab.alive:
                ab.advance()
                ab.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
                ab.life -= 1
                if ab.life <= 0:
                    ab.alive = False

        for a in self.asteroids:
            # moves asteroids if alive
            if a.alive:
                a.advance()
                a.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

        # generates more asteroids if total number is less than 4
        if len(self.asteroids) < 4:
            add_asteroid = LargeRock()
            self.asteroids.append(add_asteroid)

    def check_collisions(self):

        for a in self.asteroids:

            # asteroid / bullet collision
            for b in self.bullets:
                if b.alive and a.alive:
                    ab_contact = a.radius + b.radius
                    if abs(b.center.x - a.center.x) < ab_contact and \
                            abs(b.center.y - a.center.y) < ab_contact:
                        b.alive = False
                        a.hit(self.asteroids)
                        self.score.update_score(a.point_value)

            # asteroid / alien bullet collision
            for ab in self.alien_bullet:
                if ab.alive and a.alive:
                    aab_contact = a.radius + ab.radius
                    if abs(ab.center.x - a.center.x) < aab_contact and \
                            abs(ab.center.y - a.center.y) < aab_contact:
                        ab.alive = False
                        a.hit(self.asteroids)

            # asteroid / ship collision
            if self.ship.alive and a.alive:
                as_contact = a.radius + self.ship.radius
                if abs(self.ship.center.x - a.center.x) < as_contact and \
                      abs(self.ship.center.y - a.center.y) < as_contact:
                    self.ship.alive = False
                    # play sound when player dies
                    self.dead_player.play()

        for al in self.alien:

            # alien / bullet collision
            for b in self.bullets:
                if b.alive and al.alive:
                    alb_contact = al.radius + b.radius
                    if abs(b.center.x - al.center.x) < alb_contact and \
                            abs(b.center.y - al.center.y) < alb_contact:
                        b.alive = False
                        al.alive = False
                        self.dead_alien.play()
                        self.score.update_score(al.point_value)

            # alien / ship collision
            if self.ship.alive and al.alive:
                als_contact = al.radius + self.ship.radius
                if abs(self.ship.center.x - al.center.x) < als_contact and \
                        abs(self.ship.center.y - al.center.y) < als_contact:
                    self.ship.alive = False
                    al.alive = False
                    # play sound when player dies
                    self.dead_player.play()

        # ship / alien bullet collision
        for ab in self.alien_bullet:
            if ab.alive and self.ship.alive:
                aba_contact = ab.radius + self.ship.radius
                if abs(ab.center.x - self.ship.center.x) < aba_contact and \
                        abs(ab.center.y - self.ship.center.y) < aba_contact:
                    ab.alive = False
                    self.ship.alive = False
                    # play sound when player dies
                    self.dead_player.play()

        # clean up dead asteroids
        bring_out_your_dead(self.asteroids)
        # clean up dead bullets
        bring_out_your_dead(self.bullets)
        # clean up dead alien
        bring_out_your_dead(self.alien)
        # clean up dead alien bullets
        bring_out_your_dead(self.alien_bullet)

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

            # added since pressing UP + LEFT together prevents SPACE from firing bullets
            if key == arcade.key.LSHIFT:
                bullet = Bullet()
                bullet.align_with_ship(self.ship)
                self.bullets.append(bullet)

            if key == arcade.key.SPACE:
                bullet = Bullet()
                bullet.align_with_ship(self.ship)
                self.bullets.append(bullet)

        # If ship died, pressing ENTER makes ship regenerate.
        if key == arcade.key.ENTER:
            self.held_keys.add(arcade.key.ENTER)
            self.ship = Ship()
            # -100 points for resetting ship
            self.score.score -= 100

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
