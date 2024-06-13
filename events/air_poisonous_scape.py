import random
import util.console_colors
from events.event import Event
from proccessing.bloom_filter import BloomFilter
from util.console_colors import Colors


class AirPoisonousScape(Event):
    """
    AirPoisonousScape event class inheriting from Event.
    """

    def __init__(self, probability):
        """
        Initialize the AirPoisonousScape event with given probability.

        :param probability: Probability of the event occurring.
        """
        super().__init__(probability)

    def play_event(self, spaceship):
        """
        Execute the AirPoisonousScape event.

        :param spaceship: The spaceship object affected by the event.
        """
        if self.triggers():
            print(Colors.WARNING + "There is an air poisonous scape!" + Colors.ENDC)

            # Generate random analysis data
            analysis = [[random.randint(-1000, 1000), random.randint(-1000, 1000)] for _ in range(100000)]

            # Initialize Bloom Filter
            bloom_filter = BloomFilter(100000, 0.05)

            # Add analysis data to Bloom Filter
            for data in analysis:
                bloom_filter.add(data)

            dead_count = 0

            # Iterate through spaceship rooms
            for i in range(5):
                for j in range(5):
                    test_room = (i, j)

                    # Check if room is possibly in the Bloom Filter
                    if bloom_filter.check(test_room):
                        util.console_colors.print_cyan(f"Room {test_room} is possibly in the array")

                        # Check if room is actually in the analysis data
                        if test_room in analysis:
                            # Act: 50% of the people in the room die
                            util.console_colors.print_green(f"Room {test_room} was indeed in the array")
                            victims_count = 0
                            for k in range(4):
                                target = spaceship.rooms[i][j][k]
                                if target.alive:
                                    target.kill(spaceship.route, "Air poisonous")
                                    util.console_colors.print_red(f"{target.name} died from poisoned air")
                                    dead_count += 1
                                    victims_count += 1
                                if victims_count == 2:  # Assuming 50% mortality rate
                                    break

                        else:
                            # False positive: everyone in the room dies
                            util.console_colors.print_red("False positive!")
                            for k in range(4):
                                target = spaceship.rooms[i][j][k]
                                if target.alive:
                                    target.kill(spaceship.route, "Air poisonous")
                                    util.console_colors.print_red(f"{target.name} died from poisoned air")
                                    dead_count += 1

                    else:
                        # No action: 80% mortality in the room and one of the nearby rooms
                        print(f"Room {test_room} is definitely not in the array")
                        victims_count = 0
                        for k in range(4):
                            target = spaceship.rooms[i][j][k]
                            if target.alive:
                                target.kill(spaceship.route, "Air poisonous")
                                util.console_colors.print_red(f"{target.name} died from poisoned air")
                                dead_count += 1
                                victims_count += 1
                            if victims_count == 3:  # Assuming 80% mortality rate
                                break

                        # Choose random nearby room
                        row, col = random.choice(adjacent_positions(i, j))
                        victims_count = 0
                        for k in range(4):
                            target = spaceship.rooms[row][col][k]
                            if target.alive:
                                target.kill(spaceship.route, "Air poisonous")
                                util.console_colors.print_red(f"{target.name} died from nearby room poisoned air")
                                dead_count += 1
                                victims_count += 1
                            if victims_count == 3:  # Assuming 80% mortality rate
                                break

            util.console_colors.print_bold(f"{dead_count} people died due to air poisonous scape!")


def adjacent_positions(row, column):
    """
    Get adjacent positions to a given row and column within a 5x5 matrix.

    :param row: Row index.
    :param column: Column index.
    :return: List of adjacent positions (row, column).
    """
    displacements = [-1, 0, 1]
    adjacent = []

    for dr in displacements:
        for dc in displacements:
            if dr == 0 and dc == 0:
                continue
            new_row = row + dr
            new_column = column + dc
            if 0 <= new_row < 5 and 0 <= new_column < 5:
                adjacent.append((new_row, new_column))

    return adjacent

# Example usage
if __name__ == "__main__":
    # Example of creating and triggering the AirPoisonousScape event
    air_poison_event = AirPoisonousScape(0.4)  # Probability of occurrence
    spaceship = ...  # Assuming spaceship object exists

    if air_poison_event.triggers():
        air_poison_event.play_event(spaceship)

