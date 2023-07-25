from django.urls import path
from . import views 
urlpatterns = [
    path('login/',views.loginPage, name="login"),
    path('register/',views.registerPage, name="register"),
    path('profile/<str:pk>/',views.userProfile, name="user-profile"),
    path('logout/',views.logoutPage, name="logout"),
    path('',views.home, name="home"),
    path('room/<str:pk>/',views.room, name="room"),
    path('create-room/',views.CreateRoom, name="Create_room"),
    path('update-room/<str:pk>',views.updateRoom, name="update_room"),
    path('delete-room/<str:pk>',views.deleteRoom, name="delete_room"),
    path('delete-msg/<str:pk>',views.deleteMessage, name="delete_msg"),
    path('update-user/',views.updateUser, name="update_user"),
    path('topics/',views.topicsPage, name="topics"),
    path('activities/',views.activityPage, name="activity")
]