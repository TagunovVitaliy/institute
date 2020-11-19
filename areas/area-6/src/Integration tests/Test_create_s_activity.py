import unittest
from ..Controllers.Controller import *
from .Storage import *
import copy


class TestCreateTeacher(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_create_s_activity(self):
        new = ScientificActivity(1, "Robotic-Engineering", [])
        idx = self.logic.add_s_activity(new)
        self.assertEqual(idx, new.get_s_activity_id())
        self.assertEqual(self.logic.interface.get_s_activity_by_id(idx), new)

        existing = self.logic.interface.get_s_activity_by_id(0)
        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.add_s_activity(existing)
            self.assertEqual(str(exception_msg), f"Add: Scientific Activity with id {existing.get_s_activity_id()} "
                                                 f"already in Storage")

    def test_delete_s_activity(self):
        delete_id = 0
        existing = self.logic.interface.get_s_activity_by_id(delete_id)

        idx = self.logic.del_s_activity(delete_id)
        self.assertEqual(idx, existing.get_s_activity_id())

        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.del_s_activity(delete_id)
            self.assertEqual(str(exception_msg), f"Delete: No Scientific Activity by this id {delete_id} in Storage")


if __name__ == '__main__':
    unittest.main()

