import unittest
from ..Controllers.Controller import *
from .Storage import *
import copy


class TestUpdateTeacher(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_update_teacher(self):
        update_id = 0
        update_data = {"name": "Ivan Ivanov",
                       "role": TeacherType.part_time_teacher,
                       "scientific_activities": []}
        existing = copy.deepcopy(self.logic.interface.get_teacher_by_id(update_id))
        existing.set_name(update_data["name"])
        existing.set_role(update_data["role"])
        existing.set_scientific_activities(update_data["scientific_activities"])

        idx = self.logic.upd_teacher(update_id, update_data)
        self.assertEqual(idx, existing.get_teacher_id())
 ##       new_teacher = self.logic.interface.get_teacher_by_id(idx)
 ##       self.assertEqual(new_teacher, existing)

    def test_add_s_activity_to_teacher(self):
        teacher_id = 0
        new = ScientificActivity(1, "Security", [])
        existing = copy.deepcopy(self.logic.interface.get_teacher_by_id(0))
        self.assertTrue(existing.add_activity(new))

        idx = self.logic.add_s_activity_to_teacher(teacher_id, new)
        self.assertEqual(idx, teacher_id)
#        self.assertEqual(self.logic.interface.get_teacher_by_id(idx), existing)

if __name__ == '__main__':
    unittest.main()
