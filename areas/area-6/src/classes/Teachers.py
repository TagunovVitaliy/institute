from .Scientific_activities import ScientificActivity
from .Enums import TeacherType

class Teacher:
    def __init__(self, id: int, name: str, role: TeacherType, **kwargs):
        self.teacher_id = id
        self.name = name
        self.role = role
        if not (
                isinstance(name, str) and
                isinstance(id, int)
        ):
            raise TypeError
        if 'scientific_activities' in kwargs:
            self.scientific_activities = kwargs['scientific_activities']

    def get_teacher_id(self):
        return self.teacher_id

    def get_name(self):
        return self.name

    def get_role(self) -> TeacherType:
        return self.role

    def get_scientific_activities(self):
        return self.scientific_activities

    def set_name(self, name):
        self.name = name

    def set_role(self, role):
        self.role = role

    def set_scientific_activities(self, scientific_activities):
        self.scientific_activities = scientific_activities

    def add_activity(self, s_activity: ScientificActivity):
        self.scientific_activities.append(s_activity)