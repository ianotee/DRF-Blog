from django.urls import path
from .import views 

urlpatterns = [
    path('', views.urls_list,name='urls_list'),
    path('list/',views.list, name="list"),
    path('Details/<str:pk>/', views.Details,name="Details"),
    path('create/',views.create,name='create'),
    path('update/<str:pk>/',views.update, name='update'),
    path('delete/<str:pk>/',views.delete, name="delete"),

    
]



