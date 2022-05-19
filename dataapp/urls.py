from django.urls import path
from . import views

# Url namespace 
app_name = 'dataapp'

urlpatterns = [
     # This view is used to test celery 1
    path('visitors', views.VisitorsView.as_view(), name='Visitors'),

    # This view is used to test celery 2
    path('form', views.FormView.as_view(), name='userform'),
  
]