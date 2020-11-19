import unittest
from..classes.Scientific_activities import ScientificActivity

class Test_ScientificActivity(unittest.TestCase):

    def test_scientific_activity_created_with_right_attributes(self):
        s_activity = ScientificActivity("name")
        assert s_activity.get_name()=="name"

    def test_scientific_activity_could_not_be_created_with_invalid_type(self):
        self.assertRaises(TypeError, ScientificActivity, 1)



if __name__ == '__main__':
    unittest.main()
