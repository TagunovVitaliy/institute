import abc
from datetime import date
from typing import List

from classes.Teachers import Teacher
from classes.Scientific_activities import ScientificActivity
from classes.Users import User

class Storage(abc.ABC):

    @staticmethod
    def create_s_activity(**kwargs) -> int:
        pass

    @staticmethod
    def create_teacher(**kwargs) -> int:
        pass

    @staticmethod
    def create_user(**kwargs) -> int:
        pass

    @staticmethod
    def get_s_activity_by_id(s_activity_id: int) -> ScientificActivity:
        pass

    @staticmethod
    def get_teacher_by_id(teacher_id: int) -> Teacher:
        pass

    @staticmethod
    def get_teachers_by_s_activity(s_activity_id: int) -> List[Teacher]:
        pass

    @staticmethod
    def get_s_activities() -> List[ScientificActivity]:
        pass

    @staticmethod
    def get_full_s_activities() -> List[ScientificActivity]:
        pass