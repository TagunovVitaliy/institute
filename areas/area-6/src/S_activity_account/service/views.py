import json

import jsonpickle
from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest

from db.sa_controller import Controller
from db.sa_repository import Repository

def body_to_dict(body: HttpRequest.body) -> dict or list:
    return json.loads(body)

def return_data(func):
    def wrapper(*args, **kwargs) -> HttpResponse:
        data = func(*args, **kwargs)
        data_json = jsonpickle.encode(data, unpicklable=False)
        return HttpResponse(data_json, content_type='application/json')

    return wrapper

def return_data_template(func):
    def wrapper(*args, **kwargs) -> HttpResponse:
        request, data = func(*args, **kwargs)
        if not data['ok']:
            return render(request, 'error.html', context=data)
        return render(request, f'{data["template"]}.html', context=data)

    return wrapper

class SAService:
    def __init__(self, storage: Repository, controller: Controller):
        self.storage = storage
        self.controller = controller

    @staticmethod
    @return_data_template
    def main(request: HttpRequest):
        return request, {'ok': True, 'template': 'main'}

    @transaction.atomic
    @return_data_template
    def create_s_activity(self, request: HttpRequest):
        if request.method == 'POST':
            try:
                body = body_to_dict(request.body)
            except json.decoder.JSONDecodeError:
                return request, {'ok': False, 'error': 'InvalidBody'}
            try:
                id_s_activity = self.controller.create_s_activity(self.storage, **body)
            except ValueError:
                data = {'error': 'ValueError', 'ok': False, 'message': 'InvalidBody'}
            except FileNotFoundError:
                data = {'error': 'FileNotFoundError', 'ok': False, 'message': 'Position does not exist'}
            except FileExistsError:
                data = {'error': 'FileExistsError', 'ok': False, 'message': 'Scientific Activity already exist'}
            else:
                data = {'ok': True, 'id': id_s_activity, 'template': 'result_create', 'action': 'Created',
                        'body': 's_activity'}
            return request, data
        elif request.method == 'GET':
            return request, {'ok': True, 'template': 'create_s_activity'}
        else:
            return request, {'ok': False, 'error': 'InvalidMethod'}

    @transaction.atomic
    @return_data_template
    def add_teacher(self, request: HttpRequest):
        if request.method == 'POST':
            try:
                body = body_to_dict(request.body)
            except json.decoder.JSONDecodeError:
                return request, {'ok': False, 'error': 'InvalidBody'}
            try:
                id_teacher = self.controller.add_teacher_to_s_activity(self.storage, **body)
            except ValueError:
                return request, {'error': 'ValueError', 'ok': False, 'message': 'InvalidBody'}
            except FileNotFoundError:
                return request, {'error': 'FileNotFoundError', 'ok': False, 'message': 'Scientific Activity not found'}
            except RuntimeError:
                transaction.rollback()
                return request, {'error': 'RuntimeError', 'ok': False, 'message': 'Status cannot be updated'}
            else:
                return request, {'ok': True, 'id': id_teacher, 'template': 'result_create', 'action': 'Added',
                                 'body': 'teacher'}
        elif request.method == 'GET':
            return request, {'ok': True, 'template': 'create_teacher'}
        else:
            return request, {'ok': False, 'error': 'InvalidMethod'}

    @transaction.atomic
    @return_data_template
    def add_user(self, request: HttpRequest):
        if request.method == 'POST':
            try:
                body = body_to_dict(request.body)
            except json.decoder.JSONDecodeError:
                return request, {'ok': False, 'error': 'InvalidBody'}
            try:
                id_user = self.controller.add_user_to_s_teacher(self.storage, **body)
            except ValueError:
                return request, {'error': 'ValueError', 'ok': False, 'message': 'InvalidBody'}
            except FileNotFoundError:
                return request, {'error': 'FileNotFoundError', 'ok': False, 'message': 'Scientific Activity not found'}
            except RuntimeError:
                transaction.rollback()
                return request, {'error': 'RuntimeError', 'ok': False, 'message': 'Status cannot be updated'}
            else:
                return request, {'ok': True, 'id': id_user, 'template': 'result_create', 'action': 'Added',
                                 'body': 'teacher'}
        elif request.method == 'GET':
            return request, {'ok': True, 'template': 'create_user'}
        else:
            return request, {'ok': False, 'error': 'InvalidMethod'}

    @return_data_template
    def get_teachers_by_s_activity(self, request: HttpRequest, teacher_id: int):
        if request.method == 'GET':
            try:
                teachers = self.controller.get_teachers_by_s_activity(self.storage, teacher_id)
            except TypeError:
                return request, {'ok': False, 'error': 'TypeError'}
            except FileNotFoundError:
                return request, {'error': 'FileNotFoundError', 'ok': False, 'message': 'Teachers not found'}
            else:
                return request, {'ok': True, 'data': teachers, 'template': 'teachers'}
        else:
            return request, {'ok': False, 'error': 'InvalidMethod'}


    @return_data_template
    def get_s_activities(self, request: HttpRequest):
        if request.method == 'GET':
            s_activities = self.controller.get_s_activities(self.storage)
            return request, {'ok': True, 'data': s_activities, 'template': 's_activities'}
        else:
            return request, {'ok': False, 'error': 'InvalidMethod'}

    @return_data_template
    def get_full_s_activities(self, request: HttpRequest):
        if request.method == 'GET':
            s_activities = self.controller.get_full_s_activities(self.storage)
            return request, {'ok': True, 'data': s_activities, 'template': 's_activities_full'}
        else:
            return request, {'ok': False, 'error': 'InvalidMethod'}