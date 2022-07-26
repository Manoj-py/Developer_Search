from unicodedata import name
from .import views
from django.urls import path

urlpatterns = [
    path("login/",views.loginUser, name ="login"),
    path("logout/",views.logoutUser, name ="logout"),
    path('register/',views.registerUser, name="register"),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>', views.userprofiles, name="user-profile"),
    path('accounts/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-skill/',views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>/',views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/',views.deleteSkill, name="delete-skill"),
]