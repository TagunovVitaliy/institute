import unittest
from ..Controllers.Controller import *
from .Storage import *


class TestCreateUser(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_create_user(self):
        new = User(1, "Ivan Ivanov", [])
        idx = self.logic.add_user(new)
        self.assertEqual(idx, new.get_user_id())
        self.assertEqual(self.logic.interface.get_user_by_id(idx), new)

        existing = self.logic.interface.get_user_by_id(0)
        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.add_user(existing)
            self.assertEqual(str(exception_msg), f"Add: User with id {existing.get_user_id()} "
                                                 f"already in Storage")

    def test_delete_user(self):
        delete_id = 0
        existing = self.logic.interface.get_user_by_id(delete_id)

        idx = self.logic.del_user(delete_id)
        self.assertEqual(idx, existing.get_user_id())

        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.del_user(delete_id)
            self.assertEqual(str(exception_msg), f"Delete: No User by this id {delete_id} in Storage")

if __name__ == '__main__':
    unittest.main()
