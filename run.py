#!/home/dmytro/Envs/turing/bin python3.5
from subtractor import Subtractor


if __name__ == '__main__':

    print('Welcome to Turing subtraction machine!')
    print('Please provide data that prompted to perform calculations on two integer numbers')

    try:
        minuend = int(input('Enter minuend: '))
        take = int(input('Enter take: '))
        Sub = Subtractor(minuend, take)
        result, steps = Sub.evaluate()
        print('Result is: {} ({} steps was taken to perform calculation)'.format(result, steps))
    except ValueError as e:
        print('One of two possible errors occurred:')
        print('whether you specified not an integer values or you entered minuend greater than take.')
        print(e)
        print('Please be careful next time!')
