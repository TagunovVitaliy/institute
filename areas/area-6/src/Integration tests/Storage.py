from ..Storage.interfaces import *

class ReadyStorage(Interface):

    def __init__(self):
        super().__init__()
        self.teacher = [Teacher(0, "Shustova Larisa", TeacherType.part_time_teacher, [])]
        self.s_activity = [ScientificActivity(0, "Programming", [])]
        self.user = [User(0, "Tagunov Vitaliy", [])]
        self.i_plan = [IndividualPlan(0, "Plan", date(3000, 1, 1), [])]
        self.s_work = [ScientificWork(0, "Information system development", 5, date(3000, 1, 1), date(3000, 1, 1), ScientificWorkType.seminar, [], ScientificWorkStatus.none)]

    def get_teacher_by_id(self, teacher_id: int) -> Teacher:
        for teacher in self.teacher:
            if teacher.get_teacher_id() == teacher_id:
                return teacher
        raise RuntimeError(f"Get: No Teacher by this id {teacher_id} in Storage")

    def get_s_activity_by_id(self, s_activity_id: int) -> ScientificActivity:
        for s_activity in self.s_activity:
            if s_activity.get_s_activity_id() == s_activity_id:
                return s_activity
        raise RuntimeError(f"Get: No Scientific Activity by this id {s_activity_id} in Storage")

    def get_user_by_id(self, user_id: int) -> User:
        for user in self.user:
            if user.get_user_id() == user_id:
                return user
        raise RuntimeError(f"Get: No Teacher by this id {user_id} in Storage")

    def get_individual_plan_by_id(self, i_plan_id: int) -> IndividualPlan:
        for i_plan in self.i_plan:
            if i_plan.get_i_plan_id() == i_plan_id:
                return i_plan
        raise RuntimeError(f"Get: No Individual Plan by this id {i_plan_id} in Storage")

    def get_s_work_by_id(self, s_work_id: int) -> ScientificWork:
        for s_work in self.s_work:
            if s_work.get_s_work_id() == s_work_id:
                return s_work
        raise RuntimeError(f"Get: No Scientific Work by this id {s_work_id} in Storage")

    def create_teacher(self, teacher: Teacher) -> int:
        if teacher.get_role() != TeacherType.part_time_teacher:
            raise ValueError(f"Add: Teacher with id {teacher.get_teacher_id()} is not part-time")
        for existing in self.teacher:
            if existing.get_teacher_id() == teacher.get_teacher_id():
                raise RuntimeError(f"Add: Teacher with id {teacher.get_teacher_id()} already in Storage")
        self.teacher.append(teacher)
        return teacher.get_teacher_id()

    def create_scientific_activity(self, scientific_activity: ScientificActivity) -> int:
        for existing in self.s_activity:
            if existing.get_s_activity_id() == scientific_activity.get_s_activity_id():
                raise RuntimeError(f"Add: Scientific Activity with id {scientific_activity.get_s_activity_id()} already in Storage")
        self.s_activity.append(scientific_activity)
        return scientific_activity.get_s_activity_id()

    def create_scientific_work(self, scientific_work: ScientificWork) -> int:
        for existing in self.s_work:
            if existing.get_s_work_id() == scientific_work.get_s_work_id():
                raise RuntimeError(f"Add: Scientific Work with id {scientific_work.get_s_work_id()} already in Storage")
        self.s_work.append(scientific_work)
        return scientific_work.get_s_work_id()

    def create_user(self, user: User) -> int:
        for existing in self.user:
            if existing.get_user_id() == user.get_user_id():
                raise RuntimeError(f"Add: User with id {user.get_user_id()} already in Storage")
        self.user.append(user)
        return user.get_user_id()

    def create_individual_plan(self, individual_plan: IndividualPlan) -> int:
        for existing in self.i_plan:
            if existing.get_i_plan_id() == individual_plan.get_i_plan_id()  :
                raise RuntimeError(f"Add: Individual plan with id {individual_plan.get_i_plan_id()} already in Storage")
        self.i_plan.append(individual_plan)
        return individual_plan.get_i_plan_id()

    def upd_teacher(self, teacher: Teacher) -> int:
        for i, existing in enumerate(self.teacher):
            if existing.get_teacher_id() == teacher.get_teacher_id():
                self.teacher[i] = teacher
                return teacher.get_teacher_id()
        raise RuntimeError(f"Update: No Teacher by this id {teacher.get_teacher_id()} in Storage")

    def upd_s_activity(self, scientific_activity: ScientificActivity) -> int:
        for i, existing in enumerate(self.s_activity):
            if existing.get_s_activity_id() == scientific_activity.get_s_activity_id():
                self.s_activity[i] = scientific_activity
                return scientific_activity.get_s_activity_id()
        raise RuntimeError(f"Update: No Scientific Activity by this id {scientific_activity.get_s_activity_id()} in Storage")

    def upd_user(self, user: User) -> int:
        for i, existing in enumerate(self.user):
            if existing.get_user_id() == user.get_user_id():
                self.user[i] = user
                return user.get_user_id()
        raise RuntimeError(f"Update: No Teacher by this id {user.get_user_id()} in Storage")

    def upd_i_plan(self, individual_plan: IndividualPlan) -> int:
        for i, existing in enumerate(self.i_plan):
            if existing.get_i_plan_id() == individual_plan.get_i_plan_id():
                self.i_plan[i] = individual_plan
                return individual_plan.get_i_plan_id()
        raise RuntimeError(f"Update: No Individual plan by this id {individual_plan.get_i_plan_id()} in Storage")

    def upd_s_work(self, scientific_work: ScientificWork) -> int:
        scientific_work.check_status()
        for i, existing in enumerate(self.s_work):
            if existing.get_s_work_id() == scientific_work.get_s_work_id():
                self.s_work[i] = scientific_work
                return scientific_work.get_s_work_id()
        raise RuntimeError(f"Update: No Scientific Work by this id {scientific_work.get_s_work_id()} in Storage")

    def del_teacher_by_id(self, teacher_id: int) -> int:
        for i, existing in enumerate(self.teacher):
            if existing.get_teacher_id() == teacher_id:
                self.teacher.pop(i)
                return teacher_id
        raise RuntimeError(f"Delete: No Teacher by this id {teacher_id} in Storage")

    def del_s_activity_by_id(self, s_activity_id: int) -> int:
        for i, existing in enumerate(self.s_activity):
            if existing.get_s_activity_id() == s_activity_id:
                self.s_activity.pop(i)
                return s_activity_id
        raise RuntimeError(f"Delete: No Scientific Activity by this id {s_activity_id} in Storage")

    def del_user_by_id(self, user_id: int) -> int:
        for i, existing in enumerate(self.user):
            if existing.get_user_id() == user_id:
                self.user.pop(i)
                return user_id
        raise RuntimeError(f"Delete: No User by this id {user_id} in Storage")

    def del_i_plan_by_id(self, i_plan_id: int) -> int:
        for i, existing in enumerate(self.i_plan):
            if existing.get_i_plan_id() == i_plan_id:
                self.i_plan.pop(i)
                return i_plan_id
        raise RuntimeError(f"Delete: No Individual plan by this id {i_plan_id} in Storage")

    def del_s_work_by_id(self, s_work_id: int) -> int:
        for i, existing in enumerate(self.s_work):
            if existing.get_s_work_id() == s_work_id:
                self.s_work.pop(i)
                return s_work_id
        raise RuntimeError(f"Delete: No Scientific Work by this id {s_work_id} in Storage")