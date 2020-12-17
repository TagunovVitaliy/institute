from ..Storage.interfaces import *

class Controller:

    def __init__(self, interface: Interface):
        self.interface = interface

    def add_teacher(self, teacher: Teacher) -> int:
        return self.interface.create_teacher(teacher)

    def add_s_activity(self, scientific_activity: ScientificActivity) -> int:
        return self.interface.create_scientific_activity(scientific_activity)

    def add_user(self, user: User) -> int:
        return self.interface.create_user(user)

    def add_i_plan(self, individual_plan: IndividualPlan) -> int:
        return self.interface.create_individual_plan(individual_plan)

    def add_s_work(self, scientific_work: ScientificWork) -> int:
        return self.interface.create_scientific_work(scientific_work)

    def add_stage(self, stage: Stage) -> int:
        return self.interface.create_stage(stage)

    def del_teacher(self, teacher_id: int) -> int:
        return self.interface.del_teacher_by_id(teacher_id)

    def del_s_activity(self, s_activity_id: int) -> int:
        return self.interface.del_s_activity_by_id(s_activity_id)

    def del_user(self, user_id: int) -> int:
        return self.interface.del_user_by_id(user_id)

    def del_i_plan(self, i_plan_id: int) -> int:
        return self.interface.del_i_plan_by_id(i_plan_id)

    def del_s_work(self, s_work_id: int) -> int:
        return self.interface.del_s_work_by_id(s_work_id)

    def upd_teacher(self, teacher_id: int, info: dict) -> int:
        teacher = self.interface.get_teacher_by_id(teacher_id)
        for key, value in info.items():
            if key == "name":
                teacher.set_name(value)
            elif key == "role":
                teacher.set_role(value)
            elif key == "scientific_activities":
                teacher.set_scientific_activities(value)
        return self.interface.upd_teacher(teacher)

    def upd_s_activity(self, s_activity_id: int, info: dict) -> int:
        s_activity = self.interface.get_s_activity_by_id(s_activity_id)
        for key, value in info.items():
            if key == "name":
                s_activity.set_name(value)
            elif key == "users":
                s_activity.set_users(value)
        return self.interface.upd_s_activity(s_activity)

    def upd_user(self, user_id: int, info: dict) -> int:
        user = self.interface.get_user_by_id(user_id)
        for key, value in info.items():
            if key == "name":
                user.set_name(value)
            elif key == "individual_plans":
                user.set_i_plans(value)
        return self.interface.upd_user(user)

    def upd_i_plan(self, i_plan_id: int, info: dict) -> int:
        individual_plan = self.interface.get_individual_plan_by_id(i_plan_id)
        for key, value in info.items():
            if key == "name":
                individual_plan.set_name(value)
            elif key == "start_date":
                individual_plan.set_start_date(value)
            elif key == "scientific_works":
                individual_plan.set_scientific_works(value)
        return self.interface.upd_i_plan(individual_plan)

    def upd_s_work(self, s_work_id: int, info: dict) -> int:
        s_work = self.interface.get_s_work_by_id(s_work_id)
        for key, value in info.items():
            if key == "name":
                s_work.set_name(value)
            elif key == "point":
                s_work.set_points(value)
            elif key == "term_date":
                s_work.set_term_date(value)
            elif key == "actual_date":
                s_work.set_actual_date(value)
            elif key == "type":
                s_work.set_type(value)
            elif key == "stages":
                s_work.set_stages(value)
            elif key == "status":
                s_work.set_status(value)
        return self.interface.upd_s_work(s_work)

    def add_s_activity_to_teacher(self, teacher_id: int, scientific_activity: ScientificActivity) -> int:
        try:
            self.interface.get_s_activity_by_id(scientific_activity.get_s_activity_id())
        except RuntimeError:
            self.interface.create_scientific_activity(scientific_activity)
        teacher = self.interface.get_teacher_by_id(teacher_id)
            #if teacher.add_activity(scientific_activity) is False:
               # raise RuntimeError(f"Teacher with id {teacher_id} fully equipped")
        return self.interface.upd_teacher(teacher)

    def add_user_to_s_activity(self, s_activity_id: int, user: User) -> int:
        try:
            self.interface.get_user_by_id(user.get_user_id())
        except RuntimeError:
            self.interface.create_user(user)
        s_activity = self.interface.get_s_activity_by_id(s_activity_id)
        return self.interface.upd_s_activity(s_activity)

    def add_i_plan_to_user(self, user_id: int, i_plan: IndividualPlan) -> int:
        try:
            self.interface.get_individual_plan_by_id(i_plan.get_i_plan_id())
        except RuntimeError:
            self.interface.create_individual_plan(i_plan)
        user = self.interface.get_user_by_id(user_id)
        return self.interface.upd_user(user)

    def add_s_work_to_i_plan(self, i_plan_id: int, s_work: ScientificWork) -> int:
        try:
            self.interface.get_s_work_by_id(s_work.get_s_work_id())
        except RuntimeError:
            self.interface.create_scientific_work(s_work)
        i_plan = self.interface.get_individual_plan_by_id(i_plan_id)
        return self.interface.upd_i_plan(i_plan)