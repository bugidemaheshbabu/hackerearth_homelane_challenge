from django.urls import path

from . import views

urlpatterns = [
    path('get-date-info/<str:date>/', views.get_date_info, name='Get_date_info'),
    path('get-state-info/<str:state_name>/', views.get_state_info, name='Get_state_info'),
    path('get-pinpoint-state/<str:state_name>/<str:date>/', views.get_pinpoint_state_info, name='Pinpoint_state'),
]