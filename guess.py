import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")

print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

def get_difficulty_choice(prompt: str = "Enter your choice (1/2/3): ") -> int:
    """Solicita y valida la elección de dificultad; devuelve 1, 2 o 3."""
    valid = {"1", "2", "3"}
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return int(choice)
        print("Invalid choice. Please enter 1, 2 or 3.")

difficulty_choice = get_difficulty_choice()
chances = 0

if difficulty_choice == 1:
    chances = 10
elif difficulty_choice == 2:
    chances = 5
else:
    chances = 3

secret_number = random.randint(1, 100)
answers = []
det = "a"

while chances > 0:
    print(f"\nYou have {chances} chances left.")
    answer = input(f"Give it {det} try: ")
    try:
        if answer in answers:
            print("You idiot or what? You tried that number already.")
        else:
            if int(answer) == secret_number:
                chances = 0
                print("Nice! You won.")
            else:
                answers.append(answer)
                det = "another"
                chances -= 1
    except:
        print("You had better type a number, you fool.")
print("The game is done. Good luck for the next one!")