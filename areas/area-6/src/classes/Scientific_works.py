from datetime import *
import datetime
from .Stages import Stage
from .Enums import ScientificWorkType

class ScientificWork:
    def __init__(self, id, name, points, term, type, stages):
        self.id = id
        self.name = name
        self.points = points
        if term < date.today():
            raise ValueError()
        self.term = term
        self.type = type
        if not (
                isinstance(id, int) and isinstance(name, str)
                and isinstance(points, list)
                and isinstance(term, datetime.date)
        ):
            raise TypeError
        self.stages = stages

    def get_s_work_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def get_term(self):
        return self.term

    def get_type(self) -> ScientificWorkType:
        return self.type

    def get_stages(self):
        return self.stages

    def set_name(self, name):
        self.name = name

    def set_points(self, points):
        self.points = points

    def set_type(self, type):
        self.type = type

    def set_term(self, term):
        self.term = term

    def set_stages(self, stages):
        self.stages = stages

    def add_stage(self, stage: Stage):
        self.stages.append(stage)

    def check_deadline(self):
        if self.term > date.today():
            return True
        else:
            return False

 #   def get_statistic(self):