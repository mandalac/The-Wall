from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.succes),
    path('logout', views.logout),
    path('add_a_message', views.create_message),
    path('add_a_comment/<int:message_id>', views.create_comment),

]
