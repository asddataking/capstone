from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('pricing/',views.price, name='pricing'),
    path('signup/', views.signup, name='signup')
]