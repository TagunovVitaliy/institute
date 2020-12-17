import unittest
from ..Controllers.Controller import *
from .Storage import *


class TestCreateTeacher(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_create_teacher(self):
        new = Teacher(1, "Ivan Ivanov", TeacherType.part_time_teacher, [])
        idx = self.logic.add_teacher(new)
        self.assertEqual(idx, new.get_teacher_id())
        self.assertEqual(self.logic.interface.get_teacher_by_id(idx), new)

        existing = self.logic.interface.get_teacher_by_id(0)
        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.add_teacher(existing)
            self.assertEqual(str(exception_msg), f"Add: Teacher with id {existing.get_teacher_id()} "
                                                 f"already in Storage")

    def test_teacher_could_not_be_created_with_type_full_time(self):
        with self.assertRaises(ValueError) as exception_msg:
            new = Teacher(2, "Ivan Ivanov", TeacherType.full_time_teacher, [])
            idx = self.logic.add_teacher(new)
            self.assertEqual(str(exception_msg), f"Create: Full time teachers cannot be created, id={idx}")


    def test_delete_teacher(self):
        delete_id = 0
        existing = self.logic.interface.get_teacher_by_id(delete_id)

        idx = self.logic.del_teacher(delete_id)
        self.assertEqual(idx, existing.get_teacher_id())

        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.del_teacher(delete_id)
            self.assertEqual(str(exception_msg), f"Delete: No Teacher by this id {delete_id} in Storage")

if __name__ == '__main__':
    unittest.main()
