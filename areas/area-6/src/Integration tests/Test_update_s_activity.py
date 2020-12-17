import unittest
from ..Controllers.Controller import *
from .Storage import *
import copy

class TestUpdateScientificActivty(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_update_s_activity(self):
        update_id = 0
        update_data = {"name": "Scientific research",
                       "users": []}
        existing = copy.deepcopy(self.logic.interface.get_s_activity_by_id(update_id))
        existing.set_name(update_data["name"])
        existing.set_users(update_data["users"])

        idx = self.logic.upd_s_activity(update_id, update_data)
        self.assertEqual(idx, existing.get_s_activity_id())
 ##       new_teacher = self.logic.interface.get_teacher_by_id(idx)
 ##       self.assertEqual(new_teacher, existing)

    def test_add_user_to_s_activity(self):
        s_activity_id = 0
        new = User(1, "Vitaliy Tagunov", [])
        existing = copy.deepcopy(self.logic.interface.get_s_activity_by_id(0))
        self.assertTrue(existing.add_user(new))

        idx = self.logic.add_user_to_s_activity(s_activity_id, new)
        self.assertEqual(idx, s_activity_id)

if __name__ == '__main__':
    unittest.main()
