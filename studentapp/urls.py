from django.urls import path
from . import views

app_name = 'studentapp'

urlpatterns = [
    path('login/', views.login, name='login')
]
