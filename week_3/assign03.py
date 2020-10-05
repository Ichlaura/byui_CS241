# Lewis Lockhart :: CS-241
from threading import Timer
from threading import Lock
"""
A little CLI robot game. It allows for the basic move and shoot methods. 
It also features some extra methods like charge, and nuke.
"""


class LilRobot:
    """ The main robot class for the CLI robot game. """
    def __init__(self):
        # Variable list
        self.count = 5
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel_amount = 100
        self.move_fuel_cost = 5
        self.laser_fuel_cost = 15
        self.charge_increment = 5
        self.evm_fuel_cost = 30
        self.bk_fuel_cost = 80

    def can_do(self, cost):
        """ Measures the energy demands against the supply. """
        if cost > self.fuel_amount:
            print('Insufficient fuel to perform action')
            return False
        else:
            return True

    def left(self):
        """ Move left. """
        if self.can_do(self.move_fuel_cost):
            # Update fuel amount
            self.fuel_amount -= self.move_fuel_cost
            # Update position
            self.x_coordinate -= 1

    def right(self):
        """ Move right. """
        if self.can_do(self.move_fuel_cost):
            # Update fuel amount
            self.fuel_amount -= self.move_fuel_cost
            # Update position
            self.x_coordinate += 1

    def up(self):
        """ Move up. """
        if self.can_do(self.move_fuel_cost):
            # Update fuel amount
            self.fuel_amount -= self.move_fuel_cost
            # Update position
            self.y_coordinate -= 1

    def down(self):
        """ Move down. """
        if self.can_do(self.move_fuel_cost):
            # Update fuel amount
            self.fuel_amount -= self.move_fuel_cost
            # Update position
            self.y_coordinate += 1

    def fire(self):
        """ Shoots the laser. """
        if self.can_do(self.laser_fuel_cost):
            # Update fuel amount
            self.fuel_amount -= self.laser_fuel_cost
            print('Pew! Pew!')

    def status(self):
        """ Outputs x,y position and fuel level. """
        print(f'({self.x_coordinate}, {self.y_coordinate}) - Fuel: {self.fuel_amount}')

    def evm(self):
        """
        evm - Evasive Maneuvering
        Executes several commands: right - up - right - down - right - up.
        """
        if self.can_do(self.evm_fuel_cost):
            print('right - up - right - down - right - up')
            self.right()
            self.up()
            self.right()
            self.down()
            self.right()
            self.up()
            self.status()

    def bk(self):
        """
        bk - Blitzkrieg
        Executes several commands: right - fire - right - fire - right - fire.
        """
        if self.can_do(self.bk_fuel_cost):
            print('right - fire - right - fire - right - fire')
            self.fire()
            self.right()
            self.fire()
            self.left()
            self.fire()
            self.right()
            self.fire()
            self.left()
            self.status()

    def charge(self):
        """ charge - Deploy Solar Charger """
        if self.fuel_amount == 100:
            # Don't charge if fuel is at 100
            print(f'No Charge Required - Current fuel: {self.fuel_amount}')
        else:
            print('Supercharge ... ')
            # Add to fuel amount
            self.fuel_amount += self.charge_increment
            # Output new fuel level
            print(f'Complete - Current fuel: {self.fuel_amount}')

    def nuke(self):
        """ nuke - Detonates 48,000 megaton nuclear warhead. """
        print('Detonation sequence started ...')

        def arming():
            """ Fake arming. """
            print('Arming warhead ...')
        m1 = Timer(1, arming)
        m1.start()

        def arming_complete():
            """ Fake arming complete. """
            print('... complete')
            print('Warhead Ready!')
        m2 = Timer(4, arming_complete)
        m2.start()

        def count_down():
            """ Real countdown for fake bomb. """
            if self.count <= 0:
                # Raise error before fake bomb pretends to explode.
                raise Exception('*** You Jerk ***')
            print(f'{self.count}')
            self.count -= 1

        # A horrible pile of timers.
        # There has to be a better way to do this. TODO: Please advise.
        c1 = Timer(5, count_down)
        c1.start()
        c2 = Timer(6, count_down)
        c2.start()
        c3 = Timer(7, count_down)
        c3.start()
        c4 = Timer(8, count_down)
        c4.start()
        c5 = Timer(9, count_down)
        c5.start()
        c6 = Timer(10, count_down)
        c6.start()


def main():
    """
    Instantiates the LilRobot class.
    Prompts for user commands until the program is 'quit'.
    """
    # Instantiation of robot class
    lr = LilRobot()
    prompt = True
    # Prompts and routes commands from the user
    while prompt is True:
        cmd = input("Enter command: ")
        # Valid commands
        options = ['left', 'right', 'up', 'down', 'fire', 'status', 'quit', 'charge',
                   'evm', 'bk', 'nuke']
        # If command is valid, map it to the correct method
        # There has to be a better way to do this. TODO: Please advise.
        if cmd in options:
            if cmd == 'left':
                lr.left()
            elif cmd == 'right':
                lr.right()
            elif cmd == 'up':
                lr.up()
            elif cmd == 'down':
                lr.down()
            elif cmd == 'fire':
                lr.fire()
            elif cmd == 'status':
                lr.status()
            elif cmd == 'quit':
                prompt = False
                print('Goodbye.')
            elif cmd == 'charge':
                lr.charge()
            elif cmd == 'evm':
                lr.evm()
            elif cmd == 'bk':
                lr.bk()
            elif cmd == 'nuke':
                prompt = False
                lr.nuke()


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
