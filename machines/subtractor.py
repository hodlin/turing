#!/home/dmytro/Envs/turing/bin python3.5
from .algorithm import states_table
from .turing_machine import TuringMachine


class Subtractor(TuringMachine):
    """
    Realization of Turing machine for subtraction two integer numbers
    """
    _state_table = states_table

    @staticmethod
    def is_valid(minuend, take):
        """
        Validates the 'minuend' to be greater than 'take'
        :return bool: True if values are valid, False otherwise
        """
        return minuend >= take

    def __init__(self, minuend, take):

        if not Subtractor.is_valid(minuend, take):
            raise ValueError("Minuend (entered: '{}') should be greater than take (entered: '{}')"
                             .format(minuend, take))

        super().__init__()

        self._tape = ['blank'] + Subtractor.to_unary(minuend) + \
                     ['blank'] + Subtractor.to_unary(take) + \
                     ['blank']

    def evaluate(self):
        """
        Performing calculation and returning decimal result
        :return: decimal result of calculation
        """
        self._run()
        result = [value for value in self._tape if value != 'blank']
        return Subtractor.to_decimal(result), self._steps

    def _run(self):
        """
        Execution of an algorithm
        :return: unary result of subtraction
        """
        state = 'q0'   # initial state

        while True:
            self._steps += 1
            current_value = self._tape[self._head]
            instructions = Subtractor._state_table[state][current_value]
            self._tape[self._head] = instructions['write']
            self._head += instructions['move']
            state = instructions['next']
            print(self._tape)
            print(self._head, state)
            if state == 'stop':
                break


if __name__ == '__main__':
    pass
