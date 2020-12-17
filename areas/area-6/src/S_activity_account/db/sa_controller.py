from datetime import datetime, date
from typing import List

from db.interfaces import Storage

from classes import Enums

class Controller:

    @staticmethod
    def create_s_activity(db: Storage, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        if None in (name, description) or \
                '' in (name, description):
            raise ValueError

        s_activity_id = db.create_s_activity(name=name, description=description)

        return s_activity_id

    @staticmethod
    def add_teacher_to_s_activity(db: Storage, **kwargs):
        s_activity_id = kwargs.get('s_activity_id')
        name = kwargs.get('name')
        surname = kwargs.get('surname')
        role = kwargs.get('role')
        if None in (name, surname, role) or \
                '' in (name, surname, role):
            raise ValueError

        if db.get_s_activity_by_id(s_activity_id) is None:
            raise FileNotFoundError

        teacher_id = db.create_teacher(name=name, surname=surname, role=role, s_activity_id=s_activity_id)

        return teacher_id

    @staticmethod
    def add_user_to_s_teacher(db: Storage, **kwargs):
        teacher_id = kwargs.get('teacher_id')
        name = kwargs.get('name')
        if name == None or \
               name == '':
            raise ValueError

        if db.get_teacher_by_id(teacher_id) is None:
            raise FileNotFoundError

        user_id = db.create_user(name=name, teacher_id=teacher_id)

        return user_id

    @staticmethod
    def get_teachers_by_s_activity(db: Storage, s_activity_id: int):
        if isinstance(s_activity_id, int):
            if db.get_s_activity_by_id(s_activity_id) is not None:
                return db.get_teachers_by_s_activity(s_activity_id)
            else:
                raise FileNotFoundError
        else:
            raise TypeError

    @staticmethod
    def get_s_activities(db: Storage):
        return db.get_s_activities()

    @staticmethod
    def get_full_s_activities(db: Storage):
        return db.get_full_s_activities()