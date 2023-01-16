import re


def word_repetition(sent: str) -> dict:

    # Remove punctuation and split
    split_string = re.sub(r'[^\w\s]', '', sent).split(' ')
    response = {}

    for word in split_string:
        lower_case = word.lower()
        response[lower_case] = response[lower_case] + \
            1 if lower_case in response.keys() else 1

    print(response)
    return response


word_repetition(
    "Hi how are things? How are you? Are you a developer? I am also a developer")
