from django.urls import path
from . import  views

app_name= 'premium'

urlpatterns=[
    path('', views.subscribe_premium, name="subscribe"),
    path('subsribers/', views.premium_users, name="subscribers"),
    path('update_subscription/<int:id>/',views.update_subscription, name="update_subscription"),
    path('delete_subscription/<int:id>/', views.delete_subscription, name="delete_subscription"),
    path('sendto/', views.sendtoemail, name="sendemail"),
    path('custom_message/',views.custom_message, name="custom_message")
]