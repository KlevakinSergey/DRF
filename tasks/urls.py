
from django.urls import path
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'tasks_list', TaskAddView)
# router.register(r'tags_list', TagAddView)
# urlpatterns = router.urls



urlpatterns = [

    path('tasks_list/', TaskListView.as_view(), name='tasks-list'),
    path('tags_list/', TagListView.as_view(), name='tags-list'),
    path('create_task/', TaskCreateView.as_view(), name='task-create'),
    path('tasks_list/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('create_tag/', TagCreateView.as_view(), name='tag-create'),
    path('tags_list/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

]