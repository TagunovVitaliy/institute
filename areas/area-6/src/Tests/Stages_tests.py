import unittest
from datetime import *
from ..classes.Stages import Stage

class Test_Stage(unittest.TestCase):

    def test_scientific_work_could_not_be_created_with_invalid_type(self):
        self.assertRaises(TypeError, Stage, 1.1, "", 1)

    def test_stage_created_with_right_attributes(self):
        stage = Stage(1,1,date(3000, 10, 7))
        assert stage.get_number() == 1
        assert stage.get_points() == 1
        assert stage.get_term() == date(3000, 10, 7)

    def test_deadline_is_not_expired(self):
        stage = Stage(1,1,date(3000, 10, 7))
        self.assertTrue(stage.check_deadline())

    def test_deadline_is_expired(self):
        stage1 = Stage(1,1,date(2000, 10, 7))
        self.assertFalse(stage1.check_deadline())

if __name__ == '__main__':
    unittest.main()
