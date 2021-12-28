import pytest
from main import QuantityMeasurementProblem
from QuantityMeasurmentException import QuantityMeasurementException


class TestQuantitymeasurmentProblem:
    @pytest.fixture()
    def test_quantity_measurment(self):
        self.length = QuantityMeasurementProblem()

    @staticmethod
    def test_null_check():
        with pytest.raises(QuantityMeasurementException) as exe:
            length1 = QuantityMeasurementProblem(0)
            length2 = QuantityMeasurementProblem(None)
            length1 == length2
        assert exe.value.message == 'Null'

    @staticmethod
    def test_reference_check():
        with pytest.raises(QuantityMeasurementException) as exe:
            ref1 = QuantityMeasurementProblem(1)
            ref2 = QuantityMeasurementProblem(2)
            ref1 != ref2
        assert exe.value.message == 'References are not Equal'

    @staticmethod
    def test_type_check():
        with pytest.raises(QuantityMeasurementException) as exe:
            type1 = QuantityMeasurementProblem(1)
            type2 = QuantityMeasurementProblem(1)
            type1 != type2
        assert exe.value.message == 'Type Not Equal'
