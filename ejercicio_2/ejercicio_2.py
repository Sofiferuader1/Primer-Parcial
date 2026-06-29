from super_heroes_data import superheroes
import re


class Cola:
    def __init__(self):
        self.datos = []

    def arribo(self, dato):
        self.datos.append(dato)

    def atencion(self):
        if not self.cola_vacia():
            return self.datos.pop(0)
        return None

    def cola_vacia(self):
        return len(self.datos) == 0


def mostrar_personaje(personaje):
    villano = "Si" if personaje["is_villain"] else "No"

    print("Nombre:", personaje["name"])
    print("Alias:", personaje["alias"])
    print("Nombre real:", personaje["real_name"])
    print("Biografia:", personaje["short_bio"])
    print("Primera aparicion:", personaje["first_appearance"])
    print("Villano:", villano)
    print("-" * 60)


def listar_personajes(personajes):
    for personaje in personajes:
        print(personaje["name"])


def buscar_posicion(personajes, nombre):
    for i in range(len(personajes)):
        if personajes[i]["name"] == nombre:
            return i
    return -1


def listar_villanos(personajes):
    for personaje in personajes:
        if personaje["is_villain"]:
            print(personaje["name"])


def cargar_villanos_en_cola(personajes):
    cola = Cola()

    for personaje in personajes:
        if personaje["is_villain"]:
            cola.arribo(personaje)

    return cola


def listar_villanos_antes_1980(cola):
    while not cola.cola_vacia():
        villano = cola.atencion()

        if villano["first_appearance"] < 1980:
            print(villano["name"], "-", villano["first_appearance"])


def listar_superheroes_por_iniciales(personajes):
    iniciales = ("Bl", "G", "My", "W")

    for personaje in personajes:
        if not personaje["is_villain"] and personaje["name"].startswith(iniciales):
            print(personaje["name"])


def modificar_ant_man(personajes):
    for personaje in personajes:
        if personaje["name"] == "Ant Man":
            personaje["real_name"] = "Scott Lang"
            return personaje
    return None


def listar_biografia_time_traveling_o_suit(personajes):
    patron = r"\b(time-traveling|suit)\b"

    for personaje in personajes:
        biografia = personaje["short_bio"].lower()

        if re.search(patron, biografia):
            mostrar_personaje(personaje)


def eliminar_personaje(personajes, nombre):
    for personaje in personajes:
        if personaje["name"] == nombre:
            personajes.remove(personaje)
            return personaje
    return None


# Programa principal

personajes = superheroes.copy()

print("Cantidad de personajes cargados:", len(personajes))
print()

print("1) Listado ordenado de manera ascendente por nombre:")
personajes_ordenados = sorted(personajes, key=lambda personaje: personaje["name"])
listar_personajes(personajes_ordenados)
print()

print("2) Posicion de The Thing y Rocket Raccoon:")
posicion_the_thing = buscar_posicion(personajes, "The Thing")
posicion_rocket = buscar_posicion(personajes, "Rocket Raccoon")

print("The Thing esta en la posicion:", posicion_the_thing)
print("Rocket Raccoon esta en la posicion:", posicion_rocket)
print()

print("3) Listado de villanos:")
listar_villanos(personajes)
print()

print("4) Villanos en cola que aparecieron antes de 1980:")
cola_villanos = cargar_villanos_en_cola(personajes)
listar_villanos_antes_1980(cola_villanos)
print()

print("5) Superheroes que comienzan con Bl, G, My y W:")
listar_superheroes_por_iniciales(personajes)
print()

print("6) Listado ordenado por nombre real:")
personajes_ordenados_real = sorted(
    personajes,
    key=lambda personaje: personaje["real_name"] if personaje["real_name"] is not None else ""
)

for personaje in personajes_ordenados_real:
    print(personaje["real_name"], "-", personaje["name"])
print()

print("7) Listado de superheroes ordenados por fecha de aparicion:")
superheroes_ordenados_fecha = sorted(
    [personaje for personaje in personajes if not personaje["is_villain"]],
    key=lambda personaje: personaje["first_appearance"]
)

for personaje in superheroes_ordenados_fecha:
    print(personaje["name"], "-", personaje["first_appearance"])
print()

print("8) Modificar el nombre real de Ant Man a Scott Lang:")
ant_man = modificar_ant_man(personajes)

if ant_man is not None:
    mostrar_personaje(ant_man)
else:
    print("Ant Man no estaba en la lista.")
print()

print("9) Personajes que en su biografia incluyen time-traveling o suit:")
listar_biografia_time_traveling_o_suit(personajes)
print()

print("10) Eliminar Electro y Baron Zemo:")

electro = eliminar_personaje(personajes, "Electro")
baron_zemo = eliminar_personaje(personajes, "Baron Zemo")

if electro is not None:
    print("Electro estaba en la lista y fue eliminado:")
    mostrar_personaje(electro)
else:
    print("Electro no estaba en la lista.")

if baron_zemo is not None:
    print("Baron Zemo estaba en la lista y fue eliminado:")
    mostrar_personaje(baron_zemo)
else:
    print("Baron Zemo no estaba en la lista.")

print("Cantidad final de personajes:", len(personajes))


