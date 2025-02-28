from django.urls import path

from . import views

app_name = 'myinfo_integration'

urlpatterns = [
    path('auth/', views.MyInfoAuthView.as_view(), name='auth'),
    path('callback/', views.MyInfoCallbackView.as_view(), name='callback'),
]
