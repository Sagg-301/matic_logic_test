def fizz_buzz():
    response = []
    for n in range(1, 101):
        if (n % 5 == 0) and (n % 3 == 0):
            response.append('fizz buzz')
            continue
        if (n % 3 == 0):
            response.append('fizz')
            continue
        if (n % 5 == 0):
            response.append('buzz')
            continue

        response.append(n)
    print(response)
    return response


fizz_buzz()
