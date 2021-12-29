"""I this we are solving the quantity
    measurement problem using TDD approach"""
from QuantityMeasurmentException import QuantityMeasurementException


class QuantityMeasurementProblem:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    @staticmethod
    def feat_fun():
        FEET = 3
        return FEET

    @staticmethod
    def yard_fun():
        YARD = 1
        return YARD

    def __eq__(self, other):
        yard = QuantityMeasurementProblem.yard_fun()
        feat = QuantityMeasurementProblem.feat_fun()
        if other.length is None:
            raise QuantityMeasurementException('Null')
        elif self.unit == other.unit or other.length == self.length:
            print("Values Not Equal")
            return True
        elif type(self.length) != type(other.length):
            raise QuantityMeasurementException('Type Not Equal')
        elif self.length != other.length:
            raise QuantityMeasurementException('References are not Equal')
        elif other.length > 0:
            return other.length / 3
        else:
            raise QuantityMeasurementException("Invalid")
