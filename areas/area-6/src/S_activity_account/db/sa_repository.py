from datetime import date

from django.db import IntegrityError
from classes.Teachers import Teacher as MyTeacher
from classes.Scientific_activities import ScientificActivity as MyScientificActivity
from classes.Users import User as MyUser

from db.interfaces import Storage

from service.models import *

class Repository(Storage):

    @staticmethod
    def create_s_activity(**kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        try:
            s_activity = ScientificActivity.objects.create(name=name, description=description)
            return s_activity.id
        except IntegrityError:
            raise FileExistsError

    @staticmethod
    def create_teacher(**kwargs):
        name = kwargs.get('name')
        surname = kwargs.get('surname')
        role = kwargs.get('role')
        s_activity_id = kwargs.get('s_activity_id')

        teacher = Teacher.objects.create(name=name, surname=surname, role=role, s_activity_id=s_activity_id)
        return teacher.id

    @staticmethod
    def create_user(**kwargs):
        name = kwargs.get('name')
        teacher_id = kwargs.get('teacher_id')

        user = User.objects.create(name=name, teacher_id=teacher_id)
        return user.id

    @staticmethod
    def get_s_activity_by_id(s_activity_id: int) -> MyScientificActivity:
        try:
            s_activity = ScientificActivity.objects.get(id=s_activity_id)
        except ScientificActivity.DoesNotExist:
            return None
        else:
            return MyScientificActivity(s_activity.id, s_activity.name, s_activity.description)

    @staticmethod
    def get_teacher_by_id(teacher_id: int) -> MyTeacher:
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return None
        else:
            return MyTeacher(teacher.id, teacher.name, teacher.surname, teacher.role)

    @staticmethod
    def get_teachers_by_s_activity(s_activity_id: int):
        teachers = Teacher.objects.filter(s_activity_id=s_activity_id)
        if teachers.exists():
            teachrs = []
            for teacher in teachers:
                t = MyTeacher(teacher.id, teacher.name, teacher.surname, teacher.role, teacher.users)
                teachrs.append(t)
            return teachrs
        else:
            return []

    @staticmethod
    def get_s_activities():
        s_activities = ScientificActivity.objects.all()
        if s_activities.exists():
            ret_sas = []
            for s_activity in s_activities:
                sas = MyScientificActivity(s_activity.id, s_activity.name, s_activity.description)
                ret_sas.append(sas)
            return ret_sas
        else:
            return []

    @staticmethod
    def get_full_s_activities():
        teachers = Teacher.objects.all()
        if teachers.exists():
            intermed = {}
            for teacher in teachers:
                teach = MyTeacher(teacher.id, teacher.name, teacher.surname, teacher.role)
                s_activity = teacher.s_activity

                if s_activity.id in intermed:
                    intermed[s_activity.id].teachers.append(teach)
                else:
                    sas = MyScientificActivity(s_activity.id, s_activity.name, s_activity.description, [teach])
                    intermed[s_activity.id] = sas
            return list(intermed.values())
        else:
            return []
