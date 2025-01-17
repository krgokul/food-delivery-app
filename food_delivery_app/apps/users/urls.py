from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserList.as_view(), name="user_list"),  # URL for user creation
    path("<int:pk>", views.UserDetail.as_view(), name="user_detail"),
]
