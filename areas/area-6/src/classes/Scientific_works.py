from datetime import *
import datetime
from .Stages import Stage
from .Enums import ScientificWorkType

class ScientificWork:
    def __init__(self, id, name, point, term_date, actual_date, type, stages):
        self.id = id
        self.name = name
        self.point = point
        self.term_date = term_date
        self.actual_date = actual_date
        self.type = type
        if not (
                isinstance(id, int) and isinstance(name, str)
                and isinstance(point, int)
                and isinstance(term_date, datetime.date)
        ):
            raise TypeError
        self.stages = stages

    def get_s_work_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_point(self):
        return self.point

    def get_term_date(self):
        return self.term_date

    def get_actual_date(self):
        return self.actual_date

    def get_type(self) -> ScientificWorkType:
        return self.type

    def get_stages(self):
        return self.stages

    def set_name(self, name):
        self.name = name

    def set_points(self, point):
        self.point = point

    def set_type(self, type):
        self.type = type

    def set_term_date(self, term_date):
        self.term_date = term_date

    def set_actual_date(self, actual_date):
        self.actual_date = actual_date

    def set_stages(self, stages):
        self.stages = stages

    def add_stage(self, stage: Stage):
        self.stages.append(stage)

    def check_deadline(self):
        if self.term_date > date.today():
            return True
        else:
            return False

 #   def get_statistic(self):