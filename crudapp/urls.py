from django.urls import path
from . import views

# Url namespace 
app_name = 'crudapp'

urlpatterns = [
     # This view is used to test celery 1
    path('', views.AddHomeView.as_view(), name='addItem'),

    # This view is used to test celery 2
    path('list/', views.ListItems.as_view(), name='listItem'),
    
    # This view is used to test Caching
    path('blog/', views.BlogView.as_view(), name='blog'),

    # This view is used to test Celery beat
    path('numbers/', views.NumberView.as_view(), name='numbers'),
]