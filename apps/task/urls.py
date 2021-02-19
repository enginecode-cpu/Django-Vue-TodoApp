from django.urls import path
from .views import TaskView
from .views import TaskComplete
from .views import TaskDelete


urlpatterns = [
    path('', TaskView.as_view(), name='tasks_list_url'),
    path('<str:id>/toggle/', TaskComplete.as_view()),
    path('<str:id>/delete/', TaskDelete.as_view()),
]
