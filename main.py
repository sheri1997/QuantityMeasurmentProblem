"""I this we are solving the quantity
    measurement problem using TDD approach"""
from QuantityMeasurmentException import QuantityMeasurementException


class QuantityMeasurementProblem:
    def __init__(self, length):
        self.length = length

    @staticmethod
    def length_equal(feat, inches):
        if feat == 1 and inches == 12:
            return True
        elif feat == 0 and inches == 0:
            return True
        else:
            return False

    @staticmethod
    def quantity_measurement(feat, inches):
        equal = QuantityMeasurementProblem.length_equal(feat, inches)
        if equal:
            print("Equal Length")
        else:
            raise QuantityMeasurementException("Not Equal")


length = QuantityMeasurementProblem.quantity_measurement(1, 12)
print(length)

