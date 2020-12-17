import unittest
from ..Controllers.Controller import *
from .Storage import *
import copy


class TestUpdateScientificWork(unittest.TestCase):
    interface = ReadyStorage()
    logic = Controller(interface)

    def test_constructor(self):
        self.assertEqual(self.logic.interface, self.interface)

    def test_update_s_work(self):
        update_id = 0
        update_data = {"name": "Developing",
                       "point": 4,
                       "term_date": date(3000, 11, 11),
                       "actual_date": date(3000, 11, 11),
                       "type": ScientificWorkType.publication,
                       "stages": [],
                       "status": ScientificWorkStatus.done
                       }
        existing = copy.deepcopy(self.logic.interface.get_s_work_by_id(update_id))
        existing.set_name(update_data["name"])
        existing.set_points(update_data["point"])
        existing.set_term_date(update_data["term_date"])
        existing.set_actual_date(update_data["actual_date"])
        existing.set_type(update_data["type"])
        existing.set_stages(update_data["stages"])
        existing.set_status(update_data["status"])

        idx = self.logic.upd_s_work(update_id, update_data)
        self.assertEqual(idx, existing.get_s_work_id())
        updated_s_work = self.logic.interface.get_s_work_by_id(idx)
        new_date = updated_s_work.get_actual_date()
        self.assertEqual(new_date, date.today())

if __name__ == '__main__':
    unittest.main()
