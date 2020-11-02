"""
File: skeet.py
Original Author: Br. Burton
Completed by: Lewis Lockhart
This program implements an awesome version of skeet.

--> EXTRAS ADDED <--
 1. Better centering of the number on the StrongTarget
 2. A GameSound class to handle all the implemented sound effects
    - Rifle fire
    - Target destroyed
    - Target generation
    - Strong target hit (not destroyed)
    - Safe target destroyed
    - Bonus target destroyed 
 3. Bonus target
 4. Multi-color changer for bonus target
 5. Score color: Negative = pink, positive = green
 6. Adjusted create_target so bonus targets get generated 
    at a 10% probability.
 7. Game pauses if any key is pressed.
"""

import arcade
import math
import random
from abc import abstractmethod  # needed to resolve some console errors

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 15
RIFLE_HEIGHT = 100
RIFLE_COLOR = arcade.color.GRAY

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.GRAY
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15
BONUS_TARGET_SIZE = 10

VOLUME = 0.1


class Velocity:
    """
    Holds velocity variables.
    """
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0


class Point:
    """
    Point class for moving objects.
    """
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.angle = 0.0

    def draw(self):
        """ Draws the rifle. """
        arcade.draw_rectangle_filled(self.center.x, self.center.y,
                                     RIFLE_WIDTH, RIFLE_HEIGHT,
                                     RIFLE_COLOR, self.angle)


class GameSound:
    def __init__(self, sound_file, pan):
        self.sound = arcade.Sound(sound_file)
        self.pan = pan
        self.volume = VOLUME

    def play(self):
        """ Play """
        self.sound.play(pan=self.pan, volume=self.volume)


class FlyingObj:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True

    @abstractmethod
    def draw(self):
        """ Added by child classes. """
        pass

    def advance(self):
        """ Moves the object forward. """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def is_off_screen(self, _screen_width, _screen_height):
        """ Checks to see if the object is on the screen. """
        if self.center.x > _screen_width or self.center.y > _screen_height:
            return True
        else:
            return False


class Bullet(FlyingObj):
    """ Template for the bullets in the game. """
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.color = BULLET_COLOR

    def draw(self):
        """ Creates a circle for the bullet. """
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

    def fire(self, angle):
        """ Does some fancy math stuff for the bullet path. """
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED


class Target(FlyingObj):
    """ Base class for the child targets. """
    def __init__(self):
        super().__init__()
        self.center.y = random.uniform(SCREEN_HEIGHT/2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-2, 2)

    @abstractmethod
    def hit(self):
        """ Added by child classes. """
        pass


class StandardTarget(Target):
    """ Basic target, round, one hit, one point. """
    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS
        self.point = 1
        self.color = TARGET_COLOR
        self.t_break = GameSound(":resources:sounds/hit2.wav", pan=-1.0)

    def draw(self):
        """ Draws the circle for the target object. """
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

    def hit(self):
        """ If hit, change alive to false. """
        self.t_break.play()
        self.alive = False
        return self.point


class StrongTarget(Target):
    """ Strong target, round, three hits, five points. """
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 2)
        self.radius = TARGET_SAFE_RADIUS
        self.point = 5
        self.color = TARGET_COLOR
        self.lives = 3
        self.ting = GameSound(":resources:sounds/coin4.wav", pan=-1.0)
        self.t_break = GameSound(":resources:sounds/hit2.wav", pan=-1.0)

    def draw(self):
        """ Draws the circle for the target object. """
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, self.color, 2)
        # Adds the self.lives count to the center of the circle
        text_x = self.center.x - (self.radius / 2.5)
        text_y = self.center.y - (self.radius / 1.1)
        arcade.draw_text(repr(self.lives), text_x, text_y, self.color, font_size=20)

    def hit(self):
        """ If hit, reduce life count. If count = 0, change self.alive to false. """
        self.lives -= 1
        if self.lives > 0:
            self.ting.play()
            self.alive = True
            self.point = 1
            return self.point
        else:
            self.t_break.play()
            self.alive = False
            self.point = 5
            return self.point


class SafeTarget(Target):
    """ Safe target, square, one hit, minus 10 points. """
    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS
        self.point = -10
        self.color = TARGET_SAFE_COLOR
        self.oops = GameSound(":resources:sounds/jump1.wav", pan=-1.0)

    def draw(self):
        """ Draws the square on the screen. """
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.radius*1.5, self.radius*1.5, self.color)

    def hit(self):
        """ If hit, change alive to false. """
        self.alive = False
        self.oops.play()
        return self.point


class BonusTarget(Target):
    """ Bonus target, round, three hits, five points. """
    def __init__(self):
        super().__init__()
        self.velocity.dx = random.uniform(2, 6)
        self.velocity.dy = random.uniform(-2, 2)
        self.radius = BONUS_TARGET_SIZE
        self.point = 20
        self.blip = GameSound(":resources:sounds/laser5.wav", pan=-1.0)

    def draw(self):
        """ Draws the rect for the target object. """
        # Color options
        color_set = [arcade.color.PINK, arcade.color.LIGHT_BLUE, arcade.color.YELLOW, arcade.color.LIGHT_GREEN]
        # Select random color
        color = random.choice(color_set)
        # Draw rectangle
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.radius, self.radius, color)

    def hit(self):
        """ If hit, change alive to false. """
        self.blip.play()
        self.alive = False
        return self.point


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []
        self.targets = []

        self.gun_fire = GameSound(":resources:sounds/hit4.wav", pan=-1.0)
        self.release = GameSound(":resources:sounds/rockHit2.wav", pan=-1.0)

        self.pause = False

        arcade.set_background_color(arcade.color.EERIE_BLACK)


    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20

        # Change score color based on negative / positive
        if self.score >= 0:
            # Positive score
            arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.LIGHT_GREEN)
        else:
            # Negative score
            arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.PINK)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        if self.pause:
            pass
        else:
            self.check_collisions()
            self.check_off_screen()

            # decide if we should start a target
            if random.randint(1, 50) == 1:
                self.release.play()
                self.create_target()

            for bullet in self.bullets:
                bullet.advance()

            for target in self.targets:
                target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        rand_int = random.randint(1, 10)

        if rand_int in range(1, 4):
            target = StandardTarget()
            self.targets.append(target)

        elif rand_int in range(4, 7):
            target = StrongTarget()
            self.targets.append(target)

        elif rand_int in range(7, 10):
            target = SafeTarget()
            self.targets.append(target)

        elif rand_int == 10:
            target = BonusTarget()
            self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"
        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        if self.pause:
            pass
        else:
            self.rifle.angle = self._get_angle_degrees(y, x)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        if self.pause:
            pass
        else:
            angle = self._get_angle_degrees(x, y)
            self.gun_fire.play()
            bullet = Bullet()
            bullet.fire(angle)

            self.bullets.append(bullet)

    def on_key_press(self, symbol: int, modifiers: int):
        self.pause = not self.pause

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
