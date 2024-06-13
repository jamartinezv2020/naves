from util.console_colors import Colors
from util.util import belts, pick_random_person, routes
from proccessing.hashing import hash1, hash2, hash3


class Spaceship:

    def __init__(self):
        self.rooms = [[[] for _ in range(5)] for _ in range(5)]  # Inicialización de habitaciones
        self.actual_belt = self.origin = 'Beta'  # Cinturón actual y origen de la nave
        self.route = self.origin  # Ruta de la nave

    def select_travelers(self):
        i = 0
        while i < 100:  # Seleccionar 100 viajeros
            selected_person = pick_random_person()  # Seleccionar una persona aleatoria
            lastname = selected_person.name.split(" ")[1]  # Obtener el apellido de la persona
            n = hash1(lastname)  # Calcular hash1 del apellido
            m = hash2(lastname)  # Calcular hash2 del apellido
            w = hash3(selected_person.id)  # Calcular hash3 del ID de la persona

            # Intentar asignar la persona a una habitación según los hashes
            if len(self.rooms[n][m]) < 4:
                self.rooms[n][m].append(selected_person)
            elif len(self.rooms[m][n]) < 4:
                self.rooms[m][n].append(selected_person)
            elif len(self.rooms[n][w]) < 4:
                self.rooms[n][w].append(selected_person)
            elif len(self.rooms[w][n]) < 4:
                self.rooms[w][n].append(selected_person)
            elif len(self.rooms[w][m]) < 4:
                self.rooms[w][m].append(selected_person)
            elif len(self.rooms[m][w]) < 4:
                self.rooms[m][w].append(selected_person)
            else:
                # Si no hay habitaciones disponibles según los hashes, buscar la primera disponible
                for j in range(5):
                    for k in range(5):
                        if len(self.rooms[j][k]) < 4:
                            self.rooms[j][k].append(selected_person)
                            break
                    else:
                        continue
                    break
            i += 1

    def show_rooms(self):
        for i in range(5):
            for j in range(5):
                print("Room ", i + 1, " ", j + 1)
                for k in range(4):
                    person = self.rooms[i][j][k]
                    print(person.name + " " + person.state())  # Mostrar el nombre y el estado de la persona

    def travel(self):
        print("Traveling from ", Colors.OKBLUE + self.actual_belt + Colors.ENDC, " to ",
              Colors.OKCYAN + routes[self.actual_belt] + Colors.ENDC, "...")
        print("Exiting " + self.actual_belt + " belt...")

        # Ejecutar eventos al salir del cinturón actual
        for event in belts[self.actual_belt]:
            event.play_event(self)

        self.route += " -> " + routes[self.actual_belt]  # Actualizar la ruta de la nave
        self.actual_belt = routes[self.actual_belt]  # Actualizar el cinturón actual

        print("Entering " + self.actual_belt + " belt...")

        # Ejecutar eventos al entrar al nuevo cinturón
        for event in belts[self.actual_belt]:
            event.play_event(self)

        # Asignar la ruta actual a las personas vivas en las habitaciones
        for i in range(5):
            for j in range(5):
                for k in range(4):
                    if self.rooms[i][j][k].alive:
                        self.rooms[i][j][k].route = self.route

