import random
from events.event import Event
from util.console_colors import Colors

class SolarStorm(Event):
    def __init__(self, probability):
        """
        Initialize a SolarStorm event with given probability.

        :param probability: Probability of the event occurring.
        """
        super().__init__(probability)

    def play_event(self, spaceship):
        """
        Execute the SolarStorm event.

        :param spaceship: The spaceship object affected by the event.
        """
        if self.triggers():
            print(Colors.WARNING + "A Solar storm is hitting the spaceship!" + Colors.ENDC)
            
            # Simulate impact on the spaceship (sample behavior)
            stream = [random.randint(-100, 100) for _ in range(1000)]
            
            # Example of how the event could impact the spaceship
            for impact in stream:
                if impact < 0:
                    spaceship.damage_hull()
                else:
                    spaceship.reduce_energy()

            # Additional actions specific to SolarStorm can be programmed here
            # Example: spaceship.reduce_shield_strength()

# Example usage
if __name__ == "__main__":
    # Example of creating and triggering the SolarStorm event
    solar_storm = SolarStorm(0.5)  # Probability of occurrence
    spaceship = ...  # Assuming spaceship object exists

    if solar_storm.triggers():
        solar_storm.play_event(spaceship)
