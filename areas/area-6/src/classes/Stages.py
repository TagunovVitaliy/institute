from datetime import *
import datetime

class Stage:

    def __init__(self, id, description):
        self.stage_id = id
        self.description = description
        if not (
                isinstance(id, int) and
                isinstance(description, str)
        ):
            raise TypeError

    def get_stage_id(self):
        return self.stage_id

    def set_number(self, number):
        self.number = number