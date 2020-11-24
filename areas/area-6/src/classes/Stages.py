from datetime import *
import datetime

class Stage:

    def __init__(self, id: int, description: str):
        self.stage_id = id
        self.description = description
        if not (
                isinstance(id, int) and
                isinstance(description, str)
        ):
            raise TypeError

    def get_stage_id(self):
        return self.stage_id

    def set_stage_id(self, id):
        self.stage_id = id