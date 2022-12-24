def naloga():
    operation = input('''
            Please type the option you would like to explore.
            Calc for calculator
            Guess for guessing game
            Fizz for FizzBuzz
            MinMax for getting minimum and maximum numbers of a set
            Triangle for triangle generation
            ARLTP for All roads lead to philosophy game    
                ''')

    def newfunc():
        operation = input('''
    Please type the math operation you would like to perform
    + for adition
    - for substraction
    * for multiplication
    / for division
        ''')

        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

        if operation == '+':
            print('{} + {} = ' .format(number_1, number_2))
            print(number_1 + number_2)

        elif operation == '-':
            print('{} - {} = ' .format(number_1, number_2))
            print(number_1 - number_2)

        elif operation == '*':
            print('{} * {} = ' .format(number_1, number_2))
            print(number_1 * number_2)

        elif operation == '/':
            print('{} / {} = ' .format(number_1, number_2))
            print(number_1 / number_2)

        else:
            print('You have not selected a valid operator, please run the program again')
        again()


    def again():
        calc_again = input('''
        Do you want to perform another calculation?
        Type Y for YES or N for NO
        ''')

        if calc_again.upper() == 'Y':
            newfunc()

        elif calc_again.upper() == 'N':
            print('See you')

        else:
            again()

    def guessinggame():
        print("Let's play a guessing game!")
        import random
        randomNumber = random.randint(1, 100)
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

    def fizzbuzz():
        print("Please select the maximum number for list range")
        selectnumber = int(input())
        range_1 = range(1, selectnumber + 1)
        thelist = list(range_1)


        for i in range_1:
            if thelist[i-1] % 3 == 0 and thelist[i-1] % 5 == 0:
                thelist[i-1] = "FizzBuzz"
            elif thelist[i-1] % 3 == 0:
                thelist[i-1] = "Fizz"
            elif thelist[i-1] % 5 == 0:
                thelist[i-1] = "Buzz"
        print(thelist)

    def minmax():
        print("Please input a set of numbers.")
        userinput = input("Enter space seperated integers: ")
        userset = set(int(item) for item in userinput.split())
        print(min(userset))
        print(max(userset))

    def triangle():
        rows = int(input("Enter number of rows: "))

        for i in range(rows):
            for j in range(i + 1):
                print("* ", end="")
            print("\n")



    if operation == "Calc":
        newfunc()

    elif operation == "Guess":
        guessinggame()

    elif operation == "Fizz":
        fizzbuzz()

    elif operation == "MinMax":
        minmax()

    elif operation == "Triangle":
        triangle()


naloga()