from django.urls import path
from . import views

# Url namespace 
app_name = 'crudapp'

urlpatterns = [
    path('', views.AddHomeView.as_view(), name='addItem'),
    path('list/', views.ListItems.as_view(), name='listItem'),
]