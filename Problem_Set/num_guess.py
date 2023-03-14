from random import randint

def guessNumber(num):
    guess_num = int(input("Guess the number: "))

    if num > guess_num:
        print("Too Low !!")
        if num % guess_num == 0:
            print("Hint: Number is divisible by your guess.")
        elif (guess_num < num / 2):
            print("Hint: your guess is less than the half of number.")
        else:
            print("Hint: Your guess is less than the number. Try near", round(num / 10) * 10)
        return guessNumber(num)
    
    elif num < guess_num:
        print("Too High !!")
        if num % guess_num == 0:
            print("Hint: Number is divisible by your guess.")
        elif guess_num > num * 2:
            print("Hint: Your guess is more than the double of number.")
        else:
            print("Hint: Your guess is more than the number. Try near", round(num / 10) * 10)
        return guessNumber(num)
    
    else:
        return num, guess_num


r_num = randint(1, 100)
result = guessNumber(r_num)
print("Success !!", result)

