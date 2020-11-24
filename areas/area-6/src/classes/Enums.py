from enum import Enum

class TeacherType(Enum):
    none = 0
    part_time_teacher = 1
    full_time_teacher = 2

class ScientificWorkType(Enum):
    none = 0
    seminar = 1
    publication = 2