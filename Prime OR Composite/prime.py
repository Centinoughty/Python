def prime(number):
    prime = 0
    composite = 0

    for i in range(2, (number//2)+1):
        if number % i == 0:
            composite += 1
            return "Composite"
        else:
            prime += 1
            if i == number//2:
                return "Prime"
