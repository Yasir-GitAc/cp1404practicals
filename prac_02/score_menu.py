import random

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            valid_score = get_valid_score()
            score = valid_score
            print(f"Score: {score}")
        elif choice == "P":
            user_score = float(input("give score: "))
            result = evaluate_score(user_score)
            print(f"Result: {result} ")
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def print_asterisks(score):
    print("*" * score)


def get_valid_score():
    score = random.randint(0, 100)
    return score

main()