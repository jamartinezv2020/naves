import random
from events.event import Event
from util.console_colors import Colors

class Pirates(Event):
    def __init__(self, probability):
        """
        Initialize a Pirates event with given probability.

        :param probability: Probability of the event occurring.
        """
        super().__init__(probability)
        self.distinct_ships = 100
        self.fleet_size = 1000

    def play_event(self, spaceship):
        """
        Execute the Pirates event.

        :param spaceship: The spaceship object affected by the event.
        """
        if self.triggers():
            print(Colors.WARNING + "A fleet of pirate ships has been sighted!" + Colors.ENDC)
            
            # Generate random ships
            ships = [random.randint(0, self.distinct_ships - 1) for _ in range(self.fleet_size)]
            
            # Exact counting
            distinct_ships_count = 0
            seen_ships = [False] * self.distinct_ships
            for ship in ships:
                if not seen_ships[ship]:
                    seen_ships[ship] = True
                    distinct_ships_count += 1
            
            if distinct_ships_count == self.distinct_ships:
                # All distinct ships have been counted
                women_kidnapped = 0
                attempts = 100
                while women_kidnapped < 10 and attempts > 0:
                    # Randomly select rooms and targets to kidnap females
                    for target in spaceship.rooms[random.randint(0, 4)][random.randint(0, 4)]:
                        if target.gender == "Female" and target.alive:
                            target.kill(spaceship.route, 'pirates')
                            print(Colors.HEADER + target.name + ' has been kidnapped!' + Colors.ENDC)
                            women_kidnapped += 1
                            break
                        attempts -= 1
                print(women_kidnapped, "females kidnapped!")
            else:
                # Not all distinct ships have been counted, kidnap males
                males_kidnapped = 0
                attempts = 100
                while males_kidnapped < 10 and attempts > 0:
                    # Randomly select rooms and targets to kidnap males
                    for target in spaceship.rooms[random.randint(0, 4)][random.randint(0, 4)]:
                        if target.gender == "Male" and target.alive:
                            target.kill(spaceship.route, 'pirates')
                            print(Colors.HEADER + target.name + ' has been kidnapped!' + Colors.ENDC)
                            males_kidnapped += 1
                            break
                        attempts -= 1
                print(males_kidnapped, "males kidnapped!")

# Example usage
if __name__ == "__main__":
    # Example of creating and triggering the Pirates event
    pirates_event = Pirates(0.5)  # Probability of occurrence
    spaceship = ...  # Assuming spaceship object exists

    if pirates_event.triggers():
        pirates_event.play_event(spaceship)

