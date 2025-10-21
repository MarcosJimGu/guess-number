import random
import sys
from typing import Optional, Set

LIVES_MAP = {1: 10, 2: 5, 3: 3}
RANGE_MIN = 1
RANGE_MAX = 100

def get_difficulty_choice(prompt: str = "Selecciona dificultad (1=Fácil, 2=Media, 3=Difícil): ") -> int:
    """Solicita y valida la elección de dificultad; devuelve 1, 2 o 3."""
    valid = {"1", "2", "3"}
    while True:
        try:
            choice = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada. Saliendo.")
            sys.exit(0)
        if choice in valid:
            return int(choice)
        print("Opción inválida. Introduce 1, 2 o 3.")

def get_int_in_range(prompt: str, min_v: int = RANGE_MIN, max_v: int = RANGE_MAX) -> Optional[int]:
    """Lee un entero dentro del rango [min_v, max_v]. Devuelve None si la entrada no es válida."""
    try:
        raw = input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada. Saliendo.")
        sys.exit(0)

    if not raw:
        print("Entrada vacía. Introduce un número.")
        return None

    try:
        value = int(raw)
    except ValueError:
        print("Por favor, introduce un número entero válido.")
        return None

    if not (min_v <= value <= max_v):
        print(f"Introduce un número entre {min_v} y {max_v}.")
        return None

    return value

def main() -> None:
    print("Bienvenido al juego de adivinar el número.")
    print(f"Estoy pensando en un número entre {RANGE_MIN} y {RANGE_MAX}.\n")

    print("Niveles de dificultad:")
    print("1. Fácil (10 intentos)")
    print("2. Medio (5 intentos)")
    print("3. Difícil (3 intentos)\n")

    difficulty = get_difficulty_choice()
    chances = LIVES_MAP[difficulty]
    secret_number = random.randint(RANGE_MIN, RANGE_MAX)
    guessed: Set[int] = set()

    while chances > 0:
        print(f"\nTe quedan {chances} intento(s).")
        guess = get_int_in_range("Introduce tu número: ")
        if guess is None:
            continue

        if guess in guessed:
            print("Ya intentaste ese número. Prueba con otro.")
            continue

        guessed.add(guess)

        if guess == secret_number:
            print("¡Correcto! Has ganado.")
            break

        chances -= 1
        if guess < secret_number:
            print("Demasiado bajo.")
        else:
            print("Demasiado alto.")

    else:
        # Ejecutado cuando se agotan los intentos sin haber hecho 'break'
        print(f"\nSe acabaron los intentos. El número era {secret_number}.")

if __name__ == "__main__":
    main()