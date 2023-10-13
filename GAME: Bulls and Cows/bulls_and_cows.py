import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number = ""
secret_numbers = []
for i in range (0, 4):
    secret_number = numbers[random.randint(0, len(numbers)-1)]
    secret_numbers.append(secret_number)
    numbers.remove(secret_number)

for i in range(0, len(secret_numbers)):
    number = number+str(secret_numbers[i])

score = 0
while True:
    bulls = 0
    cows = 0
    text = input("Guess the number: ")
    guess_number = []
    if str(text) != str(number):
        if len(text) == 4:
            for i in range(0, 4):
                guess_number.append(int(text[i]))

            for i in range(0, 4):
                if guess_number[i] == secret_numbers[i]:
                    bulls += 1
                else:
                    pass

            for i in range(0, 4):
                if guess_number[i] in secret_numbers:
                    if guess_number[i] == secret_numbers[i]:
                        pass
                    else:
                        cows += 1
                else:
                    pass

            print(f"Bulls: {bulls}, Cows: {cows}")
            score += 1

        else:
            print("Enter a 4-digit number.")
            pass
    else:
        print(f"Bulls: 4... Score: {score}")
        break
