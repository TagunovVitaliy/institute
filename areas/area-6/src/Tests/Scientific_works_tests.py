import unittest
from datetime import *
from ..classes.Scientific_works import ScientificWork

class Test_ScientificWork(unittest.TestCase):

    def test_scientific_work_could_not_be_created_with_invalid_type(self):
        self.assertRaises(TypeError, ScientificWork, 1.1, 1, "", 1, 1)

    def test_scientific_work_created_with_right_attributes(self):
        s_work = ScientificWork(1,"",1,date(3000, 10, 7),"")
        assert s_work.get_id() == 1
        assert s_work.get_name() == ""
        assert s_work.get_points() == 1
        assert s_work.get_term() == date(3000, 10, 7)
        assert s_work.get_type() == ""


if __name__ == '__main__':
    unittest.main()
