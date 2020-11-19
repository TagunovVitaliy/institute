import unittest
from ..classes.Individual_plans import IndividualPlan

class Test_IndividualPlan(unittest.TestCase):

    def test_individual_plan_created_with_right_attributes(self):
        i_plan = IndividualPlan("")
        assert i_plan.get_name() == ""

    def test_individual_plan_could_not_be_created_with_invalid_type(self):
        self.assertRaises(TypeError, IndividualPlan, 1.1)


if __name__ == '__main__':
    unittest.main()
