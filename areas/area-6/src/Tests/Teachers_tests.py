import unittest
from..classes.Teachers import Teacher

class Test_Teacher(unittest.TestCase):

    def test_user_created_with_right_attributes(self):
        teacher = Teacher("Vitalik","Scientific director")
        assert teacher.get_name() == "Vitalik"
        assert teacher.get_role() == "Scientific director"

    def test_teacher_could_not_be_created_with_invalid_type(self):
        self.assertRaises(TypeError, Teacher, 1, 1)

if __name__ == '__main__':
    unittest.main()