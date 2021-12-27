import pytest
from main import QuantityMeasurementProblem
from QuantityMeasurmentException import QuantityMeasurementException


class TestQuantitymeasurmentProblem:
    @staticmethod
    @pytest.fixture()
    def test_zero_feet():
        expected = True
        actual = QuantityMeasurementProblem.quantity_measurement(0, 0)
        assert actual == expected
        