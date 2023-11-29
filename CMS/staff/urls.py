from django.urls import path
from . import views

app_name= "staff"

urlpatterns=[
    path('', views.view_staff, name="view_staff"),
    path('addstaff/', views.add_staff, name="add_staff"),
    path('update/<int:id>/', views.update_staff, name="update_staff"),
    path('delete/<int:id>/', views.delete_staff, name="delete_staff"),
]