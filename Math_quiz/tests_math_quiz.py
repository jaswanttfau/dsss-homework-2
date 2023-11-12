import unittest

from math_quiz import generate_random_integer, generate_random_operator, generate_math_problem, math_quiz


class MathQuizTests(unittest.TestCase):
    def test_generate_random_integer(self):
        min_value = 1
        max_value = 10

        for _ in range(100):
            random_integer = generate_random_integer(min_value, max_value)
            self.assertGreaterEqual(random_integer, min_value)
            self.assertLessEqual(random_integer, max_value)

    def test_generate_random_operator(self):
        operators = ["+", "-", "*", "/"]

        for _ in range(100):
            random_operator = generate_random_operator()
            self.assertIn(random_operator, operators)

    def test_generate_math_problem(self):
        for _ in range(100):
            problem, answer = generate_math_problem()

            # Check that the problem is a valid math expression.
            self.assertEqual(eval(problem), answer)

    def test_math_quiz(self):
        score = math_quiz()

        # Check that the score is a valid integer.
        self.assertIsInstance(score, int)

        # Check that the score is between 0 and the total number of questions.
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 3.14159265359)


if __name__ == "__main__":
    unittest.main()
