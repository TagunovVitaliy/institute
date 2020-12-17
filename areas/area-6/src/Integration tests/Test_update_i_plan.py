import unittest
from ..Controllers.Controller import *
from .Storage import *
import copy


class TestUpdateIndividualPlan(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_update_i_plan(self):
        update_id = 0
        update_data = {"name": "New_i_plan",
                       "start_date": date(2020, 10, 10),
                       "scientific_works": []}
        existing = copy.deepcopy(self.logic.interface.get_individual_plan_by_id(update_id))
        existing.set_name(update_data["name"]),
        existing.set_start_date(update_data["name"]),
        existing.set_scientific_works(update_data["scientific_works"])

        idx = self.logic.upd_i_plan(update_id, update_data)
        self.assertEqual(idx, existing.get_i_plan_id())

    def test_add_s_work_to_i_plan(self):
        i_plan_id = 0
        new = ScientificWork(1, "Testing", 5, date(3000, 10, 10), date(3000, 10, 10), ScientificWorkType.seminar, [])
        existing = copy.deepcopy(self.logic.interface.get_individual_plan_by_id(0))
        self.assertTrue(existing.add_scientific_work(new))

        idx = self.logic.add_s_work_to_i_plan(i_plan_id, new)
        self.assertEqual(idx, i_plan_id)


if __name__ == '__main__':
    unittest.main()
