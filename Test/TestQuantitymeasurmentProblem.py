import pytest
from main import QuantityMeasurementProblem
from QuantityMeasurmentException import QuantityMeasurementException


class TestQuantitymeasurmentProblem:
    @pytest.mark.parametrize('length1, unit1, length2, unit2', [0, "feat", 0, "feat"])
    def test_zero_value_check(self, length1, unit1, length2, unit2):
        quantity1 = QuantityMeasurementProblem(length1, unit1)
        quantity2 = QuantityMeasurementProblem(length2, unit2)
        assert quantity1 == quantity2

    @pytest.mark.parametrize('length1, unit1, length2, unit2', [None, "feet", None, "feet"])
    def test_null_reference_check(self, length1, unit1, length2, unit2):
        quantity1 = QuantityMeasurementProblem(length1, unit1)
        quantity2 = QuantityMeasurementProblem(length2, unit2)
        with pytest.raises(QuantityMeasurementException) as exe:
            quantity1 == quantity2
        assert exe.value.message == 'Type Not Equal'

    @pytest.mark.parametrize('length1, unit1, length2, unit2', [0, 'feet', 2, 'yard'])
    def test_reference_check(self, length1, unit1, length2, unit2):
        quantity1 = QuantityMeasurementProblem(length1, unit1)
        quantity2 = QuantityMeasurementProblem(length2, unit2)
        with pytest.raises(QuantityMeasurementException) as exe:
            quantity1 == quantity2
        assert exe.value.message == 'References are not Equal'

    @pytest.mark.parametrize('length1, unit1 , length2, unit2', [0, 'feet', "hello", 'yard'])
    def test_type_check(self, length1, unit1, length2, unit2):
        quantity1 = QuantityMeasurementProblem(length1, unit1)
        quantity2 = QuantityMeasurementProblem(length2, unit2)
        with pytest.raises(QuantityMeasurementException) as exe:
            quantity1 == quantity2
        assert exe.value.message == 'Type Not Equal'

    @pytest.mark.parametrize('length1 ,unit1, length2, unit2', [0, 'feet', 0, 'yard'])
    def test_value_check(self, length1, unit1, length2, unit2):
        quantity1 = QuantityMeasurementProblem(length1, unit1)
        quantity2 = QuantityMeasurementProblem(length2, unit2)
        with pytest.raises(QuantityMeasurementException) as exe:
            quantity1 == quantity2
        assert exe.value.message == 'Values Not Equal'
