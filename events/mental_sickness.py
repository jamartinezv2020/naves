import random
from events.event import Event
from util.console_colors import Colors, print_red, print_warning


class MentalSickness(Event):
    def __init__(self, probability):
        """
        Initialize a MentalSickness event with given probability.

        :param probability: Probability of the event occurring.
        """
        super().__init__(probability)

    def play_event(self, spaceship):
        """
        Execute the MentalSickness event.

        :param spaceship: The spaceship object affected by the event.
        """
        if self.triggers():
            print_warning("A mental sickness outbreak has struck the crew members.")

            # Gather ages of all crew members
            ages = []
            for i in range(5):
                for j in range(5):
                    for k in range(4):
                        ages.append(int(spaceship.rooms[i][j][k].age))

            # Calculate average age
            average = sum(ages) / len(ages)

            # Simulate mental sickness impact
            dead_count = 0
            for i in range(5):
                for j in range(5):
                    for k in range(4):
                        target = spaceship.rooms[i][j][k]
                        # Simulate probability of death based on age and random chance
                        if int(target.age) < int(average) and random.choice([True, False]):
                            target.kill(spaceship.route, "Mental sickness")
                            print_red(f'{target.name} ({target.age} years old) has become mentally ill and thrown themselves into space')
                            dead_count += 1

            print(dead_count, "people died due to mental illness")
            print("Average age:", int(average))

# Example usage
if __name__ == "__main__":
    # Example of creating and triggering the MentalSickness event
    mental_sickness = MentalSickness(0.5)  # Probability of occurrence
    spaceship = ...  # Assuming spaceship object exists

    if mental_sickness.triggers():
        mental_sickness.play_event(spaceship)


