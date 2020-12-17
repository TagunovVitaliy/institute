import unittest
#from ..Controllers.Create_teacher import *
from ..Controllers.Controller import *
from .Storage import *
import copy


class TestCreateIndividualPlan(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_create_i_plan(self):
        new = IndividualPlan(1, "IdPlan1", date(2020, 10, 10), [])
        idx = self.logic.add_i_plan(new)
        self.assertEqual(idx, new.get_i_plan_id())
        self.assertEqual(self.logic.interface.get_individual_plan_by_id(idx), new)

        existing = self.logic.interface.get_individual_plan_by_id(0)
        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.add_i_plan(existing)
            self.assertEqual(str(exception_msg), f"Add: Individual plan with id {existing.get_i_plan_id()} "
                                                 f"already in Storage")

    def test_delete_i_plan(self):
        delete_id = 0
        existing = self.logic.interface.get_individual_plan_by_id(delete_id)

        idx = self.logic.del_i_plan(delete_id)
        self.assertEqual(idx, existing.get_i_plan_id())

        with self.assertRaises(RuntimeError) as exception_msg:
            self.logic.del_i_plan(delete_id)
            self.assertEqual(str(exception_msg), f"Delete: No Individual plan by this id {delete_id} in Storage")

if __name__ == '__main__':
    unittest.main()
