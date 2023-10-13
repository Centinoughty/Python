def armstrong_check(number):
    num = number
    copy = number
    count = 0
    sum = 0
    while num > 0:
        num = num // 10
        count = count + 1

    while copy > 0:
        sum = sum + (copy%10)**count
        copy = copy // 10

    if sum == number:
        return 1
    else:
        return 0
