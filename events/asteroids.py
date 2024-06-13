import random
from events.event import Event
from proccessing.sort import stochastic_quicksort
from util.console_colors import Colors


class Asteroids(Event):
    """
    Asteroids event class inheriting from Event.
    """

    def __init__(self, probability):
        """
        Initialize the Asteroids event with given probability.

        :param probability: Probability of the event occurring.
        """
        super().__init__(probability)

    def play_event(self, spaceship):
        """
        Execute the Asteroids event.

        :param spaceship: The spaceship object affected by the event.
        """
        if self.triggers():
            print(Colors.WARNING + "Asteroids incoming!" + Colors.ENDC)

            # Generate random asteroids
            asteroids = [random.randint(1, 100) for _ in range(100)]

            # Sort asteroids using stochastic quicksort
            asteroids = stochastic_quicksort(asteroids)

            dead_count = 0
            for asteroid in asteroids:
                if asteroid < 25:
                    print(f"Asteroid {asteroid} avoided!")
                else:
                    # Determine target room in the spaceship
                    i = (asteroid - 1) // 20
                    j = ((asteroid - 1) % 20) // 4
                    k = random.randint(0, 3)
                    target = spaceship.rooms[i][j][k]

                    # Attempt to kill a crew member in the target room
                    for _ in range(4):
                        if target.alive:
                            target.kill(spaceship.route, 'asteroids')
                            print(f'{Colors.FAIL}{target.name} has been hit!{Colors.ENDC}')
                            dead_count += 1
                            break
                        k = (k + 1) % 4

            print(f"{dead_count} people died due to asteroids!")

# Example usage
if __name__ == "__main__":
    # Example of creating and triggering the Asteroids event
    asteroids_event = Asteroids(0.3)  # Probability of occurrence
    spaceship = ...  # Assuming spaceship object exists

    if asteroids_event.triggers():
        asteroids_event.play_event(spaceship)

