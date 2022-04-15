from django.urls import path, re_path
from drf_yasg import views as drf_yasg_views
from drf_yasg import openapi
from . import views

app_name = 'api'

urlpatterns = [
    path('users', views.UserCreateAPIView.as_view(), name='user_create'),
    path('tasks', views.TaskListCreateAPIView.as_view(), name='task_list_create'),
    path(
        'task/<int:id>',
        views.TaskRetrieveUpdateDestroyAPIView.as_view(),
        name='task_retrieve_update_destroy'
    ),
    re_path(r'^docs/$', drf_yasg_views.get_schema_view(
        openapi.Info(
            title='Todo App',
            default_version='v1.0.0',
            description='API for all things',
        ),
        public=True,
    ).with_ui('redoc', cache_timeout=0), name='docs'),
]
