"""
File: pong.py
Original Author: Br. Burton
Completed by: Lewis Lockhart
"""
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5


class Velocity:
    """
    Holds velocity variables for the Ball class.
    """
    def __init__(self):
        self.dx = 0.00
        self.dy = 0.00


class Point:
    """
    Point class for moving objects - Ball and Paddle classes.
    """
    def __init__(self):
        self.x = 0.00
        self.y = 0.00


class Ball:
    """
    Ball class:
        Has: center, velocity, ball_color
        Can: rand_color, draw, advance, bounce_horizontal, bounce_vertical, restart
    """
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.velocity.dx = 3
        self.velocity.dy = 2

        # This is used to enable dynamic ball color
        self.ball_color = arcade.color.WHITE

    def rand_color(self):
        """ Sets self.ball_color to a random color when called. """
        color = [arcade.color.YELLOW, arcade.color.CYAN, arcade.color.WHITE, arcade.color.LIGHT_BLUE, arcade.color.BISQUE, arcade.color.RED, arcade.color.BLUE]
        self.ball_color = random.choice(color)

    def draw(self):
        """ Draws the ball in the UI. """
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, self.ball_color)

    def advance(self):
        """ Moves the ball in the UI by setting x to dx, and y to dy. """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_horizontal(self):
        """ Reverses direction of the ball on impact. """
        self.velocity.dx *= -1

    def bounce_vertical(self):
        """ Reverses direction of the ball on impact. """
        self.velocity.dy *= -1

    def restart(self):
        """ Not a true restart. Resets the ball location, speed, and color. """
        # Sets random start location on the left side of the screen
        self.center.y = random.randrange((0 + BALL_RADIUS), (SCREEN_HEIGHT - BALL_RADIUS))
        self.center.x = 0.00
        # For getting the new ball color
        self.rand_color()
        # Sets random velocity
        self.velocity.dx = random.randrange(2, 4)
        self.velocity.dy = random.randrange(2, 4)


class Paddle:
    """
        Player paddle:
            Has: center
            Can: draw, move_up, move_down
    """
    def __init__(self):
        self.center = Point()
        self.center.x = SCREEN_WIDTH - 20
        self.center.y = PADDLE_HEIGHT

    def draw(self):
        """ Draws the paddle on the screen. """
        arcade.draw_rectangle_filled(self.center.x, self.center.y,
                                     PADDLE_WIDTH, PADDLE_HEIGHT,
                                     arcade.color.LIGHT_GRAY)

    def move_up(self):
        """ Moves the paddle up via user input. """
        if self.center.y < (SCREEN_HEIGHT - (PADDLE_HEIGHT/2)):
            self.center.y += MOVE_AMOUNT

    def move_down(self):
        """ Moves the paddle down via user input. """
        if self.center.y > (0 + (PADDLE_HEIGHT/2)):
            self.center.y -= MOVE_AMOUNT


class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20

        if self.score < 0:
            # Display score as RED if in the negative
            arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.RED)
            # Display score as GREEN if 0 or positive
        if self.score >= 0:
            arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.GREEN)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Move the ball forward one element in time
        self.ball.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
                    abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                    self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
            self.score += SCORE_HIT

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        if self.ball.center.x < (0 + BALL_RADIUS) and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        if self.ball.center.y < (0 + BALL_RADIUS) and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > (SCREEN_HEIGHT - BALL_RADIUS) and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()

        if self.holding_right:
            self.paddle.move_up()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False


# Creates the game and starts it going
window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
