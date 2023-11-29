from django.urls import path
from patients import views
app_name='patients'


urlpatterns = [
     path('',views.viewpatients, name='view_patients'),
     path('addpatient/',views.addpatient, name="add_patient"),
     path('update/<int:id>/',views.patient_update, name="update_patient"),
     path('delete/<int:id>/', views.patient_delete, name="delete_patient"),
     path('update_treat/<int:id>/', views.treat_update,name='update_treat'),
     path('addtreat/', views.addtreat, name='add_treat'),
     path('delete_treatment/<int:id>/',views.treat_delete, name='delete_treat'),
     path('viewmore/<int:id>/',views.detailed_patient, name="detailed_patient"),
     path('viewmoret/<int:id>/', views.detailed_treat, name="detailed_treat"),
     path('download', views.download_table, name ="download"),
     path('count/', views.dashboard, name="count"),



 ]