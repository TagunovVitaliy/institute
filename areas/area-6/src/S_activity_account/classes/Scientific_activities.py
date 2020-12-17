from classes.Teachers import Teacher
from typing import List

class ScientificActivity:
    def __init__(self, id: int, name: str, description: str, teachers: List[Teacher] = None):
        self.s_activity_id = id
        self.s_activity_name = name
        self.description = description
        if not (
                isinstance(name, str) and
                isinstance(id, int) and
                isinstance(description, str)
        ):
            raise TypeError
        self.teachers = teachers[:] if teachers else []

    def get_s_activity_id(self):
        return self.s_activity_id

    def get_name(self):
        return self.s_activity_name

    def get_description(self):
        return self.description

    def get_teachers(self) -> List[Teacher]:
        return self.teachers

    def set_s_activity_id(self, id: int):
        self.s_activity_id = id

    def set_name(self, name: str):
        self.s_activity_name = name

    def set_description(self, description: str):
        self.description = description

    def set_teachers(self, teachers: List[Teacher]):
        self.teachers = teachers[:]

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)
        return True

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__