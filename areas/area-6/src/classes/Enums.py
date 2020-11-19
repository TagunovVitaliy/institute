from enum import Enum

class TeacherType(Enum):
    none = 0
    scientific_director = 1
    simple_teacher = 2

class ScientificWorkType(Enum):
    none = 0
    seminar = 1
    publication = 2