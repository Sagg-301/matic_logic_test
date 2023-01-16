from ..Fibonacci import fibonacci
from ..FizzBuzz import fizz_buzz
from ..WordRepetition import word_repetition


def test_fibonacci_0():
    result = fibonacci(0)
    assert result == 0


def test_fibonacci_7():
    result = fibonacci(7)
    assert result == 13


def test_fibonacci_15():
    result = fibonacci(15)
    assert result == 610


def test_fizz_buzz():
    response = fizz_buzz()

    assert response == [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizz buzz', 16, 17, 'fizz', 19, 'buzz', 'fizz', 22, 23, 'fizz', 'buzz', 26, 'fizz', 28, 29, 'fizz buzz', 31, 32, 'fizz', 34, 'buzz', 'fizz', 37, 38, 'fizz', 'buzz', 41, 'fizz', 43, 44, 'fizz buzz', 46, 47, 'fizz', 49,
                        'buzz', 'fizz', 52, 53, 'fizz', 'buzz', 56, 'fizz', 58, 59, 'fizz buzz', 61, 62, 'fizz', 64, 'buzz', 'fizz', 67, 68, 'fizz', 'buzz', 71, 'fizz', 73, 74, 'fizz buzz', 76, 77, 'fizz', 79, 'buzz', 'fizz', 82, 83, 'fizz', 'buzz', 86, 'fizz', 88, 89, 'fizz buzz', 91, 92, 'fizz', 94, 'buzz', 'fizz', 97, 98, 'fizz', 'buzz']


def test_word_repetition_example():
    result = word_repetition(
        "Hi how are things? How are you? Are you a developer? I am also a developer")

    assert result == {'hi': 1, 'how': 2, 'are': 3, 'things': 1,
                      'you': 2, 'a': 2, 'developer': 2, 'i': 1, 'am': 1, 'also': 1}


def test_word_repetition_only_one_word():
    result = word_repetition(
        "Matic matic matic matic matic matic")

    assert result == {'matic': 6}
