class Person:
    def __init__(self, id, name, gender, age):
        """
        Initialize a Person object with specified attributes.

        :param id: Person's ID.
        :param name: Person's name.
        :param gender: Person's gender.
        :param age: Person's age.
        """
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.family = []
        self.alive = True
        self.route = ''
        self.death_cause = ''

    def add_family_member(self, id):
        """
        Add a family member's ID to the Person's family list.

        :param id: Family member's ID.
        """
        self.family.append(id)

    def show_family(self):
        """
        Print all family member IDs.
        """
        for member_id in self.family:
            print(member_id)

    def state(self):
        """
        Return the state of the Person (alive or deceased with death cause and route).
        """
        return "Alive" if self.alive else f"Died due to: {self.death_cause}. Route: {self.route}"

    def kill(self, last_route, death_cause):
        """
        Set the Person's state to deceased with specified death details.

        :param last_route: Last route traveled.
        :param death_cause: Cause of death.
        """
        self.alive = False
        self.route = last_route
        self.death_cause = death_cause

    def __str__(self):
        """
        Return a string representation of the Person (their name).
        """
        return self.name

