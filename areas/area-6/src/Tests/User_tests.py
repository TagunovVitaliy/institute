import unittest
from ..classes.Users import User
from ..classes.Individual_plans import IndividualPlan

class Test_User(unittest.TestCase):

    def test_user_created_with_right_attributes(self):
        user = User(1,"")
        assert user.get_user_id()==1
        assert user.get_name()==""

    def test_user_could_not_be_created_with_invalid_type(self):
        self.assertRaises(TypeError, User, 1.1, 1)

    def test_set_individual_plan(self):
        user = User(1,"")
        i_plan = IndividualPlan("")
        user.set_individual_plan(i_plan)
        assert user.get_individual_plan() == i_plan

if __name__ == '__main__':
    unittest.main()
