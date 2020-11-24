import abc
from ..classes.Teachers import *
from ..classes.Scientific_activities import *
from ..classes.Users import *
from ..classes.Individual_plans import *
from ..classes.Scientific_works import *
from ..classes.Stages import *

class Interface:

    def __init__(self):
        pass

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__

    def create_teacher(self, teacher: Teacher) -> int:
        pass

    def create_scientific_activity(self, scientific_activity: ScientificActivity) -> int:
        pass

    def create_user(self, user: User) -> int:
        pass

    def create_individual_plan(self, individual_plan: IndividualPlan) -> int:
        pass

    def create_scientific_work(self, scientific_work: ScientificWork) -> int:
        pass

    def create_stage(self, stage: Stage) -> int:
        pass

    def get_teacher_by_id(self, teacher_id: int) -> Teacher:
        pass

    def get_s_activity_by_id(self, s_activity_id: int) -> ScientificActivity:
        pass

    def get_user_by_id(self, user_id: int) -> User:
        pass

    def get_individual_plan_by_id(self, i_plan_id: int) -> IndividualPlan:
        pass

    def get_s_work_by_id(self, s_work_id: int) -> ScientificWork:
        pass

    def upd_teacher(self, teacher: Teacher) -> int:
        pass

    def upd_s_activity(self, scientific_activity: ScientificActivity) -> int:
        pass

    def upd_user(self, user: User) -> int:
        pass

    def upd_i_plan(self, individual_plan: IndividualPlan) -> int:
        pass

    def upd_s_work(self, scientific_work: ScientificWork) -> int:
        pass

    def del_teacher_by_id(self, teacher_id: int) -> int:
        pass

    def del_s_activity_by_id(self, s_activity_id: int) -> int:
        pass

    def del_user_by_id(self, user_id: int) -> int:
        pass

    def del_i_plan_by_id(self, i_plan_id: int) -> int:
        pass

    def del_s_work_by_id(self, s_work_id: int) -> int:
        pass

