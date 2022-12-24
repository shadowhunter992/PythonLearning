def guessinggame():
    print("Let's play a guessing game!")
    import random
    randomNumber = random.randint(1,100)
    number_guess = int(input("Enter your guess!"))
    while number_guess != randomNumber:

        if number_guess > randomNumber:
            print("The number is smaller than your guess.")
            number_guess = int(input("Enter your guess!"))

        elif number_guess < randomNumber:
            print("The number is larger than your guess.")
            number_guess = int(input("Enter your guess!"))


    if number_guess == randomNumber:
        print("Bravo, you've guessed it!")

        guessinggame()

guessinggame()

#še naloga FizzBuzz 1-100
#vsaka številka ki je deljiva z 3 je Fizz, vsaka ki z 5 je buzz, vsaka ki je oboje FizzBuzz
#združi vse naloge v main2
#switch case poglej (match)

