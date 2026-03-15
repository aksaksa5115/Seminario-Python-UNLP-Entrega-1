import random
categorias = {
    "informatica":[
        "python",
        "programa",
        "variable",
        "funcion",
        "bucle",
        "entero",
        "lista",
    ],
    "paises": [
        "argentina",
        "brasil",
        "paraguay",
        "uruguay",
        "chile",

    ],
    "objetos":[
        "silla",
        "escritorio",
        "pc",
        "cadena",
    ] 
}

words = ""

category_selected = ""
while category_selected == "":
    print("seleccione alguna de las siguientes categorias: ")
    i = 1
    for cat in categorias:
        print(i, "-", cat)
        i += 1
    category_selected = input("selecciona el numero de alguna de las categorias: ")

    if not category_selected.isdigit():
        print("debes ingresar un numero de alguna categoria existente")
        category_selected = ""
        continue
    
    category_selected = int(category_selected)

    if category_selected < 1 or category_selected > len(categorias):
        print("ese numero de categoria es inexistente, seleccione otro")
        category_selected = ""

claves = list(categorias)
words = categorias[claves[category_selected - 1]]

word = random.choice(words)
guessed = []
attempts = 6
points = 0

words = ""
print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        points += 6
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    
    if len(letter) > 1 or len(letter) == 0 or letter < 'A' or letter > 'z':
        print("entrada no valida")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        if points > 0:
            points += -1
        print("Esa letra no está en la palabra.")
    
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    points = 0
print("tu puntaje final fue de:", points)
    