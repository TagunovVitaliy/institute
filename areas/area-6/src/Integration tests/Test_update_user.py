import unittest
from ..Controllers.Controller import *
from .Storage import *
import copy


class TestUpdateUser(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_update_user(self):
        update_id = 0
        update_data = {"name": "Ivan Ivanov",
                       "individual_plans": []}
        existing = copy.deepcopy(self.logic.interface.get_user_by_id(update_id))
        existing.set_name(update_data["name"])
        existing.set_i_plans(update_data["individual_plans"])

        idx = self.logic.upd_user(update_id, update_data)
        self.assertEqual(idx, existing.get_user_id())

    def test_add_i_plan_to_user(self):
        user_id = 0
        new = IndividualPlan(1, "Security", date(300, 1, 1), [])
        existing = copy.deepcopy(self.logic.interface.get_user_by_id(0))
        self.assertTrue(existing.add_i_plan(new))

        idx = self.logic.add_i_plan_to_user(user_id, new)
        self.assertEqual(idx, user_id)


if __name__ == '__main__':
    unittest.main()
