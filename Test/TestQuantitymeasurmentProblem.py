import pytest
from main import QuantityMeasurementProblem
from QuantityMeasurmentException import QuantityMeasurementException


class TestQuantitymeasurmentProblem:
    @pytest.fixture()
    def _test_quantity_measurment(self):
        self.length = QuantityMeasurementProblem()

    @staticmethod
    def test_null_check():
        with pytest.raises(QuantityMeasurementException) as exe:
            length1 = QuantityMeasurementProblem(0)
            length2 = QuantityMeasurementProblem(None)
            length1 == length2
        assert exe.value.message == 'Null'

    