input_number = int(input('Enter number from 1 to 100: '))
if (input_number % 5 == 0) and (input_number % 3) == 0:
    print("FizzBuzz")
elif input_number % 5 == 0:
    print('Buzz')
elif (input_number % 3) == 0:
    print('Fizz')
else:
    pass
