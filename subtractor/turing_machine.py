import abc


class TuringMachine(metaclass=abc.ABCMeta):
    """
    Abstract Turing machine
    """

    _state_table = {}

    @staticmethod
    def to_unary(decimal):
        """
        Converts decimal number to unary
        :param decimal: decimal number
        :return: list of '1'
        """
        return [1 for _ in range(decimal)]

    @staticmethod
    def to_decimal(unary):
        """
        Converts unary number to decimal
        :param unary: list of '1'
        :return: decimal number
        """
        return sum(unary)

    @abc.abstractmethod
    def __init__(self):
        """
        Initializing empty tape, setting head position to 1
        and steps counter to 0
        """
        self._tape = []
        self._head = 1
        self._steps = 0

    @abc.abstractmethod
    def evaluate(self):
        pass

    @abc.abstractmethod
    def _run(self):
        pass
