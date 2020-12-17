from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from db.sa_repository import Repository
from db.sa_controller import Controller

from service.views import SAService


sa_service = SAService(Repository(), Controller())

app_name = 'service'
urlpatterns = [
    path('', sa_service.main),
    path('s_activity', sa_service.create_s_activity),
    path('s_activities', sa_service.get_s_activities),
    path('s_activities_full', sa_service.get_full_s_activities),
    path('teacher', sa_service.add_teacher),
    path('user', sa_service.add_user),
    path('s_activity/<int:s_activity_id>/teachers', sa_service.get_teachers_by_s_activity),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
