from classes.Users import User
from classes.Enums import TeacherType
from typing import List

class Teacher:
    def __init__(self, teacher_id: int, name: str, surname: str, role: TeacherType, users: List[User] = None):
        self.teacher_id = teacher_id
        self.name = name
        self.surname = surname
        self.role = role
        self.users = users[:] if users else []
        if not (
                isinstance(name, str) and
                isinstance(teacher_id, int)
        ):
            raise TypeError


    def get_teacher_id(self):
        return self.teacher_id

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_role(self) -> TeacherType:
        return self.role

    def get_users(self) -> List[User]:
        return self.users

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.name = surname

    def set_role(self, role: TeacherType):
        self.role = role

    def set_users(self, users: List[User]):
        self.users = users[:]

    def add_user(self, user: User):
        self.users.append(user)
        return True