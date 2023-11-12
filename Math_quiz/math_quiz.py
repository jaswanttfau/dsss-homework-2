import random


def generate_random_integer(min, max):
    """Generates a random integer between min and max (inclusive)."""
    return random.randint(min, max)


def generate_random_operator():
    """Generates a random mathematical operator (+, -, *, or /)."""
    operators = ["+", "-", "*", "/"]
    return random.choice(operators)


def generate_math_problem():
    """Generates a random math problem with two integers and an operator.

    Returns a tuple of (problem, answer).
    """
    num1 = generate_random_integer(1, 10)
    num2 = generate_random_integer(1, 5)
    operator = generate_random_operator()

    problem = f"{num1} {operator} {num2}"

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        answer = num1 / num2
    else:
        raise ValueError(f"Unsupported operator: {operator}")

    return problem, answer


def math_quiz():
    """Presents the user with math problems and gives them points for correct answers.

    Returns the user's score.
    """
    score = 0
    total_questions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        problem, answer = generate_math_problem()

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"Invalid answer: {user_answer}")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

    return score


if __name__ == "__main__":
    math_quiz()
