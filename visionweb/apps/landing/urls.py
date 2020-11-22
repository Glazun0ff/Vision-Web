from django.urls import path

from . import views
from .views import AllUsersView


app_name = 'landing'
urlpatterns = [
    path('', views.index, name='index'),
    path('send-email/', views.send_email, name='send_email'),
    path('all-users/', AllUsersView.as_view()),
]
