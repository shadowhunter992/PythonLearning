def naloga():
    operation = input('''
            Please type the option you would like to explore.
            1 for calculator
            2 for guessing game
            3 for FizzBuzz
            4 for getting minimum and maximum numbers of a set
            5 for triangle generation
            6 for All roads lead to philosophy game    
                ''')

    def calculator():
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

            again()

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
        [print(x) for x in thelist]

        again()

    def minmax():
        print("Please input a set of numbers.")
        userinput = input("Enter space seperated integers: ")
        userset = list(int(item) for item in userinput.split())
        def minimum1(userset):
            current_min = userset[0]    #1
            for num in userset:
                if num < current_min:
                    current_min = num
            return current_min
        def maximum1(userset):
            current_max = userset[0]
            for num in userset:
                if num > current_max:
                    current_max = num
            return current_max

        print(minimum1(userset))
        print(maximum1(userset))

        again()

    def triangle():
        triangle_height = int(input('Enter triangle height:\n'))
        print('')
        for x in range(1, triangle_height + 1):
            print(x * "*")
        again()

    def again():
        nal_again = input('''
            Do you wish to select another option from the menu?
            Type Y for YES or N for NO
            ''')

        if nal_again.upper() == 'Y':
            naloga()

        elif nal_again.upper() == 'N':
            print('See you')

        else:
            again()


    if operation == "1":
        calculator()

    elif operation == "2":
        guessinggame()

    elif operation == "3":
        fizzbuzz()

    elif operation == "4":
        minmax()

    elif operation == "5":
        triangle()


naloga()