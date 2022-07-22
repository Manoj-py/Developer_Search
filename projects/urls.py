from .import views
from django.urls import path,include

urlpatterns = [
    path('', views.projects, name = "projects"),
    path('project/<str:pk>', views.project, name = "project"),
    path('create-project', views.createproject, name="create-project"),
    path('update-project/<str:pk>', views.updateproject, name = "update-project"),
    path('delete-project/<str:pk>', views.deleteproject, name = "delete-project"),
    
]