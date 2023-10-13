def fibonacci(number):
    series = [0, 1]
    string = ""
    for i in range(0, number-2):
        series.append(series[-2]+series[-1])

    for i in range(0, len(series)):
        string = string + str(series[i]) + ", "

    string = string.strip()
    string = string[:-1]

    return string
