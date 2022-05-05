from django.urls import path
from . import views
urlpatterns = [
    path('', views.AddHomeView.as_view(), name='addItem'),
    path('list/', views.ListItems.as_view(), name='listItem'),
]