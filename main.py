"""I this we are solving the quantity
    measurement problem using TDD approach"""
from QuantityMeasurmentException import QuantityMeasurementException


class QuantityMeasurementProblem:
    def __init__(self, length):
        self.length = length

    def __eq__(self, other):
        if other.length is None:
            raise QuantityMeasurementException('Null')
        elif other.length > 0:
            return other.length * 12
        else:
            raise QuantityMeasurementException('Length is Invalid')

