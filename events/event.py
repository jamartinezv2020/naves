from abc import ABC, abstractmethod
from random import random


class Event(ABC):
    """
    Abstract base class representing an event in a spaceship simulation.
    """

    def __init__(self, probability):
        """
        Initialize an Event with given probability.

        :param probability: Probability of the event occurring.
        """
        self.probability = probability

    @abstractmethod
    def play_event(self, spaceship):
        """
        Abstract method to be implemented by subclasses.
        Executes the event's action on the spaceship.

        :param spaceship: The spaceship object affected by the event.
        """
        pass

    def triggers(self):
        """
        Determine if the event triggers based on its probability.

        :return: True if the event triggers, False otherwise.
        """
        return self.probability > random()

# Example usage and testing
if __name__ == "__main__":
    class DummyEvent(Event):
        """
        Dummy event subclass for testing purposes.
        """
        def play_event(self, spaceship):
            print("Dummy event executed")

    # Example of creating and testing a DummyEvent
    dummy_event = DummyEvent(0.5)  # Probability of occurrence
    if dummy_event.triggers():
        dummy_event.play_event(None)  # Passing None as spaceship object

