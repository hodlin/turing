#!/home/dmytro/Envs/turing/bin python3.5
from subtractor import Subtractor


if __name__ == '__main__':

    minuend = int(input('Enter minuend: '))
    take = int(input('Enter take: '))

    Sub = Subtractor(minuend, take)
    result, steps = Sub.evaluate()

    print('Result is: {} ({} steps was taken to calculate)'.format(result, steps))
