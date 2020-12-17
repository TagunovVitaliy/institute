import unittest
from ..Controllers.Controller import *
from .Storage import *


class TestCreateScientificWork(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_create_s_work(self):
        new = ScientificWork(1, "Testing", 5, date(3000, 10, 10), date(3000, 10, 10), ScientificWorkType.seminar, [])
        idx = self.logic.add_s_work(new)
        self.assertEqual(idx, new.get_s_work_id())
        self.assertEqual(self.logic.interface.get_s_work_by_id(idx), new)

        existing = self.logic.interface.get_s_work_by_id(0)
        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.add_s_work(existing)
            self.assertEqual(str(exception_msg), f"Add: Scientific work with id {existing.get_s_work_id()} "
                                                 f"already in Storage")

    def test_delete_s_work(self):
        delete_id = 0
        existing = self.logic.interface.get_s_work_by_id(delete_id)

        idx = self.logic.del_s_work(delete_id)
        self.assertEqual(idx, existing.get_s_work_id())

        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.del_s_work(delete_id)
            self.assertEqual(str(exception_msg), f"Delete: No Scientific work by this id {delete_id} in Storage")


if __name__ == '__main__':
    unittest.main()
