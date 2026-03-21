import random
categories = {
    "informatica": [
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
    "objetos": [
        "silla",
        "escritorio",
        "pc",
        "cadena",
    ]
}

category_selected = ""
while category_selected == "":
    print("seleccione alguna de las siguientes categorias: ")
    i = 1
    for cat in categories:
        print(i, "-", cat)
        i += 1
    category_selected = input("selecciona el numero de una categorias: ")

    if not category_selected.isdigit():
        print("debes ingresar un numero de alguna categoria existente")
        category_selected = ""
        continue

    category_selected = int(category_selected)

    if category_selected < 1 or category_selected > len(categories):
        print("ese numero de categoria es inexistente, seleccione otro")
        category_selected = ""

keys = list(categories)
words = categories[keys[category_selected - 1]]

words_random = random.sample(words, len(words))
index = 0
jugar = True
points = 0
right_words = 0
print("¡Bienvenido al Ahorcado!")
while jugar:
    guessed = []
    attempts = 6

    print()
    if index == len(words_random):
        print("completaste la categoria!!!")
        print(f"palabras acertadas: {right_words} de {len(words_random)}")
        print("selecciona otra categoria para volver a jugar")
        break
    word = words_random[index]
    index += 1
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
            right_words += 1
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
            points -= 1
            print("Esa letra no está en la palabra.")

        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        print("Selecciona para volver a intentar o salir del juego")
        print("1 - volver a intentar")
        print("2 - salir del juego")
        choice = ""
        while choice == "":
            choice = input("selecciona una opción: ")
            if not choice.isdigit():
                print("seleccione una opción valida")
                choice = ""
                continue
            if int(choice) > 2 or int(choice) < 1:
                print("seleccione un numero valido")
                choice = ""
            elif int(choice) == 2:
                jugar = False

print("tu puntaje final fue de:", points)
