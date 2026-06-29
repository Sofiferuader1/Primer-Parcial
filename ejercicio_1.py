# Ejercicio 1
# Dada una lista simple de Python de 15 superhéroes:
# 1) Buscar de forma recursiva si Capitan America está en la lista.
# 2) Listar de forma recursiva todos los superhéroes.
def buscar_capitan_america(superheroes, indice=0):
    if indice == len(superheroes):
        return False

    if superheroes[indice] == "Capitan America":
        return True

    return buscar_capitan_america(superheroes, indice + 1)


def listar_superheroes(superheroes, indice=0):
    if indice == len(superheroes):
        return

    print(superheroes[indice])

    listar_superheroes(superheroes, indice + 1)


superheroes = [
    "Iron Man",
    "Thor",
    "Hulk",
    "Viuda Negra",
    "Ojo de Halcón",
    "Capitan America",
    "Spider-Man",
    "Doctor Strange",
    "Pantera Negra",
    "Bruja Escarlata",
    "Ant-Man",
    "Avispa",
    "Capitana Marvel",
    "Falcon",
    "Vision"
]

print("Listado de superheroes:")
listar_superheroes(superheroes)

print()

if buscar_capitan_america(superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America no está en la lista.")