from django.urls import path
from .views import UserList

urlpatterns = [
    path('user/',UserList.as_view(), name = 'UserList'),
]




